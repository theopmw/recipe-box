# Recipe Box

Hungry? [Recipe Box]() has you covered! 

## **Site Goals**

This project is part of my [Code Institute](https://codeinstitute.net/) Full Stack Software Development Diploma, specifically for the **Data Centric Development** Module. The objective of this project is to "build a full-stack site that allows users to manage a common dataset about a particular domain" using **CRUD** operations - **C**reate, **R**ead, **U**pdate and **D**elete.

I love to cook and have various recipes all over the place (in folders or books around the kitchen, saved online, printed, in emails etc) most of which I have modified in some way. Creating this project is a great way to finally store all these recipes in one place in a way that can easily be shared with others. It also allows other users to share and store recipes securely.

The site has been designed to be mobile first and easily accessible and responsive on a range of devices. This is to allow users to easily look up recipes on any device, wherever they are.

If the site is successful and generates interest and traffic, there is scope to substantially increase the scale of the site, it is anticipated that the site could be expanded to include the following features:

- Add a way for users to like/favourite a recipe, which will then save it to their profile page
- Add a way for users to rate recipes, with a star rating system
- Add a way for users to be able to comment on recipes
- Add ability for users to generate an easily printable version of a recipe
- Add a way for users to easily be able to share recipes on social media or via email

## **UX**

### User Stories

**As a user, I would like to:**

- [x] Access the site from mobile, tablet and desktop devices.
- [x] Easily register to have my own profile   
![User Stories Register](assets/images/readme_screenshots/user_stories/user_stories_register.png)
- [x] Easily log in to my profile   
![User Stories Sign In](assets/images/readme_screenshots/user_stories/user_stories_signin.png)
- [x] Easily log out of my profile   
![User Stories Sign Out](assets/images/readme_screenshots/user_stories/user_stories_signout.png)
- [x] Receive feedback when I Log In   
![User Stories Sign In Feedback](assets/images/readme_screenshots/user_stories/user_stories_signin_confirmation.png
)
- [x] Receive feedback when I Log Out    
![User Stories Log Out Feedback](assets/images/readme_screenshots/user_stories/user_stories_signout_confirmation.png)
- [x] Be able to browse all recipes submitted to the website   
![User Stories All Recipes](assets/images/readme_screenshots/user_stories/user_stories_all_recipes.png)
- [x] Search recipes by ingredient, name or category   
![User Stories Search](assets/images/readme_screenshots/user_stories/user_stories_search.png)
- [x] Add my own recipes   
![User Stories Create Recipe](assets/images/readme_screenshots/user_stories/user_stories_create_recipe.png)
- [x] Edit my own recipes   
![User Stories Edit Recipe](assets/images/readme_screenshots/user_stories/user_stories_edit_recipe.png)
- [x] Delete my own recipes   
![User Stories Delete Recipe](assets/images/readme_screenshots/user_stories/user_stories_delete_recipe.png)
- [x] Be given feedback when I have added, edited, or deleted a recipe   
![User Stories Add Recipe Feedback](assets/images/readme_screenshots/user_stories/user_story_add_recipe_feedback.png)
![User Stories Edit Recipe Feedback](assets/images/readme_screenshots/user_stories/user_stories_update_recipe_feedback.png)
![User Stories Delete Recipe Feedback](assets/images/readme_screenshots/user_stories/user_stories_delete_recipe_feedback.png)
- [x] Have easy access to the recipes I have personally submitted   
![User Stories User Recipes](assets/images/readme_screenshots/user_stories/user_stories_user_recipes.png)


**As an admin I would like to do all of the above and additionally:**

- [x] Access, edit and delete ALL recipes   
![User Stories Admin Access](assets/images/readme_screenshots/user_stories/user_stories_admin_access.png)

### Developer goals

* Create a easy to use, online cookbook where users can utilise CRUD (Create, Read, Update, Delete) functionality to  post, view, edit and delete recipies
* Allow only the owner of the recipe or an admin/superuser the ability to edit or delete a recipe.
* Provide users with the ability to search recipes by name, ingredient or tag.
* Further develop understanding of Python, Flask, Jinja & MongoDB (non-relational database).
* Improve knowledge of HTML, CSS & JavaScript.
* Use Materialize CSS to develop a website.
* Use Heroku to deploy the app.

### Wireframes

### Design

The site takes inspiration form similar sites such as [BBC Good Food](https://www.bbcgoodfood.com/), [Olive Magazine](https://www.olivemagazine.com/) and [Delicious Magazine](https://www.deliciousmagazine.co.uk/). The aim was to keep the site asthetic clean and simple to provide a positive UX and keep the focal point on the food and ensure recipe instrutions are clear and easy to follow.

#### Colour Scheme

Dark green (#1b5e20), black (#00000) and white (#fffff) were the 3 colours used throughout the site. These colours were chosen as they complement each other well and create a clean UI.

### Typography

Sonsie One and Rozha One were the two fonts used in the brand logo as they complement each other well. 

Rozha One was used throughout the site for page headings and sub-headings as it is a bold font, is clear to read, and ties the headings in nicely with the branding of the site.

Roboto was used for the main text of the site as it is very clear and legible. This font was used for the main blocks of text as it is very easy to read.

### Imagery

The imagery used throught the site have been taken from a range of online recipe sites, futher details and links can be found in the Acknowlegements section below.

## Features

### **Page Features**

### Consistent Site Features and Components

- All pages of the site contain the same **Header** and **Footer** components.

- **Header** 
    - The Header consists of the site logo in the center of the page, with the navbar menu items situated underneath it.

    - The navigation menu (situated beneath the site logo on all pages), was built using the Materialize CSS **Navbar** component It consists of the following menu items (aligned left).   
        - **If no user signed in:**  Home, Recipes, Sign In, Register   

        - **If User Signed in:** Home, Recipes, Profile, Add Recipe, Sign Out

    - Aligned to the right of the navigation menu is a search bar that allows users to search for recipes by name, ingredient or tag.

    - The navigation menu is condensed into a hamburger icon on tablet devices and smaller, to provide positive UX and not overcrowd the UI.

- **Footer**
    - The footer consists of a newletter signup button that launches a modal containing the signup form and links to Recipe Box social media (note that as Recipe Box is for eductional purposes only and therefore does not have social media, the links redirect to the specific platform home page)

    - Below this, the site copyright information is displayed

### Home Page (available to all users, no need to register account)

- The **Home Page** features 6 Materialize cards displaying the top 6 recipes based on user views. Each time a user clicks on a recipe  card to view the full recipe, a view is added to the DB and the recipes with the most views are rendered on the page.

- Below the top 6 recipes is a "MORE RECIPES HERE" button that redirects the user to the Recipes Page, which features all recipes stored on the site (see below).

### Recipes Page (available to all users, no need to register account)

- The **Recipes Page** displays Materialize cards featuring all recipes on the site. This section features pagination to display 6 recipes per page. 

- The Materialize cards feature The following recipe information:

    - An image of the recipe
    - The recipe name/title
    - The recipe description
    - The recipe prep time
    - The recipe cook time
    - The recipe servings
    - The recipe difficulty
    - A link to view the full recipe

- The pagination is designed to only show the left chevron when the page is greater than 1 and the right chevron when on any page except the last. The active page is also made clear to th user so they can easily see which page they are currently viewing.

### Recipe Page (available to all users, no need to register account)

- Once a user clicks the **"SEE FULL RECIPE"** link at the bottom of a recipe card, the **Recipe Page** is launched to display the full recipe instructions.

- The page features the following recipe information:

    - An image of the recipe
    - The recipe name/title
    - The recipe description
    - The recipe prep time
    - The recipe cook time
    - The recipe servings
    - The recipe difficulty
    - If the user in session created the recipe or the admin user is logged in, **EDIT** and **DELETE** buttons are displayed to allow the user/admin to either edit or delete the recipe (these links will be covered in further detail below).
    - The recipe instructions
    - The recipe method

### Sign In Page (available to all users, no need to register account)

- The **Sign In** page features a form, handled by [WTForms](https://wtforms.readthedocs.io/en/2.3.x/) (covered in further detail below) and styled using [Materialize CSS](https://materializecss.com/).

- The form features a **Username** field (WTForms StringField), a **Password** field (WTForms PasswordField) and a **Sign In** button (WTForms SubmitField).

- The form checks the username/password combination and will redirect to the Sign In page if they do not match a document from the **users collection** in the DB, a flash message is also displayed to provide feedback to the user: "Invalid username/password combination. Please try again."

- If the user does not have an account, there is a link below the Sign In button to take them to the **Register Page**.

- After successful registration, the user is redirected to thier profile page and a flash message is displayed to welcome them to the site: "Welcome, \<username>".

### Register Page (available to all users, no need to register account)

- The **Register Page** features a form, handled by [WTForms](https://wtforms.readthedocs.io/en/2.3.x/) (covered in further detail below) and styled using [Materialize CSS](https://materializecss.com/).

- The form features a **Username** field (WTForms StringField), a **Password** field (WTForms PasswordField), A **Repeat Password** field (WTForms PasswordField), and a **Register** button (WTForms SubmitField).

- The form checks if the username already exists in the DB and if it does, will redirect back to the Register page and flash a message to the user to provide feedback: "Sorry, that username is already taken. Please try another".

- The form uses WTForms to check if the passwords match and if they don't will display an error message to the user: "Passwords do not match, please try again".

- If the user already has an account, there is a link below the Register button to take them to the **Sign In Page**. 

- After successful registration, the user is redirected to thier profile page and a flash message is displayed to welcome them to the site: "Welcome, \<username>".

### Profile Page (only available to registered users)

- Upon successful loggin, the user is directed to their **Profile Page**.

- On loggin, there is a flash message displayed on the profile page to welcome the user to the site: "Welcome, \<username>".

- The Profile Page features a page heading "\<username>'s Recipe Box" with a sub-heading "Your Recipes..."

- Below these headings Materialize cards displaying the recipes submitted by the user in session (same layout as described in "Recipes Page" section above).

### Add Recipe Page (only available to registered users)

- The **Add Recipe Page** features a form, handled by [WTForms](https://wtforms.readthedocs.io/en/2.3.x/) (covered in further detail below) and styled using [Materialize CSS](https://materializecss.com/).

- The form features the following fields:
    - **Recipe Name**: WTForms StringField, styled with a [Materialze input field](https://materializecss.com/text-inputs.html)
    - **Recipe Description**: WTForms TextAreaField, styled with a [Materialze text area input field](https://materializecss.com/text-inputs.html)
    - **Prep Time**: WTForms StringField, styled with a [Materialze input field](https://materializecss.com/text-inputs.html)
    - **Cook Time**: WTForms StringField, styled with a [Materialze input field](https://materializecss.com/text-inputs.html)
    - **Servings**: WTForms SelectField, styled with a [Materialze select field](https://materializecss.com/select.html)
    - **Tags**: WTForms StringField, styled with a [Materialze input field](https://materializecss.com/text-inputs.html)
    - **Difficulty**: WTForms SelectField, styled with a [Materialze select field](https://materializecss.com/select.html)
    - **Image Link**: WTForms StringField, styled with a [Materialze input field](https://materializecss.com/text-inputs.html)
    - **Ingredients**: WTForms TextAreaField, styled with a [Materialze text area input field](https://materializecss.com/text-inputs.html)
        - Each ingredient is to be input on it's own line (instruction given to user in the form input label) and the splitline() method is applied in the recipe.html template to render the ingredient list correctly in the DOM, with each ingredient on its own line.
        - This field has been designed as a text area to provide a simple, intuitive UX. By recording the infomation in this way, the user can easily edit the information and there are less keystrokes required to input the information. The idea was for the field to act in a similar way to a traditional word processor so that is is familiar to the user.
    - **Method**: WTForms TextAreaField, styled with a [Materialze text area input field](https://materializecss.com/text-inputs.html)
        - Each step is to be input on it's own line (instruction given to user in the form input label) and the splitline() method is applied in the recipe.html template to render the steps correctly in the DOM, with each step on its own line.
        - This field has been designed as a text area to provide a simple, intuitive UX. By recording the infomation in this way, the user can easily edit the information and there are less keystrokes required to input the information. The idea was for the field to act in a similar way to a traditional word processor so that is is familiar to the user and easy to understand.
    - **Add Recipe** WTForms SubmitField, styled with a Materialize button

- The validation of all fields is handled by [WTForms Built-in Validators](https://wtforms.readthedocs.io/en/2.3.x/validators/#built-in-validators) and error messages are displayed to the user if ther input does not meet the field criteria.

- After a recipe has been successfully added to the DB, the user is redirected to the Profile Page and a flash message is displayed to provide feedback: "Recipe Added Successfully".

### Edit Recipe Page (only available to user that owns the recipe and admin user)

- The **Edit Recipe Page** behaves in the exact same way as the Add Recipe Page, other than that the form fields are alredy pre-filled with the recipe information the user provided when adding/previously editing the recipe, this had been pulled from the recipe document in the DB.

- Beneath the form fields are 2 Buttons:
    - A **"Cancel"** button which redirects the user back to the Recipes Page.
    - An **"Update Recipe"** button (WTForms SubmitField) for the user to update there changes to the recipe.
   

### Delete Recipe Page (only available to user that owns the recipe and admin user)

- The **Delete Recipe Page** features the name of the recipe to be deleted, followed by a message to warn the user that this action cannot be undone. This is followed by 2 buttons:
    - A **"Cancel"** button to cancel the delete process and redirect the user back to the Recipes Page
    - A **"Delete Recipe"** button, to confirm and delete the recipe. This redirects the user to their Profile Page and flashes a message to conirm the recipe has been deleted.

### Search Page (available to all users, no need to register account)

- The **Seach Page** acts in a similar way to the all recipes page, but only displays recipes that match the search query.
- It also utilises Materialize cards to display the recipes and paginates the results if there are more than 6 results for the specific search query.

### **Responsive Design Features**

### Responsive for Device Size

The Materialize CSS framework was used to ensure the site is responsive on all device sizes.

#### **Mobile Devices**

- On mobile devices, the Materialze Grid System was utilised to stack information vertically on small device sizes to provide positive and efficient UX and allow information to be read easily by the user. The navigation controls are launched though a hamburger icon/menu toggler to provide a clean UX.   

![Responsive Design Mobile](assets/images/readme_screenshots/responsive_design/responsive_design_mobile_1.png)

![Responsive Design Mobile Menu](assets/images/readme_screenshots/responsive_design/responsive_design_mobile_2.png)

#### **Tablet Devices**

- At tablet size, the Materialze Grid System was used to display 2 recipe cards per row. The hamburger icon/menu toggler was retained to keep the UI clean and clear.

![Responsive Design Tablet](assets/images/readme_screenshots/responsive_design/responsive_design_tablet_1.png)

![Responsive Design Tablet Menu](assets/images/readme_screenshots/responsive_design/responsive_design_tablet_2.png)

#### **Desktop Devices**

At desktop size, the Materialze Grid System was used to display 3 recipe cards per row.

![Reponsive Design Desktop](assets/images/readme_screenshots/responsive_design/responsive_design_desktop.png)

## Information Architecture

This site utilises [MongoDB Atlas](https://www.mongodb.com/) for data storage.

See below for the schema of the site:

![Database Schema](assets/images/readme_screenshots/information_architecture/info_architecture_schema.png)

There is scope to further expand this in the following ways:

## Technologies Used

### Languages Used

* HTML
* CSS
* JavaScript
* Python

### Frameworks, Libraries and Programs Used

* [Gitpod](https://gitpod.io/) - **Gitpod** was used for the IDE while building the website.
* [Git](https://git-scm.com/) - **Git** was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub](https://github.com/) - **GitHub** is used to store the projects code after being pushed from Git.
* [Heroku](https://id.heroku.com/login) - **Heroku** was used as the deployment platform for this project.
* [Materialize CSS 1.0.0](https://materializecss.com/) - **Materialize CSS** was used to assist with the responsiveness and styling of the website.
* [JQuery](https://jquery.com/) - **JQuery** JavaScript library was used to simplify JavaScript code.
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - **Flask** WSGI web application framework was used to simplify the application build.
    * [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) - **Jinja** templating engine was used to was used for templating and simplifying the design process.
    * [Flask-WTForms](https://wtforms.readthedocs.io/en/2.3.x/) - **Flask-WTForms** was used as the flexible forms validation and rendering library (discussed in further detail below).
* [Mongo DB](https://www.mongodb.com/) _ **Mongo DB** was used to store the data for the project.
* [Favicon.io](https://favicon.io/) - **Favicon.io** was used to create the favicon for the website.
* [Font Awesome](https://fontawesome.com/) - **Font Awesome** was used on all pages throughout the website to add icons for aesthetic and UX purposes.
* [Google Fonts](https://fonts.google.com/) - **Google Fonts** were used to import the 'Sonsie One', 'Rozha One and 'Roboto' fonts into the style.css file to style the fonts used on all pages of the project.
* [EmailJS](https://www.emailjs.com/) - **EmialJS** was used for the newsletter subscribe functionality.
* [Balsamiq](https://balsamiq.com/) - **Balsamiq** was used to create the wireframes during the design process.
* [Web Formatter](https://webformatter.com/) - **Web Formatter** was used to beautify code.
* [Am I Responsive](http://ami.responsivedesign.is/) - **Am I Reponsive** was used to test page layouts during the build process.

## Testing

Detailed testing information can be found in separate [TESTING.md](https://github.com/theopmw/recipe-box/blob/master/TESTING.md) file.