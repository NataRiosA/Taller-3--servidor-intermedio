import socketserver
import socket
## Python 3.7

lPuertos =[9997, 9996, 9995, 9994, 9993, 9992]

host1 = "localhost"
socket1=socket.socket()
socket1.connect((host1,lPuertos[0]))

socket2=socket.socket()
socket2.connect((host1,lPuertos[1]))

socket3=socket.socket()
socket3.connect((host1,lPuertos[2]))

socket4=socket.socket()
socket4.connect((host1,lPuertos[3]))

socket5=socket.socket()
socket5.connect((host1,lPuertos[4]))

socket6=socket.socket()
socket6.connect((host1,lPuertos[5]))

def MenuOperacion(x,y,op):
	print(x,y,op)

	if op=='1':
		socket1.send(x.encode("UTF-8"))
		socket1.send(y.encode("UTF-8"))
		socket1.send(op.encode("UTF-8"))
	
	elif op=='2':
		socket2.send(x.encode("UTF-8"))
		socket2.send(y.encode("UTF-8"))
		socket2.send(op.encode("UTF-8"))

	elif op=='3':
		socket3.send(x.encode("UTF-8"))
		socket3.send(y.encode("UTF-8"))
		socket3.send(op.encode("UTF-8"))	

	elif op=='4':
		socket4.send(x.encode("UTF-8"))
		socket4.send(y.encode("UTF-8"))
		socket4.send(op.encode("UTF-8"))

	elif op=='5':
		socket5.send(x.encode("UTF-8"))
		socket5.send(y.encode("UTF-8"))
		socket5.send(op.encode("UTF-8"))

	elif op=='6':
		socket6.send(x.encode("UTF-8"))
		socket6.send(y.encode("UTF-8"))
		socket6.send(op.encode("UTF-8"))				
    
	else: 
		pass

class miHandler(socketserver.BaseRequestHandler):


	def handle(self):
		self.numero1=str(self.request.recv(1024).decode("UTF-8"))
		self.numero2=str(self.request.recv(1024).decode("UTF-8"))
		self.operacion=str(self.request.recv(1024).decode("UTF-8"))

		MenuOperacion(self.numero1, self.numero2, self.operacion)
		
		print ("los numeros recibidos son: ",self.numero1,"y", self.numero2, "y la operacion es: ", self.operacion)

		if self.operacion == '1':
			self.suman=socket1.recv(1024).decode("UTF-8")
			print ("La suma es: ", self.suman)
			self.request.send(self.suman.encode("UTF-8"))
			socket1.close()
			
		elif self.operacion == '2':
			self.restan=socket2.recv(1024).decode("UTF-8")
			print ("La resta es: ", self.restan)
			self.request.send(self.restan.encode("UTF-8"))
			socket2.close()

		elif self.operacion == '3':
			self.multiplican=socket3.recv(1024).decode("UTF-8")
			print ("La multiplicacion es: ", self.multiplican)
			self.request.send(self.multiplican.encode("UTF-8"))
			socket3.close()

		elif self.operacion == '4':
			self.dividen=socket4.recv(1024).decode("UTF-8")
			print ("La division es: ", self.dividen)
			self.request.send(self.dividen.encode("UTF-8"))
			socket4.close()

		elif self.operacion == '5':
			self.potencian=socket5.recv(1024).decode("UTF-8")
			print ("La potencia es: ", self.potencian)
			self.request.send(self.potencian.encode("UTF-8"))
			socket5.close()	

		elif self.operacion == '6':
			self.logaritman=socket6.recv(1024).decode("UTF-8")
			print ("El logaritmo es: ", self.logaritman)
			self.request.send(self.logaritman.encode("UTF-8"))
			socket6.close()			

		else: 
			pass


		
def main():
	print ("Servidor intermedio escuchando...")
	host2="localhost"
	puerto=9999   #entre 0 y 10000, por los 9000 no estan usados

	server1= socketserver.TCPServer((host2,puerto),miHandler)
	print ("server corriendo")
	server1.serve_forever()
main()