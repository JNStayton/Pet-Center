In this exercise, you’ll build a web application for a Pet Adoption Agency.

## Step 1: Create Database & Model
Create a Flask and Flask-SQLAlchemy project, “adopt”.

Create a single model, Pet. This models a pet potentially available for adoption:

1. id: auto-incrementing integer
2. name: text, required
3. species: text, required
4. photo_url: text, optional
5. age: integer, optional
6. notes: text, optional
7. available: true/false, required, should default to available
>>While setting up the project, add the Debug Toolbar.

## Step 2: Make Homepage Listing Pets
The homepage (at route /) should list the pets:

1. name
2. show photo, if present
3. display “Available” in bold if the pet is available for adoption

## Step 3: Create Add Pet Form
Create a form for adding pets. This should use Flask-WTF, and should have the following fields:

1. Pet name
2. Species
3. Photo URL
4. Age
5. Notes
This should be at the URL path **/add.** Add a link to this from the homepage.

## Step 4: Create Handler for Add Pet Form
This should validate the form:

1. if it doesn’t validate, it should re-render the form
2. if it does validate, it should create the new pet, and redirect to the homepage
This should be a POST request to the URL path **/add.**

## Step 5: Add Validation
WTForms gives us lots of useful validators; we want to use these for validating our fields more carefully:

1. the species should be either “cat”, “dog”, or “porcupine”
2. the photo URL must be a URL (but it should still be able to be optional!)
3. the age should be between 0 and 30, if provided

## Step 6: Add Display/Edit Form
Make a page that shows some information about the pet:

1. Name
2. Species
3. Photo, if present
4. Age, if present

It should also show a form that allows us to edit this pet:

1. Photo URL
2. Notes
3. Available
This should be at the URL **/[pet-id-number].** Make the homepage link to this.

## Step 7: Handle Edit Form
This should validate the form:

1. if it doesn’t validate, it should re-render the form
2. if it does validate, it should edit the pet
3. 
This should be a POST request to the URL path **/[pet-id-number].**

## Step 8: Clean Up Your Code!
A critical step for any project is to refactor and clean up code; it’s good to do this iteratively, as you work.

Check for:

1. function names: good functions names are “verby”, like show_add_form
consistent use of good variable names
2. every class or function should have a docstring describing its purpose
3. add comments for any parts that would benefit from this
4. add a file showing all of the Python requirements for this project