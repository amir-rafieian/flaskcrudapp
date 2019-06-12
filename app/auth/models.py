# =============================================================================
# Import libraries
# =============================================================================
from datetime import datetime
from app import db, bcrypt
from flask_login import UserMixin #works with db model, to check if user is authenticated, is active, ...
from app import login_manager

# =============================================================================
# Models
# =============================================================================
class User(UserMixin, db.Model):
    __table_name__ = "users"
    
    #having primary key is mandatory, even if table is not connected to others
    id = db.Column(db.Integer, primary_key=True) #when its primary, its already autoincrement unless we set it the other way
    user_name = db.Column(db.String(20))
    user_email = db.Column(db.String(120), unique=True, index=True)
    user_password = db.Column(db.String(80))
    registration_date = db.Column(db.DateTime, default = datetime.now)
    
    def check_password(self, password):
        return bcrypt.check_password_hash(self.user_password, password)
    
    #class methods belong to a class but are associated with any class instance
    @classmethod
    def create_user(cls, user, email, password): #we use cls instead of self, cause this method belongs to class not instance of the class
        
        user = cls(user_name = user,
                   user_email = email,
                   user_password = bcrypt.generate_password_hash(password).decode('utf-8'))
        
        db.session.add(user)
        db.session.commit()
        return user
    
    
# =============================================================================
# Log the active user id
# =============================================================================
#user_loader sets the callback for reloading a user from the session. The
#function you set should take a user ID (a ``unicode``) and return a
#user object, or ``None`` if the user does not exist:
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))






















