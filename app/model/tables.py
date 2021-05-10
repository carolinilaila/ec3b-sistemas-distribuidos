from app import db

# crio a tabela aluno
class Abc2dv(db.Model):
    __tablename__ = "tbabc2dv"
    ra = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_aluno = db.Column(db.String(60), unique=True)
    email_aluno = db.Column(db.String(50))
    logradouro = db.Column(db.String(50))
    numero = db.Column(db.String(20))
    cep = db.Column(db.String(10))
    complemento = db.Column(db.String(60))
    
    def __init__(self, nome_aluno, email_aluno,logradouro, numero, cep, complemento):
        self.nome_aluno = nome_aluno
        self.email_aluno = email_aluno
        self.logradouro = logradouro
        self.numero = numero
        self.cep = cep
        self.complemento = complemento