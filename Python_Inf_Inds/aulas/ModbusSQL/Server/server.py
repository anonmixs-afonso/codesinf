from pyModbusTCP.server import DataBank, ModbusServer
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder
from pymodbus.constants import Endian
import time
import random

class Serverinit:
    def __init__(self, host, port):
        self.db = DataBank()
        self.modserv = ModbusServer(host=host, port=port, no_block=True, data_bank=self.db)

    def defineserver(self):
        try:
            self.modserv.start()
            print("Defining the PLC parameters.\n")

            self.modserv.data_bank.set_holding_registers(708, [1])
            self.modserv.data_bank.set_holding_registers(722, [1])
            self.modserv.data_bank.set_holding_registers(1216, [1])
            self.modserv.data_bank.set_holding_registers(1312, [1])
            self.modserv.data_bank.set_holding_registers(1313, [600])
            self.modserv.data_bank.set_holding_registers(1314, [100])
            self.modserv.data_bank.set_holding_registers(1315, [100])
            self.modserv.data_bank.set_holding_registers(1316, [1])
            self.modserv.data_bank.set_holding_registers(1317, [10])
            self.modserv.data_bank.set_holding_registers(1318, [10])
            self.modserv.data_bank.set_holding_registers(1319, [1])
            self.modserv.data_bank.set_holding_registers(1324, [1])
            self.modserv.data_bank.set_holding_registers(1332, [1])
            self.modserv.data_bank.set_holding_registers(1338, [50])
            float_val12 = random.uniform(0, 100)
            builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)  
            builder.add_32bit_float(float_val12)  
            payload = builder.to_registers()  #
            self.modserv.data_bank.set_holding_registers(1302, payload)
            print(f"Setting register 710 with value: {float_val12} (encoded as {payload})")

            while True:
                float_val1 = random.uniform(0, 100)  
                float_val2 = random.uniform(0, 5000)
                float_val3 = random.uniform(0, 100)
                float_val4 = random.uniform(0, 10000)
                float_val5 = random.uniform(0, 10000)
                float_val6 = random.uniform(0, 10000)
                float_val7 = random.uniform(0, 1000)
                float_val8 = random.uniform(0, 1000)
                float_val9 = random.uniform(0, 1000)
                float_val10 = random.uniform(0, 1000)
                float_val11 = random.uniform(0, 1000)
                

                #print(f"Generated float value: {float_val1}")
                
                # Temperature
                builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)  
                builder.add_32bit_float(float_val1)  
                payload = builder.to_registers()  #
                self.modserv.data_bank.set_holding_registers(710, payload)

                # Speed
                builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)  
                builder.add_32bit_float(float_val2)  
                payload = builder.to_registers()  #
                self.modserv.data_bank.set_holding_registers(712, payload)
               
                # Flow Rate
                builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)  
                builder.add_32bit_float(float_val3)  
                payload = builder.to_registers()  #
                self.modserv.data_bank.set_holding_registers(714, payload)

                # Voltage RS
                self.modserv.data_bank.set_holding_registers(847,[float_val4])

                # Voltage ST
                self.modserv.data_bank.set_holding_registers(848,[float_val5])

                # Voltage TR
                self.modserv.data_bank.set_holding_registers(849,[float_val6])

                # Temperature TIT-02
                builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)  
                builder.add_32bit_float(float_val7)  
                payload = builder.to_registers()  #
                self.modserv.data_bank.set_holding_registers(1218, payload)
                
                # Temperature TIT-01
                builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)  
                builder.add_32bit_float(float_val8)  
                payload = builder.to_registers()  #
                self.modserv.data_bank.set_holding_registers(1220, payload)

                # Pressure PIT-02
                builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)  
                builder.add_32bit_float(float_val9)  
                payload = builder.to_registers()  #
                self.modserv.data_bank.set_holding_registers(1222, payload)

                # Pressure PIT-01
                builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)  
                builder.add_32bit_float(float_val10)  
                payload = builder.to_registers()  #
                self.modserv.data_bank.set_holding_registers(1224, payload)

                # Pressure PIT-03
                builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)  
                builder.add_32bit_float(float_val11)  
                payload = builder.to_registers()  #
                self.modserv.data_bank.set_holding_registers(1226, payload)


                #print(f"Setting register 710 with value: {float_val} (encoded as {payload})")

                time.sleep(1)  

        except Exception as e:
            print(f'Error: {e.args}.\n')

# Example usage:
# server = Serverinit(host="localhost", port=502)
# server.defineserver()
