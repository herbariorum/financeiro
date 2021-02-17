from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField

from wtforms.validators import  DataRequired

from ..model import servidores as Servidor

from app import images

class FormPhoto(FlaskForm):

    photo = FileField(u'', validators=[FileRequired(), FileAllowed(images, "Imagens apenas")], render_kw={'class': 'form-control'})
    submit = SubmitField('Submit', render_kw={'class': 'btn btn-primary'})