from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, SelectMultipleField, BooleanField
from wtforms.validators import DataRequired, Length

class NewProjectForm(FlaskForm):

    title = StringField('Título', validators=[DataRequired('Campo Requerido'), 
        Length(min=4, max=80, message='Debe tener entre %(min)d y %(max)d caracteres')])
    description = TextAreaField('Descripción')
    limit_date = DateField('Fecha Límite')
    public = BooleanField('Público')
    collaborators = SelectMultipleField('Colaboradores', coerce = int, )

    submit = SubmitField('Crear Proyecto')