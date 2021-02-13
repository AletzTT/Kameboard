from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class SignupForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=
        [DataRequired(message='Campo Requerido'),
        Length(min=4, max=64, message='La longitud debe ser entre %(min)d y %(max)d')
        ])
    
    password = PasswordField('Contraseña', validators=[DataRequired(message='Campo Requerido')])

    confirm = PasswordField('Confirmar Contraseña', validators=[DataRequired('Campo Requerido')])

    email = StringField('Email', validators=[DataRequired('Campo Requerido'), Email()])

    submit = SubmitField('Registrar')

class LoginForm(FlaskForm):

    username = StringField('Nombre de Usuario', validators=[DataRequired('Campo Requerido'), 
    Length(min=4, max=64, message='La Longitud debe ser entre %(min)d y %(max)d')])

    password = PasswordField('Contraseña', validators=[DataRequired('Campo Requerido')])

    submit = SubmitField('Ingresar')