from pyModbusTCP.server import DataBank, ModbusServer

class Serverinit:
    def __init__(self, host, port):
        self.db = DataBank()
        self.modserv = ModbusServer(host=host, port=port, no_block=True, data_bank=self.db)

    def defineserver(self):
        try:
            self.modserv.start()
            print("Defining the CLP parameters.\n")

            #Setting the value in the table
            self.db.set_holding_registers(4001, [200])  a  

            while True:
      
                print(f'The value in the 4001th register is: {self.db.get_holding_registers(4001)}.\n')

                #getting coils
                print(f'The value of the coil in the Address 0: {self.db.get_coils(0)}')
            
        except Exception as e:
            print(f'Error: {e.args}.\n')
