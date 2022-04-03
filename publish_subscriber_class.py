import socket
import json 
import pickle

class Publish_subscriber(object): 
        
        def Publisher_dict(self,ip,input_message,port):
            try: 
              sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
              jsondata = json.dumps(input_message)
              message = pickle.dumps(jsondata)
              sock.sendto(message,(ip,port)) # Sending the json data into the udp  
            except: 
                  print("Connection error via ip: ",str(ip))  
        def Publisher_string(self,ip,input_message,port):
            try: 
              sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
              
              message = input_message.encode() # Encode string to byte
              sock.sendto(message,(ip,port)) # Sending the json data into the udp  
            except: 
                  print("Connection error via ip: ",str(ip))  
        def Subscriber_dict(self,ip,buffer_size,port): 
            try: 
               exec("sock_"+str(port)+" =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)")
               address = (ip,port) 
               exec("sock_"+str(port)+".bind(address)") 
               exec("data,addr"+ "= sock_"+str(port)+".recvfrom(buffer_size)") # Btting the bit operating 
               exec("received = pickle.loads(data)")
               exec("message = json.loads(received)")
               exec("print(message,type(message),addr)")   
            except ValueError: 
                return
        def Subscriber_string(self,ip,buffer_size,port): 
            try: 
               sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
               address = (str(ip),port) 
               sock.bind(address) 
               data,addr = sock.recvfrom(buffer_size) # Btting the bit operating 
               message = data.decode()
               print(message,type(message),addr)   
            except: 
                print("connection error via ip: ",str(ip))
a = Publish_subscriber() 
a.Publisher_dict("127.0.0.1",{"input":9048},5080) 

b = Publish_subscriber() 
b.Subscriber_dict("127.0.0.1",4096,5090)

c = Publish_subscriber() 
c.Publisher_dict("127.0.0.1",{"input_1":9048},5040)
