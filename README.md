# Milestone Project 3 - Recipe Cook Book



This flask project is a online cook book recipe based on CRUD functionaility where the user can can creat, edit and delete food recipes.  The user should also be able to create, edit and delete recipe categories.  The aim of this project is to make the navigation between creating, editing and deleting recipes/categories easy and simple to complete.  The user is able to control this data as the site is using back-end functionality python, flask and MongoDB.

# UX

The focus of the user experience is to ensure that there is as little tasks for the user to do to complete their task goals.  The flow navigatoin aims to folow the user's thinking to complete this.

  - when the user navigates to a task section - create recipe / edit recipe /manage categories - the page clearly states this task
  - if the user wishes to create / edit or delete a task the buttons clearly show this command
  - once the task is completed, the site returns to the home page so that the user can easily continue to go about fulfilling other tasks
  - "as a user i want to be able to find a recipe based on my viewing or a recipe category criteria, and quickly navigate to the recipe content"
  - "as a user i want to be able to create a recipe with clear instructions of what is required to complete this task"
  

Wireframes filed in project folder


### Features

 - Navigation menu which is shared on all other pages to support the user to navigate the site easily
 - Parralex image which is shared on all pages apart from categories page to maintain site consistancy
 - The above features are all consitant in layout for creating and editing recipes
 - Home page - Card layout to diplay the recipes - visually appealing with image, recipe category, recipe title and basic info about the recipe
 - Categories page - easy list items which displays category name with options to delete/edit as well as add category of choice
 - Creating Recipe - the form layout has a dropdown link with populated categories from MongoDB.  If the user wishes to create a new category for their recipe, the saved choice will refresh for their recipe options.  The user can then insert their recipe criterias - recipe name, description, ingredients, cooking notes, preparation notes and a URL link for an image.
 
### Feature Design
 - To make the site as easy and simple to use - the user can simply add whatever data they choose, which can then be edited or deleted.  No data is pre-populated from the database as a set criteria of choices to make.
 
### Future Features
- As the recipes grow - the site should encorporate pagination to reduce the excess data and allow the user to navigate the site based on selecting various search criterias such as ingredients list, recipe name, category, most popular viewed recipes.
- The user should be able to register an account and login to the site.  With a registration the user can build a portfolio of recipes where they can perhaps create a following from other users.
- Due to the lack of skill set and knowledge these features were not implemented - and therefore the site was maintained to achieve the purpose of simply creating, editing and deleting recipes.
    
### Technologies Used

* [HTML] - structure of the site
* [CSS] - site styling
* [Javascript / jQuery ] - jQuery used to initialise materilize functions
* [Materialize] - main component in creating the structure of the site
* [Font Awesome] - icon elements
* [Flask] - flask framwork
* [Python] - functional logic of the site
* [MongDB] - site database

### Testing

Testing of the site was incremented throughout the CRUD functionality and testing.  This further included checking that the site is reposnsive on all browsers.

- Testing was on connecting database from MongoDB
- Creating Add Recipe
- Edit Recipe
- Removing duplicate recipe creations when editing
- Deleting Recipes
- Images - my original plan was to have images stored in a json file which would populate into each recipe created - however, all images populated into one card.  Therefore, a url link insert was added to let the user add the image.
- Insert fields - some javascript functionality was added and tested to ensure certain input fields were added - however, there was a problem with the app to stop running correctly.

### Deployment

Project was created on AWS Cloud 9 - after setting up the correct flask files, the project was commited to GitHub.  After creating a app on Heroku, the Github was synced to automatically update.

### Credits
- Alot of the basic functionality was used and edited from the Code Institute Data centric task manager project
- The layout and visual appearance comes from the inbuilt libraries within Materialize
- Other guidance and ideas were supported from students comments and problems they had expereinced form the Code Inst slack community
- Youtube - Corey Shafer Python Tutorials & Pretty Printed



### Acknowledgments

Code Institute slack community - various functionality problems shared on-line which supported me to investigate my problems.
