import socket
host= '127.0.0.1' #Servidor interno
porta= 5000 #Porta de comunicação
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Define metodo como TCP (SOCK_STREAM)
orig=(host,porta)
tcp.bind(orig)
tcp.listen(1)
while True:
	con, cliente = tcp.accept()
	msg=con.recv(1024)  #Estabelece mensagem recebida em 1024 bytes
	msg.decode('utf-8')
	if not msg: break
	print(cliente, ':', msg)
	resp = input('Resposta: ')
	con.send(resp.encode('utf-8'))
tcp.close
