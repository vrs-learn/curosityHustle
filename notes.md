#### These notes are relevant for the Python and Flask Bootcamp by Jose Portilla

# Pre-requisites:

* Install Anaconda
* Download the requirements file from the course.

# Installing Flask and setting up environment by using the requirements.txt file

* conda create -n mynewflaskenv python=3.8 

At the prompt enter the Y to continue.

Now to activate the environment, use below command:

* activate mynewflaskenv

Now to install the packages in requirements.txt, install as below:

* pip install -r requirements.txt 

# Python and Flask 

* Python is the coding language that allows us to use the Flash web framework.
* Flask renders HTML templates, can edit them with Jinja, and communicate with a database through the use of libraries such as SQLAlchemy (Flask-SQLAlchemy)

--------------------------------------------------------------------------

# HTML Crash

## Html Tags
Two main tags - head & body
Multiple header tags - from h1 to h6
paragraph tag  - p
loren ipsum - to generate some random text within html
strong tag = makes text bold
em tag = emphasis tag, it makes text italic
For html elements tags refer -> developer.mozilla.org

## Html Lists
Two tags for lists:
* ul -> unordered list (The items are bulleted)
* ol -> ordered list (The items are numbered)
both the tags can be nested, i.e can be put into one another. The browser is smart enough to add indentation as per the nesting.

## Divs and Spans
Divs and Spans allows us to segment portions of our HTML.

## Html attributes
src -> this attribute can be used in "img" tag to link an image or object
alt -> this attribute can be used when the "src" linked image or object is not available. Can have any text or something.
a (Anchor) tag with "href" -> Used to link to another website OR to another webpage stored locally.

## Html Forms
<form> -> tag to setup form
<input> -> tag to accept user information

### Input tag attributes:
type -> tells the browser what actual type of text it has to render (default "text"). 
        Other values:
            * "password" (Hides the text when entered in browser)
            * "email"
            * "submit" (This adds a button)
name -> identifier of the input value which can be used further
value -> actual value to be transmitted or displayed

### Html Form labels
Two main methods of submitting form information:
* GET
* POST


