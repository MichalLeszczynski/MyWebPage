from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from models import User, Post

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dc124b595879e4355112fd66b8c4c066'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


posts = [
    {
        'author': 'Michal Leszczynski',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'October 27, 2019'
    },
    {
        'author': 'Second Leszczynski',
        'title': 'Second post 1',
        'content': 'Second post content',
        'date_posted': 'September 27, 2019'
    }
]

@app.route("/")
def home():
    return render_template('home.html',posts=posts, title="Home")

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}! ', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'a@b.com' and form.password.data == 'start':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
