# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 17:09:54 2016

@author: Breno
"""


# http://stackoverflow.com/questions/20717203/python-tkinter-setting-up-button-callback-functions-with-a-loop LAMBDA

import tkinter as tk
import socket

class Tabuleiro:
    

    def __init__(self):

        self.window=tk.Tk()
        self.window.title("Batalha Naval")
        self.window.configure(width=800, height=800)


            

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
                self.button.configure(width=6, height=3, fg='yellow', command=cmd)
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
        con.send(msg.encode('utf-8'))



host= '0.0.0.0' #Servidor interno
porta= 5000 #Porta de comunicação
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Define metodo como TCP (SOCK_STREAM)
orig=(host,porta)
tcp.bind(orig)
tcp.listen(1)
con, cliente = tcp.accept()


Tabuleiro=Tabuleiro()
Tabuleiro.window.mainloop()


