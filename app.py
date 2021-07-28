import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo, DESCENDING
from forms import (
    RegisterForm, LoginForm, CreateRecipeForm, 
    EditRecipeForm, ConfirmDelete)
from bson.objectid import ObjectId
import math
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
# Credit: code to pull top 4 recipes suggested by my Code Institute mentor:
# Spencer Barriball
@app.route("/")
@app.route("/index")
def index():
    """Home page pulls 4 most viewed recipes from DB"""
    top_four_recipes = list(
        mongo.db.recipes.find().sort([('views', DESCENDING)]).limit(4))

    recipes = [
        top_four_recipes[0],
        top_four_recipes[1],
        top_four_recipes[2],
        top_four_recipes[3],
    ]

    return render_template(
        'index.html', title="Home", recipes=recipes)


# ------------------- #
#    Recipe Pages     #
# ------------------- #

# all recipes
@app.route("/recipes")
def recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


# Adapted from Spencer pagination code
# @app.route('/recipes')
# def recipes():
#     """Logic for recipe list and pagination"""
#     # number of recipes per page
#     per_page = 6
#     page = int(request.args.get('page', 1))
#     # count total number of recipes
#     total = mongo.db.recipes.count_documents({})
#     # logic for what recipes to return
#     all_recipes = mongo.db.recipes.find().skip((page - 1)*per_page).limit(per_page)
#     pages = range(1, int(math.ceil(total / per_page)) + 1)
#     return render_template('recipes.html', recipes=all_recipes, page=page, pages=pages, total=total)


# individual recipe
# Credit: code to increment views suggested by my Code Institute mentor:
# Spencer Barriball
@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    """Shows full recipe and increments view"""
    mongo.db.recipes.find_one_and_update(
        {'_id': ObjectId(recipe_id)},
        {'$inc': {'views': 1}}
    )
    recipe_db = mongo.db.recipes.find_one_or_404({'_id': ObjectId(recipe_id)})
    return render_template('recipe.html', recipe=recipe_db)


# ------------------- #
#    Create Recipe    #
# ------------------- #


@app.route('/create_recipe', methods=["GET", "POST"])
def create_recipe():
    """Creates a recipe and adds to DB recipes collection"""
    form = CreateRecipeForm(request.form)
    if form.validate_on_submit():
        # set the collection
        recipes_db = mongo.db.recipes
        # insert new recipe into DB
        recipes_db.insert_one({
            'recipe_name': request.form['recipe_name'],
            'user': session['user'],
            'description': request.form['description'],
            'prep_time': request.form['prep_time'],
            'cook_time': request.form['cook_time'],
            'serves': request.form['serves'],
            'difficulty': request.form['difficulty'],
            'image': request.form['image'],
            'tags': request.form['tags'],
            'ingredients': request.form['ingredients'],
            'method': request.form['method'],
            'views': 0
        })
        flash('Recipe Added Successfully!')
        return redirect(url_for("profile", username=session["user"]))
    return render_template(
        'create_recipe.html', title='create a recipe', form=form)


# ------------------- #
#     Edit Recipe     #
# ------------------- #


@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    """Allows User to edit their own recipes"""
    recipe_db = mongo.db.recipes.find_one_or_404({'_id': ObjectId(recipe_id)})
    if request.method == 'GET':
        form = EditRecipeForm(data=recipe_db)
        return render_template('edit_recipe.html', recipe=recipe_db, form=form)
    form = EditRecipeForm(request.form)
    if form.validate_on_submit():
        recipes_db = mongo.db.recipes
        recipes_db.update_one({
            '_id': ObjectId(recipe_id),
        }, {
            '$set': {
                'recipe_name': request.form['recipe_name'],
                'user': session['user'],
                'description': request.form['description'],
                'prep_time': request.form['prep_time'],
                'cook_time': request.form['cook_time'],
                'serves': request.form['serves'],
                'difficulty': request.form['difficulty'],
                'image': request.form['image'],
                'tags': request.form['tags'],
                'ingredients': request.form['ingredients'],
                'method': request.form['method'],
            }
        })
        flash('Recipe Edited Successfully!')
        return redirect(url_for("profile", username=session["user"]))
    return render_template('edit_recipe.html', recipe=recipe_db, form=form)


# ------------------- #
#    Delete Recipe    #
# ------------------- #


@app.route('/delete_recipe/<recipe_id>', methods=['GET', 'POST'])
def delete_recipe(recipe_id):
    """Allows session user to delete one of their recipes with confirmation"""
    recipe_db = mongo.db.recipes.find_one_or_404({'_id': ObjectId(recipe_id)})
    if request.method == 'GET':
        form = ConfirmDelete(data=recipe_db)
        return render_template('delete_recipe.html', recipe=recipe_db, form=form)
    form = ConfirmDelete(request.form)
    if form.validate_on_submit():
        recipes_db = mongo.db.recipes
        recipes_db.delete_one({
            '_id': ObjectId(recipe_id),
        })
        flash('Recipe Deleted Successfully!')
        return redirect(url_for("profile", username=session["user"]))
    return render_template('delete_recipe.html', recipe=recipe_db, form=form)


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
    # Grab recipes from DB
    recipes = mongo.db.recipes.find()

    if session["user"]:
        return render_template("profile.html", username=username, recipes=recipes)

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
