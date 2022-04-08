from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, AnyOf, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name", validators=[InputRequired()])

    species = SelectField("Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],
    )

    photo_url = StringField("Photo URL", validators=[Optional(), 
        URL(require_tld=True, message="Please provide a valid URL")])

    age = IntegerField("Age", validators=[InputRequired(message="Please provide an age"), 
        NumberRange(min=0, max=30, message="Please provide a realistic pet age")])

    notes = TextAreaField("Notes")


class EditPetForm(FlaskForm):
    """Form for adding pets"""
    
    photo_url = StringField("Photo URL", validators=[Optional(), URL(require_tld=True, message="Please provide a valid URL")])

    available = SelectField("Available?",
        choices=[(1, 'Yes'), (0, 'No')],
        coerce=int
    )

    notes = TextAreaField("Notes")