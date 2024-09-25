

import matplotlib.pyplot as plt        # importa o módulo para plotagem
#from matplotlib.ticker import StrMethodFormatter # importa módulo para formatar eixo
import numpy as np
from matplotlib import rc
#import locale                          # importa módulo para definir a localização usada no ponto decimal

def graficar(x,y,                       # eixo x e y
             titulo,                    # titulo do gráfico
             eixox,eixoy,               # nome dos eixos x e y
             xmin,xmax,xstep,           # intervalo eixo x
             ymin,ymax,ystep,           # intervalo eixo y
             lbldata,                   # legenda dos dados
             cor,tamanho,ordem,alpha,estilo,marker,   # formatacao
             figura):

    # define localização para o ponto decimal
    #locale.setlocale(locale.LC_NUMERIC,"ru_RU.utf8")
    
    # adicionando título
    #plt.title(titulo, fontsize = 16, fontweight="bold") 
    
    # Definindo as dimensões do layout da figura
    fig = plt.figure(figura,figsize = (9,5))    
    
    # Definindo ponto decimal
    #plt.gca().yaxis.set_major_formatter(StrMethodFormatter("{x:.2f}"))

    # aplica localização para o ponto decimal
    #plt.rcParams['axes.formatter.use_locale'] = True

    # Formatando grades
    plt.rcParams['axes.axisbelow'] = True 
    plt.grid(True,which = 'major')
    plt.grid(True,which = 'minor', alpha = 0.3)
    plt.minorticks_on()
    
    # Formatando legendas
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
    
    # Formatando os eixos
    plt.ylim([ymin, ymax])
    plt.xlim([xmin, xmax])
    plt.ylabel(eixoy, fontsize=12)
    plt.xlabel(eixox, fontsize=12)
    # Formatando eixos
    plt.xticks(np.arange(xmin, xmax+0.01, step=xstep))
    plt.yticks(np.arange(ymin, ymax+0.01, step=ystep))
    plt.legend()
    
    # Plotando
    plt.plot(x,y,color = cor,
             zorder = ordem, 
             linestyle=estilo, 
             lw = tamanho, 
             alpha = alpha, 
             label = lbldata,
             marker = marker,
             markersize = 10,
             fillstyle = 'none')

    # Formatando a legenda
    plt.legend(loc = 'upper right', ncol = 1)
    #plt.legend(
    #    loc = 'center',
    #    shadow=False,
    #    framealpha = 0,
    #    ncol = 2,
    #    columnspacing = 0.5,
    #    bbox_to_anchor=(0.5, -0.22),
    #    fontsize="11")

    # Salvando em arquivo   
    plt.savefig(str(titulo) + '.svg', format='svg')
    plt.savefig(str(titulo) + '.pdf', 
                dpi = fig.dpi, 
                bbox_inches='tight', 
                pad_inches=0.2)

Rt = 4
x = np.array([3, 4, 5, 6])/(2)
q0 = 2.2
sttA = np.array([6.272, 5.240, 4.881, 4.689])/q0
sttB = np.array([3.804, 3.980, 4.093, 4.154])/q0
UA   = np.array([0.2199, 0.3157, 0.3715, 0.4063])
UB   = np.array([0.7117, 0.6401, 0.6072, 0.5884])

x_analitycal = np.array([3, 3.5, 4, 4.5, 5, 5.5,6])/(2)
sttA_analitycal = [3.077, 2.761, 2.576, 2.456, 2.383, 2.317, 2.283]

x_numerical = np.array([3, 3.5, 4, 4.5, 5, 5.5,6])/(2)
sttA_numerical = [2.965, 2.616, 2.411, 2.285, 2.199, 2.132, 2.079]

x_Ling = np.array([3, 4, 6])/(2)
sttA_Ling = [2.867, 2.372, 2.112]


figura      = 1
titulo      = 'Fator de concentração de tensão tangencial em A'
eixoy       = r'$\sigma_{\theta \theta}/\sigma_v$'
eixox       = r'$d_1/2R_t$'
xmin        = 1.25
xmax        = 3.25
xstep       = 0.25
ymin        = 1.75
ymax        = 3.25
ystep       = 0.25

lbldata     = 'Solução numérica 3D (MEF)'
cor         = 'r'
tamanho     = 1.5
ordem       = 1
alpha       = 1
estilo      = 'solid'
marker      = "s"

graficar(x,sttA,titulo,eixox,eixoy,
          xmin,xmax,xstep,ymin,ymax,ystep,
          lbldata,
          cor,tamanho,ordem,alpha,estilo,marker,
          figura)

lbldata     = 'Solução analítica (Guo et al, 2021)'
cor         = '#fc4f30'
tamanho     = 1.5
ordem       = 1
alpha       = 1
estilo      = 'solid'
marker      = "D"

graficar(x_analitycal,sttA_analitycal,titulo,eixox,eixoy,
          xmin,xmax,xstep,ymin,ymax,ystep,
          lbldata,
          cor,tamanho,ordem,alpha,estilo,marker,
          figura)

lbldata     = 'Solução numérica (Guo et al, 2021)'
cor         = 'b'
tamanho     = 1.5
ordem       = 1
alpha       = 1
estilo      = 'solid'
marker      = "x"

graficar(x_numerical,sttA_numerical,titulo,eixox,eixoy,
          xmin,xmax,xstep,ymin,ymax,ystep,
          lbldata,
          cor,tamanho,ordem,alpha,estilo,marker,
          figura)

lbldata     = 'Solução analítica (Ling, 1948)'
cor         = 'g'
tamanho     = 1.5
ordem       = 1
alpha       = 1
estilo      = 'solid'
marker      = "o"

graficar(x_Ling,sttA_Ling,titulo,eixox,eixoy,
          xmin,xmax,xstep,ymin,ymax,ystep,
          lbldata,
          cor,tamanho,ordem,alpha,estilo,marker,
          figura)

lbldata     = 'Túnel isolado'
cor         = 'k'
tamanho     = 1.5
ordem       = 1
alpha       = 1
estilo      = 'dashed'
marker      = ""

graficar([1.25,5.0],[2,2],titulo,eixox,eixoy,
          xmin,xmax,xstep,ymin,ymax,ystep,
          lbldata,
          cor,tamanho,ordem,alpha,estilo,marker,
          figura)


figura      = 2
titulo      = 'Relação da convergência B e A'
eixoy       = r'$U_B/U_A$'
eixox       = r'$d_1/2R_t$'
xmin        = 1.25
xmax        = 3.25
xstep       = 0.25
ymin        = 0
ymax        = 4.25
ystep       = 0.5

lbldata     = 'Solução numérica 3D (MEF)'
cor         = 'r'
tamanho     = 1.5
ordem       = 1
alpha       = 1
estilo      = 'solid'
marker      = "s"

graficar(x,UB/UA,titulo,eixox,eixoy,
          xmin,xmax,xstep,ymin,ymax,ystep,
          lbldata,
          cor,tamanho,ordem,alpha,estilo,marker,
          figura)

lbldata     = 'Túnel isolado'
cor         = 'k'
tamanho     = 1.5
ordem       = 1
alpha       = 1
estilo      = 'dashed'
marker      = ""

graficar([0,5.0],[1,1],titulo,eixox,eixoy,
          xmin,xmax,xstep,ymin,ymax,ystep,
          lbldata,
          cor,tamanho,ordem,alpha,estilo,marker,
          figura)


figura      = 3
titulo      = 'Fator de concentração de tensão tangencial em A - teste'
eixoy       = r'$\sigma_{\theta \theta}/\sigma_v$'
eixox       = r'$d_1/2R_t$'
xmin        = 1.25
xmax        = 3.25
xstep       = 0.25
ymin        = 1.75
ymax        = 3.25
ystep       = 0.25

lbldata     = 'Solução numérica 3D (MEF)'
cor         = 'r'
tamanho     = 1.5
ordem       = 1
alpha       = 1
estilo      = 'solid'
marker      = "s"

graficar(x,sttA,titulo,eixox,eixoy,
          xmin,xmax,xstep,ymin,ymax,ystep,
          lbldata,
          cor,tamanho,ordem,alpha,estilo,marker,
          figura)

lbldata     = 'Solução analítica (Guo et al, 2021)'
cor         = '#fc4f30'
tamanho     = 1.5
ordem       = 1
alpha       = 1
estilo      = 'solid'
marker      = "D"

graficar(x_analitycal,sttA_analitycal,titulo,eixox,eixoy,
          xmin,xmax,xstep,ymin,ymax,ystep,
          lbldata,
          cor,tamanho,ordem,alpha,estilo,marker,
          figura)

lbldata     = 'Solução numérica (Guo et al, 2021)'
cor         = 'b'
tamanho     = 1.5
ordem       = 1
alpha       = 1
estilo      = 'solid'
marker      = "x"

graficar(x_numerical,sttA_numerical,titulo,eixox,eixoy,
          xmin,xmax,xstep,ymin,ymax,ystep,
          lbldata,
          cor,tamanho,ordem,alpha,estilo,marker,
          figura)

lbldata     = 'Solução analítica (Ling, 1948)'
cor         = 'g'
tamanho     = 1.5
ordem       = 1
alpha       = 1
estilo      = 'solid'
marker      = "o"

graficar(x_Ling,sttA_Ling,titulo,eixox,eixoy,
          xmin,xmax,xstep,ymin,ymax,ystep,
          lbldata,
          cor,tamanho,ordem,alpha,estilo,marker,
          figura)

lbldata     = 'Túnel isolado'
cor         = 'k'
tamanho     = 1.5
ordem       = 1
alpha       = 1
estilo      = 'dashed'
marker      = ""

graficar([1.25,5.0],[2,2],titulo,eixox,eixoy,
          xmin,xmax,xstep,ymin,ymax,ystep,
          lbldata,
          cor,tamanho,ordem,alpha,estilo,marker,
          figura)
