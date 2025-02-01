import socket
import cv2
import os
import numpy as np

class Servidor():
    """
    Classe Servidor - API Socket
    """
    def __init__(self, host, port):
        """
        Construtor da classe servidor
        """
        self._host = host
        self._port = port
        self.__tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        """
        Método que inicializa a execução do servidor
        """
        endpoint = (self._host, self._port)
        try:
            self.__tcp.bind(endpoint)
            self.__tcp.listen(1)
            print("Servidor iniciado em ", self._host, ": ", self._port)
            while True:
                con, client = self.__tcp.accept()
                self._service(con, client)
        except Exception as e:
            print("Erro ao inicializar o servidor", e.args)

    def _service(self, con, client):
        """
        Método que implementa o serviço de calculadora
        :param con: objeto socket utilizado para enviar e receber dados
        :param client: é o endereço do cliente
        """
        print("Atendendo cliente ", client)
        try:
            while True:
                # Receber tamanho da imagem
                tam = int.from_bytes(con.recv(4), 'big')

                # Receber a imagem em partes
                img_bytes = b''
                while len(img_bytes) < tam:
                    chunk = con.recv(1024)
                    img_bytes += chunk

                # Decodificar a imagem
                img = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), cv2.IMREAD_COLOR)
                if img is None:
                    raise ValueError("Imagem não decodificada corretamente.")

                # Processamento (detecção de faces)
                xml_classificador = os.path.join(os.path.relpath(
                    cv2.__file__).replace('__init__.py', ''), 'data/haarcascade_frontalface_default.xml')
                face_cascade = cv2.CascadeClassifier(xml_classificador)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)

                # Desenhar retângulos nas faces detectadas
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

                # Codificar a imagem processada
                _, img_bytes = cv2.imencode('.jpg', img)
                img_bytes = img_bytes.tobytes()
                tamanho_da_imagem_codificado = len(img_bytes).to_bytes(4, 'big')

                # Enviar tamanho da imagem processada
                con.send(tamanho_da_imagem_codificado)

                # Enviar imagem processada
                con.send(img_bytes)

                print(client, " -> Requisição atendida com sucesso!")

        except OSError as e:
            print(f"Erro de conexão com {client}: {e.args}")
            con.send(bytes("Erro de conexão", 'ascii'))
        except Exception as e:
            print(f"Erro ao processar dados do cliente {client}: {e.args}")
            con.send(bytes("Erro nos dados", 'ascii'))
        finally:
            con.close()
