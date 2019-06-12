# app/auth/__init__.py
# =============================================================================
# Import Libraries
# =============================================================================
from flask import Blueprint

authentication = Blueprint('authentication', __name__, template_folder='templates') #blueprint is saved in __name__

#As we are separating the code by its functionality, this catalog package gets its own static, 
#templates and python files


#we imported it at the bottom to avoid cross referencing issue with routes.py, as they
#are import each other
from app.auth import routes 