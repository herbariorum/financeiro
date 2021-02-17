from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SelectField, SubmitField

from wtforms.validators import  DataRequired, ValidationError

from ..model import servidores as Servidor

from app import images


class FormServidor(FlaskForm):
    bancos = [('Banco do Brasil', 'Banco do Brasil'), ('Caixa Econômica', 'Caixa Econômica')]
    tipoconta = [('Conta Corrente', 'Conta Corrente'), ('Poupança', 'Poupança')]

    nome = StringField(u'Nome', validators=[DataRequired()], render_kw={'class': 'form-control'})
    cpf = StringField(u'CPF', validators=[DataRequired()], render_kw={'class': 'form-control'})
    banco = SelectField(choices=bancos, validators=[DataRequired()], render_kw={'class': 'form-select'})
    agencia = StringField(u'Agência', validators=[DataRequired()], render_kw={'class': 'form-control'})
    conta = StringField(u'Conta', validators=[DataRequired()], render_kw={'class': 'form-control'})
    tipoconta = SelectField(choices=tipoconta, validators=[DataRequired()], render_kw={'class': 'form-select'})
    photo = FileField(validators=[FileRequired(), FileAllowed(images, "Imagens apenas")], render_kw={'class': 'form-control'})
    submit = SubmitField('Submit', render_kw={'class': 'btn btn-primary'})