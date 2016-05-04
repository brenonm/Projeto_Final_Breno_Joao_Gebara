import tkinter as tk



class Pagina_Inicial:

	def __init__(self):

		self.window=tk.Tk()
		self.window.title("Batalha Naval")
		self.window.configure(width=600, height=500)


		titulo=tk.Label(self.window, text="B4T4LH4 N4V4L")
		titulo.grid()
		entrada_ip=tk.Entry(self.window)
		entrada_ip.grid()
		conectar=tk.Button(self.window, text="Conectar")
		conectar.grid()




	def iniciar(self):
		self.window.mainloop()

Pagina=Pagina_Inicial()
Pagina.iniciar()


