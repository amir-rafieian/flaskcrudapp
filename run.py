#main run file
from app import create_app, db
from app.auth.models import User


flask_app = create_app('prod') #our configuration is in dev.py
with flask_app.app_context():
    db.create_all()
    
    #Create default user:
    if not User.query.filter_by(user_name='harry').first():
        User.create_user(user='harry',
                         email = 'harry@poter.com',
                         password = 'secret')
flask_app.run()