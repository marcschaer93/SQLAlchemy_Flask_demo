from flask import Flask, render_template, redirect, request # flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import Pet, db, connect_db

# Create a FLASK instance
app = Flask(__name__)
# Add a DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# SECRET KEY
app.config['SECRET_KEY'] = "hyptokrypo"
# DEBUG TOOLBAR
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# initializes the Flask Debug Toolbar
debug = DebugToolbarExtension(app)
# connect to DATABASE
connect_db(app)

# Create some pets
names = ['fluffy', 'stevie', 'carole', 'sira', 'sally', 'bella', 'lucy']
species = ['dog', 'cat', 'fish', 'bird', 'lizard', 'snake', 'hamster']
pets = [Pet(name=n, species=s) for n, s in zip(names, species)]

# Drop and recreate tables
with app.app_context():
	db.drop_all()
	db.create_all()
	db.session.add_all(pets)
	db.session.commit()

# ROUTES
@app.route('/')
def list_pets():
	'''List all pets'''
	pets = Pet.query.all()
	return render_template('list.html', pets=pets)

@app.route('/', methods=['POST'])
def new_pet():
    '''Create a new Pet and add it to the database.'''
    name = request.form['name']
    species = request.form['species']
    hunger = request.form['hunger']
    hunger = int(hunger) if hunger else None

    new_pet = Pet(name=name, species=species, hunger=hunger)
    db.session.add(new_pet)
    db.session.commit()

    return redirect(f"/{new_pet.id}")
    
  
@app.route('/<int:pet_id>')
def show_pet(pet_id):
	'''Show details about a pet'''
	pet = Pet.query.get_or_404(pet_id)
	return render_template('detail.html', pet=pet)

@app.route('/species/<species_id>')
def show_pets_by_species(species_id):
	'''Show details about a species'''
	pets = Pet.get_by_species(species_id)
	return render_template('species.html', pets=pets, species=species_id)

# Run the app
if __name__ == '__main__':
	app.run()
  
  
  
