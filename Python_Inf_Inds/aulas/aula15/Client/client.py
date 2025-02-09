from pyModbusTCP.client import ModbusClient
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder
from pymodbus.constants import Endian
import numpy as np

class Clientinit:

    def __init__ (self, host, port):
        self.modclient = ModbusClient(host=host, port=port)
        self.floatload = BinaryPayloadBuilder(byteorder=Endian.BIG)
        self.payload = 0

    def ihmcli (self):

        self.modclient.open()
        try:
            print("Welcome to SCADA CLI: \n")
            ch = input("Choose what to do: 1- Read values from registers, 2- Write values to register: ")
            if (int(ch) == 1):
                typreg = input("Choose: 1- Read coil, 2- Read holding registers, 3- Read holding registers bits: ")
                if (int(typreg) == 1):
                    addr = input("Address of the coil in the MODBUS table: ")
                    print(f'The value in {addr} is {self.readvalue(int(addr), int(typreg))}. \n')

                if (int(typreg) == 2):
                    addr = input("Address of the holding register in the MODBUS table: ")
                    print(f'The value in {addr} is {self.readvalue(int(addr), int(typreg))}. \n')

                if (int(typreg) == 3):
                    addr = input("Address of the holding register in the MODBUS table: ")
                    print(f'The value in binary is {self.readbitholding(int(addr))}. \n')                 
            
            if (int(ch) == 2):
                typreg = input("Choose: 1- Write coil, 2- Write holding registers, 3- Write holding registers bits: ")
                if (int(typreg) == 1):
                    addr = input("Address of the coil in the MODBUS table: ")
                    val = input("Value to write: ")
                    self.writevalue(int(addr), int(typreg), int(val))
                    

                if (int(typreg) == 2):
                    addr = input("Address of the holding register in the MODBUS table: ")
                    val = input("Value to write: ")
                    self.writevalue(int(addr), int(typreg), int(val))

                if (int(typreg) == 3):
                    addr = input("Address of the holding register in the MODBUS table: ")
                    listinput = list()
                    val = input("Value to write in bits: ")
                    vallist = [int(c) for c in str(val)] 
                    self.writebitholding(int(addr), vallist)

        except Exception as e:
            print(f'Error: {e.args}') 

    def readvalue (self, addr, typ):
        if (int(typ) == 1):
            # decoder = BinaryPayloadDecoder(payload=self.modclient.read_coils(addr, 1), byteorder=Endian.LITTLE)
            # val = decoder.decode_32bit_float()
            return self.modclient.read_coils(addr, 1)[0]
        if (int(typ) == 2):
            # return self.modclient.read_holding_registers(addr, 2)
            decoder = BinaryPayloadDecoder(payload=self.modclient.read_holding_registers(addr, 2), byteorder=Endian.LITTLE)
            val = decoder.decode_32bit_float()
            return val

    def readbitholding (self, addr):
        decoder = BinaryPayloadDecoder(payload=self.modclient.read_holding_registers(addr, 2), byteorder=Endian.LITTLE)
        val = decoder.decode_32bit_float()
        binary = np.binary_repr(np.float16(val).view(np.int16), width=16)
        listbit = list(str(binary))
        intlistbit = [int(c) for c in listbit] 
        return intlistbit

    def writebitholding (self, addr, listbitrec):
        listabit = self.readbitholding(addr)
        listaux = [a & b for a, b in zip (listbitrec, listabit)]
        listasw = [a | b for a, b in zip (listaux, listbitrec)]
        intlistbit = [int(c) for c in listasw] 
        a = 0
        for c in range (0, 16, 1):
            a = intlistbit[15-c]*(2**(c)) + a
        
        self.floatload.add_32bit_float(a)
        self.payload = self.floatload.to_registers()
        
        self.modclient.write_multiple_registers(addr, self.payload)   

    def writevalue (self, addr, typ, val):
        if (int(typ) == 1):
            return self.modclient.write_single_coil(addr, val)
        if (int(typ) == 2):
            self.floatload.add_32bit_float(val)
            self.payload = self.floatload.to_registers()
            return self.modclient.write_multiple_registers(addr, self.payload)       