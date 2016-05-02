# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 17:09:54 2016

@author: Breno
"""

import tkinter as tk

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





        self.botao1=tk.Button(self.window)
        self.botao1.configure(height=4, width=8)
        self.botao1.grid(row=1, column=1)

        self.botao2=tk.Button(self.window)
        self.botao2.configure(height=4, width=8)
        self.botao2.grid(row=1, column=2)

        self.botao3=tk.Button(self.window)
        self.botao3.configure(height=4, width=8)
        self.botao3.grid(row=1, column=3)

        self.botao4=tk.Button(self.window)
        self.botao4.configure(height=4, width=8)
        self.botao4.grid(row=1, column=4)

        self.botao5=tk.Button(self.window)
        self.botao5.configure(height=4, width=8)
        self.botao5.grid(row=1, column=5)

        self.botao6=tk.Button(self.window)
        self.botao6.configure(height=4, width=8)
        self.botao6.grid(row=1, column=6)

        self.botao7=tk.Button(self.window)
        self.botao7.configure(height=4, width=8)
        self.botao7.grid(row=1, column=7)

        self.botao8=tk.Button(self.window)
        self.botao8.configure(height=4, width=8)
        self.botao8.grid(row=1, column=8)

        self.botao9=tk.Button(self.window)
        self.botao9.configure(height=4, width=8)
        self.botao9.grid(row=1, column=9)

        self.botao10=tk.Button(self.window)
        self.botao10.configure(height=4, width=8)
        self.botao10.grid(row=1, column=10)

        self.botao11=tk.Button(self.window)
        self.botao11.configure(height=4, width=8)
        self.botao11.grid(row=2, column=1)

        self.botao12=tk.Button(self.window)
        self.botao12.configure(height=4, width=8)
        self.botao12.grid(row=2, column=2)

        self.botao13=tk.Button(self.window)
        self.botao13.configure(height=4, width=8)
        self.botao13.grid(row=2, column=3)

        self.botao14=tk.Button(self.window)
        self.botao14.configure(height=4, width=8)
        self.botao14.grid(row=2, column=4)

        self.botao15=tk.Button(self.window)
        self.botao15.configure(height=4, width=8)
        self.botao15.grid(row=2, column=5)

        self.botao16=tk.Button(self.window)
        self.botao16.configure(height=4, width=8)
        self.botao16.grid(row=2, column=6)

        self.botao17=tk.Button(self.window)
        self.botao17.configure(height=4, width=8)
        self.botao17.grid(row=2, column=7)

        self.botao18=tk.Button(self.window)
        self.botao18.configure(height=4, width=8)
        self.botao18.grid(row=2, column=8)

        self.botao19=tk.Button(self.window)
        self.botao19.configure(height=4, width=8)
        self.botao19.grid(row=2, column=9)

        self.botao20=tk.Button(self.window)
        self.botao20.configure(height=4, width=8)
        self.botao20.grid(row=2, column=10)

        self.botao21=tk.Button(self.window)
        self.botao21.configure(height=4, width=8)
        self.botao21.grid(row=3, column=1)

        self.botao22=tk.Button(self.window)
        self.botao22.configure(height=4, width=8)
        self.botao22.grid(row=3, column=2)

        self.botao23=tk.Button(self.window)
        self.botao23.configure(height=4, width=8)
        self.botao23.grid(row=3, column=3)

        self.botao24=tk.Button(self.window)
        self.botao24.configure(height=4, width=8)
        self.botao24.grid(row=3, column=4)

        self.botao25=tk.Button(self.window)
        self.botao25.configure(height=4, width=8)
        self.botao25.grid(row=3, column=5)

        self.botao26=tk.Button(self.window)
        self.botao26.configure(height=4, width=8)
        self.botao26.grid(row=3, column=6)

        self.botao27=tk.Button(self.window)
        self.botao27.configure(height=4, width=8)
        self.botao27.grid(row=3, column=7)

        self.botao28=tk.Button(self.window)
        self.botao28.configure(height=4, width=8)
        self.botao28.grid(row=3, column=8)

        self.botao29=tk.Button(self.window)
        self.botao29.configure(height=4, width=8)
        self.botao29.grid(row=3, column=9)

        self.botao30=tk.Button(self.window)
        self.botao30.configure(height=4, width=8)
        self.botao30.grid(row=3, column=10)

        self.botao31=tk.Button(self.window)
        self.botao31.configure(height=4, width=8)
        self.botao31.grid(row=4, column=1)

        self.botao32=tk.Button(self.window)
        self.botao32.configure(height=4, width=8)
        self.botao32.grid(row=4, column=2)

        self.botao33=tk.Button(self.window)
        self.botao33.configure(height=4, width=8)
        self.botao33.grid(row=4, column=3)

        self.botao34=tk.Button(self.window)
        self.botao34.configure(height=4, width=8)
        self.botao34.grid(row=4, column=4)

        self.botao35=tk.Button(self.window)
        self.botao35.configure(height=4, width=8)
        self.botao35.grid(row=4, column=5)

        self.botao36=tk.Button(self.window)
        self.botao36.configure(height=4, width=8)
        self.botao36.grid(row=4, column=6)

        self.botao37=tk.Button(self.window)
        self.botao37.configure(height=4, width=8)
        self.botao37.grid(row=4, column=7)

        self.botao38=tk.Button(self.window)
        self.botao38.configure(height=4, width=8)
        self.botao38.grid(row=4, column=8)

        self.botao39=tk.Button(self.window)
        self.botao39.configure(height=4, width=8)
        self.botao39.grid(row=4, column=9)

        self.botao40=tk.Button(self.window)
        self.botao40.configure(height=4, width=8)
        self.botao40.grid(row=4, column=10) 

        self.botao41=tk.Button(self.window)
        self.botao41.configure(height=4, width=8)
        self.botao41.grid(row=5, column=1)

        self.botao42=tk.Button(self.window)
        self.botao42.configure(height=4, width=8)
        self.botao42.grid(row=5, column=2)

        self.botao43=tk.Button(self.window)
        self.botao43.configure(height=4, width=8)
        self.botao43.grid(row=5, column=3)

        self.botao44=tk.Button(self.window)
        self.botao44.configure(height=4, width=8)
        self.botao44.grid(row=5, column=4)

        self.botao45=tk.Button(self.window)
        self.botao45.configure(height=4, width=8)
        self.botao45.grid(row=5, column=5)

        self.botao46=tk.Button(self.window)
        self.botao46.configure(height=4, width=8)
        self.botao46.grid(row=5, column=6)

        self.botao47=tk.Button(self.window)
        self.botao47.configure(height=4, width=8)
        self.botao47.grid(row=5, column=7)

        self.botao48=tk.Button(self.window)
        self.botao48.configure(height=4, width=8)
        self.botao48.grid(row=5, column=8)

        self.botao49=tk.Button(self.window)
        self.botao49.configure(height=4, width=8)
        self.botao49.grid(row=5, column=9)

        self.botao50=tk.Button(self.window)
        self.botao50.configure(height=4, width=8)
        self.botao50.grid(row=5, column=10)

        self.botao51=tk.Button(self.window)
        self.botao51.configure(height=4, width=8)
        self.botao51.grid(row=6, column=1)

        self.botao52=tk.Button(self.window)
        self.botao52.configure(height=4, width=8)
        self.botao52.grid(row=6, column=2)

        self.botao53=tk.Button(self.window)
        self.botao53.configure(height=4, width=8)
        self.botao53.grid(row=6, column=3)

        self.botao54=tk.Button(self.window)
        self.botao54.configure(height=4, width=8)
        self.botao54.grid(row=6, column=4)

        self.botao55=tk.Button(self.window)
        self.botao55.configure(height=4, width=8)
        self.botao55.grid(row=6, column=5)

        self.botao56=tk.Button(self.window)
        self.botao56.configure(height=4, width=8)
        self.botao56.grid(row=6, column=6)

        self.botao57=tk.Button(self.window)
        self.botao57.configure(height=4, width=8)
        self.botao57.grid(row=6, column=7)

        self.botao58=tk.Button(self.window)
        self.botao58.configure(height=4, width=8)
        self.botao58.grid(row=6, column=8)

        self.botao59=tk.Button(self.window)
        self.botao59.configure(height=4, width=8)
        self.botao59.grid(row=6, column=9)

        self.botao60=tk.Button(self.window)
        self.botao60.configure(height=4, width=8)
        self.botao60.grid(row=6, column=10)

        self.botao61=tk.Button(self.window)
        self.botao61.configure(height=4, width=8)
        self.botao61.grid(row=7, column=1)

        self.botao62=tk.Button(self.window)
        self.botao62.configure(height=4, width=8)
        self.botao62.grid(row=7, column=2)

        self.botao63=tk.Button(self.window)
        self.botao63.configure(height=4, width=8)
        self.botao63.grid(row=7, column=3)

        self.botao64=tk.Button(self.window)
        self.botao64.configure(height=4, width=8)
        self.botao64.grid(row=7, column=4)

        self.botao65=tk.Button(self.window)
        self.botao65.configure(height=4, width=8)
        self.botao65.grid(row=7, column=5)

        self.botao66=tk.Button(self.window)
        self.botao66.configure(height=4, width=8)
        self.botao66.grid(row=7, column=6)

        self.botao67=tk.Button(self.window)
        self.botao67.configure(height=4, width=8)
        self.botao67.grid(row=7, column=7)

        self.botao68=tk.Button(self.window)
        self.botao68.configure(height=4, width=8)
        self.botao68.grid(row=7, column=8)

        self.botao69=tk.Button(self.window)
        self.botao69.configure(height=4, width=8)
        self.botao69.grid(row=7, column=9)

        self.botao70=tk.Button(self.window)
        self.botao70.configure(height=4, width=8)
        self.botao70.grid(row=7, column=10)

        self.botao71=tk.Button(self.window)
        self.botao71.configure(height=4, width=8)
        self.botao71.grid(row=8, column=1)
        
        self.botao72=tk.Button(self.window)
        self.botao72.configure(height=4, width=8)
        self.botao72.grid(row=8, column=2)

        self.botao73=tk.Button(self.window)
        self.botao73.configure(height=4, width=8)
        self.botao73.grid(row=8, column=3)

        self.botao74=tk.Button(self.window)
        self.botao74.configure(height=4, width=8)
        self.botao74.grid(row=8, column=4)

        self.botao75=tk.Button(self.window)
        self.botao75.configure(height=4, width=8)
        self.botao75.grid(row=8, column=5)

        self.botao76=tk.Button(self.window)
        self.botao76.configure(height=4, width=8)
        self.botao76.grid(row=8, column=6)

        self.botao77=tk.Button(self.window)
        self.botao77.configure(height=4, width=8)
        self.botao77.grid(row=8, column=7)

        self.botao78=tk.Button(self.window)
        self.botao78.configure(height=4, width=8)
        self.botao78.grid(row=8, column=8)

        self.botao79=tk.Button(self.window)
        self.botao79.configure(height=4, width=8)
        self.botao79.grid(row=8, column=9)

        self.botao80=tk.Button(self.window)
        self.botao80.configure(height=4, width=8)
        self.botao80.grid(row=8, column=10)

        self.botao81=tk.Button(self.window)
        self.botao81.configure(height=4, width=8)
        self.botao81.grid(row=9, column=1)

        self.botao82=tk.Button(self.window)
        self.botao82.configure(height=4, width=8)
        self.botao82.grid(row=9, column=2)

        self.botao83=tk.Button(self.window)
        self.botao83.configure(height=4, width=8)
        self.botao83.grid(row=9, column=3)

        self.botao84=tk.Button(self.window)
        self.botao84.configure(height=4, width=8)
        self.botao84.grid(row=9, column=4)

        self.botao85=tk.Button(self.window)
        self.botao85.configure(height=4, width=8)
        self.botao85.grid(row=9, column=5)

        self.botao86=tk.Button(self.window)
        self.botao86.configure(height=4, width=8)
        self.botao86.grid(row=9, column=6)

        self.botao87=tk.Button(self.window)
        self.botao87.configure(height=4, width=8)
        self.botao87.grid(row=9, column=7)

        self.botao88=tk.Button(self.window)
        self.botao88.configure(height=4, width=8)
        self.botao88.grid(row=9, column=8)

        self.botao89=tk.Button(self.window)
        self.botao89.configure(height=4, width=8)
        self.botao89.grid(row=9, column=9)

        self.botao90=tk.Button(self.window)
        self.botao90.configure(height=4, width=8)
        self.botao90.grid(row=9, column=10)

        self.botao91=tk.Button(self.window)
        self.botao91.configure(height=4, width=8)
        self.botao91.grid(row=10, column=1)

        self.botao92=tk.Button(self.window)
        self.botao92.configure(height=4, width=8)
        self.botao92.grid(row=10, column=2)

        self.botao93=tk.Button(self.window)
        self.botao93.configure(height=4, width=8)
        self.botao93.grid(row=10, column=3)

        self.botao94=tk.Button(self.window)
        self.botao94.configure(height=4, width=8)
        self.botao94.grid(row=10, column=4)

        self.botao95=tk.Button(self.window)
        self.botao95.configure(height=4, width=8)
        self.botao95.grid(row=10, column=5)

        self.botao96=tk.Button(self.window)
        self.botao96.configure(height=4, width=8)
        self.botao96.grid(row=10, column=6)

        self.botao97=tk.Button(self.window)
        self.botao97.configure(height=4, width=8)
        self.botao97.grid(row=10, column=7)

        self.botao98=tk.Button(self.window)
        self.botao98.configure(height=4, width=8)
        self.botao98.grid(row=10, column=8)

        self.botao99=tk.Button(self.window)
        self.botao99.configure(height=4, width=8)
        self.botao99.grid(row=10, column=9)

        self.botao100=tk.Button(self.window)
        self.botao100.configure(height=4, width=8)
        self.botao100.grid(row=10, column=10)


          
Tabuleiro=Tabuleiro()
Tabuleiro.window.mainloop()


