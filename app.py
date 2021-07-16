import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from forms import RegisterForm, LoginForm
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# ------------------- #
#      Home Page      #
# ------------------- #


# Create index.html file in templates directory and extend from base
@app.route("/")
def index():
    return render_template("index.html")


# ------------------- #
#    Recipe Pages     #
# ------------------- #

# all recipes
@app.route("/recipes")
def recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


# individual recipe
@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    """Shows full recipe"""
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    print(recipe)

    return render_template("recipe.html", recipe=recipe)


# ------------------- #
#       Register      #
# ------------------- #


@app.route("/register", methods=["GET", "POST"])
def register():
    """Handles Registration form functionality"""
    print("attempt register")

    form = RegisterForm(request.form)

    print(form)
    if form.validate_on_submit():
        # get all users
        print("form validated")
        users = mongo.db.users
        # see if we already have the entered username in the DB
        existing_user = users.find_one({'username': request.form['username']})
        print(existing_user)
        # checkname = request.form['username']
        # print(checkname)

        if existing_user is None:
            # hash the entered password
            hash_password = generate_password_hash(
                request.form['password'])
            # insert the user into DB
            users.insert_one({'username': request.form['username'],
                              'password': hash_password})
            # Put new user into "session" cookie
            session["user"] = request.form['username']
            flash("Registration Successful!")
            return redirect(url_for("profile", username=session["user"]))
            # return redirect(url_for('index'))
        # if duplicate username, set flash message and reload the page
        flash('Sorry, that username is already taken. Please try another')
        return redirect(url_for('register'))
    print("seems form not validated")
    return render_template('register.html', title='Register', form=form)


# ------------------- #
#        Log In       #
# ------------------- #


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles Login form functionality"""
    # if session.get('logged_in'):
    #     if session['logged_in'] is True:
    #         return redirect(url_for('index', title="Sign In"))

    form = LoginForm()

    if form.validate_on_submit():
        # get all users
        users = mongo.db.users
        # check if username exists in DB
        existing_user = users.find_one({'username': request.form['username']})

        if existing_user:
            # check hashed password matches user input
            if check_password_hash(
                            existing_user['password'],
                            request.form['password']):
                session["user"] = request.form['username']
                print(session["user"])
                flash("Welcome, {}".format(request.form['username']))

                # redirect to home when successfully logged in
                # return redirect(url_for('index', title="Sign In", form=form))
                # redirect to profile when successfully logged in
                return redirect(
                    url_for("profile", username=session["user"]))
            else:
                # flash message if invlaid password
                flash(
                    'Invalid username/password combination. Please try again.')
                # redirect back to login page
                return redirect(url_for("login"))

        else:
            # flash message if username doesn't exist
            flash('Invalid username/password combination. Please try again.')
            # redirect back to login page
            return redirect(url_for("login"))

    return render_template("login.html", title="Sign In", form=form)


# ------------------- #
#       Profile       #
# ------------------- #


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab session user's username from DB
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

