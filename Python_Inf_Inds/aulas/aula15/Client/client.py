from pyModbusTCP.client import ModbusClient

class Clientinit:

    def __init__ (self, host, port):
        self.modclient = ModbusClient(host=host, port=port)

    def ihmcli (self):

        self.modclient.open()
        try:
            print("Welcome to SCADA CLI: \n")
            ch = input("Choose what to do: 1- Read values from registers, 2- Write values to register: ")
            if (int(ch) == 1):
                typreg = input("Choose: 1- Read coil, 2- Read holding registers: ")
                if (int(typreg) == 1):
                    addr = input("Address of the coil in the MODBUS table: ")
                    print(f'The value in {addr} is {self.readvalue(int(addr), int(typreg))}. \n')

                if (int(typreg) == 2):
                    addr = input("Address of the holding register in the MODBUS table: ")
                    print(f'The value in {addr} is {self.readvalue(int(addr), int(typreg))}. \n')
            
            if (int(ch) == 2):
                typreg = input("Choose: 1- Write coil, 2- Write holding registers: ")
                if (int(typreg) == 1):
                    addr = input("Address of the coil in the MODBUS table: ")
                    val = input("Value to write: ")
                    self.writevalue(int(addr), int(typreg), int(val))
                    

                if (int(typreg) == 2):
                    addr = input("Address of the holding register in the MODBUS table: ")
                    val = input("Value to write: ")
                    self.writevalue(int(addr), int(typreg), int(val))


        except Exception as e:
            print(f'Error: {e.args}') 

    def readvalue (self, addr, typ):
        if (int(typ) == 1):
            return self.modclient.read_coils(addr, 1)[0]
        if (int(typ) == 2):
            return self.modclient.read_holding_registers(addr, 1)[0]

    def writevalue (self, addr, typ, val):
        if (int(typ) == 1):
            return self.modclient.write_single_coil(addr, val)
        if (int(typ) == 2):
            return self.modclient.write_single_register(addr, val)        