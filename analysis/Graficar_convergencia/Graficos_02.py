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
    #plt.savefig(str(titulo) + '.svg', format='svg')
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
lblcoluna   = 'EL, SR, D1, INF'
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
lblcoluna   = 'EL, SR, D1, 3RE'
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
lblcoluna   = 'EL, SR, D1, 6RE'
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
xmin        = 3
xmax        = 40
ymin        = 0
ymax        = 1
invertx     = True
inserirx0   = True
x0          = 100*1/3

# Opção de suavização
suavizar    = False
filterx1    = 40
filterx2    = 100
wl          = 30
poly        = 10

# Plotagem da primeira curva
modelo      = 'MA_AXI_EL_SR'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 98
lblcoluna   = 'EL, SR, D1, INF'
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
lblcoluna   = 'EP, SR, DPII, D1, INF'
cor         = 'g'
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
lblcoluna   = 'EP, SR, MC, D1, INF'
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
lblcoluna   = 'EL, SR, D1, 5RE'
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
lblcoluna   = 'EP, SR, DPII, D1, 5RE'
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

# Plotagem da sexta curva
modelo      = 'MA_EP_MC_SR'
arquivo     = modelo + '\\tabela_90.txt'
ncoluna     = 98
lblcoluna   = 'EP, SR, MC, D1, 5RE'
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