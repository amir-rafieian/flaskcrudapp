# =============================================================================
# Import dependencies
# =============================================================================
from app.auth.forms import RegistrationForm, LoginForm
from app.auth import authentication as at #import blueprint
from flask import render_template, request, flash, redirect, url_for
from app.auth.models import User
from flask_login import login_user, logout_user,login_required, current_user

# =============================================================================
# Routes
# =============================================================================
@at.route('/register', methods=['GET','POST'])
def register_user():
    if current_user.is_authenticated: #If user is already loggedin we shouldn`t show registration/login form
        flash('You are already logged in')
        return redirect(url_for('main.display_books'))
    
    form = RegistrationForm()
    
    #Method-1:
    #name = None
    #email = None
    #if request.method == 'POST':
    #    name = form.name.data
    #    email = form.email.data
    #return render_template('registration.html', form = form, name=name, email=email)
    
    #Method-2: (better way)
    if form.validate_on_submit(): #This statement check if request is "POST", and also if data is valid
        User.create_user(user=form.name.data,
                         email=form.email.data,
                         password=form.password.data)
        flash('Registration was succussful!')
        return redirect(url_for('authentication.do_the_login'))
        
    return render_template('registration.html', form = form)

    

@at.route('/login', methods=['GET','POST'])
def do_the_login():
    if current_user.is_authenticated: #If user is already loggedin we shouldn`t show registration/login form
        flash('You are already logged in')
        return redirect(url_for('main.display_books'))
    
    form = LoginForm() #for the get request
    
    if form.validate_on_submit(): #for post request
        user = User.query.filter_by(user_email=form.email.data).first()
        if not user or not user.check_password(form.password.data):
            flash('Invalid Credentials, please try again')
            return redirect(url_for('authentication.do_the_login'))
        
        login_user(user, form.stay_loggedin.data) #writes the user credentials to the session
        return redirect(url_for('main.display_books'))
    
    return render_template('login.html', form=form)


@at.route('/logout')
@login_required
def log_out_user():
    logout_user()
    return redirect(url_for('main.display_books'))


# =============================================================================
# Error Handling
# =============================================================================
@at.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

























