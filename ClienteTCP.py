import socket
host = '127.0.0.1'     # Endereco IP do Servidor
porta = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (host, porta)
tcp.connect(dest)
while True:
	msg= input('Mensagem: ')
	tcp.send(msg.encode('utf-8'))
	resposta = tcp.recv(1024)
	resposta.decode('utf-8')
	print(host, ':', resposta)
