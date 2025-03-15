import threading
import time
from pyModbusTCP.client import ModbusClient
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder
from pymodbus.constants import Endian
import numpy as np
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io

kivy.require('2.0.0')  # Ensure we're using the correct Kivy version

class Clientinit:
    """
    A class to manage Modbus TCP client operations, including reading and writing values to Modbus registers.
    """
    def __init__(self, host, port):
        self.modclient = ModbusClient(host=host, port=port)
        self.floatload = BinaryPayloadBuilder(byteorder=Endian.BIG)
        self.payload = 0

    def ihmcli(self):
        """
        Provides a command-line interface for interacting with the Modbus client.
        """
        self.modclient.open()
        try:
            data = self.readindict()
            return data
        except Exception as e:
            print(f'Error: {e.args}')

    def readindict(self):
        data = {
            'Tipo Motor': self.readvalue(708, 1), 'Status PID': self.readvalue(722, 1),
            'Temperatura SA': self.readvalue(710, 2), 'Velocidade SA': self.readvalue(712, 2),
            'Vazão SA': self.readvalue(714, 2), 'Tensão RS': self.readvalue(847, 1)/10,
            'Tensao ST': self.readvalue(848, 1)/10, 'Tensão TR': self.readvalue(849, 1)/10,
            'Tipo Partida': self.readvalue(1216, 1), 'Partida Inversor': self.readvalue(1312, 1),
            'Velocidade Inversor': self.readvalue(1313, 1)/10, 'Rampa Acelereção Inversor': self.readvalue(1314, 1)/10,
            'Rampa Desaceleração Inversor': self.readvalue(1315, 1)/10, 'Partida Soft': self.readvalue(1316, 1),
            'Rampa Aceleraçãp Soft': self.readvalue(1317, 1), 'Rampa Desaceleração Soft': self.readvalue(1318, 1),
            'Partida Direta': self.readvalue(1319, 1), 'Tipo Partida': self.readvalue(1324, 1),
            'Tipo PID': self.readvalue(1332, 1), 'Status 1230': self.readbitholding(1230),
            'Status 1231': self.readbitholding(1231), 'Temperatura TIT-02': self.readvalue(1218, 2)/10,
            'Temperatura TIT-01': self.readvalue(1220, 2)/10, 'Pressão PIT-02': self.readvalue(1222, 2)/10,
            'Pressão PIT-01': self.readvalue(1224, 2)/10, 'Pressão PIT-03': self.readvalue(1226, 2)/10,
            'Controle 1328': self.readbitholding(1328), 'Controle 1329': self.readbitholding(1329),
            'Status Compressor': self.readbitholding(1330), 'Temperatura Termostato': self.readvalue(1338, 1),
            'Vazão PID': self.readvalue(1302, 2)
        }
        return data

    def readvalue(self, addr, typ):
        if int(typ) == 1:
            return self.modclient.read_holding_registers(addr, 1)[0]
        if int(typ) == 2:
            register = self.modclient.read_holding_registers(addr, 2)
            decoder = BinaryPayloadDecoder.fromRegisters(register, byteorder=Endian.BIG, wordorder=Endian.LITTLE)
            return decoder.decode_32bit_float()

    def readbitholding(self, addr):
        register = self.modclient.read_holding_registers(addr, 1)[0]
        return [int(x) for x in format(register, '016b')]

class TempGraphApp(App):
    def __init__(self, data, **kwargs):
        super().__init__(**kwargs)
        self.data = data
        self.temperature_data = {key: value for key, value in self.data.items() if 'Temperatura' in key}

    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.fig, self.ax = plt.subplots(dpi=100)
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Temperature (°C)')
        self.ax.set_title('Temperature over Time')

        self.temp_lines = {
            key: self.ax.plot([], [], label=key, color='blue', linewidth=2)[0]
            for key in self.temperature_data
        }

        self.ax.legend()
        self.image_widget = Image()
        self.layout.add_widget(self.image_widget)
        self.time = 0
        Clock.schedule_interval(self.update_graph, 1)
        return self.layout

    def update_graph(self, dt):
        y_min = float('inf')
        y_max = float('-inf')

        for key in self.temperature_data:
            new_value = self.data[key]
            current_xdata, current_ydata = self.temp_lines[key].get_data()
            current_xdata = list(current_xdata) + [self.time]
            current_ydata = list(current_ydata) + [new_value]
            self.temp_lines[key].set_data(current_xdata, current_ydata)
            y_min = min(y_min, min(current_ydata))
            y_max = max(y_max, max(current_ydata))

        self.ax.set_xlim(self.time - 100, self.time)
        if y_min != float('inf') and y_max != float('-inf'):
            self.ax.set_ylim(y_min - 5, y_max + 5)

        buf = io.BytesIO()
        canvas = FigureCanvasAgg(self.fig)
        canvas.draw()
        buf.write(canvas.tostring_argb())
        buf.seek(0)

        image_data = np.frombuffer(buf.getvalue(), dtype=np.uint8)
        image_data = image_data.reshape((int(self.fig.get_size_inches()[1] * self.fig.dpi),
                                        int(self.fig.get_size_inches()[0] * self.fig.dpi), -1))
        image_data = np.flipud(image_data)

        texture = Texture.create(size=(image_data.shape[1], image_data.shape[0]), colorfmt='rgba')
        texture.blit_buffer(image_data.tobytes(), colorfmt='rgba', bufferfmt='ubyte')
        self.image_widget.texture = texture
        self.time += 1

def update_data(data, modbus_client):
    while True:
        time.sleep(1)
        new_data = modbus_client.ihmcli()
        for key in new_data:
            data[key] = new_data[key]

if __name__ == '__main__':
    # Initialize Modbus client
    modbus_client = Clientinit(host='localhost', port=1502)  # Replace with your Modbus server details

    # Initial data dictionary
    data = modbus_client.ihmcli()

    # Run the update_data function in a separate thread to simulate real-time updates
    data_update_thread = threading.Thread(target=update_data, args=(data, modbus_client), daemon=True)
    data_update_thread.start()

    # Create and run the Kivy app with the existing data
    TempGraphApp(data=data).run()