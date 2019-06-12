DEBUG=True
SECRET_KEY = 'topsecret' #used by flask to secure the data in forms, sessions, cookies, etc
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/catalog_db'
SQLALCHEMY_TRACK_MODIFICATIONS=False #This is just to supress some warning messages
