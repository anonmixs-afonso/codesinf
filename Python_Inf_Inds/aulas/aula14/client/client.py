import socket
import cv2
import os
import numpy as np

class Cliente():
    """
    Classe Cliente - API Socket
    """
    def __init__(self, server_ip, port):
        """
        Construtor da classe Cliente
        """
        self.__server_ip = server_ip
        self.__port = port
        self.__tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        """
        Método que inicializa a execução do Cliente
        """
        endpoint = (self.__server_ip, self.__port)
        try:
            self.__tcp.connect(endpoint)
            print("Conexão realizada com sucesso!")
            self.__method()
        except Exception as e:
            print(f"Servidor não disponível: {e}")

    def __method(self):
        """
        Método que implementa as requisições do cliente
        """
        try:
            while True:
                # Leitura da imagem
                caminho_imagem = '/home/anon/Documents/Gits/GitInf_Gitkraken/codesinf/Python_Inf_Inds/aulas/aula14/client/a.jpg'
                img = cv2.imread(caminho_imagem)

                # Codificação para bytes
                _, img_bytes = cv2.imencode('.jpg', img)
                img_bytes = img_bytes.tobytes()  # Convert to byte string
                tamanho_da_imagem_codificado = len(img_bytes).to_bytes(4, 'big')

                # Enviar tamanho da imagem
                self.__tcp.send(tamanho_da_imagem_codificado)

                # Enviar a imagem em partes
                total_sent = 0
                chunk_size = 1024
                while total_sent < len(img_bytes):
                    chunk = img_bytes[total_sent:total_sent + chunk_size]
                    self.__tcp.send(chunk)
                    total_sent += len(chunk)

                # Receber a imagem processada
                tamproc = int.from_bytes(self.__tcp.recv(4), 'big')
                img_bytes = b''
                total_rec = 0
                while total_rec < tamproc:
                    chunk = self.__tcp.recv(1024)
                    img_bytes += chunk
                    total_rec += len(chunk)

                # Decodificar a imagem recebida
                processed_img = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), cv2.IMREAD_COLOR)

                # Exibir imagem processada
                cv2.imshow('Imagem Processada', processed_img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

                print("Imagem processada recebida com sucesso!")

            self.__tcp.close()
        except Exception as e:
            print("Erro ao realizar comunicação com o servidor", e.args)
