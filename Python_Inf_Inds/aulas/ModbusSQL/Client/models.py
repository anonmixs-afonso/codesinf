from db import Base
from sqlalchemy import Column, Integer, DateTime

class DadoCLP(Base):
    """
    Modelo dos dados do CLP
    """
    __tablename__ = 'dadoclp'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    tipomotor = Column(Integer)
    statuspid = Column(Integer)
    temperaturasa = Column(Integer)
    velocidadesa = Column(Integer)
    vazaosa = Column(Integer)
    tensaors = Column(Integer)
    tensaost = Column(Integer)
    tensaotr = Column(Integer)
    tipopartida = Column(Integer)
    partidainversor = Column(Integer)
    velocidadeinversor = Column(Integer)
    rampaaceleracaoinversor = Column(Integer)
    rampadesaceleracaoinversor = Column(Integer)
    partidasoft = Column(Integer)
    rampaaceleracaosoft = Column(Integer)
    rampadesaceleracaosoft = Column(Integer)
    partidadireta = Column(Integer)
    tipopartida = Column(Integer)
    tipopid = Column(Integer)
    status1230 = Column(Integer)
    status1231 = Column(Integer)
    temperaturatit02 = Column(Integer)
    temperaturatit01 = Column(Integer)
    pressaopit02 = Column(Integer)
    pressaopit01 = Column(Integer)
    pressaopit03 = Column(Integer)
    controle1328 = Column(Integer)
    controle1329 = Column(Integer)
    statuscompressor = Column(Integer)
    temperaturatermostato = Column(Integer)
    vazaopid = Column(Integer)
    

    

    def get_attr_printable_list(self):
        return [self.id,
        self.timestamp.strftime('%d/%m/%Y %H:%M:%S'),
        self.tipomotor,
        self.statuspid,
        self.temperaturasa,
        self.velocidadesa,
        self.vazaosa,
        self.tensaors,
        self.tensaost,
        self.tensaotr,
        self.tipopartida,
        self.partidainversor,
        self.velocidadeinversor,
        self.rampaaceleracaoinversor,
        self.rampadesaceleracaoinversor,
        self.partidasoft,
        self.rampaaceleracaosoft,
        self.rampadesaceleracaosoft,
        self.partidadireta,
        self.tipopartida,
        self.tipopid,
        self.status1230,
        self.status1231,
        self.temperaturatit02,
        self.temperaturatit01,
        self.pressaopit02,
        self.pressaopit01,
        self.pressaopit03,
        self.controle1328,
        self.controle1329,
        self.statuscompressor,
        self.temperaturatermostato,
        self.vazaopid
        ]
        
