import socket
<<<<<<< HEAD
host = '127.0.0.1'     # Endereco IP do Servidor
porta = 5000          # Porta que o Servidor esta
=======
host = '10.92.225.105'     # Endereco IP do Servidor
porta = 5000            # Porta que o Servidor esta
>>>>>>> origin/master
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (host, porta)
tcp.connect(dest)
while True:
	msg = tcp.recv(1024)
	msg.decode('utf-8')
	print(msg)

