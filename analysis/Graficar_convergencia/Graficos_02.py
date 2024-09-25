# -*- coding: utf-8 -*-
""" ********************************************
SCRIPT PARA PLOTAGEM DA CURVA DE CONVERGÊNCIA
Versão: 2024.1
Situação : Teste (21/09/2024) 
******************************************** """ 

#%% 1. IMPORTAR BIBLIOTECAS

import pandas as pd                    # importa o pacote para manmipular tabelas 
import matplotlib.pyplot as plt        # importa o módulo para plotagem
from scipy.signal import savgol_filter # importa filtro
import locale                          # importa módulo para definir a localização usada no ponto decimal
from matplotlib.ticker import StrMethodFormatter # importa módulo para formatar eixo
import os


#%% 2. FUNÇÃO GRAFICAR
def graficar( figura,                    # numero da figura que será plotado
              titulo,                    # titulo do arquivo do grafico
              lbleixox,lbleixoy,         # nome dos eixos x e y
              xmin,xmax,                 # intervalo eixo x
              ymin,ymax,                 # intervalo eixo y
              invertx,                   # inverter eixo x
              inserirx0,x0,              # adicionar linha pontilhada vertical
              arquivo,                   # arquivo com os dados
              ncoluna,                   # numero da coluna (dados em y)
              lblcoluna,                 # legenda da coluna
              cor,tamanho,ordem,alpha,estilo,        # estilo da linha
              suavizar,filterx1,filterx2,wl,poly):   # suavizacao

    #pastacaminho = os.path.dirname(os.path.abspath(__file__))+'\\' + arquivo

    #print(pastacaminho)

    # Lendo arquivo de dados      
    data = pd.read_csv(arquivo,sep=r'\s+').values    
    
    # Definindo as dimensões do layout da figura
    fig = plt.figure(figura,figsize = (9,5))
    
    # Eixo x
    if invertx == True:
        x = -(data[:,0]-max(data[:,0]))-x0
    elif invertx == False:
        x =  data[:,0]
    
    # dados do eixo y
    y = data[:,ncoluna]
    
    if suavizar == True:
        for i in range(1,3):
            y[filterx1:filterx2] = savgol_filter(data[filterx1:filterx2,ncoluna],wl,poly, mode = 'interp')
    
    # Plotando os dados
    plt.plot(x,y,color = cor,
              zorder = ordem, 
              linestyle=estilo, 
              lw = tamanho, 
              alpha = alpha, 
              label = lblcoluna)
    
    # Formatando os eixos
    plt.ylim([ymin, ymax])
    plt.xlim([xmin-x0, xmax-x0])
    plt.ylabel(lbleixoy, fontsize=12)
    plt.xlabel(lbleixox, fontsize=12)
    plt.legend()
    
    # numero de dígitos após o ponto decimal
    plt.gca().yaxis.set_major_formatter(StrMethodFormatter("{x:.2f}"))
    
    # Formatando grades
    plt.rcParams['axes.axisbelow'] = True 
    plt.grid(True,which = 'major')
    plt.grid(True,which = 'minor', alpha = 0.3)
    plt.minorticks_on()
    
    # Formatando fontes
    plt.rcParams['axes.unicode_minus'] = False
    plt.rc('text', usetex=True)
    plt.rc('axes', labelsize=12)
    plt.rc('xtick', labelsize=12) 
    plt.rc('ytick', labelsize=12)
    plt.rc('lines', lw=1.0,color='k')
    plt.rc('axes',lw=0.75)
    plt.rc('legend', fontsize=12)
    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "Times"
        })
    
    # Inserir linha vertical em x0
    if inserirx0 == True:
        plt.axvline(x0-x0,color = 'k', lw = 2, linestyle = 'dotted')
    
    # Formatando a legenda
    plt.legend(loc = 'lower left', ncol = 2, fontsize = 'medium', columnspacing = 1.0)
    
    # Salvando em arquivo    
    plt.savefig(str(titulo) + '.svg', format='svg')
    plt.savefig(str(titulo) + '.pdf', 
                dpi = fig.dpi, 
                bbox_inches='tight', 
                pad_inches=0.2)    
     


#%% PERFIL DE CONVERGENCIAS - GRÁFICO GUO
""" ********************************************
PERFIL DE CONVERGENCIAS - GRÁFICO GUO
************************************************ """ 

# Dados gerais da plotagem
figura      = 1
titulo      = 'Perfil de convergências - GUO_2021'
lbleixox    = r'$z/R_t$'
lbleixoy    = r'$U_B$ [\%]'
xmin        = 25
xmax        = 150
ymin        = 0
ymax        = 1
invertx     = True
inserirx0   = True
x0          = 100*4/3

# Opção de suavização
suavizar    = False
filterx1    = 40
filterx2    = 100
wl          = 30
poly        = 10

# Plotagem da primeira curva
modelo      = 'GUO_AXI_EL_SR'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 98
lblcoluna   = 'EL, SR, $d_1 = \infty$'
cor         = 'k'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'dashed'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)

# Plotagem da segunda curva
modelo      = 'GUO_EL_SR_D1_3RE'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 98
lblcoluna   = 'EL, SR, $d_1 = 3R_t$'
cor         = 'g'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'solid'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)

# Plotagem da terceira curva
modelo      = 'GUO_EL_SR_D1_6RE'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 98
lblcoluna   = 'EL, SR, $d_1 = 6R_t$'
cor         = 'r'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'solid'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)


#%% PERFIL DE CONVERGENCIAS - GRÁFICO MA
""" ********************************************
PERFIL DE CONVERGENCIAS - GRÁFICO MA
************************************************ """ 

# Dados gerais da plotagem
figura      = 2
titulo      = 'Perfil de convergências - MA_2021'
lbleixox    = r'$z/R_t$'
lbleixoy    = r'$U_B$ [\%]'
xmin        = 2
xmax        = 40
ymin        = 0
ymax        = 1
invertx     = True
inserirx0   = True
x0          = 100*1/3

# Opção de suavização
suavizar    = False
filterx1    = 40
filterx2    = 400
wl          = 30
poly        = 10

# Plotagem da primeira curva
modelo      = 'MA_AXI_EL_SR'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 98
lblcoluna   = 'EL, $d_1$ = $\infty$'
cor         = 'k'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'dashed'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)

# Plotagem da segunda curva
modelo      = 'MA_AXI_EP_DPII_SR'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 98
lblcoluna   = 'EP, DPII, $d_1$ = $\infty$'
cor         = 'b'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'dashed'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)

# Plotagem da terceira curva
modelo      = 'MA_AXI_EP_MC_SR'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 98
lblcoluna   = 'EP, MC, $d_1$ = $\infty$'
cor         = 'r'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'dashed'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)

# Plotagem da quarta curva
modelo      = 'MA_EL_SR'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 98
lblcoluna   = 'EL, $d_1$ = 5$R_t$'
cor         = 'k'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'solid'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)

# Plotagem da quinta curva
modelo      = 'MA_EP_DPII_SR'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 98
lblcoluna   = 'EP, DPII, $d_1$ = 5$R_t$'
cor         = 'b'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'solid'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)

# Plotagem da sexta curva
modelo      = 'MA_EP_MC_SR'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 98
lblcoluna   = 'EP, MC, $d_1$ = 5$R_t$'
cor         = 'r'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'solid'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)
#%% PERFIL DE CONVERGENCIAS - PARAMETRO FRICCIONAL - EP CRE

""" ********************************************
PERFIL DE CONVERGENCIAS - GRÁFICOS PARÂMETRO FRICCIONAL - EP CRE
************************************************ """ 

# Dados gerais da plotagem
figura      = 3
titulo      = 'FRICperfilconvergenciaCRE'
lbleixox    = r'$z/R_t$'
lbleixoy    = r'$U_B$ [\%]'
xmin        = 3.3
xmax        = 40
ymin        = 0
ymax        = 1.2
invertx     = True
inserirx0   = True
x0          = 100*1/3

# Opção de suavização
suavizar    = True
filterx1    = 100
filterx2    = 200
wl          = 30
poly        = 10

# Plotagem da primeira curva
modelo      = 'AXI_EP_CRE_DPII'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 98
lblcoluna   = 'EP, DPII, $d_1$ = $\infty$'
cor         = '#0C0A3E'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'solid'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)

# Plotagem da segunda curva
modelo      = 'EP_CRE_CG_D1_4RE_DPII'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 98
lblcoluna   = 'EP, CG, DPII, $d_1$ = $4R_t$'
cor         = '#7B1E7A'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'solid'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)

# Plotagem da terceira curva
modelo      = 'EP_CRE_SG_D1_4RE_DPII'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 98
lblcoluna   = 'EP, SG, DPII, $d_1$ = $4R_t$'
cor         = 'b'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'solid'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)

# Plotagem da quarta curva
modelo      = 'AXI_EP_CRE_VM'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 98
lblcoluna   = 'EP, VM, $d_1$ = $\infty$'
cor         = '#3d1308'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'dashed'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)

# Plotagem da quinta curva
modelo      = 'EP_CRE_CG_D1_4RE_VM_DALG_1'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 98
lblcoluna   = 'EP, CG, VM, $d_1$ = $4R_t$'
cor         = '#F3B700'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'dashed'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)

# Plotagem da sexta curva
modelo      = 'EP_CRE_SG_D1_4RE_VM'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 98
lblcoluna   = 'EP, SG, VM, $d_1$ = $4R_t$'
cor         = 'r'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'dashed'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)

#%% PERFIL DE CONVERGENCIAS - PARAMETRO FRICCIONAL - EP SR

""" ********************************************
PERFIL DE CONVERGENCIAS - GRÁFICOS PARÂMETRO FRICCIONAL - EP SR
************************************************ """ 

# Dados gerais da plotagem
figura      = 4
titulo      = 'FRICperfilconvergenciaSR'
lbleixoy    = r'$U_B$ [\%]'
xmin        = 2
xmax        = 40
ymin        = 0
ymax        = 2.5
invertx     = True
inserirx0   = True
x0          = 100*1/3

# Opção de suavização
suavizar    = True
filterx1    = 100
filterx2    = 200
wl          = 30
poly        = 10

# Plotagem da primeira curva
modelo      = 'AXI_EP_SR_DPII'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 98
lblcoluna   = 'EP, DPII, $d_1$ = $\infty$'
cor         = '#0C0A3E'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'solid'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)

# Plotagem da segunda curva
modelo      = 'EP_SR_CG_D1_4RE_DPII'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 98
lblcoluna   = 'EP, CG, DPII, $d_1$ = $4R_t$'
cor         = '#7B1E7A'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'solid'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)

# Plotagem da terceira curva
modelo      = 'EP_SR_SG_D1_4RE_DPII'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 98
lblcoluna   = 'EP, SG, DPII, $d_1$ = $4R_t$'
cor         = 'b'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'solid'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)


# Plotagem da quarta curva
modelo      = 'AXI_EP_SR_VM'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 98
lblcoluna   = 'EP, VM, $d_1$ = $\infty$'
cor         = '#3d1308'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'dashed'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)


# Plotagem da quinta curva
modelo      = 'EP_SR_CG_D1_4RE_VM'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 98
lblcoluna   = 'EP, CG, VM, $d_1$ = $4R_t$'
cor         = '#F3B700'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'dashed'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)


# Plotagem da sexta curva
modelo      = 'EP_SR_SG_D1_4RE_VM'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 98
lblcoluna   = 'EP, SG, VM, $d_1$ = $4R_t$'
cor         = 'r'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'dashed'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)

#%% PERFIL DE CONVERGENCIAS - PARAMETRO FRICCIONAL - EPVP CRVE

""" ********************************************
PERFIL DE CONVERGENCIAS - GRÁFICOS PARÂMETRO FRICCIONAL - EPVP CRVE
************************************************ """ 

# Dados gerais da plotagem
figura      = 5
titulo      = 'FRICperfilconvergenciaEPVP'
lbleixoy    = r'$U_B$ [\%]'
xmin        = 5
xmax        = 40
ymin        = 0
ymax        = 1.6
invertx     = True
inserirx0   = True
x0          = 100*1/3

# Opção de suavização
suavizar    = True
filterx1    = 100
filterx2    = 200
wl          = 30
poly        = 10

# Plotagem da primeira curva
modelo      = 'EPVP_CRVE_CG_D1_4RE_DPII'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 100
lblcoluna   = 'EPVP, CG, DPII, $d_1$ = $4R_t$, CP'
cor         = '#0C0A3E'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'solid'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)

# Plotagem da segunda curva
modelo      = 'EPVP_CRVE_CG_D1_4RE_DPII'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 130
lblcoluna   = 'EPVP, CG, DPII, $d_1$ = $4R_t$, LP'
cor         = '#7B1E7A'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'dashed'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)

# Plotagem da terceira curva
modelo      = 'EPVP_CRVE_CG_D1_4RE_VM'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 100
lblcoluna   = 'EPVP, CG, VM, $d_1$ = $4R_t$, CP'
cor         = 'r'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'solid'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)


# Plotagem da quarta curva
modelo      = 'EPVP_CRVE_CG_D1_4RE_VM'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 130
lblcoluna   = 'EPVP, CG, VM, $d_1$ = $4R_t$, LP'
cor         = '#E57C04'
tamanho     = 2
ordem       = 1
alpha       = 1
estilo      = 'dashed'

graficar(figura,titulo,lbleixox,lbleixoy,
          xmin,xmax,ymin,ymax,
          invertx,
          inserirx0,x0,
          arquivo,
          ncoluna,lblcoluna,
          cor,tamanho,ordem,alpha,estilo,
          suavizar,filterx1,filterx2,wl,poly)
