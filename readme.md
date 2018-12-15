# AV Empire Django website

## Overview

### What is this website for?

This website is designed to allow users to browse and purchase Audio Visual (AV) products and as such, it's an e-commerce site.

### What does it do?

The website provides an online presence for a fictional company "AV Empire" and allows users to register on it, log in and log out, to send an enquiry to the company via the contact form and to purchase the products on offer in the 'webshop'. Of course, users are also able to find out a bit about the company and browse through the products.

### How does it work?

The site's major functionality is to allow users to purchase AV products. To be able to do so users first need to register on the site. They can add products to the 'cart' and adjust the number of items in it without prior registration but as soon as they want to go to the 'checkout' (the next step in the process) they have to either register or log in (if already signed up). The final step is to fill out some personal information and debit or credit card details before submitting payment on the checkout page.

Additionally, the website allows users to submit an enquiry on the contact page. They will then get a reply to the email address they have indicated on the form, with a summary of their enquiry and also informing them that a representative from the company will be in touch in due course. No prior registration is needed for this.

## Demo

You can see the deployed version of the website [here](https://av-empire.herokuapp.com/).

## Features

- Responsive design ensures the website displays well on any screen size and device type
- User authentication and authorisation - handling registration, logging in and logging out
	- users who are not logged in will see a *Register* and *Log In* options in the Navigation bar, but those who are - will see a *Profile* and *Log Out* options instead
- Products pages - display product information that is stored on the cloud database using MySQL (ClearDB add-on)
- Cart and Checkout functionality
	- the Cart app stores the information of each product that is added to it and displays a cart total; the Checkout app also stores this information and displays a total but additionally renders a form for a one-off Stripe payment
- Using Stripe API to process user payments (this is part of the Checkout functionality)
- Contact form functionality
	- allows users to fill out a form, which after submission will trigger an email to be sent to them using Gmail SMTP (and my own Gmail account)
- Bootstrap's Breadcrumbs - located just below the main navigation - is a very useful feature, which provides supplementary links indicating the current page's location within a navigational hierarchy that can be used by the visitor to "retrace" their steps upwards through the site

## Technologies used

- HTML5
- CSS3
- JavaScript
- jQuery
- Bootstrap 3
- Python 2.7
- Django
- Stripe
- MySQL (ClearDB add-on)
- Font Awesome

## Testing

### Responsive testing and code validation

#### Browsers and devices
```
Mozilla Firefox
Google Chrome
Internet Explorer
Safari
```
The website looks good and works fine at full screen size on all of the above mentioned browsers. I used the developer tools in Google Chrome and Firefox, as well as my own Android phone and an iPad, to check how the site looks on smaller screen devices and it does well in all respects.

#### Code validation

I put my code through *W3C* (for both HTML & CSS) and *JSHint* online validation services to make sure the code is as clean and error-free as possible.

### Automated testing

To begin with I carried out some automated testing, which has the benefits of speedy application to potentially large units of code and reusability.

The main part that I tested were the forms in my **accounts** app, which take care of user registration and sign ins. The primary concern here was to check that form validation works in a number of user input scenarios.

More specifically, validation was tested for the following scenarios:
* A user not filling in at least one required field, if not multiple
* A user not providing both a username and an email (since both are required to register)
* A user not providing passwords that match
* A user not filling in the first password field
* A user not filling in the second password field (password confirmation)

In each case the tests needed to pass in order to confirm that the validation is working.

However, I also needed to be able to make them fail, so I could be sure that they equally recognise when the opposite scenario is true.

So, in brief, I simulated the opposite conditions for the same tests as follows:
* All required fields filled in *
* Both username and email present
* Both passwords match
* First password filled in
* Second password filled in

\* When a test failed, each error displayed was an "AssertionError". In the case of the first test the error given was "False is not true" because it is the only one with the statement `self.assertTrue(form.is_valid())`. All the other tests use `self.assertFalse` and so displayed *AssertionError: True is not false*.

Since this time the inputs didn't meet the conditions required to make the tests pass - that is, validation wasn't triggered by wrong or missing input - they failed, as expected.

The tests for the **accounts** app can be found in *tests.py* located in the *'accounts'* directory.

I also tested the Order form in my **checkout** app using the same procedures. For brevity, I tested only half of the 'required' fields, since all it was testing for is validation taking place when a user is not filling in a certain field, going through each, one by one.

The tests for the **checkout** app can be found in *tests.py* located in the *'checkout'* directory.

All in all, I was able to make the tests pass and also fail when using expected inputs, so they are certainly working as intended.

### Manual testing
<details>
<summary>Click to see details</summary>
<br />

I conducted manual tests on a number of features on the website - these are documented below.

#### Authorisation

I tested the security aspect of my project, which means users who have not met certain conditions will not be able to access some restricted areas of the site. This mainly concerns the Profile, Log Out and Checkout pages. When a user tries to reach any of those pages while not logged in they will get redirected back to the Log In page and so any potential errors are avoided.

This is achieved by using a `@login_required` decorator at the head of each relevant view in *accounts/views.py* as well as *checkout/views.py*, which will check whether a user is logged in before taking them to any of those pages.

#### Navigation

I tested the navigation aspect of my website to make sure that all the links provided take the user exactly where they are supposed to. A major part of this is the navigation bar at the top of every page. The *Products* drop-down menu functions correctly as part of this. Additionally, the **Breadcrumbs** feature also works well.

All of the above has also been tested on smaller screen devices and I can confirm that everything - including the collapsible 'navbar' menu - works as intended. This of course is also a big part of Responsive testing and so needs to be spot on.

#### Products and Cart pages

I tested the input of various numbers into the product quantity fields on the products pages and the cart page. Users can successfully add a minimum of 1 item (from a choice of one or more products on offer) to the cart. If there were to be any attempt to add anything less (i.e. '0' items) the system would prevent that from happening. This is achieved using a combination of `value="1"` and `min="1"` attributes, which between them ensure that the user will be able to add a minimum of 1 item to the cart and that on page load that is the default number displayed in all the input fields as a prompt for the user. Also, to avoid any potential issues with large numbers the maximum input limit was set to 999 (`max="999"`).

On the cart page, however, it was necessary to set the required minimum to 0 (`min="0"`) on all input fields because we still want the users to be able to amend the quantity of any product item down to 0 if they wish to remove a given product from the cart.

#### Checkout page

I tested the functionality of the payment form on the checkout page to ensure that validation is working correctly when the user either doesn't fill in a required field or types invalid information into one of them. This is certainly true for each field concerned (as you get an error message if a requirement is not met) so the form passes in all respects.

Additionally, after you submit the form it redirects you to the products page and you get a successful submission message near the top of the page, as intended, so once again the test is a success.

#### Contact page

I tested the Contact form on this page and verified that all the required fields do indeed have a validation message coming up for each of them (asking the user to fill it in) if the user tries to submit the form while leaving any of them blank. The one exception to this is the *Phone number* field, which is not required, however if the user enters an invalid number (in this case a number of any length other than 10 or 11 digits) then an error message will come up. If this field is left blank though - provided everything else is filled in - the form will still submit successfully. So I have verified that the form submission is accepted when inputs are valid and denied when an invalid input is provided for any of the fields.

Upon submission of the form the user should be redirected to the home page and get a successful submission notification near the top of the page. Additionally, the user should receive an email on the same email address they provided on the form, telling them that their enquiry has been received and somebody will be in touch. The email reply should also contain confirmation of all the details the user provided on the form. After testing I can confirm that all of this works as intended.

#### Issue with Contact form

I had to set up the use of an external mail server for sending emails with automatic replies to users who filled out my contact form and for this project we were advised to use a simple and free provider, namely **Gmail**. Simple, that is, as long as you have a Google/Gmail account, which I do.

Now, because Google take the security of people's accounts and associated email accounts quite seriously for obvious reasons, there is unfortunately an unavoidable problem that comes with using your personal Google account as a server for sending emails. The first time that I tried to submit the contact form on my live site I got a *server error* message because Google was blocking my 'sign in' attempts as they thought somebody else was trying to sign into my account from an "unrecognised device" and/or in an "unusual location".

I was able to resolve the issue initially by going to my Google account and turning on an option to "allow less secure apps" to access my account. However, it turned out that an additional measure had to be taken to get rid of the server error and that was to go to a *DisplayUnlockCaptcha* page on my account and click a button to "allow access to my Google account".

When it seemed that this email issue was finally resolved it then happened again about a couple of weeks later. Thankfully I was able to take care of it straight away by going to the *DisplayUnlockCaptcha* page once more. However, if it can happen to me again so soon after verifying my account and while I was testing the contact form on the same (recognised) device then it can certainly happen to anybody else testing my form from another location and/or device.

Users of my website need to be aware of this potential problem should they get a *server error* message when trying to submit the contact form. Unfortunately, this is a third-party issue and is therefore out of my control.

#### Database

The main thing to test here was the correct functionality of MySQL (ClearDB) database on Heroku - namely that it serves all the product information (that has been uploaded there) to all the relevant web pages and that it successfully stores new user data and retrieves it when users sign in, etc.

With regards to displaying all the requested product information, I checked every single product page, then the cart page (with a number of different product combinations added to it) and finally the checkout page (displaying the same selections as the cart page) and found no problems in relation to any missing data.

As for storage of user data, I tested by registering different users, logging out and then back in and every time authentication was successful. Therefore the logical conclusion here is that the database functions efficiently and as intended.

</details>

## Deployment

Firstly, to prepare for deployment, my project's main settings file had to be adapted for the different environments that the project would go through. I created a **settings** package/directory (as an app) and within it I set up **base.py**, **dev.py** and **staging.py**. The base.py is the main settings file (for the default environment) and contains settings that are shared across all three environments. The next file provides the settings for the project's development environment and the final file provides the settings for the staging environment - respectively. Each of the latter files adds some extra settings (to the base.py) that are only needed for that particular environment.

The other thing that needed to be done was to ensure I have the correct dependencies for each of the environments. This was done by creating a **requirements** directory (also in the project root) and then **base.txt**, **dev.txt** and **staging.txt** inside there. The original *requirements.txt* file was kept in the root directory since Heroku still looks for it in order to check for dependencies.

At this point the original project code had already been pushed to the appropriate remote repository on my GitHub account. So the next stage was to set up Heroku to host my website and to connect it to my GitHub account and the particular remote repository (master branch) that hosts the project code.

The following steps were taken to achieve this:

- A new Heroku app (Europe region) was created on my Heroku account
- Under the *Deploy* tab of my app in the 'Deployment method' section I selected GitHub and found my project's repository
- I then granted Heroku access to it via *Authorise application* and then enabled 'Automatic deploys' from GitHub (enabling Heroku to deploy the latest code that's uploaded to the repository)
- A python package called **gunicorn** was installed and added to **base.txt**, since it is needed to run Python web applications on Heroku
- Also added **Procfile** and **Procfile.local**, as well as **runtime.txt** (which should tell Heroku to use the latest version of Python, even if your local project isn't doing so)
- Then I set the ```DJANGO_SETTINGS_MODULE``` variable to **settings.dev** on the local project; and also set the environment on Heroku to use **settings.staging**
- Additionally, **whitenoise** package was installed to serve static files on Heroku

Another important part of the process was to set up Stripe connection details on Heroku to enable users to make payments on the live site. That involved copying the environment variables - ```STRIPE_PUBLISHABLE``` and ```STRIPE_SECRET``` keys (which were originally generated on my Stripe account) from either **dev.py** or **staging.py** and placing them in the 'Config Vars' section under the *Settings* tab on Heroku.

One of the last things to do was to set up a database on Heroku. Under the *Resources* tab of my app in the 'Add-ons' section I found **ClearDB MySQL** and provisioned it for the app. At that point the database automatically created a new *Config Variable* (```CLEARDB_DATABASE_URL```) that stores all the info needed to connect to it remotely. This is found under the *Settings* tab in 'Config Vars' section. Finally, I added the environment variables for that database in my **staging.py** file so that URL could be used to connect to my database. Also, the **dj-database-url** package was installed locally and added to **staging.txt** in order to retrieve the value of the *Config Variable* from Heroku to generate the database connection details.

Additionally, the cloud database needed to be populated with the same data that I was using locally, so first of all, migrations were run on Heroku to create tables on **ClearDB**. Then the local database was 'dumped' into a *json* file (using the **dumpdata** command) which was then pushed to my GitHub repository. Finally, the data was loaded into the staging database on Heroku using the generated *json* file.

It is worth mentioning that all the product information in the local database was initially loaded up from a csv file called *price_list.csv* that can be found in the *docs* folder.

## Wireframing

I used **Balsamiq Mockups** to create a wireframe/storyboard for my website and the mockup files can be found in the *docs* folder.

## Credits

### Content

Courtesy of the press release published by the trade association [AVIXA](https://www.avixa.org/about-avixa/who-we-are/press-room/2017/10/02/avixa-releases-global-av-industry-outlook-and-trends-analysis)

### Acknowledgements

A special thank you to **@mr_bim** and **@mormoran** who helped me out with some minor but nonetheless tricky aspects of the project.