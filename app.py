from flask import Flask, request, redirect, render_template, flash, session
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm
from sqlalchemy import desc
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///petcenter'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secretkey'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def show_homepage():
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Add a pet to the db with data from the form"""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        new_pet=Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} has been added!")
        return redirect('/')
    else:
        return render_template('add.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def show_and_edit_pet(pet_id):
    """Display and edit pet information"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.available = form.available.data
        print(form.available.data)
        pet.notes = form.notes.data
        db.session.commit()
        flash(f"{pet.name} has been updated!")
        return redirect(f'/{pet.id}')
    else:
        return render_template('view.html', pet=pet, form=form)


