#Spustaci program na spustenie proxy z kniznice sipfullproxy

from sipfullproxy import *

HOST, PORT = '0.0.0.0', 0

#Vytvorime si log subor a pridavame do neho zapisy
logging.basicConfig(format='%(asctime)s   %(message)s',filename='Dennik hovorov.log',level=logging.INFO,datefmt='%H:%M:%S')

#Ziskame si detaily
meno = socket.gethostname()
ipadresa = socket.gethostbyname(meno)

#Ziskame si port
PORT = int(input("Zadaj hodnotu na ktorej chces aby si mal port\n"))

#Zapiseme si nami zvolene parametre recordroute a topvia do globalnych premennych v kniznici
recordroute = "Record-Route: <sip:"+str(ipadresa)+":"+str(PORT)+";lr>"
topvia = "Via: SIP/2.0/UDP " + str(ipadresa)+":"+str(PORT)
setTopvia(topvia)
setRecordRoute(recordroute)

#Spustime server
server = socketserver.UDPServer((HOST, PORT), UDPHandler)
print("Server uspesne zalozeny")
server.serve_forever()

