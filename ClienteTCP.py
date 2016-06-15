import socket

host = '10.92.75.116'     # Endereco IP do Servidor
porta = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (host, porta)
tcp.connect(dest)
while True:
	msg = tcp.recv(1024)
	msg.decode('utf-8')
	print(msg)

