import socketserver
## Python 3.7

def suma(numero1,numero2):
	return numero1 + numero2

	    
class miHandler(socketserver.BaseRequestHandler):

	def handle(self):

		#de a 1024 datos se va a recibir
		self.numero1 = int(self.request.recv(1024).decode("UTF-8"))
		self.numero2 = int(self.request.recv(1024).decode("UTF-8"))	

		self.operacion = (self.request.recv(1024).decode("UTF-8"))

		print ("operacion =", self.operacion)
		print ("los numeros recibidos son: ",self.numero1,"y", self.numero2)

		self.sumando = str(suma(self.numero1, self.numero2))
		print ("suma :", self.sumando)
		
		self.request.send(self.sumando.encode("UTF-8"))
		
				

def main():
	print ("Servidor escuchando...")
	host="localhost"
	puerto=9997   #entre 0 y 10000, por los 9000 no estan usados

	server1= socketserver.TCPServer((host,puerto),miHandler)
	print ("server corriendo")
	server1.serve_forever()
main()
