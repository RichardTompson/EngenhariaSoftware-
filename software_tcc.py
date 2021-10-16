
# Importação das bibliotecas
from tkinter.font import BOLD
from tkinter.filedialog import askopenfilename
import pandas as pd
from pandas.core import frame
import statsmodels.api as sm
import numpy as np
import datetime
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from tkinter import *
from pandastable import Table, TableModel, config, data
import seaborn as sns


# Definindo as Classes
#Classes  
    
# classe SCR
class SCR:
    # definindo metodo de busca maior que determininado valor
    def scr_total_maior_que(self, df):   
        def getvalue(frame_entrada):
            # metodo para testar se o valor digitado é do tipo float 
            def isnumber(value):
                try:
                    float(value)
                except  ValueError:
                    return  False
                return  True

            # convertendo valor digitado para float
            def converter_para_float(valor):                              
                valor = float(valor.get().replace(',', '.'))
                return valor

            # verificando se o valor digitado é um numero          
            if(isnumber(valor.get().replace(',', '.'))):

                # convertendo para float             
                valor_float = converter_para_float(valor)
                
                # get valor maxino da base
                max = frame_entrada['scr_total'].max()      
                
                # verificando se o valor digitado é maior ou igual a zero e menor/igual que maximo
                if((valor_float<=max) and (valor_float >= 0)):
                    # filtrando base para valores maiores que o valor digitado
                    frame_entrada_1 = frame_entrada[frame_entrada['scr_total'] >= valor_float]
                    
                    # criando tela de exibicao
                    tela = Tk() 

                    # setando titulo da tela     
                    tela.title("Dados")

                    # setando modo exibicao da tela
                    tela.state("zoomed")

                    # criando frame
                    frame = Frame(tela)

                    # exibindo frame
                    frame.grid()  

                    # alterando o nome das colunas
                    frame_entrada_2 = config_dataframe.alterar_nome_colunas(frame_entrada_1)

                    # criando tabela
                    table = Table (frame, dataframe=frame_entrada_2[['Id', 'Nome', 'SCR Total', 'Telefone']], align = 'center', floatprecision=2,width = (largura - 100), height = (altura - 50), showtoolbar=False, showstatusbar=False)

                    # criando lista com os nomes das colunas
                    lista_colunas = list(frame_entrada_2.columns)                   
                   
                    # dando enfase na coluna com o nome do produto
                    table.columncolors[lista_colunas[6]] = '#FFFF00'  

                    # exibindo tabela     
                    table.show()

                    # exibindo tela
                    tela.mainloop()
                
                # caso o valor digitado seja menor zero
                elif(valor_float<0):
                    # criando tela
                    tela = Tk()

                    # setando titulo da tela
                    tela.title("Valores negativos")

                    # setando modo de exibicao
                    tela.state('zoomed')

                    # criando label
                    label = Label(tela, text = "Digite um valor maior ou igual a zero. ", font = 'Arial 20').grid()

                    # exibindo tela
                    tela.mainloop()
                
                if(valor_float>max):
                    # criando tela
                    tela = Tk()

                    # setando titulo da tela
                    tela.title("Valores maiores que o máximo")

                    # setando modo de exibicao
                    tela.state('zoomed')

                    # criando label
                    label = Label(tela, text = f"Não constam valores maiores que {valor_float:0.2f}. Valor máximo é: {max:0.2f} ", font = 'Arial 20').grid()

                    # exibindo tela
                    tela.mainloop()                


            # caso para digitacao de caracteres que nao sejam numeros
            if(not isnumber(valor.get().replace(',', ''))):         
                                                     
                # criando tela
                tela = Tk()

                # setando titulo
                tela.title('Mensagem')

                # setando modo de exibicao
                tela.state('zoomed') 

                # criando variavel para armazenar valor digitado 
                texto = StringVar(tela)

                # setando variavel
                texto.set("Caracteres não admtidos na busca. Reveja o valor digitado. ") 

                # criando label           
                label_nao_encontrado = Label(tela, textvariable = texto, font = 'Arial 20').grid()

                # exibindo tela
                tela.mainloop()
            
        # criando dataframe local
        frame_entrada = df.copy()   

        # criando tela
        tela = Tk()

        # criando variavel para armazenar valor
        valor = StringVar(tela)        
        
        # setando titulo tela
        tela.title("SCR Maior ou Igual")

        # setando modo exibicao da tela
        tela.state("zoomed")   

        # criando frame
        frame = LabelFrame(tela, text = 'SCR Total: ', font=("TkDefaultFont",15, 'bold'),padx = 20, pady = 20) 

        # localizando frame
        frame.place(x = 500, y = 120)        

        # criando label
        label_scr = Label(frame, text = "Maior ou Igual a: ", font=80)             
        
        # criando entrada
        e1 = Entry(frame,textvariable = valor, width=30, fg="blue", font = 80, bd = 3,selectbackground='violet')

        # criando botao
        button_scr = Button(frame, 
            text='Pesquisar', 
            fg='White', 
            bg= 'Dark blue',height = 1, font = 80, command=lambda: getvalue(frame_entrada))
       
        # exibindo
        label_scr.grid(row = 0, column = 0)
        e1.grid(row = 0, column = 1)
        button_scr.grid(row = 1, columnspan = 2, sticky = 'we')

    # definindo metodo de busca menor que determininado valor
    def scr_total_menor_que(self, df):
        def getvalue(frame_entrada):
            # metodo para testar se o valor digitado é do tipo float 
            def isnumber(value):
                try:
                    float(value)
                except  ValueError:
                    return  False
                return  True

            # convertendo valor string para float
            def converter_para_float(valor):                              
                valor = float(valor.get().replace(',', '.'))
                return valor
                
            # verificando se o valor é um numero         
            if(isnumber(valor.get().replace(',', '.'))):   
                # convertendo para float             
                valor_float = converter_para_float(valor)

                # obtendo o minimo da base
                min = frame_entrada['scr_total'].min()
                
                # verificando se o valor digitado é maior que o minimo da base e maior que zero
                if((valor_float>=min) and (valor_float >= 0)):

                    # filtrando dataframe que atende a condicao
                    frame_entrada_1 = frame_entrada[frame_entrada['scr_total'] <= valor_float]
                    
                    # criando tela
                    tela = Tk()    

                    # setando titulo  
                    tela.title("Dados")

                    # setando modo de exibicao
                    tela.state("zoomed")

                    # criando frame
                    frame = Frame(tela)

                    # exibindo frame
                    frame.grid()

                    # alterando nome das colunas
                    frame_entrada_2 = config_dataframe.alterar_nome_colunas(frame_entrada_1)

                    # criando tabela    
                    table = Table (frame, dataframe=frame_entrada_2[['Id', 'Nome', 'SCR Total', 'Telefone']], align = 'center', floatprecision=2,width = (largura - 100), height = (altura - 50), showtoolbar=False, showstatusbar=False)

                    # enfase na coluna scr
                    table.columncolors['SCR Total'] = '#FFFF00' 
                    
                    # exibindo tabela  
                    table.show()

                    # exibindo tela
                    tela.mainloop()
                
                
                # caso valor nao constam clientes que atendam a condicao            
                if(valor_float<min):
                    # criando tela
                    tela = Tk()

                    # setando titulo
                    tela.title('Mensagem')

                    # setando modo de exibicao
                    tela.state('zoomed') 

                    # criando variavel para armazenar valor digitado 
                    texto = StringVar(tela)

                    # setando variavel
                    texto.set(f"Não constam clientes com valores menores que {min:0.2f}") 

                    # criando label           
                    label_nao_encontrado = Label(tela, textvariable = texto, font = 'Arial 20').grid()

                    # exibindo tela
                    tela.mainloop()

            # caso para digitacao de caracteres que nao sejam numeros
            if(not isnumber(valor.get().replace(',', ''))):         
                                                     
                # criando tela
                tela = Tk()

                    # setando titulo
                tela.title('Mensagem')

                    # setando modo de exibicao
                tela.state('zoomed') 

                    # criando variavel para armazenar valor digitado 
                texto = StringVar(tela)

                    # setando variavel
                texto.set("Caracteres não admtidos na busca. Reveja o valor digitado. ") 

                    # criando label           
                label_nao_encontrado = Label(tela, textvariable = texto, font = 'Arial 20').grid()

                    # exibindo tela
                tela.mainloop()
            
        # criando dataframe local
        frame_entrada = df.copy()       

        # criando tela
        tela = Tk()

        # criando variavel
        valor = StringVar(tela)                
                  
        # setando titulo
        tela.title("Menor ou Igual a: ")

        # setando modo exibicao
        tela.state("zoomed")   

        # criando frame
        frame = LabelFrame(tela, text = 'SCR Total: ', padx = 20, pady = 20, font=("TkDefaultFont",15, 'bold')) 

        # localizando frame
        frame.place(x = 500, y = 120)        
            
        # criando label
        label = Label(frame, font = 80, text = "Menor ou Igual a: ")

        # criando entrada            
        e1 = Entry(frame,textvariable = valor,width=30,fg="blue",bd=3,font = 80, selectbackground='violet')    
        
      
        # criando botao
        button = Button(frame, 
                text='Pesquisar', 
                fg='White', 
                bg= 'Dark blue',height = 1, font = 80, command=lambda: getvalue(frame_entrada))       
                

        # exibindo
        label.grid(row = 0, column = 0)        
        e1.grid(row = 0, column = 1)
        button.grid(row = 1, columnspan = 2, sticky = 'we')    
        

    # definindo consulta geral SCR
    def scr_consulta(self, df):  
        # definindo selecao 1
        def sel_1(frame_entrada, coluna, title):
            
            # criando tela  
            tela = Tk()

            # setando titulo
            tela.title(title)

            # setando modo de exibicao
            tela.state("zoomed")

            # criando frame
            frame = Frame(tela)

            # exibindo frame
            frame.grid()  

            # filtrando frame de interesse
            frame_entrada_1 = frame_entrada[['id', 'nome', coluna, 'telefone']].sort_values(by=coluna)

            # renomeando colunas
            frame_entrada_2 = config_dataframe.alterar_nome_colunas(frame_entrada_1)

            # criando tabela    
            table = Table (frame, dataframe=frame_entrada_2, align='center', floatprecision=2,width = (largura - 100), height = (altura - 50), showtoolbar=False, showstatusbar=False)
                        
            # criando lista com os nomes das colunas
            lista_colunas = list(frame_entrada_2.columns)
            
            # enfase na coluna scr
            table.columncolors[lista_colunas[2]] = '#FFFF00' 

            # exibindo tabela
            table.show()

            # exibindo tela
            tela.mainloop()   
        
        
        # criando dataframe local
        frame_entrada = df.copy()

        # criando tela
        root = Tk()

        # setando titulo
        root.title("SCR")

        # setando modo exibicao
        root.state('zoomed')

        # criando frame
        frame = LabelFrame(root, text="Consultar", highlightbackground="black",highlightthickness=3, font=("TkDefaultFont",15, 'bold'))

        # localizando frame
        frame.place(x=largura//2, y = (altura//2)-200)

        # criando variavel de armazenamento valor digitado
        var = IntVar(frame)

        # criando botao de selecao
        R1 = Radiobutton(frame, text="SCR Total", font = 80, variable=var, value=1,command=lambda: sel_1(frame_entrada, 'scr_total', "SCR Total"))

        # exibindo botao de selecao
        R1.grid(sticky = W)

        # criando botao de selecao
        R2 = Radiobutton(frame, text="SCR Nosso", font = 80, variable=var, value=2,command=lambda: sel_1(frame_entrada, 'scr_nosso', "SCR Nosso"))

        # exibindo botao de selecao
        R2.grid(sticky = W)

        # crianco botao de selecao
        R3 = Radiobutton(frame, text="SCR Outros", font = 80, variable=var, value=3,command=lambda:sel_1(frame_entrada, 'scr_outros', "SCR Outros"))

        # exibindo botacao selecao
        R3.grid(sticky = W)

        # criando label
        label = Label(root)

        # localizando label
        label.place()    

        # exibindo tela    
        root.mainloop()

    # gerando gráfico de pizza
    def grafico_pie(self, df):

        # criando dataframe local
        frame_entrada = df.copy()

        # criando figura
        area = plt.figure()

        # dividindo a figura
        g1 = area.add_subplot(3,5,1)
        
        # criando labels
        labels = ['SCR Nosso', 'SCR Outros']
        labels_1 = ['SCR Nosso', 'SCR Total']
        labels_2 = ['SCR Outros', 'SCR Total']

        # filtrado valor de plotagem eixo y
        frame_entrada_1 = round(float(frame_entrada['scr_nosso'].sum()),2)

        # filtrando valor de plotagem eixo y
        frame_entrada_2 = round(float(frame_entrada['scr_outros'].sum()),2)

        # filtrando valores SCR total
        frame_entrada_3 = round(float(frame_entrada['scr_total'].sum()),2)

        # agrupado valores de plotagem no eixo y
        saida = [frame_entrada_1, frame_entrada_2] 
        saida_1 = [frame_entrada_1, frame_entrada_3]
        saida_2 = [frame_entrada_2, frame_entrada_3]
       
        # destacando parte do grafico
        explode = [0, 0.2]

        # criando grafico de pizza (shadow=True)
        g1.pie(saida, labels=labels, autopct = '%.2f%%', wedgeprops = {'linewidth': 3, 'edgecolor': 'white'})

        # transformando grafico de pizza em rosca
        centro_circulo = plt.Circle((0,0), 0.70, fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centro_circulo)    

        # dividindo a figura
        g1_1 = area.add_subplot(3,5,6)

        # criando subgrafico
        g1_1.pie(saida_1, labels=labels_1, autopct = '%.2f%%', wedgeprops = {'linewidth': 3, 'edgecolor': 'white'})

        # transformando grafico de pizza em rosca
        centro_circulo = plt.Circle((0,0), 0.70, fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centro_circulo) 

        # dividindo a figura
        g1_2 = area.add_subplot(3,5,11)

        # criando subgrafico
        g1_2.pie(saida_2, labels=labels_2, autopct = '%.2f%%', wedgeprops = {'linewidth': 3, 'edgecolor': 'white'})
       
        # transformando grafico de pizza em rosca
        centro_circulo = plt.Circle((0,0), 0.70, fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centro_circulo)

        # setando titulo do grafico
        g1.set_title("SCR")

        # criando outro subgrafico
        g2 = area.add_subplot(1,5,3)

        # rotacionando labels do eixo x
        plt.xticks(rotation=45)       

        # criando grafico de barras
        g2.bar(labels, saida)

        # setando barras no eixo y
        g2.set_yticks(saida)       

        # setando titulo
        g2.set_title("SCR")
       
        # criando outro subgrafico
        g3 = area.add_subplot(2,5,5)

        # tornando eixo x invisivel
        g3.axes.get_xaxis().set_visible(False)

        # criando grafico boxplot
        g3.boxplot(frame_entrada['scr_nosso'], patch_artist=True)   

        # setando titulo    
        g3.set_title("SCR Nosso")

        # setando eixo y
        g3.set_ylabel("(R$)")

        # criando outro subgrafico
        g4 = area.add_subplot(2,5,10)

        # tornando eixo x invisivel        
        g4.axes.get_xaxis().set_visible(False)
       
        # criando grafico boxplot
        g4.boxplot(frame_entrada['scr_outros'], patch_artist=True) 

        # setando eixo y
        g4.set_ylabel("(R$)")   

        # setando titulo   
        g4.set_title("SCR Outros")

        # maximizando figura na tela
        figManager = plt.get_current_fig_manager()
        figManager.window.state('zoomed')

        # adicionando titulo na figura
        plt.suptitle('Gráficos SCR',fontsize=20)       

        # exibindo grafico
        area.show()

        
# Definindo classe seguridade
class seguridade:    
    # definindo grafico pizza
    def grafico_seguridade_pie(self, df): 

        # criando dataframe local
        frame_entrada = df.copy()

        # padronizando coluna sim/nao
        frame_entrada = config_dataframe.alterar_campos_sim_nao(self, frame_entrada, 'seguro_auto')

        # definindo metodos para obter os parametros para os graficos
        def parametros_grafico(coluna):
            # dando enfase em um setor do grafico 
            explode=[0.2, 0]   
            
            # criando valores para serem plotados
            slice = frame_entrada[coluna].value_counts()

            # setando os labels em uma lista
            labels = list(slice.index)

            # criando uma lista para alterar os labels e inserir os novos labels nela
            novo_label = []

            # alterar os labels para novos labels
            for e in labels:
                if(e == 'sim'):
                    e = "Sim"
                if (e == 'nao'):
                    e = 'Não'
                # inserindo os novos labels na lista
                novo_label.append(e)
            return ((explode, slice, novo_label))
        
        # grafico
        # criando area
        area = plt.figure()       
       
        # criando subgraficos     
        # Seguro Auto

        # dividindo area em 2 linhas e 3 colunas
        g1 = area.add_subplot(2,3,1)

        # obtendo parametros para o grafico
        explode, slice, novo_label = parametros_grafico('seguro_auto')
        
        #criando gráfico
        g1.pie(slice, explode=explode, labels=novo_label, shadow=True, autopct = '%.2f%%')  

        # setando titulo    
        g1.set_title("Seguro Auto")        

        # Seguro vida     
        g2 = area.add_subplot(2,3,2) 

        # obtendo parametros para o grafico
        explode, slice, novo_label = parametros_grafico('seguro_vida')        
        
        # criando o grafico
        g2.pie(slice, explode=explode, labels=novo_label, shadow=True, autopct = '%.2f%%')  

        # setando titulo do grafico    
        g2.set_title("Seguro Vida")

        # Seguro residencial        
        g3 = area.add_subplot(2,3,3) 

        # obtendo parametros para o grafico
        explode, slice, novo_label = parametros_grafico('seguro_residencial')
        
        # criando o gráfico
        g3.pie(slice, explode=explode, labels=novo_label, shadow=True, autopct = '%.2f%%') 

        # setanto titulo do grafico     
        g3.set_title("Seguro Residencial")

        # Capitalizacao
        g4 = area.add_subplot(2,3,4) 

        # obtendo parametros para o grafico
        explode, slice, novo_label = parametros_grafico('capitalizacao')

        # criando o gráfico
        g4.pie(slice, explode=explode, labels=novo_label, shadow=True, autopct = '%.2f%%') 

        # setando titulo do gráfico     
        g4.set_title("Capitalização")

        # Consorcio
        g5 = area.add_subplot(2,3,5) 

        # obtendo parametros para o grafico
        explode, slice, novo_label = parametros_grafico('consorcio')

        # criando o grafico
        g5.pie(slice, explode=explode, labels=novo_label, shadow=True, autopct = '%.2f%%')  

        # setando titulo do grafico    
        g5.set_title("Consórcio")

        # Previdência
        g6 = area.add_subplot(2,3,6) 

        # obtendo parametros para o grafico
        explode, slice, novo_label = parametros_grafico('previdencia_privada')
        
        # criando o grafico
        g6.pie(slice, explode=explode, labels=novo_label, shadow=True, autopct = '%.2f%%') 

        # setanto titulo do grafico     
        g6.set_title("Previdência Privada")

        # maximizando figura na tela
        figManager = plt.get_current_fig_manager()
        figManager.window.state('zoomed')
        
        # setando titulo do grafico todo
        plt.suptitle("Posse de Produto", fontweight='bold', fontsize=20)
        
        # exibindo gráfico
        area.show() 

    # definindo gráfico de barras
    def grafico_seguridade_barras(self, df):        
        # criando dataframe local
        frame_entrada = df.copy()

        # padronizando coluna sim/nao
        frame_entrada_1 = config_dataframe.alterar_campos_sim_nao(self, frame_entrada, 'seguro_auto')

        # filtrando seguro auto
        frame_seguro_auto_sim = config_dataframe.filtrar_colunas(self, frame_entrada_1, 'seguro_auto', 'sim')
        frame_seguro_auto_nao = config_dataframe.filtrar_colunas(self, frame_entrada_1, 'seguro_auto', 'nao') 

        # filtrando seguro vida
        frame_seguro_vida_sim = config_dataframe.filtrar_colunas(self, frame_entrada_1, 'seguro_vida', 'sim')
        frame_seguro_vida_nao = config_dataframe.filtrar_colunas(self, frame_entrada_1, 'seguro_vida', 'nao')

        # filtrando seguro residencial
        frame_seguro_residencial_sim = config_dataframe.filtrar_colunas(self, frame_entrada_1, 'seguro_residencial', 'sim')
        frame_seguro_residencial_nao = config_dataframe.filtrar_colunas(self, frame_entrada_1, 'seguro_residencial', 'nao')

        # filtrando capitalizacao
        frame_capitalizacao_sim = config_dataframe.filtrar_colunas(self, frame_entrada_1, 'capitalizacao', 'sim')
        frame_capitalizacao_nao = config_dataframe.filtrar_colunas(self, frame_entrada_1, 'capitalizacao', 'nao')
        
        # filtrando consorcio
        frame_consorcio_sim = config_dataframe.filtrar_colunas(self, frame_entrada_1, 'consorcio', 'sim')
        frame_consorcio_nao = config_dataframe.filtrar_colunas(self, frame_entrada_1, 'consorcio', 'nao')

        # filtrando previdencia privada
        frame_previdencia_sim = config_dataframe.filtrar_colunas(self, frame_entrada_1, 'previdencia_privada', 'sim')
        frame_previdencia_nao = config_dataframe.filtrar_colunas(self, frame_entrada_1, 'previdencia_privada', 'nao')

        def parametros_grafico(df_sim, df_nao, title, area):
            # criando labels          
            labels = ['Sim', 'Não']

            # contagem de elementos sim
            y_sim = df_sim.shape[0]

            # contagem de elementos nao
            y_nao = df_nao.shape[0]

            # agrupando contagem em uma lista
            slice = [y_sim, y_nao]

            # quantidade de barras do grafico
            quantidade_barras = list(range(len(slice))) 

            # plotando o grafico       
            area.bar(quantidade_barras, slice) 

            # setando titulo grafico     
            area.set_title(title, fontweight='bold')

            # setando barras
            area.set_xticks(quantidade_barras)

            # setando legenda barras no eixo x
            area.set_xticklabels(labels)

            # setando titulo eixo 
            area.set_ylabel("frequência absoluta")
            area.set_xlabel("Posse")

            # inserindo total sobre as barras
            for i, v in enumerate(slice):
                area.text(i+0.1, v + 1, str(v), color='blue', fontweight='bold')

            # tornando borda de cima do grafico invisivel
            area.spines['top'].set_visible(False)

            # tornando borda da direita do grafico invisivel
            area.spines['right'].set_visible(False)       
                                
                    
        # grafico        
        # criando area
        area = plt.figure() 

        # criando subgrafico       
        
        # Seguro Auto
        # criando subgrafico
        g1 = area.add_subplot(3,5,1) 

        # criando gráfico
        parametros_grafico(frame_seguro_auto_sim, frame_seguro_auto_nao, "Seguro Auto", g1)     
        
       
        # Seguro vida       
        # criando subgrafico
        g2 = area.add_subplot(3,5,3)  

        # criando gráfico
        parametros_grafico(frame_seguro_vida_sim, frame_seguro_vida_nao, "Seguro Vida", g2)

        
        # Seguro Residencial     
        # criando subgrafico
        g3 = area.add_subplot(3,5,5)  

        # criando gráfico
        parametros_grafico(frame_seguro_residencial_sim, frame_seguro_residencial_nao, "Seguro Residencial", g3)

        
        # Consorcio           
        # criando subgrafico
        g4 = area.add_subplot(3,5,11)  

        # criando gráfico
        parametros_grafico(frame_consorcio_sim, frame_consorcio_nao, "Seguro Residencial", g4)

        # Previdencia                 
        # criando subgrafico
        g5 = area.add_subplot(3,5,13)  

        # criando gráfico
        parametros_grafico(frame_previdencia_sim, frame_previdencia_nao, "Previdência Privada", g5)
        
        # Capitalização            
        # criando subgrafico
        g6 = area.add_subplot(3,5,15)  

        # criando gráfico
        parametros_grafico(frame_capitalizacao_sim, frame_capitalizacao_nao, "Capitalização", g6)

        # maximizando figura na tela
        figManager = plt.get_current_fig_manager()
        figManager.window.state('zoomed')

        # setando titulo da figura
        plt.suptitle("Posse de Produto", fontweight='bold', fontsize=20)
        
        # exibindo
        area.show()       
    
   
    def seguridade(self):               
        def seguridade(produto, opcao): 
            if(opcao == 'geral'):  
                # criando dataframe local
                frame_entrada = df.copy()

                # padronizando sim/nao
                frame_entrada_1 = config_dataframe.alterar_campos_sim_nao(self, frame_entrada, produto)
                
                # criando tela
                tela = Tk()

                # setando tela
                tela.title(produto.upper())

                # configurando modo de exibição
                tela.state("zoomed")

                # criando frame
                frame = Frame(tela)

                # exibindo frame
                frame.grid()  

                # selecionada apenas as colunas que deseja exibir
                frame_entrada_2 = frame_entrada_1[['id', 'nome', produto, 'telefone']]

                # alterando o nome das colunas
                frame_entrada_3 = config_dataframe.alterar_nome_colunas(frame_entrada_2)
            
                # criando tabela       
                table = Table (frame, dataframe=frame_entrada_3, align = 'center', width = (largura - 100), height = (altura - 50), showtoolbar=False, showstatusbar=False)

                # criando lista com os nomes das colunas
                lista_colunas = list(frame_entrada_3.columns)

                # dando enfase na coluna com o nome do produto
                table.columncolors[lista_colunas[2]] = '#FFFF00'             

                # exibindo tabela
                table.show()
                
                # exibindo tela
                tela.mainloop()              
                

            if(opcao == 'sim' or opcao == 'nao'):

                # criando dataframe local
                frame_entrada = df.copy()

                # padronizando sim/nao
                frame_entrada_1 = config_dataframe.alterar_campos_sim_nao(self, frame_entrada, produto)

                # filtrando frame de interesse
                frame_entrada_2 = config_dataframe.filtrar_colunas(self, frame_entrada_1, produto, opcao)
                
                # criando tela
                tela = Tk()

                # setando tela
                tela.title(produto.upper())

                # configurando modo de exibição
                tela.state("zoomed")

                # criando frame
                frame = Frame(tela)

                # exibindo frame
                frame.grid()  

                # selecionada apenas as colunas que deseja exibir
                frame_entrada_3 = frame_entrada_2[['id', 'nome', produto, 'telefone']]

                # alterando o nome das colunas
                frame_entrada_4 = config_dataframe.alterar_nome_colunas(frame_entrada_3)
            
                # criando tabela       
                table = Table (frame, dataframe=frame_entrada_4, align = 'center', width = (largura - 100), height = (altura - 50), showtoolbar=False, showstatusbar=False)
                
                # criando lista com os nomes das colunas
                lista_colunas = list(frame_entrada_4.columns)

                # dando enfase na coluna com o nome do produto
                table.columncolors[lista_colunas[2]] = '#FFFF00'

                # exibindo tabela
                table.show()
                
                # exibindo tela
                tela.mainloop()              
                            
        
        # criando tela
        root = Tk()

        # setando titulo tela
        root.title("Seguridade")

        # setando modo exibicao tela
        root.state('zoomed')  

        # configuracao largura e fonte dos frames
        largura_frames = 200
        fonte_frames = 150
        #padding = '5cm'

        frame_ext = LabelFrame(root, highlightbackground="black",highlightthickness=3, text="Seguridade", font=("TkDefaultFont",15, 'bold'), width=largura_frames) 
        frame_ext.place(x=500, y=100)
        
        def selecao_opcao(produto):
            frame_opcao = LabelFrame(root, text="Posse", highlightbackground="black",highlightthickness=3, font=("TkDefaultFont",15, 'bold'), width=largura_frames) 
            frame_opcao.place(x=700, y=100)

            # configurando tamanho da fonte da opcoes:
            fonte_opcao = 200

            # criando a variacao da opcao
            var_opcao = IntVar(frame_opcao) 

            RO_1 = Radiobutton(frame_opcao, text="Não", variable=var_opcao, value=0, font = fonte_opcao, command=lambda: seguridade(produto, 'nao'))
            RO_1.grid(sticky = W)
       

            RO_2 = Radiobutton(frame_opcao, text="Sim", variable=var_opcao, value=1, font = fonte_opcao, command=lambda: seguridade(produto, 'sim'))
            RO_2.grid(sticky = W)

            RO_3 = Radiobutton(frame_opcao, text="Geral", variable=var_opcao, value=2, font = fonte_opcao, command = lambda: seguridade(produto, 'geral'))
            RO_3.grid(sticky = W)

          

            


        var = IntVar(frame_ext)      
        #var1 = IntVar(frame_ext_2)

        # configurando tamanho fonte dos produtos
        fonte_produtos = 150

        # Produtos
        RP_1 = Radiobutton(frame_ext, text="Seguro Auto", variable=var, value=10, font= fonte_produtos, command = lambda: selecao_opcao("seguro_auto"))
        RP_1.grid(sticky = W)

        RP_2 = Radiobutton(frame_ext, text="Seguro Vida", variable=var, value=20, font= fonte_produtos,command = lambda: selecao_opcao("seguro_vida"))
        RP_2.grid(sticky = W)

        RP_3 = Radiobutton(frame_ext, text="Seguro Residencial", variable=var, value=30, font= fonte_produtos,command = lambda: selecao_opcao("seguro_residencial"))
        RP_3.grid(sticky = W)

        RP_4 = Radiobutton(frame_ext, text="Capitalização", variable=var, value=40, font= fonte_produtos,command = lambda: selecao_opcao("capitalizacao"))
        RP_4.grid(sticky = W)

        RP_5 = Radiobutton(frame_ext, text="Consórcio", variable=var, value=50, font= fonte_produtos,command = lambda: selecao_opcao("consorcio"))
        RP_5.grid(sticky = W)

        RP_6 = Radiobutton(frame_ext, text="Previdência Privada", variable=var, value=60, font= fonte_produtos,command = lambda: selecao_opcao("previdencia_privada"))
        RP_6.grid(sticky = W)       
             
       
        label = Label(root)

        label.place()        
        root.mainloop()


# criando classe limite
class limite:
    def limite_uso(self, df, filtro): 

        # criando dataframe local
        frame_entrada = df.copy()

        # alterar campos sim/nao
        frame_entrada_1 = config_dataframe.alterar_campos_sim_nao(self, frame_entrada, 'usando_limite')

        # filtrando dataframe de interesse
        frame_entrada_2 = config_dataframe.filtrar_colunas(self, frame_entrada_1, 'usando_limite', filtro)        

        # criando tela  
        tela = Tk()

        # setando titulo
        tela.title("Uso de Limite")

        # setando modo de exibição
        tela.state("zoomed")

        # criando frame
        frame = Frame(tela)

        # exibindo frame
        frame.grid()

        # renomeando nome colunas
        frame_entrada_3 = config_dataframe.alterar_nome_colunas(frame_entrada_2)

        # criando tabela
        table = Table (frame, dataframe=frame_entrada_3[['Id', 'Nome', 'Usando Limite', 'Telefone']], align='center',width = (largura - 100), height = (altura - 50), showtoolbar=False, showstatusbar=False)
        
        # enfase na coluna
        table.columncolors['Usando Limite'] = '#FFFF00'

        # exibindo tabela
        table.show()

        # exibindo tela
        tela.mainloop() 

    
    def grafico_usando_sem_uso(self, df): 

        # criando dataframe local
        frame_entrada = df.copy()

        # padronizando campos sim/nao
        frame_entrada_1 = config_dataframe.alterar_campos_sim_nao(self, frame_entrada, 'usando_limite')

        # filtrando entradas sim
        frame_entrada_sim = config_dataframe.filtrar_colunas(self, frame_entrada_1, 'usando_limite', 'sim')
        
        # filtrando entradas nao
        frame_entrada_nao = config_dataframe.filtrar_colunas(self, frame_entrada_1, 'usando_limite', 'nao')
        
        # contando total de instancias em cada filtro
        x = frame_entrada_sim['usando_limite'].count()
        y = frame_entrada_nao['usando_limite'].count()
       
        # agrupando as contagens
        slice = [x, y]

        # criando labels grafico
        labels = ['Sim', 'Não']

        # destacando setor do grafico
        explode = [0.2, 0]

        # criando figura 
        area = plt.figure()

        # criando subplots
        g1 = area.add_subplot(1,2,1)
        g2 = area.add_subplot(1,2,2)

        # criando grafico
        g1.pie(slice, explode=explode, labels=labels, shadow=True, autopct = '%.2f%%')
        g2.bar(labels, slice)

        # setando titulo
        g1.set_title("Uso Limite")

        # exibindo barras horizontais
        g2.grid(axis='y')

        # setando eixo y g2
        g2.set_ylabel('Quantidade')

        # setando titulo
        plt.title("Uso de Limite")

        # maximizando grafico
        figManager = plt.get_current_fig_manager()       
        figManager.window.state('zoomed')  

        # exibindo grafico
        area.show()
     

# Classe de Gráficos
class graficos:
    # graficos de barras
    def grafico_barras(self, x, y, title, xlabel, ylabel):
        #criando grafico
        plt.bar(x, y)
        # setando titulo
        plt.title(title, fontweight='bold')
        # setando eixo x
        plt.xlabel(xlabel, fontweight='bold')
        # setando eixo y
        plt.ylabel(ylabel, fontweight='bold')
        # setando rotacao eixo x
        plt.xticks(rotation = 25) 
        # maximizando grafico
        figManager = plt.get_current_fig_manager()       
        figManager.window.state('zoomed')  
        # exibindo grade
        plt.grid(axis='y')
        # exibindo figura
        plt.show()       

    
    
    # Grafico de pizza que exibe tanto o percentual quanto o total em valores absolutos
    def pie(self, serie, coluna, title, title_legenda):
        
        # defininando o grafico
        fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(aspect = 'equal'))
       
        # rotulos da legenda
        x_val = [serie.index[0], serie.index[1]]        
        
        # colocando os pesos e as porcentagens no grafico
        def func(pct, allvals):
            val_absoluto = int(round(pct/100.*np.sum(allvals)))
            #print(pct)           

            # retornando a legenda
            return "{:.2f}%\n({:d} pessoas)".format(pct, val_absoluto)

        # criando o grafico e colocando a funcao de legenda externa e dando enfase
        explode = [0.2, 0]
        wedges, texts, autotexts = ax.pie(serie, explode=explode, shadow=True, autopct = lambda pct: func(pct, serie),textprops = dict(color = 'w') )

        # definindo a caixa de legenda externa, titulo, localizacao e onde vai ancorar o box
        ax.legend(wedges, x_val, title = title_legenda, loc = 'center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # definindo tamanho do texto dentro e do peso como bold
        plt.setp(autotexts, size=8, weight = "bold")

        # Titulo do Grafico
        ax.set_title(title)

        # maximizando grafico
        figManager = plt.get_current_fig_manager()       
        figManager.window.state('zoomed')  

        # Exibindo
        plt.show()
    

    def boxplot(self, df, coluna, orientacao, title): 
        
        # Criando o gráfico
        plt.boxplot(df[coluna], vert=orientacao)
        
        # Titulo do Grafico
        plt.title(title)

        # maximizando grafico
        figManager = plt.get_current_fig_manager()       
        figManager.window.state('zoomed')  

        # Exibindo
        plt.show()           
        

    #subplot3: significa que a area de plotagem é dividida em tres graficos menores
    def boxplot_subplot3(self, df, coluna1, coluna2, coluna3, title1, title2, title3):
        # criando figura
        area = plt.figure() 
        # criando subgrafico        
        g1 = area.add_subplot(1, 5, 1)
        # criando subgrafico
        g2 = area.add_subplot(1, 5, 3)
        # criando subgrafico
        g3 = area.add_subplot(1, 5, 5)
        # criando grafico
        g1.boxplot(df[coluna1])
        # setando titulo grafico
        g1.set_title(title1)    
       
        # criando grafico
        g2.boxplot(df[coluna2])
        # setando titulo grafico
        g2.set_title(title2)
       
        # criando grafico
        g3.boxplot(df[coluna3])
        # setando titulo grafico
        g3.set_title(title3)

        # maximizando grafico
        figManager = plt.get_current_fig_manager()       
        figManager.window.state('zoomed')  

        # exibindo figura
        area.show()


    def correlacao_geral(self, df):
        # criando dataframe local
        frame_entrada = df.copy()

        # alterando nome das colunas
        frame_entrada_1 = config_dataframe.alterar_nome_colunas(frame_entrada)
      
        # converter valores categoricos em numericos
        le_contratou = LabelEncoder() #para a coluna bmi
        le_cdc = LabelEncoder()
        le_usando_limite = LabelEncoder()
        le_restricao = LabelEncoder()
        le_parcial_fatura = LabelEncoder()
        le_aposentado = LabelEncoder()
        le_sexo = LabelEncoder()

        # aplicando conversao
        frame_entrada_1['Contratou'] = le_contratou.fit_transform(frame_entrada_1['Contratou'])
        frame_entrada_1['CDC'] = le_cdc.fit_transform(frame_entrada_1['CDC'])
        frame_entrada_1['Usando Limite'] = le_usando_limite.fit_transform(frame_entrada_1['Usando Limite'])
        frame_entrada_1['Restrição'] = le_restricao.fit_transform(frame_entrada_1['Restrição'])
        frame_entrada_1['Pgto.Parcial Fatura'] = le_parcial_fatura.fit_transform(frame_entrada_1['Pgto.Parcial Fatura'])
        frame_entrada_1['Aposentado'] = le_aposentado.fit_transform(frame_entrada_1['Aposentado'])
        frame_entrada_1['Sexo'] = le_sexo.fit_transform(frame_entrada_1['Sexo'])

        # calculando correlacao
        corr_df = frame_entrada_1.corr(method='pearson') 

        # criando figura
        plt.figure(figsize=(8, 6))   

        # criando eixos     
        ax = plt.axes()

        #annot mostra os coeficientes da matriz
        # criando matriz de correlaçao com cores
        sns.heatmap(corr_df, annot=True, ax=ax)

        # setando titulo
        ax.set_title('Correlação Geral', fontweight='bold')
        
        # maximizando grafico
        figManager = plt.get_current_fig_manager()       
        figManager.window.state('zoomed')       
        
        # exibindo grafico
        plt.show() 
     
    def correlacao_3_colunas(self, coluna1, coluna2, coluna3, rotulo1, rotulo2, rotulo3):
        # calculando correlacao
        corr_df = df[[coluna1, coluna2, coluna3]].corr(method='pearson')
        # criando rotulos  
        rotulos = [rotulo1, rotulo2, rotulo3]      
        # criando figura
        plt.figure(figsize=(8, 6))      
        # estabelecendo eixos  
        ax = plt.axes()
        # criando grafico
        sns.heatmap(corr_df, annot=True, ax=ax, xticklabels=rotulos, yticklabels=rotulos)
        # setando titulo
        ax.set_title('Correlação')

        # maximizando grafico
        figManager = plt.get_current_fig_manager()       
        figManager.window.state('zoomed')  

        # exibindo grafico
        plt.show() 

    def histograma(self, df, coluna, title, xlabel):  
        # bins = 5?
        # centralizando as barras do gráfico
        # centralizador: xs = [i +0.1 for i, _ in enumerate (df[coluna])]
        # criando grafico
        plt.hist(df[coluna], bins=100, histtype='barstacked')
        
        # setando titulo
        plt.title(title, fontweight='bold')
        # setando eixo x
        plt.xlabel(xlabel, fontweight='bold')
        # setando eixo y
        plt.ylabel('Frequência Absoluta',fontweight='bold') 
       
        # exibindo grade
        plt.grid(axis='y')         

        # rotacionando eixo x 
        plt.xticks(rotation = 90)    
       
        # exibindo valores inteiros no eixo y
        yint = []
        locs, labels = plt.yticks()
        for each in locs:
            yint.append(int(each))
        plt.yticks(yint)

        # maximizando grafico
        figManager = plt.get_current_fig_manager()       
        figManager.window.state('zoomed')  

        # exibindo
        plt.show()     
       
         
    def plot(self, coluna1, coluna2, label, xlabel, ylabel, title) :
        plt.plot(coluna1, coluna2, 'r-o', linewidth = 2.0, label=label)  
        
        #plt.axis([0, 10, 3, 5])
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation = 75)  
        plt.title(title)
        #plt.rcParams['figure.figsize'] = (25,5)
        plt.legend(loc='upper right', fontsize=7)
        #plt.savefig('figura004.png')
        plt.grid()
        plt.show()

    def total_por_ano(self, df, mes, ano):
        # criando frame local
        df = df.copy()      

        #df.index = pd.to_datetime(df.index, errors='coerce')
        # transformando a coluna de data no tipo datetime para usar a biblioteca
        df['data'] = pd.to_datetime(df['data'])

        # ordenando as datas de forma crescente
        df_ordenado = df.sort_values(by='data') 

        # agrupado as datas comuns e somando o total na data
        df_agrupado = df_ordenado.groupby(['data']).valor_empr.sum()

        # obtendo hora/data atual
        currentDateTime = datetime.datetime.now()

        # obtendo data atual
        date = currentDateTime.date()

        # strftime(): string from time
        # outra forma de obter o ano atual (year) e os quatro anos anteriores a ele
        #year = date.strftime("%Y")
        year = int(date.year)        
        year_penultimo = year - 1
        year_antepenultimo = year - 2
        year_pre_antepenultimo = year - 3
        year_pre_pre_antepenultimo = year - 4      

        # transformando YYYY-MM-DD em YYYY
        new_indice = df_agrupado.index.year  
       
        # alterando no dataframe ano-mes-dia para ano
        df_agrupado.index = new_indice

        # somando os valores por ano
        agrupado = df_agrupado.groupby(df_agrupado.index).sum() 
       
        # criando grafico
        plt.bar(agrupado.index, agrupado.values)
        # setando eixo x 
        plt.xticks(agrupado.index)    
        # setando titulo eixo y
        plt.ylabel('Total (R$)', fontsize=15) 
        # setando titulo eixo x  
        plt.xlabel('Ano', fontsize=15)       
        # exibindo
        plt.show()
         
  
        # definindo sel (seleção)
    def filtro_total_ano(self, df):    
        def sel(year, df):           
            # frame local
            frame_entrada = df
            
            #df.index = pd.to_datetime(df.index, errors='coerce')
            # transformando a coluna de data no tipo datetime para usar a biblioteca
            frame_entrada['data'] = pd.to_datetime(frame_entrada['data'])

            # ordenando as datas de forma crescente
            df_ordenado = frame_entrada.sort_values(by='data') 

            # agrupado as datas comuns e somando o total na data
            df_agrupado = df_ordenado.groupby(['data']).valor_empr.sum()
                  
            
            fig = plt.figure()

            rect = [0.1,0.3,0.8,0.5]
            eixo = fig.add_axes(rect)
            #eixo2 = fig.add_axes([0.6,0.6,0.2,0.2])
            eixo.grid(True)  
        
        
            grafico = eixo.plot(df_agrupado.index, df_agrupado.values, color = 'blue', marker="o")
            #eixo.plot(df['data'], df['temperatura'], color = 'green')
            eixo.set_xlim(datetime.datetime(year,1,1),datetime.datetime(year+1,1,1))

            #eixo.set_xlim(datetime.datetime(ano,mes-1,1),datetime.datetime(ano,mes,1))
            #eixo.set_ylim(0,500000) # eixo y de 0 a 50
            eixo.set_title('Total Emprestado x Ano-Mês', fontsize=25, pad = 20)
            eixo.set_ylabel('Total (R$)', fontsize=20)
            eixo.set_xlabel('Data (Ano-Mês)', fontsize=15)          
            eixo.legend(['Total'], loc = 'upper left', fontsize= 7)
            eixo.grid(axis='y')
            plt.show()

        
        # criando dataframe local
        frame_entrada = df.copy()
            
        root = Tk()
        root.title("Empréstimos")
        root.state('zoomed')

        frame1 = LabelFrame(root, text="Selecionar Ano: ", font=("TkDefaultFont",15, 'bold'), padx = 20, pady = 20)
        frame1.place(x=650, y = 150)

        currentDateTime = datetime.datetime.now()
        
        date = currentDateTime.date()

        # strftime(): string from time
        # outra forma de obter o ano atual (year) e os quatro anos anteriores a ele
        #year = date.strftime("%Y")
        year = int(date.year)        
        year_penultimo = year - 1
        year_antepenultimo = year - 2
        year_pre_antepenultimo = year - 3
        year_pre_pre_antepenultimo = year - 4      


        var = IntVar(frame1)
        R1 = Radiobutton(frame1, text=str(year), variable=var, font=60, value=1,command=lambda:sel(year, frame_entrada))
        R1.grid(sticky = W)

        R2 = Radiobutton(frame1, text=str(year-1), variable=var, font=60, value=2,command=lambda:sel(year-1, frame_entrada))
        R2.grid(sticky = W)

        R3 = Radiobutton(frame1, text=str(year-2), variable=var, font=60, value=3,command=lambda:sel(year-2, frame_entrada))
        R3.grid(sticky = W)

        R4 = Radiobutton(frame1, text=str(year-3), variable=var, font=60, value=4,command=lambda:sel(year-3, frame_entrada))
        R4.grid(sticky = W)

        R5 = Radiobutton(frame1, text=str(year-4), variable=var, font=60, value=5,command=lambda:sel(year-4, frame_entrada))
        R5.grid(sticky = W)

            #R3 = Radiobutton(root, text="Option ", variable=var, value=3, command=sel)
            #R3.pack( anchor = W)

        label = Label(root)

        label.place()        
        root.mainloop()

    def filtro_total_ano_mes(self, df):
        def sel(year, df):
            # frame local
            frame_entrada = df

            # alterando data para o tipo datetime           
            frame_entrada['data'] = pd.to_datetime(frame_entrada['data'])

            # criando uma coluna com o ano
            frame_entrada['ano'] = frame_entrada['data'].dt.year

            # criando uma coluna com o mes
            frame_entrada['mes'] = frame_entrada['data'].dt.month
          
            # selecionando apenas o ano de pesquisa
            selecao = frame_entrada['ano'] == year
            filtrado = frame_entrada[selecao]
            
            # Obtendo o valor emprestado por mes
            df_agrupado_mes = filtrado.groupby(filtrado['mes']).valor_empr.sum()
            
            # ordenando as datas de forma crescente
            df_ordenado = df.sort_values(by='data') 

            # agrupado as datas comuns e somando o total na data
            df_agrupado = df_ordenado.groupby(['data']).valor_empr.sum()
                        
            # agrupando por ano
            df_agrupado_por_ano = df_ordenado.groupby(df_ordenado['data'].dt.strftime('%Y'))['valor_empr'].sum()                 
                 
            # criando figura
            fig = plt.figure()  

            # criando subgrafico 
            g1 = fig.add_subplot(3, 4, 4)          

            # estabelecendo medidas do subgrafico
            rect = [0.1,0.3,0.5,0.5]

            # adicionando subgrafico a figura
            eixo = fig.add_axes(rect)
       
            # criando o grafico
            grafico= eixo.plot(df_agrupado.index, df_agrupado.values, color = 'blue', marker="o")
            
            # limitando o intervalo no eixo x
            eixo.set_xlim(datetime.datetime(year,1,1),datetime.datetime(year+1,1,1)) # Apenas um ano  

            # Setando o titulo e eixos
            eixo.set_title('Total Emprestado x Ano-Mês', fontsize=25, pad = 20)
            eixo.set_ylabel('Total (R$)', fontsize=20)
            eixo.set_xlabel('Data (Ano-Mês)', fontsize=15)        

            # Adicionando legenda  
            eixo.legend(['Total'], loc = 'upper left', fontsize= 7)

            # Plotando grafixo
            g1.bar(df_agrupado_mes.index, df_agrupado_mes.values) 
           
            # setando valores das barras no eixo x                                     
            g1.set_xticks(np.arange(0, 13, 1)) 
           
            # setando titulo e eixo y
            g1.set_ylabel("Total (R$)")
            g1.set_xlabel("Mês")
            g1.set_title('Total por Mês - Ano: {}'.format(year))

            # definindo zero como minimo no eixo y
            g1.set_ylim(ymin=0.00)

            # exibindo grades no grafico
            g1.grid(axis='y')

            # criando outro subgrafico
            g2 = fig.add_subplot(3, 4, 12)  

            # plotando subgrafico
            g2.bar(df_agrupado_por_ano.index, df_agrupado_por_ano.values)

            # setando titulo e eixos
            g2.set_xlabel("Ano")
            g2.set_ylabel("Total (R$)")
            g2.set_title('Total por Ano')
            g2.set_xticks(list(df_agrupado_por_ano.index))

            # definindo zero como minimo no eixo y
            g2.set_ylim(ymin=0.00)
                    
            # exibindo grid
            g2.grid(axis='y') 

            # maximizando grafico
            figManager = plt.get_current_fig_manager()
            figManager.window.state('zoomed')    
                                           
            # exibindo figura
            fig.show()        
        
        # criando dataframe local
        frame_entrada = df.copy()
            
        # criando tela
        root = Tk()

        # setando titulo
        root.title("Empréstimos")

        # setando modo exibicao
        root.state('zoomed')

        # criando frame
        frame1 = LabelFrame(root, text="Selecionar Ano: ", font=("TkDefaultFont",15, 'bold'), padx = 20, pady = 20)

        # setando posicao frame
        frame1.place(x=650, y = 150)

        # get na data/horario atual
        currentDateTime = datetime.datetime.now()
        
        # get somente na data
        date = currentDateTime.date()

       # obtendo ultimos cinco anos
        year = int(date.year)        
        year_penultimo = year - 1
        year_antepenultimo = year - 2
        year_pre_antepenultimo = year - 3
        year_pre_pre_antepenultimo = year - 4      

        # criando variavel armazenamento ano interesse
        var = IntVar(frame1)

        # criando botao de selecao
        R1 = Radiobutton(frame1, text=str(year), variable=var, font=60, value=1,command=lambda:sel(year, frame_entrada))
        R1.grid(sticky = W)

        R2 = Radiobutton(frame1, text=str(year-1), variable=var, font=60, value=2,command=lambda:sel(year-1, frame_entrada))
        R2.grid(sticky = W)

        R3 = Radiobutton(frame1, text=str(year-2), variable=var, font=60, value=3,command=lambda:sel(year-2, frame_entrada))
        R3.grid(sticky = W)

        R4 = Radiobutton(frame1, text=str(year-3), variable=var, font=60, value=4,command=lambda:sel(year-3, frame_entrada))
        R4.grid(sticky = W)

        R5 = Radiobutton(frame1, text=str(year-4), variable=var, font=60, value=5,command=lambda:sel(year-4, frame_entrada))
        R5.grid(sticky = W)

            
        # criando label
        label = Label(root)
        
        # exibindo label
        label.place()   

        # exibindo tela     
        root.mainloop()       
             
        

# classe investimentos
class investimentos:   
    
    # Exibir investimentos em ordem crescente/decrescente
    def invest_cresc_desc(self, df):  
        def sel_1(df):         
            frame_entrada = df.copy()  
            tela_1 = Tk()
            tela_1.title("Ordem Crescente")
            tela_1.state("zoomed")
            frame = Frame(tela_1)
            frame.grid()   
            frame_entrada = frame_entrada.rename(columns={'id': 'Id'}) 
            frame_entrada = frame_entrada.rename(columns={'nome': 'Nome'}) 
            frame_entrada = frame_entrada.rename(columns={'investimento': 'Investimento'}) 
            frame_entrada = frame_entrada.rename(columns={'telefone': 'Telefone'})       
            table = Table (frame, dataframe=frame_entrada[['Id', 'Nome', 'Investimento', 'Telefone']].sort_values(by='Investimento'), align='center', width = (largura - 100), height = (altura - 50), showtoolbar=False, showstatusbar=False)
            # destacando coluna
            table.columncolors['Investimento'] = '#FFFF00'
            table.show()
            tela_1.mainloop()   
        
        def sel_2(df):
            frame_entrada = df.copy()  
            tela_1 = Tk()
            tela_1.title("Ordem Decrescente")
            tela_1.state("zoomed")
            frame = Frame(tela_1)
            frame.grid()  
            frame_entrada = frame_entrada.rename(columns={'id': 'Id'}) 
            frame_entrada = frame_entrada.rename(columns={'nome': 'Nome'}) 
            frame_entrada = frame_entrada.rename(columns={'investimento': 'Investimento'}) 
            frame_entrada = frame_entrada.rename(columns={'telefone': 'Telefone'})        
            table = Table (frame, dataframe=frame_entrada[['Id', 'Nome', 'Investimento', 'Telefone']].sort_values(by='Investimento', ascending = False), align='center', width = (largura - 100), height = (altura - 50), showtoolbar=False, showstatusbar=False)
            # destacando coluna
            table.columncolors['Investimento'] = '#FFFF00'
            table.show()
            tela_1.mainloop()

        # criando tela
        root = Tk()
        # setando titulo tela
        root.title("Investimentos em Ordem Crescente x Decrescente")
        # setando modo exibicao
        root.state('zoomed')

        # criando frame
        frame1 = LabelFrame(root, text="Crescente x Decrescente", fg='Dark blue', font=("TkDefaultFont",15, 'bold'),padx = 20, pady = 20)
        # posicionando frame
        frame1.place(x=largura//2, y = (altura//2)-200)

        # criando variavel
        var = IntVar(frame1)
        # criando botao selecao
        R1 = Radiobutton(frame1, text="Crescente", font = ("TkDefaultFont",12), variable=var, value=1,command=lambda:sel_1(df))
        R1.grid(sticky = W)

        # criando botao de selecao
        R2 = Radiobutton(frame1, text="Decrescente", font = ("TkDefaultFont",12),variable=var, value=2,command=lambda:sel_2(df))
        R2.grid(sticky = W)

        # criando label
        label = Label(root)
        # localizando label
        label.place() 
        # exibindo tela       
        root.mainloop()

    
    # graficos
    def investimento_grafico_relplot(self, df):
        # criando frame local
        frame_entrada = df.copy()
        # alterando nome colunas
        frame_entrada_1 = config_dataframe.alterar_nome_colunas(frame_entrada)    
        # criando grafico
        sns.relplot(data=frame_entrada_1, x='Renda', y='Investimento', row="Sexo")

        # maximizando grafico
        figManager = plt.get_current_fig_manager()
        figManager.window.state('zoomed')

        # exibindo grafico
        plt.show()     
    
  
# Classe clientes            
class clientes:        

    # Definindo Setamento os rotulos na consulta por Id
    def set_rotulos(frame_entrada, tela, text, anchor, font, row, column, sticky, posicao_linha, posicao_coluna, font_label, row_label, column_label, sticky_label):
        # Criando label
        label_rotulo = Label(tela, text = text, anchor = anchor, font = font ).grid(row = row, column = column, sticky=sticky)                                        
        
        # criando variavel
        texto = StringVar(tela)    

        # posicionando na linha/coluna desejada        
        dado = frame_entrada.iat[posicao_linha,posicao_coluna]   

        # setar a variavel                          
        texto.set(dado)     

        # criando label                          
        label = Label(tela, textvariable = texto, font = font_label, anchor = anchor).grid(row = row_label, column = column_label, sticky = sticky_label)
        
        # retornado label setado com os parametros desejados
        return label

    # Consultar todos os clientes da base
    def cons_geral(self, df):
        # criando frame local        
        frame_entrada = df.copy()  

        # alterando nome das colunas            
        frame_entrada = config_dataframe.alterar_nome_colunas(frame_entrada)  

        # criando tela 
        tela = Tk()     
        tela.title("Consulta Geral")  
        tela.state('zoomed')    

        # criando frame         
        frame = Frame(tela)       
        frame.grid()  

        # criando tabela       
        table = Table (frame, dataframe=frame_entrada, align = 'center', floatprecision=2,width = (largura - 100), height = (altura - 50), showtoolbar=False, showstatusbar=False)
        
        # exibindo tabela
        table.show()        
        tela.mainloop()   

    # Consultar profissões cadastradas na base
    def listar_profissoes(self, df):
        # criando frame local
        frame_entrada = df.copy()
       
        # criando tela
        tela = Tk()     
        tela.title("Profissões")  
        tela.state('zoomed')

        # criando frame             
        frame = Frame(tela)
        frame.grid()   

        # renomeando a coluna
        frame_entrada_1 = frame_entrada.rename(columns={'profissao': 'Profissão'})       

        # criando tabela   
        table = Table (frame, dataframe=frame_entrada_1[['Profissão']].drop_duplicates(subset = ['Profissão']), width=(largura - 100),height=(altura - 50),showtoolbar=False,showstatusbar=False)
        
        # exibindo tabela
        table.show()
        tela.mainloop()

    # Consultar Id - Clientes cadastrados
    def listar_id(self, df):
        # criando dataframe local
        frame_entrada = df.copy()       

        # criando tela
        tela = Tk()     
        tela.title("Id")  
        tela.state('zoomed')

        # criando frame
        frame = Frame(tela)
        frame.grid()

        # filtrando colunas de interesse  
        frame_entrada = frame_entrada[['id', 'nome']]        

        # renomeando colunas 
        frame_entrada_1 = frame_entrada.rename(columns={'id': 'Id', 'nome': 'Nome'})       
       
        # criando tabela  
        table = Table (frame, dataframe=frame_entrada_1[['Id', 'Nome']].drop_duplicates(subset = ['Id']), width = (largura - 100), height = (altura - 50), showtoolbar=False, showstatusbar=False)
        
        # exibindo tabela        
        table.show()
        tela.mainloop()

    # Consultar clientes pelo ID
    def clientes_cons_id(self, df):       
        def getvalue(frame_entrada): 
            # variavel digitada pelo usuario          
            if(str(mystring.get()).rstrip().lstrip() in frame_entrada['id'].values):  
                # get na entrada digitada pelo usuário, retirando espaçõs anteriores/posteriores        
                entrada = df['id'] == str(mystring.get()).rstrip().lstrip()    
                
                # dataframe filtrado de acordo com entrada do usuário
                frame_entrada = df[entrada] 

                # Tela de exibição 
                tela = Tk()
                tela.title('Consulta por ID')   
                tela.state('zoomed')                            
                             

                # configuracao dos rótulos
                width_rotulos = 60
                place_rotulos = ((largura//2) - (width_rotulos//2))
                bg_rotulos = '#cccccc'
                fg_rotulos = 'black'
                fonte_rotulo = "Arial 13 bold"
                fonte_texto = 'Arial 11'       
                padx_rotulos = 50
                pady_rotulos = 10    
                linha_inicial = 4
                coluna_inicial = 10

                # Configurando margem esquerda
                rotulo_space = Label(tela, font = fonte_rotulo, fg = 'black', width = 10).grid(row=2, column = coluna_inicial - 6, sticky='we', columnspan=2) 
                rotulo_space = Label(tela, font = fonte_rotulo, fg = 'black', width = 10).grid(row=2, column = coluna_inicial - 8, sticky='we', columnspan=2)   


                # informações dos Dados Básicos     
                Label(tela, bg=bg_rotulos, fg=fg_rotulos, text="Dados Básicos", font=fonte_rotulo).grid(row=linha_inicial-1, column=coluna_inicial, sticky='we', columnspan=2)                
                #elementos_tela.rotulos(tela, bg_rotulos, fg_rotulos, "Dados Básicos", fonte_rotulo, linha_inicial-1, coluna_inicial, 'we', 2)                
                clientes.set_rotulos(frame_entrada, tela, "ID: ", W, fonte_texto, linha_inicial, coluna_inicial, W, 0, 0, fonte_texto, linha_inicial, coluna_inicial+1, W)
                clientes.set_rotulos(frame_entrada, tela, "Nome: ", W, fonte_texto, linha_inicial+1, coluna_inicial, W, 0, 1, fonte_texto, linha_inicial+1, coluna_inicial+1, W)
                clientes.set_rotulos(frame_entrada, tela, "Ano Nasc.: ", W, fonte_texto, linha_inicial+2, coluna_inicial, W, 0, 10, fonte_texto, linha_inicial+2, coluna_inicial+1, W)
                clientes.set_rotulos(frame_entrada, tela, "Sexo: ", W, fonte_texto, linha_inicial+3, coluna_inicial, W, 0, 13, fonte_texto, linha_inicial+3, coluna_inicial+1, W)

                # Inserindo quatro espaços entre os campos
                rotulo = Label(tela).grid()
                rotulo = Label(tela).grid()
                rotulo = Label(tela).grid()
                rotulo = Label(tela).grid()
                
                # Informações dos Dados Profissionais
                Label(tela, bg=bg_rotulos, fg=fg_rotulos, text="Dados Profissionais", font=fonte_rotulo).grid(row=linha_inicial+13, column=coluna_inicial, sticky='we', columnspan=2)                 
                clientes.set_rotulos(frame_entrada, tela, "Profissão: ", W, fonte_texto, linha_inicial+14, coluna_inicial, W, 0, 11, fonte_texto, linha_inicial+14, coluna_inicial+1, W)
                clientes.set_rotulos(frame_entrada, tela, "Aposentado: ", W, fonte_texto, linha_inicial+15,coluna_inicial, W, 0, 12, fonte_texto, linha_inicial+15, coluna_inicial+1, W)                  
                clientes.set_rotulos(frame_entrada, tela, "Renda: ", W, fonte_texto, linha_inicial+16,coluna_inicial, W, 0, 20, fonte_texto, linha_inicial+16, coluna_inicial+1, W)                
                

                # Inserindo dois espações entre os campos
                rotulo = Label(tela).grid()
                rotulo = Label(tela).grid()               

                # Inserindo espaço entre as colunas
                rotulo_space = Label(tela, font = fonte_rotulo, fg = 'black', width = 10).grid(row=2, column = coluna_inicial + 3, sticky='we', columnspan=2)  

                # Informações de Seguridade
                Label(tela, bg=bg_rotulos, fg=fg_rotulos, text="Seguridade", font=fonte_rotulo).grid(row=linha_inicial-1, column=coluna_inicial+8, sticky='we', columnspan=2)                
                clientes.set_rotulos(frame_entrada, tela, "Seguro Auto: ", W, fonte_texto, linha_inicial, coluna_inicial+8, W, 0, 23, fonte_texto, linha_inicial, coluna_inicial+9, W)       
                clientes.set_rotulos(frame_entrada, tela, "Seguro Residencial: ", W, fonte_texto, linha_inicial+1, coluna_inicial+8 , W, 0, 24, fonte_texto, linha_inicial+1, coluna_inicial+9, W)                 
                clientes.set_rotulos(frame_entrada, tela, "Seguro Vida: ", W, fonte_texto, linha_inicial+2, coluna_inicial+8 , W, 0, 25, fonte_texto, linha_inicial+2, coluna_inicial+9, W) 
                clientes.set_rotulos(frame_entrada, tela, "Capitalização: ", W, fonte_texto, linha_inicial+3, coluna_inicial+8 , W, 0, 26, fonte_texto, linha_inicial+3, coluna_inicial+9, W)                                 
                clientes.set_rotulos(frame_entrada, tela, "Previdência Privada: ", W, fonte_texto, linha_inicial+4, coluna_inicial+8 , W, 0, 27, fonte_texto, linha_inicial+4, coluna_inicial+9, W) 
                clientes.set_rotulos(frame_entrada, tela, "Consórcios: ", W, fonte_texto, linha_inicial+5, coluna_inicial+8 , W, 0, 28, fonte_texto, linha_inicial+5, coluna_inicial+9, W)                                 

                 # Informações de SCR
                Label(tela, bg=bg_rotulos, fg=fg_rotulos, text="SCR", font=fonte_rotulo).grid(row=linha_inicial+13, column=coluna_inicial+8, sticky='we', columnspan=2)                 
                clientes.set_rotulos(frame_entrada, tela, "SCR Nosso: ", W, fonte_texto, linha_inicial+14, coluna_inicial+8, W, 0, 4, fonte_texto, linha_inicial+14, coluna_inicial+9, W)
                clientes.set_rotulos(frame_entrada, tela, "SCR Outros: ", W, fonte_texto, linha_inicial+15, coluna_inicial+8, W, 0, 5, fonte_texto, linha_inicial+15, coluna_inicial+9, W)
                clientes.set_rotulos(frame_entrada, tela, "SCR Total: ", W, fonte_texto, linha_inicial+16, coluna_inicial+8, W, 0, 6, fonte_texto, linha_inicial+16, coluna_inicial+9, W)

                # Inserindo espaço entre as colunas
                rotulo_space = Label(tela, font = fonte_rotulo, fg = 'black', width = 10).grid(row=2, column = coluna_inicial + 11, sticky='we', columnspan=2)  

                # Informações
                Label(tela, bg=bg_rotulos, fg=fg_rotulos, text="Demais Informações", font=fonte_rotulo).grid(row=linha_inicial-1, column=coluna_inicial+16, sticky='we', columnspan=2)                 
                clientes.set_rotulos(frame_entrada, tela, "Tomou CDC Antes: ", W, fonte_texto, linha_inicial, coluna_inicial+16, W, 0, 3, fonte_texto, linha_inicial, coluna_inicial+17, W)
                clientes.set_rotulos(frame_entrada, tela, "Usando Limite: ", W, fonte_texto, linha_inicial+1, coluna_inicial+16, W, 0, 7, fonte_texto, linha_inicial+1, coluna_inicial+17, W)
                clientes.set_rotulos(frame_entrada, tela, "Hist. Restrição: ", W, fonte_texto, linha_inicial+2, coluna_inicial+16, W, 0, 8, fonte_texto, linha_inicial+2, coluna_inicial+17, W)
                clientes.set_rotulos(frame_entrada, tela, "Pgto. Parcial Cartão: ", W, fonte_texto, linha_inicial+3, coluna_inicial+16, W, 0, 9, fonte_texto, linha_inicial+3, coluna_inicial+17, W)
                clientes.set_rotulos(frame_entrada, tela, "Telefone: ", W, fonte_texto, linha_inicial+4, coluna_inicial+16, W, 0, 21, fonte_texto, linha_inicial+4, coluna_inicial+17, W)

                # Informações de Investimentos
                Label(tela, bg=bg_rotulos, fg=fg_rotulos, text="Investimentos", font=fonte_rotulo).grid(row=linha_inicial+13, column=coluna_inicial+16, sticky='we', columnspan=2)                 
                clientes.set_rotulos(frame_entrada, tela, "Investimentos: ", W, fonte_texto, linha_inicial+14, coluna_inicial+16, W, 0, 2, fonte_texto, linha_inicial+14, coluna_inicial+17, W)
                 
            else:
                # Tela de exibição
                tela = Tk()
                tela.title('Mensagem')
                tela.state('zoomed')

                # Mensagem se o item não for encontrado na base              
                label_nao_encontrado = Label(tela, text="Id não encontrado. Confira/Pesquise o dado inserido e refaça a busca se necessário.", font='Arial 20')                        
                label_nao_encontrado.grid(row = 6, column = 0)

                # Exibindo a tela
                tela.mainloop()

        # criando dataframe local
        frame_entrada = df.copy()

        # Tela de Exibição
        tela = Tk()
        tela.title('Pesquisa ID')
        tela.state('zoomed')           

        # Frame externo ao botão de pesquisa
        frame = LabelFrame(tela, text = 'Pesquisar por ID', font=("TkDefaultFont",15, 'bold'), padx = 20, pady = 20)   
        frame.place(x = 450, y = 50) 

        # Frame externo ao botão de 'listar id'
        frame_1 = LabelFrame(tela, text = 'Listar ID', font = 80, padx = 20, pady = 20)   
        frame_1.place(x = 450, y = 190)         

        # Label do campo de pesquisa
        label_id = Label(frame, text = "Digite o id: ", font = 80)  

        # pegando a string digitada pelo usuario
        mystring = StringVar(tela)    

        # atribuindo o campo digitado pelo usuario a uma variável    
        e_1 = Entry(frame,textvariable = mystring,width=20,fg="blue",bd=3,font = 80, selectbackground='violet')

        # criando o botão de pesquisar
        button_id = Button(frame, text='Pesquisar', fg='White', font =80, bg= 'Dark blue',height = 1, width = 10, command=lambda: getvalue(frame_entrada))

        # criando o botão de listar id
        button_listar_id = Button(frame_1, text='Listar ID', fg='Black',font =80, height = 1, width = 10, command=lambda: clientes.listar_id(self, frame_entrada ))

               
        # Exibindo
        label_id.grid(row = 5, column = 0, sticky = E)
        e_1.grid(row = 5, column = 1, sticky = 'we')    
        button_id.grid(columnspan=2, sticky='we')
        button_listar_id.grid(columnspan = 2, sticky = 'we')
        tela.mainloop()
    
    # Localizar profissões cadastradas
    def clientes_profissao(self, df):  
        def getvalue():
            # valor digitado (sem espaços) e vendo se consta na base
            if(str(profissao.get().rstrip().lstrip().lower()) in df['profissao'].values):
                # filtrando a base pelo item digitado              
                entrada = df['profissao'] == str(profissao.get().rstrip().lstrip().lower())
                # filtrando o dataframe de acordo com o item digitado
                frame_entrada = df[entrada] 
                aposentado_var = StringVar()

                # Alterando nome das colunas do dataframe
                frame_entrada = config_dataframe.alterar_nome_colunas(frame_entrada)

                # Tela de exibição
                tela = Tk()
                tela.title('Dados')
                tela.state('zoomed')

                # Frame da tela                         
                frame = Frame(tela)

                # Exibindo o frame
                frame.grid()   

                # Criando a tabela      
                table = Table (frame, dataframe=frame_entrada, align = 'center', floatprecision=2,width = (largura - 100), height = (altura - 50), showtoolbar=False, showstatusbar=False)
                
                # destacando coluna
                table.columncolors['Profissão'] = '#FFFF00'

                # Exibndo a tabela
                table.show()

                # Exibindo a tela
                tela.mainloop()
            else:
                # Tela de exibição
                tela = Tk()
                tela.title('Dados não encontrados')
                tela.state('zoomed')   

                # mensagem em caso de não encontrar o item digitado                                  
                label_nao_encontrado = Label(tela, text="Profissão não encontrada. Liste as profissões cadastradas e refaça a busca.", font = 'Arial 20').grid(row = 6, column = 0)                               
                
                # Exibindo a tela
                tela.mainloop()
        
        # criando dataframe local
        frame_entrada = df.copy()

        # Criando a tela
        tela = Tk()

        # criando a variável para atribuir o item digitado
        profissao = StringVar(tela) 
        
        # configurando titulo da tela
        tela.title("Pesquisar profissão ")

        # configurando modo de exibicao da tela
        tela.state("zoomed")   

        # criando o frame para pesquisar 
        frame = LabelFrame(tela, text = 'Pesquisar Profissões', font=("TkDefaultFont",15, 'bold'), padx = 20, pady = 20) 

        # localizando o frame na tela  
        frame.place(x = 450, y = 50) 

        # criando frame para listar 
        frame1 = LabelFrame(tela, text = 'Listar Profissões', font =80, padx = 20, pady = 20)

        # localizando o frame na tela   
        frame1.place(x = 450, y = 190) 
        
        # criando label
        label_profissao = Label(frame, text = "Digite a profissao: ", font = 80) 

        # atribuindo entrada a uma variavel       
        e_1 = Entry(frame,textvariable = profissao,width=40,fg="blue",bd=3,selectbackground='violet', font = 80)

        # criando butao de pesquisar
        button_profissao = Button(frame, 
            text='Pesquisar', 
            fg='White', 
            bg= 'Dark blue',height = 1, font = 80, command=getvalue)

        # criando o botação para exibir
        button_listar_profissao = Button(frame1, 
            text='Exibir', 
            fg='Black',
            height = 1, width = 15, font = 80, command=lambda:clientes.listar_profissoes(self, frame_entrada))
        
        # Exibindo
        label_profissao.grid(row = 5, column = 0, sticky = E)
        e_1.grid(row = 5, column = 1, sticky = 'we')    
        button_profissao.grid(columnspan=2, sticky='we')
        button_listar_profissao.grid(columnspan = 2, sticky = 'we')
        tela.mainloop()   


# classe para manipulação do dataframe original
class config_dataframe:
    def query_duas_colunas(self, df, coluna1, filtro_col1, coluna2, filtro_col2):    
        # criando dataframe local
        df = df.copy()

        # excluindo aspas entrada
        coluna1 = coluna1.replace("'", '')

        # excluindo aspas entrada
        coluna2 = coluna2.replace("'", "")

        # criando query
        query = '{} == "{}" & {} == "{}"'.format(coluna1, filtro_col1, coluna2, filtro_col2)

        # aplicando query no dataframe
        frame_entrada = df.query(query)

        # retornando dataframe
        return frame_entrada
    


    # altera o nome das colunas
    def alterar_nome_colunas(df):
        # criando dataframe local
        frame_entrada = df.copy()

        # renomeando as colunas        
        frame_entrada = frame_entrada.rename(columns={'id': 'Id'}) 
        frame_entrada = frame_entrada.rename(columns={'nome': 'Nome'})
        frame_entrada = frame_entrada.rename(columns={'investimento': 'Investimento'})
        frame_entrada = frame_entrada.rename(columns={'cdc_antes': 'CDC'})
        frame_entrada = frame_entrada.rename(columns={'scr_nosso': 'SCR Nosso'})
        frame_entrada = frame_entrada.rename(columns={'scr_outros': 'SCR Outros'})
        frame_entrada = frame_entrada.rename(columns={'scr_total': 'SCR Total'})
        frame_entrada = frame_entrada.rename(columns={'usando_limite': 'Usando Limite'})
        frame_entrada = frame_entrada.rename(columns={'restricao_hist': 'Restrição'})
        frame_entrada = frame_entrada.rename(columns={'pgto_parcial_fatura': 'Pgto.Parcial Fatura'}) 
        frame_entrada = frame_entrada.rename(columns={'ano_nasc': 'Ano Nasc.'}) 
        frame_entrada = frame_entrada.rename(columns={'profissao': 'Profissão'}) 
        frame_entrada = frame_entrada.rename(columns={'aposentado': 'Aposentado'})  
        frame_entrada = frame_entrada.rename(columns={'sexo': 'Sexo'}) 
        frame_entrada = frame_entrada.rename(columns={'valor_empr': 'Valor Emprést.'})  
        frame_entrada = frame_entrada.rename(columns={'tempo_conta': 'Tempo Conta'}) 
        frame_entrada = frame_entrada.rename(columns={'linha': 'Linha'})  
        frame_entrada = frame_entrada.rename(columns={'data': 'Data'})
        frame_entrada = frame_entrada.rename(columns={'contatofone': 'Contato(fone)'})  
        frame_entrada = frame_entrada.rename(columns={'valor_fatura_mes': 'Valor Fatura'}) 
        frame_entrada = frame_entrada.rename(columns={'renda': 'Renda'})         
        frame_entrada = frame_entrada.rename(columns={'telefone': 'Telefone'}) 
        frame_entrada = frame_entrada.rename(columns={'contratou': 'Contratou'})
        frame_entrada = frame_entrada.rename(columns={'seguro_auto': 'Seguro Auto'})
        frame_entrada = frame_entrada.rename(columns={'seguro_residencial': 'Seguro Residencial'})
        frame_entrada = frame_entrada.rename(columns={'seguro_vida': 'Seguro Vida'})
        frame_entrada = frame_entrada.rename(columns={'capitalizacao': 'Capitalização'})
        frame_entrada = frame_entrada.rename(columns={'previdencia_privada': 'Prev.Privada'})
        frame_entrada = frame_entrada.rename(columns={'consorcio': 'Consórcio'})

        # retornando dataframe renomeado
        return frame_entrada

    # alterar tipo de dado das colunas
    def alterar_tipo_dado(df):
        # criando dataframe local
        df = df.copy()

        # alterando o tipo de dado da coluna id para string
        df['id'] = df['id'].astype(str)

        # trocando virgula por ponto na coluna investimento
        df['investimento'] = df['investimento'].str.replace(',','.')

        # alterando o tipo de dado da coluna investimento para float
        df['investimento'] = df['investimento'].astype(float)

        # alterando virgula por ponto na coluna
        df['valor_fatura_mes'] = df['valor_fatura_mes'].str.replace(',','.')

        # alterando o tipo de dado da coluna para float
        df['valor_fatura_mes'] = df['valor_fatura_mes'].astype(float)

        # alterando virgula por ponto na coluna
        df['renda'] = df['renda'].str.replace(',','.')

        # alterando o tipo de dado da coluna para float
        df['renda'] = df['renda'].astype(float)

        # retornando o dataframe
        return df      
    
    # alterar colunas com apenas valores de sim e nao
    def alterar_campos_sim_nao(self, df, coluna):
        # criando dataframe local
        df = df.copy()

        df[coluna] = df[coluna].map(lambda x: x.lower() if isinstance(x,str) else x)

        df[coluna] = df[coluna].replace("~", "")
        
        # retornando o dataframe    
        return df

    # filtrar as colunas de interesse
    def filtrar_colunas(self, df, coluna, filtro):
        dataframe = df

        # selecionando a coluna de interesse     
        selecao = dataframe[coluna]==filtro

        # filtrando o dataframe de interesse
        dataframe= dataframe[selecao]

        # retornando o dataframe
        return dataframe  

    # alterar as profissoes da coluna profissao
    def alterar_profissao(self, df):
        dataframe = df

        # criando um dicionario vazio
        dic = {}

        # laço para tratar cada valor unico da coluna
        for e in dataframe['profissao'].unique():

            # criando um variavel string vazia para armazenar novo nome da profissao            
            profissao = ""   

            # separando as partes da variavel original pelo '_'          
            partes = e.split('_')
            
            # pegando cada parte da palavra separada, 
            for i in partes:
                # Cada para com a letra inicial maiuscula
                maiuscula = i.capitalize()
                # agrupando a nova palavra com cada uma das suas partes
                profissao = profissao + maiuscula + " "
            
            # atribuindo cada nova palavra no dicionario
            dic['%s' %e] = profissao          
        
        # alterando as profissoes originais pelas novas palavras
        dataframe['profissao']=dataframe['profissao'].map(dic)

        # retornado o dataframe
        return dataframe

# Ocultar janela principal
Tk().withdraw()

# abrir arquivo
filename = askopenfilename()

# ler arquivo csv
# alguns parametros opcionais: engine = 'python', error_bad_lines = False, sep = ',')
df = pd.read_csv(filename, sep = ';')

# remover valores nulos para evitar erros
df.dropna(inplace = True) 

# Tela Inicial de Exibição
menu_inicial = Tk()
menu_inicial.state('zoomed')    

# convertendo o tipo de dado da coluna
df = config_dataframe.alterar_tipo_dado(df)       

# criando a classe CDC
class CDC:      
    # filtrando clientes com posse/sem posse
    def CDC_posse(self, df, filtro):
        # criando dataframe local          
        frame_entrada = df.copy()   

        # alterando o nome da colunas
        frame_entrada_1 = config_dataframe.alterar_nome_colunas(frame_entrada)     

        # padronizando os valores de sim e de nao   
        frame_entrada_2 = config_dataframe.alterar_campos_sim_nao(self, frame_entrada_1, 'CDC')

        # filtrando dataframe de interesse
        frame_entrada_3 = config_dataframe.filtrar_colunas(self, frame_entrada_2, 'CDC', filtro)   
      
        # Tela de exibição
        tela = Tk()        
        tela.title('Posse CDC:'+' ' + filtro.upper())
        tela.state('zoomed')

        # frame da tela
        frame = Frame(tela)

        # exibindo frame
        frame.grid()

        # criando tabela
        table = Table (frame, dataframe=frame_entrada_3, align='center', floatprecision=2,width = (largura-100), height = (altura - 50), showtoolbar=False, showstatusbar=False)
        
        # destacando coluna
        table.columncolors['CDC'] = '#FFFF00'
        
        # exibindo tabela
        table.show()

        # exibindo tela
        tela.mainloop()           
    
    
    # Profissao dos Tomadores de Empréstimos
    def profissao_tomadores(self, df, coluna, filtro, coluna_relacionamento, title, xlabel):
        # criando dataframe local
        frame_entrada=df.copy()     

        # padronizando campos sim e nao     
        frame_entrada_1 = config_dataframe.alterar_campos_sim_nao(self, frame_entrada, coluna)

        # filtrando dataframe de interesse
        frame_entrada_2 = config_dataframe.filtrar_colunas(self, frame_entrada_1, coluna, filtro) 

        # alterando os valores da coluna profissao   
        frame_entrada_3 = config_dataframe.alterar_profissao(self, frame_entrada_2)    

        # criando grafico  
        graficos.histograma(self, frame_entrada_3, coluna_relacionamento, title, xlabel)
        
    
    # Faixa de Renda dos Tomadores de Empréstimos
    def renda_tomadores(self, df, coluna, filtro, title, xlabel):
        frame_entrada = df.copy()
        
        # filtrando o dataframe de interesse
        frame_entrada_1 = config_dataframe.filtrar_colunas(self, frame_entrada, coluna, filtro) 

        # criando as classes de renda              
        classes = [0, 1100.00, 2200.00, 3300.00, 4400.00, 5500.00, 1000000.00]

        # criando os rótulos do gráfico
        labels = ['0 a 1100,00', '1100,00 a 2200,00', '2200,00 a 3300,00', '3300,00 a 4400,00', '4400,00 a 5500,00', '5500,00 acima' ]
        
        # criando faixa de classes   
        faixa = pd.cut(frame_entrada_1['renda'], classes, labels = labels, include_lowest = True)   

        # contando
        faixa_contagem = faixa.groupby(faixa.values).count()

        # ordenando de maneira crescente
        faixa_ordenada = faixa_contagem.sort_values(ascending=True)

        # criando grafico
        graficos.grafico_barras(self, faixa_ordenada.index, faixa_ordenada.values, 'CDC x Renda', 'Faixa Renda', 'Frequência Absoluta')
               
    
    # tomadores de empréstimos que possuem e nao possuem restricao
    def restricao_tomadores(self, df, coluna, filtro, title, xlabel): 
        # criando dataframe local      
        frame_entrada=df.copy()

        # extraindo contagem de elementos
        serie = frame_entrada[coluna].value_counts()                  

        # criando o grafico
        graficos.pie(self, serie, 'restricao_hist', 'Posse de Empréstimo', 'Restrição')


    # posse ou nao posse de emprestimos
    def posse(self, df, coluna, title):
        # criando o dataframe local
        frame_entrada=df.copy()

        # extraindo contagem de elementos
        serie = df[coluna].value_counts() 

        # criando o grafico
        graficos.pie(self, serie, 'cdc_antes', 'Posse de Empréstimo', 'Posse')

    

    def filtro_ultimos_anos(self, df):
        # criando frame local
        df = df.copy() 
        
        # somando o total vendido por data
        df2 = df.groupby(['data']).valor_empr.sum()     
             
        # criando o grafico
        graficos.filtro_total_ano_mes(self, df)

    def total_por_ano(self, df):
        # criando frame local
        df = df.copy()
        
        # criando grafico
        graficos.total_por_ano(self,df, 'mes', 'ano')    
    

    def cdc_grafico_relplot_1(self, df):
        # criando frame local
        frame_entrada = df.copy()     

        # alterando nome das colunas
        frame_entrada_1 = config_dataframe.alterar_nome_colunas(frame_entrada)    
        
        # criando o grafico
        sns.relplot(data=frame_entrada_1, x='Renda', y='Investimento', col='Sexo', row="CDC")

        # maximizando grafico
        figManager = plt.get_current_fig_manager()
        figManager.window.state('zoomed')
        
        # exibindo
        plt.show()    
 

# criando classe restricoes
class restricoes:
    # Funções do Menu Restrições
    def restricoes_possui(self,df, filtro):
        # criando datagrame local
        frame_entrada = df.copy() 

        # padronizando sim/nao
        frame_entrada = config_dataframe.alterar_campos_sim_nao(self, frame_entrada, 'restricao_hist')
       
        # filtrando dataframe de interesse       
        frame_entrada = config_dataframe.filtrar_colunas(self, df, 'restricao_hist', filtro)
       
        # criando tela     
        tela = Tk()

        # setando titulo
        tela.title("Restrição: " + filtro)

        # setando modo exibicao
        tela.state("zoomed")

        # criando frame
        frame = Frame(tela)

        # exibindo frame
        frame.grid()

        # renomeando colunas  
        frame_entrada = config_dataframe.alterar_nome_colunas(frame_entrada) 

        # criando tabela
        table = Table (frame, dataframe=frame_entrada[['Id', 'Nome', 'Restrição', 'Telefone']], align='center',width = (largura - 100), height = (altura - 50), showtoolbar=False, showstatusbar=False)
        
        # destacando coluna
        table.columncolors['Restrição'] = '#FFFF00'

        # exibindo tabela        
        table.show()

        # exibindo tela
        tela.mainloop()           

    def restricoes_nao_possui_usando_limite(self, df, coluna1, filtro_col1, coluna2, filtro_col2):
        # criando dataframe local
        df = df.copy()

        # padronizando sim/nao
        df1 = config_dataframe.alterar_campos_sim_nao(self, df, coluna1)
        df2 = config_dataframe.alterar_campos_sim_nao(self, df1, coluna2)
       
        # aplicando query 
        frame_entrada = config_dataframe.query_duas_colunas(self, df2, coluna1, filtro_col1, coluna2, filtro_col2)

        # criando tela
        tela = Tk()

        # setando titulo
        tela.title("Sem restrição e Usando Limite")

        # setando modo de exibicao
        tela.state("zoomed")

        # criando frame
        frame = Frame(tela)

        # exibindo frame
        frame.grid()         
        
        # renomeando colunas
        frame_entrada = config_dataframe.alterar_nome_colunas(frame_entrada)

        # criando tabela
        table = Table (frame, dataframe=frame_entrada[['Id', 'Nome', 'Restrição', 'Usando Limite', 'Telefone']], align='center', floatprecision=2,width = (largura - 100), height = (altura - 50), showtoolbar=False, showstatusbar=False)                
        
        # destacando coluna
        table.columncolors['Restrição'] = '#FFFF00'

        # destacando coluna
        table.columncolors['Usando Limite'] = '#FFFF00'

        # exibindo tabela        
        table.show()

        # exibindo tela
        tela.mainloop()           
    
    def sem_restricao_pagou_parcial_cartao(self, df, coluna1, filtro_col1, coluna2, filtro_col2):
        # criando dataframe local
        df = df.copy()

        # padronizando sim/nao
        df1 = config_dataframe.alterar_campos_sim_nao(self, df, coluna1)
        df2 = config_dataframe.alterar_campos_sim_nao(self, df1, coluna2)
       
        # aplicando query 
        frame_entrada = config_dataframe.query_duas_colunas(self, df2, coluna1, filtro_col1, coluna2, filtro_col2)

        # criando tela
        tela = Tk()

        # setando titulo
        tela.title("Sem restrição e Pagamento Parcial Fatura")

        # setando modo de exibicao
        tela.state("zoomed")

        # criando frame
        frame = Frame(tela)

        # exibindo frame
        frame.grid()         
        
        # renomeando colunas
        frame_entrada = config_dataframe.alterar_nome_colunas(frame_entrada)

        # criando tabela
        table = Table (frame, dataframe=frame_entrada[['Id', 'Nome', 'Restrição', 'Pgto.Parcial Fatura', 'Telefone']], align='center', floatprecision=2,width = (largura - 100), height = (altura - 50), showtoolbar=False, showstatusbar=False)                
                
        # destacando coluna
        table.columncolors['Restrição'] = '#FFFF00'

        # destacando coluna
        table.columncolors['Pgto.Parcial Fatura'] = '#FFFF00'

        # exibindo tabela        
        table.show()

        # exibindo tela
        tela.mainloop()

        
    def sem_restricao_aposentado(self, df, coluna1, filtro_col1, coluna2, filtro_col2):        

        # criando dataframe local
        df = df.copy()

        # padronizando sim/nao
        df1 = config_dataframe.alterar_campos_sim_nao(self, df, coluna1)
        df2 = config_dataframe.alterar_campos_sim_nao(self, df1, coluna2)
       
        # aplicando query 
        frame_entrada = config_dataframe.query_duas_colunas(self, df2, coluna1, filtro_col1, coluna2, filtro_col2)

        # criando tela
        tela = Tk()

        # setando titulo
        tela.title("Sem restrição e Aposentados")

        # setando modo de exibicao
        tela.state("zoomed")

        # criando frame
        frame = Frame(tela)

        # exibindo frame
        frame.grid()         
        
        # renomeando colunas
        frame_entrada = config_dataframe.alterar_nome_colunas(frame_entrada)

        # criando tabela
        table = Table (frame, dataframe=frame_entrada[['Id', 'Nome', 'Restrição', 'Aposentado', 'Telefone']], align='center', floatprecision=2,width = (largura - 100), height = (altura - 50), showtoolbar=False, showstatusbar=False)                
        
        # destacando coluna
        table.columncolors['Restrição'] = '#FFFF00'

        # destacando coluna
        table.columncolors['Aposentado'] = '#FFFF00'
        
        # exibindo tabela        
        table.show()

        # exibindo tela
        tela.mainloop()
    
        
    def grafico_restricoes_sim_nao(self, df): 
        # criando dataframe local
        df = df.copy()

        # padronizando campos sim/nao
        frame_entrada = config_dataframe.alterar_campos_sim_nao(self, df, 'restricao_hist')        

        # filtrando dataframes de interesse
        frame_entrada_sim = config_dataframe.filtrar_colunas(self, frame_entrada, 'restricao_hist', 'sim') #df[entrada_sim]
        frame_entrada_nao = config_dataframe.filtrar_colunas(self, frame_entrada, 'restricao_hist', 'nao') #df[entrada_nao]

        # contagem de sim e nao                                 
        x = frame_entrada_sim['restricao_hist'].count()
        y = frame_entrada_nao['restricao_hist'].count()
        
        # inserindo contagem em uma lista
        slice = [x, y]       
        
        # criando labels
        labels = ['Sim', 'Não']

        # destacando setor grafico de pizza         
        explode = [0.2, 0]      
        
        # criando figura
        area = plt.figure()

        # adicionando subfigura
        g1 = area.add_subplot(1,5,1)

        # criando grafico na subfigura
        g1.pie(slice, explode=explode, labels=labels, shadow=True, autopct = '%.2f%%')

        # setando titulo grafico
        g1.set_title("Restrições(percentual)")

        
        # criando subfigura
        g2 = area.add_subplot(1,5,3)

        # criando grafico na subfigura
        g2.bar(labels, slice)

        # localizando labels no eixo x
        for i, v in enumerate(slice):
            # setando texto acima das barras
            g2.text(i+0.1, v + 1, str(v), color='blue', fontweight='bold')

        # tornando borda de cima do grafico invisivel
        g2.spines['top'].set_visible(False)

        # tornando borda da direita do grafico invisivel
        g2.spines['right'].set_visible(False)

        # setando titulo do grafico
        g2.set_title("Restrições (frequência)")

        # setando titulo eixo y
        g2.set_ylabel("Frequência Absoluta")

        # criando dicionario vazio
        contagem = {}

        # filtrando dataframe de interesse e contando a quantidade de registro em cada um
        frame_entrada_seguro_auto = config_dataframe.query_duas_colunas(self, frame_entrada, 'restricao_hist', 'sim', 'seguro_auto', 'sim')       
        contagem['Seguro Auto'] = frame_entrada_seguro_auto.shape[0]

        
        frame_entrada_seguro_residencial = config_dataframe.query_duas_colunas(self, frame_entrada, 'restricao_hist', 'sim', 'seguro_residencial', 'sim')
        contagem['Seguro Residencial'] = frame_entrada_seguro_residencial.shape[0]

        frame_entrada_seguro_vida = config_dataframe.query_duas_colunas(self, frame_entrada, 'restricao_hist', 'sim', 'seguro_vida', 'sim')
        contagem['Seguro Vida'] = frame_entrada_seguro_vida.shape[0]

        frame_entrada_capitalizacao = config_dataframe.query_duas_colunas(self, frame_entrada, 'restricao_hist', 'sim', 'capitalizacao', 'sim')
        contagem['Capitalizacao'] = frame_entrada_capitalizacao.shape[0]

        frame_entrada_consorcio = config_dataframe.query_duas_colunas(self, frame_entrada, 'restricao_hist', 'sim', 'consorcio', 'sim')
        contagem['Consorcio'] = frame_entrada_consorcio.shape[0]

        frame_entrada_previdencia = config_dataframe.query_duas_colunas(self, frame_entrada, 'restricao_hist', 'sim', 'previdencia_privada', 'sim')
        contagem['Previdencia'] = frame_entrada_previdencia.shape[0]

        frame_entrada_contratou_sim = config_dataframe.query_duas_colunas(self, frame_entrada, 'restricao_hist', 'sim', 'contratou', 'sim')
        contagem['Contratou CDC'] = frame_entrada_contratou_sim.shape[0]

        frame_entrada_contratou_nao = config_dataframe.query_duas_colunas(self, frame_entrada, 'restricao_hist', 'sim', 'contratou', 'nao')
        contagem['Nao Contratou CDC'] = frame_entrada_contratou_nao.shape[0]

        # transformando o dicionado com o produto e quantidade em um dataframe
        dataframe_contagem = pd.DataFrame(list(contagem.items()),
                   columns=['Produto', 'Quantidade'])

        # Criando valores para eixo x e y        
        labels = dataframe_contagem['Produto'].values
        slice = dataframe_contagem['Quantidade'].values
        
        # criando subfigura
        g3 = area.add_subplot(2,3,3)

        # contando a quantidade de barrinhas necessarias para o grafico
        quantidade_barras = list(range(len(labels)))
        
        # criando grafico
        g3.bar(quantidade_barras, slice)

        # localizando texto no eixo y
        for i, v in enumerate(slice):
            g3.text(i+0.1, v + 0.4, str(v), color='blue', fontweight='bold')

        # tornando borda de cima invisivel
        g3.spines['top'].set_visible(False)

        # tornando borda direita invisivel
        g3.spines['right'].set_visible(False)

        # setando titulo
        g3.set_title("Restrições x Posse Produto")

        # setando eixo y
        g3.set_ylabel("Frequência Absoluta")

        # setando labels eixo x
        g3.set_xticklabels(labels)
        
        # valores utilizados no eixo x para plotagem
        plt.xticks(quantidade_barras, rotation=80)

        # maximizando grafico
        figManager = plt.get_current_fig_manager()       
        figManager.window.state('zoomed')  

        # exibindo figura
        area.show()       
         


# Classe estatisticas
class estatisticas:
    def estatisticas(self): 
        # criando tela
        tela = Tk()

        # setando titulo tela
        tela.title("Estatísticas")

        # setando modo exibicao
        tela.state("zoomed")

        # criando frame
        frame = LabelFrame(tela, relief = 'raised', fg = 'Dark blue', font=("TkDefaultFont",15, 'bold'),text = 'Estatísticas', bd = 1, padx = 15, pady = 20)            
        
        # localizando o frame
        frame.place(x = 150, y = 40, width = 1050)

        # criando variaveis para armazenar os valores das estatisticas
        estatisticas_investimento = DoubleVar(frame) 
        estatisticas_scr_nosso = StringVar(frame) 
        estatisticas_scr_outros = StringVar(frame) 
        estatisticas_scr_total = StringVar(frame) 
        estatisticas_valor_empr = StringVar(frame)
        estatisticas_tempo_conta = StringVar(frame)  
        estatisticas_valor_fatura_mes = StringVar(frame)
        estatisticas_renda = StringVar(frame)  
        
        # criando o label com nome das medidas estatisticas
        label_quantidade = Label(frame, font = 'Arial 9 bold', text = 'Quantidade\nMédia\nDesvio Padrão\nMínimo\nPercentil 25\nPercentil 50\nPercentil 75\nMáximo', justify = LEFT, anchor = W, padx = 20).grid(row = 2, column = 0) 
        
        # setando variaveis com as estatísticas
        estatisticas_investimento.set(round(df['investimento'].describe(), 2).to_string(index = False))
        estatisticas_scr_nosso.set(round(df['scr_nosso'].describe(), 2).to_string(index = False))    
        estatisticas_scr_outros.set(round(df['scr_outros'].describe(), 2).to_string(index = False))
        estatisticas_scr_total.set(round(df['scr_total'].describe(), 2).to_string(index = False))
        estatisticas_valor_empr.set(round(df['valor_empr'].describe(), 2).to_string(index = False))
        estatisticas_tempo_conta.set(df['tempo_conta'].describe().astype(int).to_string(index = False))
        estatisticas_valor_fatura_mes.set(round(df['valor_fatura_mes'].describe(), 2).to_string(index = False))
        estatisticas_renda.set(round(df['renda'].describe(), 2).to_string(index = False))
        
        # criando label coluna investimentos
        label11 = Label(frame, text = 'Investimento', justify = CENTER, anchor = CENTER, background='light blue',padx = 10, font = 'Arial 12 bold', fg='black').grid(row = 1, column = 3)
        label1 = Label(frame, textvariable = estatisticas_investimento,justify = RIGHT, anchor = W, padx = 10).grid(row = 2, column = 3) 

        # criando label coluna scr nosso
        label12 = Label(frame, text = 'SCR Nosso', justify = CENTER, anchor = CENTER, background='#00FFFF',padx = 10, font = 'Arial 12 bold', fg='black').grid(row = 1, column = 4)  
        label2 = Label(frame, textvariable = estatisticas_scr_nosso,justify = RIGHT, anchor = W, padx = 10).grid(row = 2, column = 4)

        # criando label coluna scr outros
        label13 = Label(frame, text = 'SCR Outros', justify = CENTER, anchor = CENTER, background='light blue',padx = 10, font = 'Arial 12 bold', fg='black').grid(row = 1, column = 5)   
        label3 = Label(frame, textvariable = estatisticas_scr_outros,justify = RIGHT, anchor = W, padx = 10).grid(row = 2, column = 5)

        # criando label coluna scr total
        label14 = Label(frame, text = 'SCR Total', justify = CENTER, anchor = CENTER, background='#00FFFF',padx = 10, font = 'Arial 12 bold', fg='black').grid(row = 1, column = 6)
        label4 = Label(frame, textvariable = estatisticas_scr_total,justify = RIGHT, anchor = W, padx = 10).grid(row = 2, column = 6)

        # criando label coluna valor emprestado
        label15 = Label(frame, text = 'Valor Empr.', justify = CENTER, anchor = CENTER, background='light blue',padx = 10, font = 'Arial 12 bold', fg='black').grid(row = 1, column = 7)
        label5 = Label(frame, textvariable = estatisticas_valor_empr,justify = RIGHT, anchor = W, padx = 10).grid(row = 2, column = 7)

        # criando label coluna tempo conta
        label16 = Label(frame, text = 'Tempo Conta', justify = CENTER, anchor = CENTER, background='#00FFFF',padx = 10, font = 'Arial 12 bold', fg='black').grid(row = 1, column = 8)
        label6 = Label(frame, textvariable = estatisticas_tempo_conta, justify = RIGHT, anchor = W, padx = 10).grid(row = 2, column = 8)

        # criando label coluna fatura mes
        label17 = Label(frame, text = 'Fatura Mês', justify = CENTER, anchor = CENTER, background='light blue',padx = 10, font = 'Arial 12 bold', fg='black').grid(row = 1, column = 9)
        label7 = Label(frame, textvariable = estatisticas_valor_fatura_mes,justify = RIGHT, anchor = W, padx = 10).grid(row = 2, column = 9)

        # criando label coluna renda
        label18 = Label(frame, text = 'Renda', justify = CENTER, anchor = CENTER, background='#00FFFF',padx = 10, font = 'Arial 12 bold', fg='black').grid(row = 1, column = 10)
        label8 = Label(frame, textvariable = estatisticas_renda,justify = RIGHT, anchor = W, padx = 10).grid(row = 2, column = 10)    
           
        # criando label sexo x tomadores de empréstimo
        frame2 = LabelFrame(tela, relief = 'raised', fg = 'Dark blue', text = 'Contratam Empréstimos', bd = 1, padx = 15, pady = 20)    
        
        # localizando o frame
        frame2.place(x = 150, y = 310)

        # criando a variavel para armazenar a estatistica
        crosstab_var = StringVar(frame2)

        # cruzando as colunas sexo x contratou
        crosstab_vg = pd.crosstab(df['sexo'], df['contratou'], rownames = ['Sexo'], margins = True, margins_name = 'Total')
        
        # setando a variavel com o cruzamento das colunas
        crosstab_var.set(crosstab_vg.to_string(index = False))
        
        # criando os labels
        label_rotulo_cross = Label(frame2, text = 'Sexo\nFem\nMas\nTotal', justify = CENTER, font = 'Arial 10 bold', anchor = CENTER, padx = 5).grid(row = 0, column = 0, sticky = 'we')
        label_cross = Label(frame2, textvariable = crosstab_var,background='light blue',justify = CENTER, anchor = CENTER, padx = 5, font = "Arial 10").grid(row = 0, column = 1, sticky = 'we')      

        # criando frame sexo x usando limite
        frame3 = LabelFrame(tela, relief = 'raised', fg = 'Dark blue', text = 'Aposentados', bd = 1, padx = 15, pady = 20)    
        
        # localizando o frame
        frame3.place(x = 350, y = 310)

        # criando a variavel para armazenar a estatistica
        crosstab_var2 = StringVar(frame3)

        # cruzando a coluna sexo x aposentado
        crosstab_vg2 = pd.crosstab(df['sexo'], df['aposentado'], rownames = ['Sexo'], margins = True, margins_name = 'Total')
        
        # setando a variavel com a estatistica
        crosstab_var2.set(crosstab_vg2.to_string(index = False))
        
        # criando os labels
        label_rotulo_cross2 = Label(frame3, text = 'Sexo\nFem\nMas\nTotal', justify = CENTER, font = 'Arial 10 bold', anchor = CENTER, padx = 5).grid(row = 0, column = 2, sticky = 'we')
        label_cross2 = Label(frame3, textvariable = crosstab_var2, background='light blue',justify = CENTER, anchor = CENTER, padx = 5, font = "Arial 10").grid(row = 0, column = 3, sticky = 'we')

        # criando o frame sexo x usando limite
        frame4 = LabelFrame(tela, relief = 'raised', fg = 'Dark blue', text = 'Usando Limite', bd = 1, padx = 15, pady = 20)    
        
        # localizando o frame
        frame4.place(x = 550, y = 310)

        # criando a variavel para armazenar a estatistica
        crosstab_var3 = StringVar(frame4)

        # cruzando as colunas sexo x usando limite
        crosstab_vg3 = pd.crosstab(df['sexo'], df['usando_limite'], rownames = ['Sexo'], margins = True, margins_name = 'Total')
        crosstab_var3.set(crosstab_vg3.to_string(index = False))
        
        # criando labels
        label_rotulo_cross3 = Label(frame4, text = 'Sexo\nFem\nMas\nTotal', justify = CENTER, font = 'Arial 10 bold', anchor = CENTER, padx = 5).grid(row = 0, column = 4, sticky = 'we')
        label_cross3 = Label(frame4, textvariable = crosstab_var3, background='light blue',justify = CENTER, anchor = CENTER, padx = 5, font = "Arial 10").grid(row = 0, column = 5, sticky = 'we')

        # criando frame sexo x restrição
        frame5 = LabelFrame(tela, relief = 'raised', fg = 'Dark blue', text = 'Restrição em Histórico', bd = 1, padx = 15, pady = 20)    
        
        # localizando o frame
        frame5.place(x = 750, y = 310)
        
        # criando a variavel para armazenar a estatistica
        crosstab_var4 = StringVar(frame5)

        # cruzando as colunas sexo x restricao_hist
        crosstab_vg4 = pd.crosstab(df['sexo'], df['restricao_hist'], rownames = ['Sexo'], margins = True, margins_name = 'Total')
        
        # setando a variavel
        crosstab_var4.set(crosstab_vg4.to_string(index = False))
        
        # criando labels
        label_rotulo_cross4 = Label(frame5, text = 'Sexo\nFem\nMas\nTotal', justify = CENTER, font = 'Arial 10 bold', anchor = CENTER, padx = 5).grid(row = 0, column = 4, sticky = 'we')
        label_cross4 = Label(frame5, textvariable = crosstab_var4, background='light blue',justify = CENTER, anchor = CENTER, padx = 5, font = "Arial 10").grid(row = 0, column = 5, sticky = 'we')

        # criando frame sexo x pagamento_parcial_fatura
        frame6 = LabelFrame(tela, relief = 'raised', fg = 'Dark blue', text = 'Pagamento parcial da fatura', bd = 1, padx = 15, pady = 20)    
        
        # localizando frame        
        frame6.place(x = 990, y = 310)

        # criando variavel para armazenar estatistica
        crosstab_var5 = StringVar(frame6)

        # cruzando as colunas sexo x pgto parcial fatura
        crosstab_vg5 = pd.crosstab(df['sexo'], df['pgto_parcial_fatura'], rownames = ['Sexo'], margins = True, margins_name = 'Total')
        
        # setando variavel com a estatistica
        crosstab_var5.set(crosstab_vg5.to_string(index = False))
        
        # criando labels
        label_rotulo_cross5 = Label(frame6, text = 'Sexo\nFem\nMas\nTotal', justify = CENTER, font = 'Arial 10 bold', anchor = CENTER, padx = 5).grid(row = 0, column = 4, sticky = 'we')
        label_cross5 = Label(frame6, textvariable = crosstab_var5, background='light blue',justify = CENTER, anchor = W, padx = 5, font = "Arial 10").grid(row = 0, column = 5, sticky = 'we')

        # criando metodo do botao 
        def botao_Click():
            # estatisticas das colunas
            df_seguridade = df[['seguro_auto', 'seguro_vida', 'seguro_residencial']].describe()            
            
            # renomeando o indice da coluna
            df_seguridade.rename(index={'count': 'Quantidade registros', 'unique': 'Quant. de valores distintos', 'top': 'Mais frequente', 'freq': 'Frequência'}, inplace=True)
            
            # setando novo indice
            df_seguridade['Estatísticas'] = df_seguridade.index
            
            # ordenando as colunas
            cols = ['Estatísticas', 'seguro_auto', 'seguro_vida', 'seguro_residencial']

            # aplicando ordem das colunas no dataframe
            df_seguridade = df_seguridade[cols]

            # renomeando as colunas
            df_seguridade.rename(columns={'seguro_vida': 'Seguro Vida', 'seguro_auto': 'Seguro Auto', 'seguro_residencial': 'Seguro Residencial'}, inplace=True)

            # criando tela     
            tela = Tk()

            # criando frame
            frame = Frame(tela)

            # exibindo frame
            frame.grid()    

            # criando tabela          
            table = Table (frame, dataframe=df_seguridade, width = 700, align='center', height = 700, showtoolbar=False, showstatusbar=False)
            
            # dando enfase na coluna
            table.columncolors['Estatísticas'] = '#FFFF00' 

            # exibindo coluna
            table.show()

            # exibindo tela
            tela.mainloop()

        def botao_Click_1():
            # estatisticas das colunas
            df_outras_seguridades = df[['consorcio', 'capitalizacao', 'previdencia_privada']].describe()
            
            # renomeando indice
            df_outras_seguridades.rename(index={'count': 'Quantidade registros', 'unique': 'Quant. de valores distintos', 'top': 'Mais frequente', 'freq': 'Frequência'}, inplace=True)
            
            # criando nova coluna
            df_outras_seguridades['Estatísticas'] = df_outras_seguridades.index  

            # ordenando as colunas          
            cols = ['Estatísticas', 'consorcio', 'capitalizacao', 'previdencia_privada']

            # aplicando a ordem das colunas no dataframe
            df_outras_seguridades = df_outras_seguridades[cols] 

            # renomeando a coluna           
            df_outras_seguridades.rename(columns={'consorcio': 'Consorcio', 'capitalizacao': 'Capitalizacao', 'previdencia_privada': 'Previdencia Privada'}, inplace=True)
            
            # criando tela
            tela = Tk()

            # criando frame
            frame = Frame(tela)

            # exibindo frame
            frame.grid() 

            # criando tabela             
            table = Table (frame, dataframe=df_outras_seguridades, width = 700, align='center', height = 700, showtoolbar=False, showstatusbar=False)
            
            # dando enfase na coluna
            table.columncolors['Estatísticas'] = '#FFFF00' 
            
            # exibindo tabela
            table.show()

            # exibindo tela
            tela.mainloop()

        # criando frame botoes
        frame_botoes = LabelFrame(tela, text='Exibir Estatísticas', fg='Dark blue', font=("TkDefaultFont",15, 'bold'),padx = 20, pady = 20)
        
        # localizando frame
        frame_botoes.place(x=150, y=500)

        # criando botao pesquisar categoricos
        botao = Button(
            frame_botoes, 
            text = "Seguros", 
            command=lambda: botao_Click(),
            fg='White', width=20,
            bg= 'Dark blue',height = 1, font = 80
            )
        botao.grid(row=100, column=5)

        # criando botao outras seguridades
        botao_1 = Button(
            frame_botoes, 
            text = "Outras Seguridades", 
            command=lambda: botao_Click_1(),
            fg='White', width=20,
            bg= 'blue',height = 1, font = 80
            ) 
        botao_1.grid(row=100, column=7)

    # criando grafico
    def boxplot_renda(self):    
        # chamando metodo da classe graficos     
        graficos.boxplot(self, df, 'renda', False, 'Boxplot Renda')
        
    # boxplot scr (nosso, outros e total)
    def boxplot_scr(self):    
        # chamando metodo da classe graficos    
        graficos.boxplot_subplot3(self, df, 'scr_nosso', 'scr_outros', 'scr_total', 'SCR Nosso', 'SCR Outros', 'SCR Total')

    # correlacao tre colunas
    def correlacao_3_colunas(self):  
        # chamando metodo da classe graficos    
        graficos.correlacao_3_colunas(self, 'renda', 'investimento', 'scr_total', 'Renda', 'Investimento', 'SCR Total')
            
    # correlacao geral
    def correlacao_geral(self):
        # chamando metodo da classe graficos
        graficos.correlacao_geral(self, df)         
                                
      
# Menu Principal
# Menu Clientes
meu_Menu = Menu(menu_inicial)
clientes_menu = Menu(meu_Menu, tearoff = 0)
clientes_menu.add_command(label = "Listar Clientes", command = lambda: clientes.cons_geral(menu_inicial, df))
clientes_menu.add_command(label = "Pesquisar por Id", command = lambda: clientes.clientes_cons_id(menu_inicial, df))
clientes_menu.add_command(label = "Buscar Profissões", command = lambda: clientes.clientes_profissao(menu_inicial, df))
meu_Menu.add_cascade(label = "Clientes", menu = clientes_menu)

# Menu CDC
CDC_menu = Menu(meu_Menu, tearoff = 0)
CDC_menu.add_command(label = "Listar Tomadores", command = lambda: CDC.CDC_posse(menu_inicial, df, 'sim'))
CDC_menu.add_command(label = "Listar Não Tomadores", command = lambda: CDC.CDC_posse(menu_inicial, df, 'nao'))
CDC_menu.add_command(label = "Gráfico: Profissao x Tomadores", command = lambda: CDC.profissao_tomadores(menu_inicial, df, 'cdc_antes', 'sim', 'profissao', 'Profissão x Tomadores de Empréstimos', 'Profissões'))
CDC_menu.add_command(label = "Gráfico: Renda x Tomadores", command = lambda: CDC.renda_tomadores(menu_inicial, df, 'cdc_antes', 'sim', 'Renda x Tomadores de Empréstimos', 'Faixa de Renda'))
CDC_menu.add_command(label = "Gráfico: Restrição x Tomadores", command = lambda: CDC.restricao_tomadores(menu_inicial, df, 'restricao_hist', 'sim', "Restrição x Tomadores Empréstimos", 'Restrição'))
CDC_menu.add_command(label = "Gráfico: Posse CDC", command = lambda: CDC.posse(menu_inicial, df, 'cdc_antes', "Posse de Empréstimo"))
CDC_menu.add_command(label = "Gráfico: Total Selecionado por Ano", command = lambda: CDC.filtro_ultimos_anos(menu_inicial, df))
CDC_menu.add_command(label = "Gráfico: Scatter", command = lambda: CDC.cdc_grafico_relplot_1(menu_inicial, df))
meu_Menu.add_cascade(label = "CDC", menu = CDC_menu)

# Menu SCR
SCR_menu = Menu(meu_Menu, tearoff = 0)
SCR_menu.add_command(label = "Consultar", command = lambda: SCR.scr_consulta(menu_inicial, df))
SCR_menu.add_command(label = "SCR Total Maior ou Igual", command = lambda: SCR.scr_total_maior_que(menu_inicial, df))
SCR_menu.add_command(label = "SCR Total Menor ou Igual", command = lambda: SCR.scr_total_menor_que(menu_inicial, df))
SCR_menu.add_command(label = "Gráfico", command = lambda: SCR.grafico_pie(menu_inicial, df))
meu_Menu.add_cascade(label = "SCR", menu = SCR_menu)


# Menu Limite
Limite_menu = Menu(meu_Menu, tearoff = 0)
Limite_menu.add_command(label = "Utilizando", command = lambda: limite.limite_uso(menu_inicial, df, 'sim'))
Limite_menu.add_command(label = "Sem Utilização", command = lambda: limite.limite_uso(menu_inicial, df, 'nao'))
Limite_menu.add_command(label = "Gráfico", command = lambda: limite.grafico_usando_sem_uso(menu_inicial, df))
meu_Menu.add_cascade(label = "Limite", menu = Limite_menu)

# Menu Restrições
restricoes_menu = Menu(meu_Menu, tearoff = 0)
restricoes_menu.add_command(label = "Possui", command = lambda: restricoes.restricoes_possui(menu_inicial, df, 'sim'))
restricoes_menu.add_command(label = "Não Possui", command = lambda: restricoes.restricoes_possui(menu_inicial, df, 'nao'))
restricoes_menu.add_command(label = "Não possui restrição E Usando Limite", command = lambda: restricoes.restricoes_nao_possui_usando_limite(menu_inicial, df, 'restricao_hist', 'nao', 'usando_limite', 'sim'))
restricoes_menu.add_command(label = "Não possui restrição E Pagou parcial cartão", command = lambda: restricoes.sem_restricao_pagou_parcial_cartao(menu_inicial, df, 'restricao_hist', 'nao', 'pgto_parcial_fatura', 'sim'))
restricoes_menu.add_command(label = "Não possui restrição E são aposentados", command = lambda: restricoes.sem_restricao_aposentado(menu_inicial, df, 'restricao_hist', 'nao', 'aposentado', 'sim'))
restricoes_menu.add_command(label = "Gráfico", command = lambda: restricoes.grafico_restricoes_sim_nao(menu_inicial, df))
meu_Menu.add_cascade(label = "Restricões", menu = restricoes_menu)

# Menu Investimentos
investimentos_menu = Menu(meu_Menu, tearoff = 0)
investimentos_menu.add_command(label = "Crescente x Decrescente", command = lambda: investimentos.invest_cresc_desc(menu_inicial, df))
investimentos_menu.add_command(label = "Grafico: Scatter Plot", command = lambda: investimentos.investimento_grafico_relplot(menu_inicial, df))
meu_Menu.add_cascade(label = "Investimentos", menu = investimentos_menu)


# Menu Estatisticas
dados_menu = Menu(meu_Menu, tearoff = 0)
dados_menu.add_command(label = "Estatísticas", command = lambda: estatisticas.estatisticas(menu_inicial))
dados_menu.add_command(label = "BoxPlot Renda", command = lambda: estatisticas.boxplot_renda(menu_inicial))
dados_menu.add_command(label = "BoxPlot SCR", command = lambda: estatisticas.boxplot_scr(menu_inicial))
dados_menu.add_command(label = "Correlação Renda/Inv./SCR", command = lambda: estatisticas.correlacao_3_colunas(menu_inicial))
dados_menu.add_command(label = "Correlação Geral", command = lambda: estatisticas.correlacao_geral(menu_inicial))
meu_Menu.add_cascade(label = "Estatísticas", menu = dados_menu)


# Menu Seguridade
seguridade_menu = Menu(meu_Menu, tearoff = 0)
seguridade_menu.add_command(label = "Consultar", command = lambda: seguridade.seguridade(menu_inicial))
seguridade_menu.add_command(label = "Gráfico Percentual", command = lambda: seguridade.grafico_seguridade_pie(menu_inicial, df))
seguridade_menu.add_command(label = "Gráfico Frequência", command = lambda: seguridade.grafico_seguridade_barras(menu_inicial, df))
meu_Menu.add_cascade(label = "Seguridade", menu = seguridade_menu)


# criando menu principal
menu_inicial.config(menu=meu_Menu)

#dando um nome para a aplicacao
menu_inicial.title("Gerenciador TCC")

#manter largura e altura pré-definida, sem possibilidade de alterar pelo usuario
menu_inicial.resizable(0,0)

# configuracao display inicial
larg_screen = menu_inicial.winfo_screenwidth()
alt_screen = menu_inicial.winfo_screenheight()
largura = larg_screen - 100
altura = alt_screen - 50
#print(larg_screen, alt_screen)

# posicao da janela inicial
posicao_x = larg_screen/2 - largura/2
posicao_y = alt_screen/2 - altura/2

# configurando a geometria
menu_inicial.geometry("%dx%d+%d+%d" %(largura, altura, posicao_x, posicao_y))


menu_inicial.mainloop()
