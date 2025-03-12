from pyModbusTCP.server import DataBank, ModbusServer
from server import Serverinit

print("Inicializing Server...\n")

servcall = Serverinit('localhost', 502)
servcall.defineserver()
