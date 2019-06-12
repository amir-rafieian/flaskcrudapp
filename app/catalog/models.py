# =============================================================================
# Import dependencies
# =============================================================================
from app import db
from datetime import datetime

# =============================================================================
# Models
# =============================================================================
class Publication(db.Model):
    __tablename__ = 'publication' #the name of the table we gonna create
    
    #having primary key is mandatory, even if table is not connected to others
    id = db.Column(db.Integer, primary_key=True) #when its primary, its already autoincrement unless we set it the other way
    name = db.Column(db.String(80), nullable=True)
    email = db.Column(db.String(120))
    
    def __init__(self,name, email):
        self.name = name
        self.email = email
        
    def __repr__(self): #it return the string version of the class
        return 'Publisher name is {}, email: {}'.format(self.name, self.email)

        

class Book(db.Model):
    __tablename__ = 'book'

    #having primary key is mandatory
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    # ESTABLISH A RELATIONSHIP BETWEEN PUBLICATION AND BOOK TABLES
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))
    
    # If we wanted to implement a multi column unique constraints:
    #__table_args__ = (UniqueConstraint('title','author',name='_title_author_uq'))

    def __init__(self, title, author, avg_rating, book_format, image, num_pages, pub_id):

        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = book_format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return '{} by {}'.format(self.title, self.author)

