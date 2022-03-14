# Testing and Bugreports

* [Testing](#testing)
    * [Navigation](#navigation)
    * [Information](#information)
    * [Authentication](#authentication)
    * [Purchase](#purchase)
    * [Contact](#contact)
    * [CRUD](#crud)

    Contact

* [Bugreports](#bugreports)
    * [Confirmation Email](#confirmation-email)


https://robert-l-zelhorst-portfolio.herokuapp.com/





# Testing

##  Navigation
### User Expectation
*   As a user, I want a website that is easy and intuitively to use.
*   As a user, I want to see what the website is about at first glance.
*   As a user, I want a website that works on all screen sizes.
*   As a user, I want to be able to traverse to relevant social media.
### Intention
*   The navigation bar on the top of the screen is mostly focussed on the homepage, with a spyscroll following the user where it goes. The scrollspy also shows if the user is in the cart. The user can also find the login/registration and logout/dashboard links here. The superusers also have access to Manage Site. Also the site should be responsive to most if not all screen sizes. Lastly every user will start on the homepage in the hero section. It should be obvious where the site is about upon seeing this. And the social media links should work.
### Tests
1.  See if scrollspy works on the homepage & cart.
2.  See if login/register change to logout/dashboard upon login in and vice versa.
3.  See if non superusers can see the Manage site link. And if superuser actually can see the link.
4.  See if site is responsive.
5.  See if landing is obvious to users.
6.  Check to social media links.
### Results
1.  Scrollspy works as intended.
2.  Upon logging in the relevant links change.
3.  Non Superuser do not see the Manage Site link. Superusers do.
4.  Tested on all standard dimensions in the chrome developer tools aswell as my Sony Xperia XZ and various other smartphones in the family. It seems that that Iphone 4 in the chrome devtools has a slight problem with the info-card, as it bleeds over into the about page.

![Iphone 4 Issue](https://github.com/Zelhorst92/MyPortfolio/blob/main/readme-images/iphone4-issue.png?raw=true)

5.  Landing is obvious. Name, profesion, socialmedia links and call to action are all present.

![Landing Page Visual](https://github.com/Zelhorst92/MyPortfolio/blob/main/readme-images/landing-page-obvious.png?raw=true)

6.  Social media links, link to appropriate sites, in a new tab.
### Conclusion
*   All tests passed.
### Bugs
*   None.
### Comments
*   The Iphone 4 size problem has been noted, but as it is an old phone and it does not hamper functionality that much; it will be left as is.

[Back to top](#testing-and-bugreports)

##  Information
### User Expectation
* As a user, I want to read about the site owner;
    * Past builds
    * Experiences with;
        * Languages
        * Frameworks
        * etc.
    * Public personal information.
* As a site ower, I want to see all the relevant information on the site.
### Intention
*   The homepage functions as an online resume for the site owner. All the information to inform visitors ie. the users should be there; Summary, skills, services, past projects.
### Tests
*   Visual test if everything is present. (Information change is handled in the CRUD test.)
### Result
*   Test passed. All information is present.

![Information Test](https://github.com/Zelhorst92/MyPortfolio/blob/main/readme-images/information-test.png?raw=true)

### Conclusion
*   All tests passed.
### Bugs
*   None.
### Comments
*   None.

[Back to top](#testing-and-bugreports)

##  Authentication
### User Expectation
* As a user, I want to register to the website.
* As a user, I want to login to the website.

### Intention
*   The user could register to the site, to save its contact information for buying a service and to look back their order history on their dashboard.
### Tests
1.  Register to the site.
2.  Receive confirmation email.
3.  Confirm Email.
4.  Login and view dashboard.
5.  Logout.
### Result
*   All worked as intented. See pdf for screens.

[Authentication Test Pdf](https://github.com/Zelhorst92/MyPortfolio/blob/main/readme-images/authentication-test.pdf)

### Conclusion
*   All tests passed.
### Bugs
*   None.
### Comments
*   None.

[Back to top](#testing-and-bugreports)

##  Purchase
### User Expectation
* As a user, I want to buy products from the site owner.
    * View the product details
    * View all the products I want to buy and change quantity if necessary. (cart)
    * View a summary before proceeding to buy any product. (checkout)
    * View a successfull order summary. (checkout success)
* As a user, I want to look back at older orders.
### Intention
*   The user wants to buy a service from the site owner. The user will take the path of purchasing a service.
### Tests
*   Complete a path of purchase.
### Result
*   Purchase was successful. See the document below.

[Purchase Path Test Pdf](https://github.com/Zelhorst92/MyPortfolio/blob/main/readme-images/purchase-path-test.pdf)

*   The confirmation email shows `{&quot;1&quot;: 1}` where it should show the order.
### Conclusion
*   Test successful.
### Bugs
*   Confirmation email has a problem with showing the order. 
### Comments
*   Style of the confirmationmail could be better. As this is not webpage breaking, it does hamper user experience a little bit.

[Back to top](#testing-and-bugreports)

##  Contact
### User Expectation
* As a user, I want to contact the site owner.
* As a site ower, I want to receive messages from users.

### Intention
*   The user should be able to contact the site owner via the contact form at the bottom of the home page.
### Tests
*   Send a message with the contact form.
### Result
*   Test passed. Message sent and received when CONTACT_FORM_ENABLED was true. User gets error message when CONTACT_FORM_ENABLED was none. See document below.

[Contact Test](https://github.com/Zelhorst92/MyPortfolio/blob/main/readme-images/contact-test.pdf)

### Conclusion
*   Test passed.
### Bugs
*   None.
### Comments
*   None.

[Back to top](#testing-and-bugreports)

##  CRUD
### User Expectation
*   As a site ower, I want to login as an administrator.
*   As a site ower, I want to change all the relevant information on the site
    *   About information, Name/profession etc.
    *   Skills, Add/change/delete/hide
    *   Services, Add/change/delete/hide
    *   Previous projects, Add/change/delete/hide

### Intention
*   The siteowner and/or its superuser should be able to alter the information on the homepage, add/edit/delete or hide the skills, services and previous projects. Only the siteowner and superuser should be able to access the site manager.
### Tests
1.  See if normal users can access the admin panel/site manager.
2.  Complete a path of addition/edition/hiding and deleting a skill/service/previous project, edit about. One path will be supported with screens, the rest will be tested and confirmed;
    *   Skill path.
    *   Service path.
    *   Project path.
    *   About edit.
### Result
1.  Test passed. Normal users are unable to access the admin panel or any add/edit/delete url. See the document.
2.  All the paths were successful with the exception of the deletion modal. It seems that the modals generated with each individual item are not unique.

[CRUD Test](https://github.com/Zelhorst92/MyPortfolio/blob/main/readme-images/CRUD-test.pdf)
### Bugs
*   Modal not unique to the id of the item that needs to be deleted. See [Wrong Modal](#wrong-modal)
### Comments
*   It also seems that the ordering of the items after editing changes. This does not break anything and is therefore not a bug. But it is worth looking into as the ordering also determines in what order the items appear on the homepage. To give the siteowner more control over where goes what, the order should also be determinable. Possible with overriding the id of the items.

[Back to top](#testing-and-bugreports)


# Bugreports

## Confirmation Email
### Bug
*   The confirmation email shows `{&quot;1&quot;: 1}` where it should show the order.
### Fix
*   Change from
```
{{ order.original_cart }}
```
to
```
{% for item in order.lineitems.all %}
    {{ item.quantity }} * {{ item.service.name }} for €{{ item.service.price }}.
{% endfor %}
```
### Conclusion/Result
*   Wrong call in earlier statement. The order.lineitems.all works.
### Status
*   Resolved.

[Back to top](#testing-and-bugreports)

## Wrong Modal
### Bug
*   Modal not unique to the id of the item that needs to be deleted.
### Fix
*   Change the id of the modal from 
```
<div class="modal fade" id="ConfirmModal" tabindex="-1" aria-labelledby="ConfirmModalLabel" aria-hidden="true">
``` 
to
```
<div class="modal fade" id="ConfirmModal{{skill.id}}" tabindex="-1" aria-labelledby="ConfirmModal{{skill.id}}Label" aria-hidden="true">
```
and the anchor target from
```
<a href="#ConfirmModal" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#ConfirmModal">Delete</a>
```
to
```
<a href="#ConfirmModal{{skill.id}}" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#ConfirmModal{{skill.id}}">Delete</a>
```

### Conclusion/Result
*   This will make the modal unique to their respective deletion button.
### Status
*  Resolved.

[Back to top](#testing-and-bugreports)
