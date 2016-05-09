import tkinter as tk
 



class Pagina_Inicial:

	def __init__(self):


		self.window=tk.Tk()
		self.window.title("Batalha Naval")
		self.window.geometry("200x200")

		foto = tk.PhotoImage(file="titulo.gif")
		x = tk.Label(self.window, image=foto)
		x.pack()


		titulo=tk.Label(self.window, text="B4T4LH4 N4V4L", font=("Helvetica", 16))
		titulo.pack()
		entrada_ip=tk.Entry(self.window)
		entrada_ip.pack()
		conectar=tk.Button(self.window, text="Conectar")
		conectar.pack(#command=conectar com o servidor tcp)

	def iniciar(self):
		self.window.mainloop()		

	
pagina=Pagina_Inicial()
pagina.iniciar()	




