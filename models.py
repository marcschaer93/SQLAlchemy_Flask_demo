from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

def connect_db(app):
    """Connect the database to the Flask app."""
    db.app = app
    db.init_app(app)
    
# MODELS GO HERE
# Create the Pet model
class Pet(db.Model):
    """Pet Model"""

    __tablename__ = 'pets'

    def __repr__(self):
        # p = pet instance
        p = self
        return f"<Pet id={p.id} name={p.name} species={p.species} hunger={p.hunger}>"	

    # CLASS methods
    @classmethod
    def get_all_hungry(cls):
        '''Return all pets with hunger > 20'''
        return cls.query.filter(Pet.hunger > 20).all()
    
    @classmethod
    def get_by_species(cls, species):
        """Return all pets of a given species."""
        return cls.query.filter_by(species=species).all()

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    species = db.Column(db.String(30), nullable=True)
    hunger = db.Column(db.Integer, nullable=False, default=20)


    def greet(self):
        """Greet using name."""
        return f"I'm {self.name} the {self.species}"

    def feed(self, amt=20):
        """Feed the pet and make it less hungry."""
        self.hunger -= amt
        self.hunger = max(self.hunger, 0)
