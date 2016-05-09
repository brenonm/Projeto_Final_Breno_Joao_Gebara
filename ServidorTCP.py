import socket
host= 'localhost' #Servidor interno
porta= 5000 #Porta de comunicação
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Define metodo como TCP (SOCK_STREAM)
orig=(host,porta)
tcp.bind(orig)
tcp.listen(1)
con, cliente = tcp.accept()
while True:
	msg=con.recv(1024)  #Estabelece mensagem recebida em 1024 bytes
	msg.decode('utf-8')
	if not msg: break
	print(cliente, ':', msg)
	msg = input('Resposta: ')
	con.send(msg.encode('utf-8'))

