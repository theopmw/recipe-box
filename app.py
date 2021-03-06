import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo, DESCENDING
from forms import (
    RegisterForm, LoginForm, CreateRecipeForm,
    EditRecipeForm, ConfirmDelete)
from bson.objectid import ObjectId
import re
import math
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Create index.html file in templates directory and extend from base
# Credit: code to pull top 6 recipes modified from code
# suggested by my Code Institute mentor: Spencer Barriball
@app.route("/")
@app.route("/index")
def index():
    """Home page pulls 6 most viewed recipes from DB"""
    top_six_recipes = mongo.db.recipes.find().sort(
        [('views', DESCENDING)]).limit(6)

    return render_template(
        'index.html', recipes=top_six_recipes)


# all recipes
# Credit: code for pagination modified from code
# supplied by my Code Institute mentor: Spencer Barriball
@app.route('/recipes')
def recipes():
    """Logic for all recipes list and pagination"""
    # number of recipes per page
    per_page = 6
    page = int(request.args.get('page', 1))
    # count total number of recipes
    total = mongo.db.recipes.count_documents({})
    # logic for what recipes to return
    all_recipes = mongo.db.recipes.find().skip(
        (page - 1)*per_page).limit(per_page)
    pages = range(1, int(math.ceil(total / per_page)) + 1)
    # store total number of pages
    page_count = len(pages)
    return render_template(
        'recipes.html', recipes=all_recipes,
        page=page, pages=pages, page_count=page_count, total=total)


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


# Credit: code for search logic modified from code supplied by my
# Code Institute mentor: Spencer Barriball
@app.route('/search', methods=['GET', 'POST'])
def search():
    """Logic for recipe search and pagination"""
    # pull query from the form
    orig_query = request.args.get("query", "")

    query = {'$regex': re.compile('.*{}.*'.format(orig_query), re.IGNORECASE)}
    per_page = 6
    page = int(request.args.get("page", 1))
    results = mongo.db.recipes.find({
        '$or': [
            {'recipe_name': query},
            {'tags': query},
            {'ingredients': query},
        ]
    }).skip((page - 1)*per_page).limit(per_page)
    total = results.count()
    pages = range(1, int(math.ceil(total / per_page)) + 1)
    # store total number of pages
    page_count = len(pages)
    # find instances of the entered word in DB
    # recipe_name, tags or ingredients documents

    if total > 0:
        return render_template(
            'search.html', query=orig_query, results=results,
            page=page, pages=pages, page_count=page_count, total=total)
    else:
        flash('Sorry! No Recipes Found, Please Try Another Search.')
        return render_template(
            'search.html', query=orig_query, results=results, total=total)


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
        'create_recipe.html', form=form)


@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    """Allows user to edit their own recipes"""
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
        flash('Recipe Updated Successfully!')
        return redirect(url_for("profile", username=session["user"]))
    return render_template('edit_recipe.html', recipe=recipe_db, form=form)


@app.route('/delete_recipe/<recipe_id>', methods=['GET', 'POST'])
def delete_recipe(recipe_id):
    """Allows session user to delete one of their recipes with confirmation"""
    recipe_db = mongo.db.recipes.find_one_or_404({'_id': ObjectId(recipe_id)})
    if request.method == 'GET':
        form = ConfirmDelete(data=recipe_db)
        return render_template(
            'delete_recipe.html', recipe=recipe_db, form=form)
    form = ConfirmDelete(request.form)
    if form.validate_on_submit():
        recipes_db = mongo.db.recipes
        recipes_db.delete_one({
            '_id': ObjectId(recipe_id),
        })
        flash('Recipe Deleted Successfully!')
        return redirect(url_for("profile", username=session["user"]))
    return render_template('delete_recipe.html', recipe=recipe_db, form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Handles Registration form functionality"""
    print("attempt register")

    form = RegisterForm(request.form)

    if form.validate_on_submit():
        # get all users
        users = mongo.db.users
        # see if we already have the entered username in the DB
        existing_user = users.find_one({'username': request.form['username']})

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
        # if duplicate username, set flash message and reload the page
        flash('Sorry, that username is already taken. Please try another')
        return redirect(url_for('register'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles Login form functionality"""
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
                flash("Welcome, {}".format(request.form['username']))

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
            flash('Invalid username/password combination. Please try again')
            # redirect back to login page
            return redirect(url_for("login"))

    return render_template("login.html", form=form)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """Logic for user recipes list and pagination"""
    # grab session user's username from DB
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # number of recipes per page
    per_page = 6
    page = int(request.args.get('page', 1))
    # logic for what recipes to return
    user_recipes = mongo.db.recipes.find(
        {'user': session['user']}).skip((page - 1) * per_page).limit(per_page)
    # count total number of recipes
    total = user_recipes.count()
    print(total)
    pages = range(1, int(math.ceil(total / per_page)) + 1)
    # store total number of pages
    print(pages)
    page_count = len(pages)
    print(page_count)
    return render_template(
        'profile.html', recipes=user_recipes,
        page=page, pages=pages, page_count=page_count,
        total=total, username=username)


@app.route("/logout")
def logout():
    """Handles Logout funtionality"""
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.errorhandler(404)
def handle_404(error):
    """404 error handler"""
    return render_template(
        '404.html'), 404


@ app.errorhandler(500)
def handle_500(error):
    """500 error handler"""
    return render_template(
        '500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
