import tkinter as tk
#from PIL import ImageTk, Image
 



class Pagina_Inicial:

    def __init__(self):


        self.window=tk.Tk()
        self.window.title("Batalha Naval")
        self.window.geometry("400x400")


		#foto = ImageTk.PhotoImage(Image.open("titulo.gif"))
		#panel = Label(root, image = foto)
		#panel.pack(side = "bottom", fill = "both", expand = "yes")

        titulo=tk.Label(self.window, text="B4T4LH4 N4V4L", font=("Helvetica", 26))
        titulo.pack()

        self.check=tk.Button(self.window, text="servidor")
        self.check2=tk.Button(self.window, text="cliente")
        cmd=lambda: self.callback2()
        self.check.configure(command=cmd)
        cmd2=lambda: self.callback()
        self.check2.configure(command=cmd2)
        self.check.pack()
        self.check2.pack()
		
		
    def iniciar(self):
        
        self.window.mainloop()
	
    def callback(self):
        entrada_ip=tk.Entry(self.window)
        entrada_ip.pack()
        conectar=tk.Button(self.window, text="Conectar")
        conectar.pack()
        self.check.pack_forget()
        self.check2.pack_forget()
		

    def callback2(self):
        aguardando=tk.Label(self.window, text="Aguardando...")
        aguardando.pack()   
        self.check.pack_forget()
        self.check2.pack_forget()
			
				


pagina=Pagina_Inicial()
pagina.iniciar()
