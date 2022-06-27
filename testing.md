# Testing for BookHideout

## Features 

### Home page:
* Call to action on home page
    * Expected: There is a clear and obvious call to action on the home page
    * Works: YES
* Easy to use navbar
    * Expected: All links work to every page, on every page. Same for footer.
    * Works: YES
* Collapsed mobile view navbar
    * Expected: The navbar collapses down for easier viewing on smaller screens
    * Works: YES
* Sign-up to newsletter form in footer
    * Expected: Submitting an email in the newsletter subscription form in the footer gives feedback about subscribing
    * Works: YES
* External links open in new page
    * Expected: Clicking on the Facebook link in footer will open the Facebook page in new tab
    * Works: YES
* Shop now button
    * Expected: Clicking the shop now button will display a page with all products
    * Works: YES
* Search bar
    * Expected: Searching for books by title, author or ISBN will show books matching the search query
    * Works: YES
* Basket icon
    * Expected: Total of basket is displayed under the basked icon and updated with every item added to the basket
    * Works: YES
* Account icon
    * Expected: Account icon reflects login status of user 
    * Works: YES
* Lower navbar
    * Expected: Clicking links on the lower navbar filters or sorts the products in a relevant maner
    * Works: YES

### Products page
* Product details
    * Expected: Clicking on product image takes the user to the products detail page
    * Works: YES
* Number of products
    * Expected: Number of products in the upper left corner reflects number of products displayed on page
    * Works: YES
* Sort by
    * Expected: Selecting a sort option in the upper right corner will sort the products in the selected manner
    * Works: YES
* Edit and delete links
    * Expected: Edit and delete buttons below each product can be seen by a logged-in superuser but not by other users
    * Works: YES
* Sale prices
    * Expected: If an item is on sale, the old price is struck through and the sale price is displayed 
    * Works: YES

### Product details page
* Information about product
    * Expected: Information about a product is clear and well layed out
    * Works: YES
* Add to basket button
    * Expected: Clicking add to basked button results in adding item to basket, showing success message and total on basket and updating basket summary in basket preview
    * Works: YES
* Keep shopping button
    * Expected: Takes the user back to the all products overview
    * Works: YES
* Edit and delete links
    * Expected: Edit and delete buttons over the quantity form can be seen by a logged-in superuser but not by others
    * Works: YES
* Quantity form
    * Expected: User can adjust the quantity of the product to be added to the basket using the quantity form
    * Works: YES
* Genre links
    * Expected: Clicking on a genre link will bring the user to the all products page with the genre relevant genre link active. Only books of the selected genre are visible
    * Works: YES

### Shopping basket page
* Shopping basket icon
    * Expected: Clicking the shopping basket icon brings the user to an overview of the current basket content
    * Works: YES
* Quantity form and update link
    * Expected: Adjusting the quantity and clicking the update link will adjust the basket content. The change will be reflected in the subtotal and grand total.
    * Works: YES
* Remove link
    * Expected: Removes item from basket. The change will be reflected in the grand total and the item disappears from the list.
    * Works: YES
* Keep shopping button
    * Expected: Takes the user back to the all products overview
    * Works: YES
* Secure checkout button
    * Expected: Takes the user to a checkout page 
    * Works: YES

### Checkout page
* Checkout form
    * Expected: The user sees a form to fill it with shipping and payment information, if the user is logged in and has previously saved his info, the form is pre-filled
    * Works: YES
* Form validation
    * Expected: If the user enters invalid data to the checkout form, the form is not submitted and information about the error is given
    * Works: YES
* Save delivery information option
    * Expected: Logged in user sees a checkbox to save info to their profile. Other users see links to sign-up and login page
    * Works: YES
* Edit basket button
    * Expected: Takes the user back to the shopping basked page
    * Works: YES
* Complete order button
    * Expected: Completes the order, payment is taken, user is given an order confirmation. Order confirmation is also sent to the email provided in the checkout form and saved in the order history. A success message is displayed
    * Works: YES
* Order summary
    * Expected: A summary of all the items to be purchased is displayed including grand total 
    * Works: YES

### Checkout success page
* Order confirmation
    * Expected: Oder confirmation is displayed
    * Works: YES

### Account pages
* Sign-up form 
    * Expected: Filling the form and clicking the Sign Up button creates a new user. A confirmation email is send to the email used in the form
    * Works: YES
* Email registration confirmation Email
    * Expected: After a user registers they are sent an email to confirm that email address
    * Works: YES
* Sign in button
    * Expected: There is a sign in button which brings user to login page - visible when logged out and isn't visible when users are logged in
    * Works: YES
* Logout button
    * Expected: When clicked it takes user to logout page. Visible when logged in, not visible when logged out.
    * Works: YES
* Forgot password link 
    * Expected: When user clicks the forgot password button, an email is sent to their registered email address
    * Works: YES

### User profile page
* My profile link
    * Expected: Clicking the my profile link in the dropdown of the account link brings the user to their profile
    * Works: YES
* My profile page
    * Expected: Displays users default delivery information and order history
    * Works: YES
* Update information
    * Expected: Clicking the update information button renders a form to update the delivery information pre-filled with the current delivery information. Submitting the form updates the delivery information
    * Works: YES
* Order number link
    * Expected: Clicking on the order number links displays a past order confirmation for the selected order
    * Works: YES

### Product management
* Product management link
    * Expected: A signed in superuser can see a product management link in the account dropdown. Clicking on the link takes the user to a add product page
    * Works: YES
* Add product page
    * Expected: Displays a form to fill in with the details for a new product
    * Works: YES
* Change image button
    * Expected: Clicking the button takes the user to a open dialog and enables them to pick an image for the product
    * Works: NO - user is able to pick an image, but the image is not displayed in the all products page or product details page 
* Add image by URL
    * Expected: After adding url to image and submitting add book form, image is visible on all products page and product details page
    * Works: NO
* Form validation
    * Expected: If the user enters invalid data to the add book form, the form is not submitted and information about the error is given
    * Works: YES
* Add book button
    * Expected: Clicking the button submits the add book form, a new product is created, a success message is displayed, the user is redirected to the product details page of the book just created
    * Works: YES
* Cancel button
    * Expected: Takes the user back to the all products page
    * Works: YES
* Edit book link
    * Expected: Clicking the edit book link in the all products or products details page takes the user to an edit product page
    * Works: YES
* Edit product page
    * Expected: Displays a form to update the product details pre-filled with the data for the selected product 
    * Works: YES
* Change image button
    * Expected: Clicking the button takes the user to a open dialog and enables them to pick an image for the product
    * Works: NO - user is able to pick an image, but the image is not displayed in the all products page or product details page 
* Add image by URL
    * Expected: After adding url to image and submitting edit book form, image is visible on all products page and product details page
    * Works: NO
* Delete book option
    * Expected: Clicking delete button on all products page or product details page displays a modal with a delete confirmation, clicking yes deletes the relevant product
    * Works: YES

### Sales management
* Sales management link
    * Expected: A signed in superuser can see a sales management link in the account dropdown. Clicking on the link takes the user to a sales overview page
    * Works: YES
* Sales management page
    * Expected: An overview page that shows a list of all the sales that are currently in the database
    * Works: YES
* Add sale button
    * Expected: Takes the user to the add sale page
    * Works: YES 
* Add sale page
    * Expected: Displays a form to fill in with the details for a new sale
    * Works: YES
* Form validation
    * Expected: If the user enters invalid data to the add book form, the form is not submitted and information about the error is given. The user cannot create a sale that overlaps with another sale
    * Works: YES
* Add sale button
    * Expected: Clicking the button submits the add sale form, a new sale is created, a success message is displayed, the user is redirected to the sales management page
    * Works: YES
* Cancel button
    * Expected: Takes the user back to the sales management page
    * Works: YES
* Edit button
    * Expected: Clicking the edit button in the sales management page takes the user to an edit sale page
    * Works: YES
* Delete button
    * Expected: Clicking the delete button deletes the relevant sale
    * Works: YES
