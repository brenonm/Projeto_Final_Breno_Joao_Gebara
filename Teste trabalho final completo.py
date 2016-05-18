# -*- coding: utf-8 -*-
"""
Created on Sun May  1 20:21:42 2016

@author: Breno
"""
import tkinter as tk




import random

class Batalha:
    def __init__(self):
        self.jogadas=[]
        self.matriz_1=[[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],
                     [21,22,23,24,25,26,27,28,29,30],[31,32,33,34,35,36,37,38,39,40],
                     [41,42,43,44,45,46,47,48,49,50],[51,52,53,54,55,56,57,58,59,60],
                     [61,62,63,64,65,66,67,68,69,70],[71,72,73,74,75,76,77,78,79,80],
                     [81,82,83,84,85,89,90],[91,92,93,94,95,96,97,98,99,100]]
        
        self.matriz_2=[[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],
                     [21,22,23,24,25,26,27,28,29,30],[31,32,33,34,35,36,37,38,39,40],
                     [41,42,43,44,45,46,47,48,49,50],[51,52,53,54,55,56,57,58,59,60],
                     [61,62,63,64,65,66,67,68,69,70],[71,72,73,74,75,76,77,78,79,80],
                     [81,82,83,84,85,89,90],[91,92,93,94,95,96,97,98,99,100]]
         
    def vez_jogador(self,linha,coluna):  
        if len(self.jogadas) % 2 == 0:
            self.matriz_1[linha][coluna]='jogador 1'
            self.jogadas.append(1)  
            self.proxima='jogador 2'
            return 'jogador 1' 
        else: 
            self.matriz_1[linha][coluna]='jogador 1' 
            self.jogadas.append(1)  
            self.proxima='jogador 1'
            return 'jogador 2' 
        print(self.matriz_1)




class Barco:
    nada = 0
    água = 1
    acerto = 2
    afundou = 3
    outro = -1
    
    tamahos = {
        "a" : 5,
        "b" : 4,
        "d" : 3,
        "s" : 3,
        "m" : 2
    }
    
    abreviações = [
        "a",
        "b",
        "d",
        "s",
        "m"
    ]
    
    nomes = {
        "a" : "porta-aviões",
        "b" : "cruzador",
        "d" : "navio",
        "s" : "patrulheiro",
        "m" : "bote"
    }
    
    confirmações = {
        nada : "nada",
        água : "água",
        acerto : "acerto",
        afundou : "afundou"
    }
    
    embarcações = [
       
        "porta-aviões",
        "cruzador",
        "navio",
        "patrulheiro",
        "bote"

    ]



    @staticmethod
    def adquirir_nome_estado(state):
        
        return {Barco.nada : "nada",
                Barco.acerto : "acerto",
                Barco.afundou : "afundou"} [state]

    def __init__(self, x=None, y=None, type=None, vertical=None):
        
        self._x = x
        self._y = y
        self._type = type
        self._vertical = vertical
        self._nome_completo = None
        
        if self._type is not None:
            assert self._type in self.tamanhos.keys()
            self._tamanhos = Barco.tamanhos[self._type]
            
            for nomes in self.Barco:
                if nomes.lower()[0] == self._type:
                    self._nome_completo = nomes
                    break
        
        self._acerto = set([])


    def teste_vertical(self):
        
        return self._vertical
        
    def coordenadas(self):

        return (self._x, self._y)
        
    def origem(self):
        
        return self.coords()
        
    def get_size(self):
    
        return self._size
        
    def quadrados_ocupados(self):
        
        if self._vertical:
            return [(self._x, self._y + i) for i in range(self._size)]
        else:
            return [(self._x + i, self._y) for i in range(self._size)]
            
    def get_covering_set(self):
        '''Return the *set* of covering squares.'''
        
        return set(self.get_covering_squares())
        
    def lista_acertos(self):
        
        return [coord in self._hit for coord in self.get_covering_squares()]
        
    def marcador(self, x, y):
    
        self._hit.add((x, y))
        
    def rotate(self):
        
        self._vertical = not self._vertical

    def conflito_posição_barcos(self, other):
        
        s1 = self.get_covering_set()
        s2 = other.get_covering_set()
        return len(s1.intersection(s2)) > 0
        
    def get_nome(self):
    
        return self._type
        
    def get_abreviação(self):
        
        return self._type
        
    def get_nome_completo(self):
        
        return self._full_name
        
    def teste_afundou(self):
    
        return len(self._acerto) == self._tamanhos
        
    def _get_str_v(self):
        if self._vertical:
            return "vertical"
        else:
            return "horizontal"
        
    def __str__(self):
        return "Barco %s @ %s orientado %sly" % (self._type, str((self._x, self._y)), self._get_str_v())

class Carrega_Barco(object):
    '''Load ship object from a file.'''
    
    @staticmethod
    def read(fname):
        f = open(fname)
        barcos = []
        
        for line in f:
            if len(line.strip()) == 0 or line.strip().count(" ") != 3:
                continue
                
            barco_type, x, y, v = l = line.strip().split()
            
            if barco_type in Barco.tamanhos:
                barcos = Barco(x=int(x), y=int(y), type=barco_type, vertical=v)
                embarcações.append(barcos)
                
        f.close()
                
        return embarcações

class ShipPlacementPanel:
    '''A frame which contains visualizations for placing ships.'''
    
    # the size of a single tile
    SHIP_TILE_SIZE = 20
    SHIP_TILE_COLOR = "steel blue"
    TAG = "staging_ship"
    CANVAS_WIDTH = 150

    def __init__(self):
        '''Create a new panel with the given parent.'''
        self._ship_name = StringVar()
        
        
    def _draw_staged_ship(self):
        '''Draw the curren.'''
        
        # remove prior drawings
        self._clear_staging_grid()
        
        if self._staged_ship.is_vertical():
            x = 0
            x_pad = (self._c.winfo_width() - self.SHIP_TILE_SIZE) / 2.0
            y_pad = (self._c.winfo_height() - self.SHIP_TILE_SIZE * self._staged_ship.get_size()) / 2.0
        
            for y in range(self._staged_ship.get_size()):
                self._draw_ship_tile(
                    x_pad + x * self.SHIP_TILE_SIZE, 
                    y_pad + y * self.SHIP_TILE_SIZE)
        else:
            y = 0
            x_pad = (self._c.winfo_width() - self.SHIP_TILE_SIZE * self._staged_ship.get_size()) / 2.0
            y_pad = (self._c.winfo_height() - self.SHIP_TILE_SIZE) / 2.0
            
            for x in range(self._staged_ship.get_size()):
                self._draw_ship_tile(
                    x_pad + x * self.SHIP_TILE_SIZE, 
                    y_pad + y * self.SHIP_TILE_SIZE)

import socket

class Pagina_Inicial:

    def __init__(self):


        self.window=tk.Tk()
        self.window.title("Batalha Naval")
        self.window.geometry("400x400")
        self.window.wm_iconbitmap("icone.ico")
     


        #foto = ImageTk.PhotoImage(Image.open("titulo.gif"))
        #panel = Label(root, image = foto)
        #panel.pack(side = "bottom", fill = "both", expand = "yes")

        #photo = tk.PhotoImage(file="titulo.gif")
        #w = tk.Label(window, image=photo)
        #w.pack()

        titulo=tk.Label(self.window, text="B4T4LH4 N4V4L", font=("Helvetica", 28))
        titulo.pack(side = "top",fill="both", expand="yes")

        self.check=tk.Button(self.window, text="servidor", font=("Helvetica", 26))
        self.check2=tk.Button(self.window, text="cliente", font=("Helvetica", 26))
        cmd=lambda: self.callback2()
        self.check.configure(command=cmd, fg="blue")
        cmd2=lambda: self.callback()
        self.check2.configure(command=cmd2, fg="blue")
        self.check.pack(side = "top", fill = "both", expand = "yes")
        self.check2.pack(side = "top", fill = "both", expand = "yes")
        
      
      
    
    def callback(self):
        self.entrada_ip=tk.Entry(self.window)
        self.entrada_ip.pack(side = "top", expand = "yes")
        self.conectar=tk.Button(self.window, text="Conectar", font=("Helvetica", 26), fg="blue")
        cmd3=lambda: self.pegarip()
        self.conectar.configure(command=cmd3)
        self.conectar.pack(side = "top", expand = "yes")
        self.check.pack_forget()
        self.check2.pack_forget()
        self.server = 0     # Endereco IP do Servidor
        porta = 5000            # Porta que o Servidor esta
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.dest = (self.server, porta)
        
    def pegarip(self):
    
        self.server=self.entrada_ip.get()
        self.tcp.connect(self.dest) 
        Tabuleiro().window.mainloop()



    def callback2(self):
        self.aguardando=tk.Label(self.window, text="Erro na Conexão", font=("Helvetica", 26))
        self.aguardando.pack(side = "top", fill = "both", expand = "yes")   
        self.check.pack_forget()
        self.check2.pack_forget()
        host= '0.0.0.0' #Servidor interno
        porta= 5000 #Porta de comunicação
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Define metodo como TCP (SOCK_STREAM)
        orig=(host,porta)
        tcp.bind(orig)
        tcp.listen(1)
        self.con, cliente = tcp.accept()
        Tabuleiro().window.mainloop()

            
                

    

class Tabuleiro:
    
    inicio=Pagina_Inicial()

    def __init__(self):

        self.window=tk.Tk()
        self.window.title("Batalha Naval")
        self.window.configure(width=800, height=800)
        self.window.wm_iconbitmap('icone.ico')

       
    

        A=tk.Label(self.window, text="A")
        A.grid(row=0, column=1)

        B=tk.Label(self.window, text="B")
        B.grid(row=0, column=2)

        C=tk.Label(self.window, text="C")
        C.grid(row=0, column=3)

        D=tk.Label(self.window, text="D")
        D.grid(row=0, column=4)

        E=tk.Label(self.window, text="E")
        E.grid(row=0, column=5)

        F=tk.Label(self.window, text="F")
        F.grid(row=0, column=6)

        G=tk.Label(self.window, text="G")
        G.grid(row=0, column=7)

        H=tk.Label(self.window, text="H")
        H.grid(row=0, column=8)

        I=tk.Label(self.window, text="I")
        I.grid(row=0, column=9)

        J=tk.Label(self.window, text="J")
        J.grid(row=0, column=10)

        espaco=tk.Label(self.window , text='                        ')
        espaco.grid(row=0, column=11)

        A=tk.Label(self.window, text="A")
        A.grid(row=0, column=13)

        B=tk.Label(self.window, text="B")
        B.grid(row=0, column=14)

        C=tk.Label(self.window, text="C")
        C.grid(row=0, column=15)

        D=tk.Label(self.window, text="D")
        D.grid(row=0, column=16)

        E=tk.Label(self.window, text="E")
        E.grid(row=0, column=17)

        F=tk.Label(self.window, text="F")
        F.grid(row=0, column=18)

        G=tk.Label(self.window, text="G")
        G.grid(row=0, column=19)

        H=tk.Label(self.window, text="H")
        H.grid(row=0, column=20)

        I=tk.Label(self.window, text="I")
        I.grid(row=0, column=21)

        J=tk.Label(self.window, text="J")
        J.grid(row=0, column=22)
        

        numero1=tk.Label(self.window, text="1")
        numero1.grid(row=1,column=23)

        numero2=tk.Label(self.window, text="2")
        numero2.grid(row=2,column=23)

        numero3=tk.Label(self.window, text="3")
        numero3.grid(row=3,column=23)

        numero4=tk.Label(self.window, text="4")
        numero4.grid(row=4,column=23)

        numero5=tk.Label(self.window, text="5")
        numero5.grid(row=5,column=23)

        numero6=tk.Label(self.window, text="6")
        numero6.grid(row=6,column=23)

        numero7=tk.Label(self.window, text="7")
        numero7.grid(row=7,column=23)

        numero8=tk.Label(self.window, text="8")
        numero8.grid(row=8,column=23)

        numero9=tk.Label(self.window, text="9")
        numero9.grid(row=9,column=23)

        numero10=tk.Label(self.window, text="10")
        numero10.grid(row=10,column=23)

        numero1=tk.Label(self.window, text="1")
        numero1.grid(row=1,column=0)

        numero2=tk.Label(self.window, text="2")
        numero2.grid(row=2,column=0)

        numero3=tk.Label(self.window, text="3")
        numero3.grid(row=3,column=0)

        numero4=tk.Label(self.window, text="4")
        numero4.grid(row=4,column=0)

        numero5=tk.Label(self.window, text="5")
        numero5.grid(row=5,column=0)

        numero6=tk.Label(self.window, text="6")
        numero6.grid(row=6,column=0)

        numero7=tk.Label(self.window, text="7")
        numero7.grid(row=7,column=0)

        numero8=tk.Label(self.window, text="8")
        numero8.grid(row=8,column=0)

        numero9=tk.Label(self.window, text="9")
        numero9.grid(row=9,column=0)

        numero10=tk.Label(self.window, text="10")
        numero10.grid(row=10,column=0)


        i=0
        j=0

    
        

        for i in range(1,11):
            for j in range(1,11):
                self.button=tk.Button(self.window)
                cmd = lambda i=i, j=j: self.button_callback(i,j)
                self.button.configure(width=6, height=3, command=cmd)
                self.button.grid(row=i, column=j)

        n=0
        m=0

        for n in range(1,11):
            for m in range(13,23):
                self.botao=tk.Button(self.window)
                cmd=lambda n=n, m=m: self.button_callback(n,m)
                self.botao.configure(width=6, height=3, command=cmd)
                self.botao.grid(row=n, column=m)
    

    def button_callback(self, row, column):
        msg=(str(row) + " , " + str(column))
        self.inicio.con.send(msg.encode('utf-8'))




PaginaInicial=Pagina_Inicial()
PaginaInicial.window.mainloop()
Tabuleiro=Tabuleiro()
Tabuleiro.window.mainloop()
ShipPlacementPanel=ShipPlacementPanel()
Carrega_Barco=Carrega_Barco()
Batalha=Batalha()
