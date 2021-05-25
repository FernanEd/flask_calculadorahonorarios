from flask_wtf import FlaskForm
from wtforms import  SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange

class HonorariosForm(FlaskForm):
    honorarios = FloatField('Honorarios', validators=[DataRequired(message='Por favor introduzca un numero positivo'), NumberRange(min=0, message='Por favor introduzca un numero positivo') ] )
    submit = SubmitField('Calcular')