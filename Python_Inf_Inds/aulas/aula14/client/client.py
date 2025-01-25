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
        endpoint = (self.__server_ip,self.__port)
        try:
            self.__tcp.connect(endpoint)
            print("Conexão realizada com sucesso!")
            self.__method()
        except:
            print("Servidor não disponível")

    
    def __method(self):
        """
        Método que implementa as requisições do cliente
        """
        try:
            msg = ''
            while True:

                # leitura da imagem
                caminho_imagem = '/home/anon/temp_to_transfer/Programs/INF_INDS/Cpp_Inf_Inds/Codes_in_Class/InformaticaIndustrialUFJF/Python/Python 3/ExemploProcessamentoImagem/a.jpg'
                img = cv2.imread(caminho_imagem)

                # codificação para bytes
                _, img_bytes = cv2.imencode('.jpg', img) 
                img_bytes = bytes(img_bytes)
                tamanho_da_imagem_codificado = len(img_bytes).to_bytes(4, 'big')             

                # decodificação
                tam = int.from_bytes(tamanho_da_imagem_codificado, 'big')
                img = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), cv2.IMREAD_COLOR)
               
                self.__tcp.send(bytes(str(tam),'ascii'))
                self.__tcp.send(bytes(str(img),'ascii'))

                resp = self.__tcp.recv(1024)
                print("= ",resp.decode('ascii'))
            self.__tcp.close()
        except Exception as e:
            print("Erro ao realizar comunicação com o servidor", e.args)
