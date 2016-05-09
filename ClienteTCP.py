import socket
host = '10.92.225.105'     # Endereco IP do Servidor
porta = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (host, porta)
tcp.connect(dest)
while True:
	msg= input('Mensagem: ')
	tcp.send(msg.encode('utf-8'))
	msg = tcp.recv(1024)
	msg.decode('utf-8')
	print(host, ':', msg)

