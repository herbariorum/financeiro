from datetime import datetime
from app import db

class servidores(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80))
    cpf = db.Column(db.String(15))
    banco = db.Column(db.String(80))
    agencia = db.Column(db.String(80))
    conta = db.Column(db.String(80))
    tipoconta = db.Column(db.String(80))
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    photo = db.Column(db.String(128), default=None, nullable=True)
    photo_url = db.Column(db.String(128), default=None, nullable=True)


    def __repr__(self):
        return str(self.nome)


class saldos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mes = db.Column(db.Integer, nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    saldo = db.Column(db.Numeric(10,2), nullable=False)

    def __repr__(self):
        return str(self.saldo)


class lancamentos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo = db.Column(db.String(80), nullable=False)
    categoria = db.Column(db.String(80))
    descricao = db.Column(db.String(150))
    valor = db.Column(db.String(8), nullable=False)
    data_lancamento = db.Column(db.DateTime, nullable=False, default=datetime.now)

    # def __repr__(self):
        # return "{}, {}, {}, {}, {}, {}".format(self.id, self.tipo, self.categoria, self.descricao, self.valor, self.data_lancamento)