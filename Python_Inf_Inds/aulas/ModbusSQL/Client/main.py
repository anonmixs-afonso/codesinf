from client import Clientinit
from creategraph import TempGraphApp
import threading
import time
import io
# Initialize the client
client = Clientinit('localhost', 1502)
data = client.ihmcli()

graph = TempGraphApp(data=data)

def update_data(data, modbus_client):
    while True:
        time.sleep(1)
        new_data = client.ihmcli()
        for key in new_data:
            data[key] = new_data[key]



data_update_thread = threading.Thread(target=update_data, args=(data, client), daemon=True)
data_update_thread.start()

TempGraphApp(data=data).run()