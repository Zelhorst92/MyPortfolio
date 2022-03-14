# My Portfolio!

# Introduction

Welcome to my portfolio!

...


~ Robert L. Zelhorst

# Table of Content
- [User Experience](#user-experience)
  * [Site Owner Goal](#site-owner-goal)
  * [User Goals](#user-goals)
  * [User Stories](#user-stories)
  * [User Requirements](#user-requirements)
  * [User Expectations](#user-expectations)
- [Design](#design)
  * [Wireframes](#wireframes)
  * [Design Choices](#design-choices)
    * [The Structure](#the-structure)
    * [Fonts](#fonts)
    * [Colours](#colours)
  * [Database Structure](#database-structure)
  * [Logic Flowchart](#logic-flowchart)
- [Features](#features)
  * [Existing Features](#existing-features)
  * [Future Features](#future-features)
- [Technologies](#technologies)
  * [Languages](#languages)
  * [Libraries and Tools](#libraries-and-tools)
- [Testing](#testing)
- [Deployment](#deployment)
  * []
- [Credits](#credits)
  * [Code](#code)
  * [Thanks](#thanks)
  * [Afterword](#afterword)

# User Experience
## Site Owner Goals
* Inform the visitors of the experience and capabilities of the site owner. Ie. Sell oneself/an online resume.
* Sell services, like making a landingpage etc., ~~or give visitors the possibility to buy the site owner a coffee.~~
* Have the users contact the site owner.

---

## User Goals
* A website where you can find what the site owner does.
* A website where I can read about the site owner.
    * About the site owner experience and capabilities.
    * ~~A blog~~
* A website where I can register and login to.
* A website where you can buy services from the site owner.
    * Products
    * ~~Donations~~

---

## User/Siteowner Stories
As a user, I want;
* a website that is easy and intuitively to use.
* to see what the website is about at first glance.
* a website that works on all screen sizes.
* to be able to traverse to relevant social media.
* to read about the site owner.
    * ~~Blog/forum~~
    * Past builds
    * Experiences with;
        * Languages
        * Frameworks
        * etc.
    * Public personal information.
* to contact the site owner.

* to register to the website.
* to login to the website.
* to buy products ~~/donate to~~ from the site owner.
    * View the product details
    * View all the products I want to buy and change quantity if necessary. (cart)
    * View a summary before proceeding to buy any product. (checkout)
    * View a successfull order summary. (checkout success)
* to look back at older orders.

* ~~I want to read the blog.~~
* ~~I want to comment on the blog.~~

As a site ower, I want;
* to see all the relevant information on the site.
* to login as an administrator.
* to change all the relevant information on the site
    * About information, Name/profession etc.
    * Skills, Add/change/delete/hide
    * Services, Add/change/delete/hide
    * Previous projects, Add/change/delete/hide
* to receive messages from users.
* ~~I want to post/update/delete blog posts.~~

[Back to top](#table-of-content)

---

## User Requirements
* Easy navigation.
* Intuitively know what the website is about.
* The ability to register and/or login.
* The ability to purchase services from the site owner and/or donate.
* ~~The ability to read the blog.~~
* ~~The ability to comment/like or dislike on the blog.~~

## User Expectation
* See relevant information about the site owner.
* An overview of experience.
* An overview of past projects.
* Contact the site owner.
* Buy services from site owner.
* Get confirmation on buying a product.
* View past buyorders.
* ~~Comment on blog.~~

[Back to top](#table-of-content)

---

# Design
## Wireframes
I have made wireframes for the sizes Mobile, Tablet and Desktop.
As per Bootstrap order, from small to large. To make the wireframes I have used the program [Balsamig Wireframes](https://balsamiq.com/wireframes/ "Link to Balsamig Wireframes").

#### Mobile Wireframes
* [Mobile Landing Page Wireframe](/readme-images/wireframes/mobile-landing-page.png)

#### Tablet Wireframes
* [Tablet Landing Page Wireframe](/readme-images/wireframes/tablet-landing-page.png)

#### Desktop Wireframes
* [Desktop Landing Page Wireframe](/readme-images/wireframes/desktop-landing-page.png)

#### Other Wireframes

[Back to top](#table-of-content)

## Design Choices
The goal of this site is to be the site owners online resume. Therefore readability is paramount with not much other distractions.

### The structure
For the structure of the website I will use the framework [Bootstrap 5.1](https://getbootstrap.com/docs/5.1/getting-started/introduction/ "Link to bootstrap 5.1").
This framework allows for a proper responsive website which is build up from a mobile-first perspective.
The grid-system that Bootstrap provides is very usefull to have a well working responsive website.
Furthermore Bootstrap has a wide browser compatibility, is quite easy to use and is very customizable.

### Fonts
I will be using a font from [Google Fonts](https://fonts.google.com/ "Google Fonts"), specifically the [Rubik Font](https://fonts.google.com/specimen/Rubik "Rubik Font").
An easy to read, compact and professional looking font.

### Colours
I have chosen for a colour scheme that not to energetic, to goal of the site is mostly to inform. The colours should reprent the site owners personality of being calm and reserved, therefor a calm and reserved colour scheme.

I will use [Bootswatch Slate](https://bootswatch.com/slate/ "Bootswatch Slate") as a base.

![Colour Palette Scheme](https://github.com/Zelhorst92/MyPortfolio/blob/main/readme-images/newcolourpalette%20.png?raw=true "Colour Palette Scheme")

* #191919, Eerie Black
* #272B30, Gunmetal
* #7A8288, Grayweb
* #C8C8C8, Silver, From the clouds of the landing-page image.
* #E9ECEF, Cultured

Suplemented with black and white where necessary.

[Back to top](#table-of-content)

---

## Database Structure

Below the database schema used in this project.
9 Models + 2 models from allauth with their relations shown.

![Database schema](https://github.com/Zelhorst92/MyPortfolio/blob/main/readme-images/my_portfolio_data_schema.png?raw=true "Database schema")
[Back to top](#table-of-content)

---

# Features
## Existing Features
### Navigation
At the top op the page there is a persistion navigation bar. It is present on all pages and has a scroll spy which will follow the user when the user is scrolling along the home page aswell as view the shopping cart.
On smaller devices the navigation bar will collapse into a hamburger menu which will have a dropdown menu on the right side.

### Home page
As this is an online resume the user will on page load see the site owners name, profesion, relevant social media links, aswell as a beautiful image of a misty mountain. Further down the page the user will see a short description of who the site owner is and another picture of the siteowner. Below this the user can see a quick overview of the skillset the site owner.

Below the skills multiple servcies are being shown which can be bought. The user can view the details of these services. 

Even further down there is a gallery of the previos projects done by the site owner. Its a contineous slideshow.

At the bottom the user can see the contact form to get in touch with the site owner. Their message will be directed to the site owners emailaddress. The contact form functionality can be shut down with the variable CONTACT_FORM_ENABLED.

### Service details
Here the user can find the details about the service the user possibly wants to purchase and can also add them to their shopping cart from here. There is also a quantity selector present so that the user can add multiple of the same service into the shopping cart at the same time.

### Shopping cart
In the shopping cart the user can find a summary of services that the user has put in the cart; the individual price per service, the quantity of each service and the subtotals. Aswell the cart total cost, the discount if this applies, the included VAT and the net total. In here the user can also change the quantity of services in the cart. From here the user can proceed to the checkout.
The discount only applies if more then one different services are being bought. The discount and the VAT values can be set with the COMBINATION_DISCOUNT_PERCENTAGE and VAT_PERCENTAGE respectively.

### Checkout
In the checkout the user can see the exactly the same as in the shopping cart but without the ability to change the quantity. This is so the user can view the order one more time to be sure it is all correct. If so the user can fill in the payment form and their credit card information which will be checked by Stripe. If the user is registered, the user can also opt to save its credentials. Else it will be shown a link to register instead. If all information is filled in correctly, the payment intent will be processed by stripe and if successfull the user will be redirected to the checkout success page and receive a confirmation email.

### Checkout Success
When the user has successfully finished a payment the order form will be shown. Here the user can find the order number and the orderdate aswell their basic information; Their full name, email, phone number and country. Below this, are the services bought, price per service, quantities and totals are shown once again. This for that the user is absolutely sure that it has bought the correct service(s) the user wanted to buy. The user also receives the same order info via the mail.

### Register/Login
The user can opt to register to the site. Here is the allauth package used from Django. This functionality includes a registration, email confirmation, login, logout and forgot password.

### Dashboard
If the user is registered it can find a form there to update its contact information which then can be used at the checkout. It also works vice versa, at the checkout the user can opt to choose to save the date to it dashboard. The user can also find its orderhistory here, with the most recent order on the top.

### Order history
From the dashboard the user can select a past order and view this. It is the same template as the checkout success.

### Super_user & CRUD
The site owner and those who are flagged as a super_user can modify almost all information that is present on the main page. If the user is a super_user, then a link to the admin-panel/Manage Site is present in the navigation. From here the user can add/edit/delete the about information, the skills, the services for sale and previous projects.

### 
...

[Back to top](#table-of-content)

## Future Features
### Gallery links
It would be nice to have a direction button to the previous projects websites and/or github links directly from the gallery, so that the users can have a more detailed look of these websites.

### Coffee
It would be nice to have a cup of coffee as a buyable item aswell. This is not a service and in current form it would apply for the discount. A cup of coffee of 2 euro and a website of 1500 euros would come to a discount of 150,20. That means the current programming would have to be revised as in a discount exempt or an attribute for purely discount of services. Possibly the cup of coffee could be donated via different means, bypassing the discount completely.

### Database; Categories for previous projects
At the moment the previous projects dont have an attribute categories. They could share the same category list as the services have as it is in principle the same.

### CRUD; Add/Edit/Delete Categories
At the moment it is not possible to add, edit or delete categories for services.
This would be the first thing I would add in the future. The principle would be the same as adding/editing or deleting any other models that currently exist.

### Register/Login addition
In the dashboard there is need for a change password option. At the moment users can only change passwords via the Forgot Password functionality.

### A Better Confirmation email
The current confirmation email does what it needs to do, but its structure is very basic. This can be improved upon.

### A way to control the ordering of the items in the database
At the moment it seems that the ordering of items is based on what item is the oldest added or edited. As this has an influence on the homepage ordering of items on screen, this should be brought under control. Overiding the assigned id or introducing a SKU.

[Back to top](#table-of-content)

---

# Technologies
## Languages
*   [HTML](https://en.wikipedia.org/wiki/HTML "Link to the HTML wikipedia page")
*   [CSS](https://en.wikipedia.org/wiki/CSS "Link to the CSS wikipedia page")
*   [JavaScript](https://en.wikipedia.org/wiki/JavaScript "Link to the JavaScript wikipedia page")
*   [Python](https://www.python.org/ "Link to the python webpage")


## Libraries and Tools
### Libraries & Frameworks
*   [Bootstrap](https://getbootstrap.com/ "Link to bootstrap")
*   [Bootswatch](https://bootswatch.com/ "Link to bootswatch")
*   [Fontawsome](https://fontawesome.com/ "Link to fontawesome")
*   [Googlefonts](https://fonts.google.com/ "Link to googlefonts") 
*   [jQuery](https://jquery.com/ "Link to JQuery")
*   [Stripe](http://stripe.com/ "Link to stripe")
*   [Django](https://www.djangoproject.com/ "Link to django")

### Validators
*   [W3C Css-validator](https://jigsaw.w3.org/css-validator/ "Link to the w3 css validator")
*   [W3C Markup-validator](https://validator.w3.org/ "Link to w3c markup validator")
*   [Python Validator](https://infoheap.com/python-lint-online/ "Link to pyhton lint validator")

### Tools
*   [Gitpod](https://www.gitpod.io/ "Link to gitpod")
*   [Github](https://github.com/ "Link to github")
*   [Git](https://git-scm.com/ "Link to git")
*   [Heroku](https://www.heroku.com/ "Link to Heroku")
*   [Jinja](https://jinja.palletsprojects.com/en/3.0.x/ "Link to jinja literature")
*   [Amazon AWS](https://aws.amazon.com "Link to Amazon AWS")
*   [Tinypng](https://tinypng.com/ "Link to tinypng") 
*   [Balsamiq Wireframes](https://balsamiq.com/wireframes/ "Link to balsamiq wireframes")
*   [Db diagram](https://dbdiagram.io/ "Link to db diagram")
*   [Coolors](https://coolors.co/)
*   [Contrast Checker](https://webaim.org/resources/contrastchecker/)
*   [Techsini](http://techsini.com/ "Link to techsini.com")
*   [Favicon.cc](https://www.favicon.cc/ "Link to a favicon creator")
*   [Temp Mail](https://temp-mail.org/ "Link to temp-mail")
*   [Devicon](https://devicon.dev/ "Link to Devicon")
*   [Passwordgenerator](https://passwordsgenerator.net/ "Link to passwordsgenerator")

https://devicon.dev/

[Back to top](#table-of-content)

---

# Testing
This is done in a seperate file:

[TESTING.md](# "Link to tests and bugs file")

---

# Deployment
## Clone the repository
- Click on the dropdown menu which says **Code** on the Github Repository.
- You will see several options; 
    - **Clone with a link**, 
    - **Open with GitHub Desktop** 
    - **download ZIP**

#### Clone with a link
- When you want to clone; use the **Clone with HTTPS option**, copy the link displayed.
- Open your IDE and go to the terminal.
- Change the working directory to the location where the cloned directory is to go.
- Use the **git clone** command and paste the url copied in the second step.

#### Open with GitHub Desktop
- If you have GitHub Desktop installed, you can click on this and it will import and clone the repository for you, after selecting where it needs to go.

#### Download the ZIP
- You can also download the whole repository in a zip file and use the IDE software you want.

## Prepare the Repository
### Install requirements
The webapplication relies on several modules and libraries to function. You can find these in the requirements.txt. If you are using an IDE which support [pip](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) you can use the following command:

  ```
  pip3 install -r requirements.txt
  ```

If you are not using or installing pip, find the requirements.txt and install the required modules via any other means. The application will not work without.

### Create env file
In your IDE, create a file containing your environmental variables called env.py at root level. This is because env.py contains private information such as your secret key and is therefore not added to the repository from the get go. It needs to contain the following:

  ```
  import os

  os.environ.setdefault("IP", "0.0.0.0")
  os.environ.setdefault("PORT", "5000")
  os.environ.setdefault("SECRET_KEY", "YOUR_SECRET_KEY")
  os.environ.setdefault("MONGO_URI", "YOUR_MONGODB_URI")
  os.environ.setdefault("MONGO_DBNAME", "YOUR_DATABASE_NAME")
  os.environ.setdefault("DEBUG", "1")
  ```

As you can see, the **SECRET_KEY**, **MONGO_URI** and **MONGO_DBNAME** are placeholders. You have to provide those yourself. The SECRET_KEY can be anything, but the longer the key, the safer it is. The MONGO_URI and DATABASE_NAME will made when you set up the database. You should add the env.py to your .gitignore file, so that others have no access to it.

### Create or Update Procfile and requirements.txt
To run the application on for example Heroku, you need an up to date requirements.txt and procfile. Both are included but if you added anything, you need to update them. You can do that with the following commands in your IDE terminal:
- For your requirements.txt:

  ```
  pip3 freeze --local > requirements.txt
  ```
- For your procfile:

  ```
  echo web: python app.py > Procfile
  ```

- For this application the procfile should contain the following line:
    ```
    web: python app.py
    ```
- If you have more .py files, the procfile should reflect that.

## Prepare the Database
### MongoDB
- Log in or sign-up to [MongoDB](https://www.mongodb.com/).
- Under deployment and databases, create a new cluster. Green button on the right.
- Within the cluster, go to collections and create a new Database.
  - Call this recipe_manager.
  - This is your databasename, use this in your env.py.
- Then in the new database recipe_manager you want to create 3 collections; categories, recipes and users.
  - See [Database Structure](#database-structure) on how to structure them. There should be 3.
    - keep in mind that the _id is genenated by mongoDB itself and does not have to be included.
### Mongo_URI
- To find your mongo_URI link for in your env.py file, go back to main page of the cluster you made earlier.
- Click on the Connect button, on the right side of your clusters name.
- Select 'Connect to your application.
- Select the version of python you are using and copy the link provided.
  - Use this link in your env.py
  - Yes, within the double quotations.

### Set up Database User
- To set up a user that can read and write to your database go to Database Access, on the left.
- Add a new database user.

### Set up network access
- Go to Network Access, on the left.
- Add 0.0.0.0/0 to the IP Adress list.

### Create index
- The application works but search along a text index. You will have to create this.
- In your preffered IDE, go to your terminal and run:
  ```
  python3
  ```
- Then the following:
  ```
  from app import mongo
  
  mongo.db.recipes.create_index([("recipe_name", "text"), ("recipe_category", "text"), ("recipe_description", "text")])
  ```
- This creates an index along the recipe_name, recipe_category and recipe_description which are used to search for recipes.

## Run Application locally
- If you have installed all the requirements, set up the database and made the env.py file, the application is ready the be run locally.
- run the following command in your IDE terminal:

  ```
  python3 app.py. 
  ```

## Deploy application to Heroku
- Log in or sign-up to [Heroku](https://dashboard.heroku.com/).
- On the mainpage, select 'New' and pick 'create new app'
- Chose app-name and region.
- After creation, select 'Deploy' and from there select 'Deployment method'.
- Pick GitHub, find your github username, select the appropriate repository and connect.
- Going back up to navigation and go to 'Settings'.
- Here go to Config Vars and click 'Reveal Config Vars'.
  - Here you enter in the exact same data as you did in your env.py, with the exeption of the debug line.
  - No DEBUG.
- Without the debug it should look this:

  ```
  IP = 0.0.0.0
  PORT = 5000
  SECRET_KEY = YOUR_SECRET_KEY
  MONGO_URI = YOUR_MONGODB_URI
  MONGO_DBNAME = DATABASE_NAME
  ```
  - No DEBUG here.

- Go back to the 'Deploy' page.
- Click on 'Enable automatic deployment'.
- Click on 'Deploy branch'.
  - Heroku will now build the application. This might take a while.
- When the building is complete, you can now click 'view app' to open the application.
- Because the heroku app is now linked to github, the changes you push to GitHub are automatically pushed the heroku aswell.

[Back to top](#table-of-content)

# Credits

## Aditional Sources

Stamp picture = https://www.pngfind.com/mpng/iohTbwb_mail-stamp-template-postmark-png-image-postage-stamp/
...

## Thanks
...

## Afterword
...

[Back to top](#table-of-content)