import socket
import os  
# Cliente Taller 3: operaciones matemáticas con servidor intermedio

print ("taller 3")
host="localhost"
puerto=9999
socket1=socket.socket()
socket1.connect((host,puerto))

def menu():
    print("**********MENU DE OPERACIONES*******************")
    print("1. SUMA")
    print("2. RESTA")
    print("3. MULTIPLICACION")
    print("4. DIVICION")
    print("5. POTENCIACION")
    print("6. LOGARITMACION")
    print("0. PARA SALIR")

menu()    
   

def digitarNumero():
    x=(input("ingrese el primer numero: "))
    y=(input("Ingrese el segundo numero: "))
    socket1.send(x.encode("UTF-8"))
    socket1.send(y.encode("UTF-8"))

while True:
   p=(input("Digite la operacion a realizar: "))
   
   if p=="1":
      digitarNumero()               
      socket1.send(p.encode("UTF-8"))
      suman=socket1.recv(1024).decode("UTF-8")
      print (" El resultado de la La suma es: ", suman)
      print("\n Que tengas un buen dia,si deseas realizar otra operacion ejecute de nuevo el cliente. ")
      break
     

   if p=="2":
      digitarNumero()
      socket1.send(p.encode("UTF-8"))
      restan=socket1.recv(1024).decode("UTF-8")
      print("El resultado de la La resta es: ", restan)
      print("\n Que tengas un buen dia,si deseas realizar otra operacion ejecute de nuevo el cliente. ")
      break
      
   if p=="3":
      digitarNumero()
      socket1.send(p.encode("UTF-8"))
      multiplican=socket1.recv(1024).decode("UTF-8")
      print("El resultado de la La multiplicacion es: ", multiplican)
      print("\n Que tengas un buen dia,si deseas realizar otra operacion ejecute de nuevo el cliente. ")
      break

   if p=="4":
      digitarNumero()
      socket1.send(p.encode("UTF-8"))
      dividen=socket1.recv(1024).decode("UTF-8")
      print("El resultado de la La division es: ", dividen) 
      print("\n Que tengas un buen dia,si deseas realizar otra operacion ejecute de nuevo el cliente. ")
      break  

   if p=="5":
      digitarNumero()
      socket1.send(p.encode("UTF-8"))
      potencian=socket1.recv(1024).decode("UTF-8")
      print("El resultado de la potencia es: ", potencian)
      print("\n Que tengas un buen dia,si deseas realizar otra operacion ejecute de nuevo el cliente. ")
      break

   if p=="6":
      digitarNumero()
      socket1.send(p.encode("UTF-8"))
      logaritmacion=socket1.recv(1024).decode("UTF-8")
      print("El resultado de del logaritmo es: ", logaritmacion)
      print("\n Que tengas un buen dia,si deseas realizar otra operacion ejecute de nuevo el cliente. ")
      break        

      
      
     