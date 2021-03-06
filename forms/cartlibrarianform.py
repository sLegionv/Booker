from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class LibrarianForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    author = StringField('Автор', validators=[DataRequired()])
    genre = StringField('Жанр', validators=[DataRequired()])
    barcode = StringField('Штрих-код', validators=[DataRequired()])
    description = StringField('Описание', validators=[DataRequired()])
    image = StringField('Ссылка картинки', validators=[DataRequired()])
    icon = StringField('Ссылка иконки', validators=[DataRequired()])
    submit = SubmitField('Добавить книгу')