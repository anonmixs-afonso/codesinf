from pyModbusTCP.client import ModbusClient
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder
from pymodbus.constants import Endian
import numpy as np

class Clientinit:
    """
    A class to manage Modbus TCP client operations, including reading and writing values to Modbus registers.

    Attributes:
    modclient (ModbusClient): The Modbus client object for communicating with a Modbus server.
    floatload (BinaryPayloadBuilder): A payload builder used for building float payloads.
    payload (int): Placeholder for a payload value, initialized as 0.
    """

    def __init__ (self, host, port):
        """
        Initializes a new instance of the Clientinit class.

        Args:
            host (str): The host IP address of the Modbus server.
            port (int): The port number of the Modbus server.
        """

        self.modclient = ModbusClient(host=host, port=port)
        self.floatload = BinaryPayloadBuilder(byteorder=Endian.BIG)
        self.payload = 0

    def ihmcli (self):
        """
        Provides a command-line interface for interacting with the Modbus client.

        Allows the user to choose between reading and writing values to Modbus registers.
        Depending on the user's choice, the appropriate read or write operation is performed.
        """
        self.modclient.open()
        try:
            print("Welcome to SCADA CLI: \n")
            ch = input("Choose what to do: 1- Read values from registers, 2- Write values to register, 3- Read dict: ")
            if (int(ch) == 1):
                typreg = input("Choose: 1- Read holding registers (int), 2- Read holding registers (float), 3- Read holding registers bits: ")
                if (int(typreg) == 1):
                    addr = input("Address of the coil in the MODBUS table: ")
                    print(f'The value in {addr} is {self.readvalue(int(addr), int(typreg))}. \n')

                if (int(typreg) == 2):
                    addr = input("Address of the holding register in the MODBUS table: ")
                    print(f'The value in {addr} is {float(self.readvalue(int(addr), int(typreg)))}. \n')

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
            if (int(ch) == 3):
                temp = self.readindict()
                print(f'Data: {temp}')

        except Exception as e:
            print(f'Error: {e.args}') 
        
    def readindict (self):
        #data = {'Voltage RS': self.readvalue(847, 1)}
        data = {'Tipo Motor': self.readvalue(708, 1), 'Status PID': self.readvalue(722, 1), 
        'Temperatura SA': self.readvalue(710, 2), 'Velocidade SA': self.readvalue(712, 2), 
        'Vazão SA': self.readvalue(714, 2), 'Tensão RS': self.readvalue(847, 1)/10, 'Tensao ST': self.readvalue(848, 1)/10,
        'Tensão TR': self.readvalue(849, 1)/10, 'Tipo Partida': self.readvalue(1216, 1), 'Partida Inversor': self.readvalue(1312, 1),
        'Velocidade Inversor': self.readvalue(1313, 1)/10, 'Rampa Acelereção Inversor': self.readvalue(1314, 1)/10, 'Rampa Desaceleração Inversor': self.readvalue(1315, 1)/10,
        'Partida Soft': self.readvalue(1316, 1), 'Rampa Aceleraçãp Soft': self.readvalue(1317, 1), 'Rampa Desaceleração Soft': self.readvalue(1318, 1),
        'Partida Direta': self.readvalue(1319, 1), 'Tipo Partida': self.readvalue(1324, 1), 'Tipo PID': self.readvalue(1332, 1), 'Status 1230': self.readbitholding(1230),
        'Status 1231': self.readbitholding(1231), 'Temperatura TIT-02': self.readvalue(1218, 2)/10, 'Temperatura TIT-01': self.readvalue(1220, 2)/10, 'Pressão PIT-02': self.readvalue(1222, 2)/10, 
        'Pressão PIT-01': self.readvalue(1224, 2)/10, 'Pressão PIT-03': self.readvalue(1226, 2)/10,  'Controle 1328': self.readbitholding(1328), 'Controle 1329': self.readbitholding(1329),
        'Status Compressor': self.readbitholding(1330), 'Temperatura Termostato': self.readvalue(1338, 1), 'Vazão PID': self.readvalue(1302, 2)
        }
        return data

    def readvalue (self, addr, typ):
        """
        Reads a value from a Modbus register.

        Args:
            addr (int): The address of the register to read.
            typ (int): The type of register to read (1 for integer, 2 for float).

        Returns:
            int or float: The value read from the register.
        """
        if (int(typ) == 1):
            ##Holding
            return self.modclient.read_holding_registers(addr, 1)[0]
            ##Floating
        if (int(typ) == 2):
            register = self.modclient.read_holding_registers(addr, 2)
            decoder = BinaryPayloadDecoder.fromRegisters(register, byteorder=Endian.BIG, wordorder=Endian.LITTLE)
            val = decoder.decode_32bit_float()
            print(f'Inside {val}.\n')
            return val

    def readbitholding (self, addr):
        """
        Reads a holding register and returns its value as a list of bits.

        Args:
            addr (int): The address of the holding register to read.

        Returns:
            list: A list of bits representing the value of the holding register.
        """
        register = self.modclient.read_holding_registers(addr, 1)[0]
        # Convertendo o valor do registrador para uma lista de bits
        return [int(x) for x in format(register, '016b')]

    def writebitholding (self, addr, listbitrec):
        """
        Writes a modified value to a holding register based on bit-wise manipulation.

        Args:
            addr (int): The address of the holding register to write to.
            listbitrec (list): A list of bits to write to the holding register.

        """
        listabit = self.readbitholding(addr)
        listaux = [a & b for a, b in zip (listbitrec, listabit)]
        listasw = [a | b for a, b in zip (listaux, listbitrec)]
        intlistbit = [int(c) for c in listasw] 
        a = 0
        for c in range (0, 16, 1):
            a = intlistbit[15-c]*(2**(c)) + a
        self.modclient.write_single_register(addr, a)  

    def writevalue (self, addr, typ, val):
        """
        Writes a value to a Modbus register.

        Args:
            addr (int): The address of the register to write to.
            typ (int): The type of register (1 for coil, 2 for holding register).
            val (int): The value to write to the register.

        Returns:
            bool: True if the value was successfully written to the register, False otherwise.
        """
        return self.modclient.write_single_register(addr, val)
        # 1324 -> Inversor(2)
        # 1313 -> Velocidade(600)
        # 1314 -> Rampa ace (100)
        # 1315 -> Rampa des (100)
        # 1312 -> Partida (1)
