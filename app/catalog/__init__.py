# app/catalog/__init__.py
# =============================================================================
# Import Libraries
# =============================================================================
from flask import Blueprint

main = Blueprint('main', __name__, template_folder='templates') #blueprint is saved in __name__

#As we are separating the code by its functionality, this catalog package gets its own static, 
#templates and python files


#we imported it at the bottom to avoid cross referencing issue with routes.py, as they
#are import each other
from app.catalog import routes 