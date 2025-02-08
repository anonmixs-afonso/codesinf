from pyModbusTCP.server import DataBank, ModbusServer
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder
from pymodbus.constants import Endian
import time

class Serverinit:
    def __init__(self, host, port):
        self.db = DataBank()
        self.modserv = ModbusServer(host=host, port=port, no_block=True, data_bank=self.db)
    def defineserver(self):
        try:
            self.modserv.start()
            print("Defining the CLP parameters.\n")

            #Setting the value in the table
            #self.db.set_holding_registers(4001, [200])    
              
            while True:
                decoder = BinaryPayloadDecoder(payload=self.db.get_holding_registers(4001, 2), byteorder=Endian.LITTLE)
                val = decoder.decode_32bit_float()

                #print(f'The value in the 4001th register is: {self.db.get_holding_registers(4001)}.\n')
                print(f'The value in the 4001th register is: {val}.\n')

                #getting coils
                print(f'The value of the coil in the Address 0: {self.db.get_coils(0)}')
                time.sleep(1)
            
        except Exception as e:
            print(f'Error: {e.args}.\n')
