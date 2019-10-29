from flask import render_template, url_for, flash, redirect
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post
from blog import app, db, bcrypt


posts = [
    {
        "author": "Michal Leszczynski",
        "title": "Blog post 1",
        "content": "First post content",
        "date_posted": "October 27, 2019",
    },
    {
        "author": "Second Leszczynski",
        "title": "Second post 1",
        "content": "Second post content",
        "date_posted": "September 27, 2019",
    },
]


@app.route("/")
def home():
    return render_template("home.html", posts=posts, title="Home")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in.', "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "a@b.com" and form.password.data == "start":
            flash(f"You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)
