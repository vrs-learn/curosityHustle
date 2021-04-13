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

# HTML Crash (Check 01-HTML-Crash-Course for examples)

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
src -> this attribute can be used in "img" tag to link an image or object.
alt -> this attribute can be used when the "src" linked image or object is not available. Can have any text or something.
a (Anchor) tag with "href" -> Used to link to another website OR to another webpage stored locally.

## Html Forms
form -> tag to setup form
input -> tag to accept user information

### Input tag attributes:
type -> tells the browser what actual type of text it has to render (default "text"). 
Other values:
* "password" (Hides the text when entered in browser)
* "email"
* "submit" (This adds a button)
* "radio"
name -> identifier of the input value which can be used further
value -> actual value to be transmitted or displayed
placeholder -> provides a diffused text which is shown in the webpage. This text goes away as soon as the user starts writing something in it.

### Html Form labels
Two main methods of submitting form information:
* GET (requests a represntation of specified resource. It sends back the information to our action URL)
* POST (submits data to be processed)

#### Using Form, labels and actions:
* label -> tag that provides a label for another tagged id.
* action -> attribute of form tag. It contains a target URL to be triggered once a submit button is clicked.
* method -> get or post. attribute of form tag.

When using an action and method attributes in the form tag, when a submit is hit on the webpage, the values mentioned in the form are passed as parameters to the URL mentioned in the action tag.

### Linking Radio buttons, Drop Down menus and Text area inputs.
To link radio buttons, use same name in both the input tags.
```xml
<input type="radio" id="yes" name="dog_choice" value="yes">
<input type="radio" id="no" name="dog_choice" value="no">
```

* select -> tag to create a dropdown. ("name" attribute is used to provide a name to the tag.)
* option -> a child tag of select, which provides the options in the dropdown ("value" attribute to pick the value when the user selects the value from the form.)

textarea -> tag to create text box to enter free text.

--------------------------------------------------------------------------

# CSS Crash (Check 02-CSS for examples)
CSS -> Cascading Style Sheet.
It allows to change the style attributes of HTML elements (like color , background, borders etc.)

How to use .css:
* Create a .css file
* Use css syntax to link elements tags
* add style attribute name-value pairs
* connect css to html

To link a css file to an HTML page, in the head tag, create a new child tag named link as below and enter the CSS filename in the href:
```xml
<link rel="stylesheet" href="CSS FILENAME">
```

To style selected items use classes and ids to style. Every HTML element can accept a class or id attribute.
We can then specifically connect to these classes or ids from our CSS with a special syntax.
* .(periods) for a class call.
* \# for an ID call.

## Adding Google fonts to stylesheet.
First find the font on the fonts.google.com and select it. It should show you the pop-up with the link and CSS rules.
The link would go into the head tag of the html page.
The CSS rules can then be used in the css file.

--------------------------------------------------------------------------
# Bootstrap (Check 03-Bootstrap4 for examples)

At its core, bootstrap is just a CSS file and a Javascript file.
www.getbootstrap.com

## Basics and Buttons:
Bootstrap contains its compiled CSS and JS files. These are configured to auto adjust to the device where its opened.
To use bootstrap CSS and JS files, use the CSS and JS links available in getbootstrap.com in the head tag. Then we use the same classes which are available in the documentation in our tags in the html pages.
Below are the links which have to be used.
```xml
<!-- CSS only -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
<!-- JavaScript Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js" integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous"></script>
```

--------------------------------------------------------------------------
# Python Basics
Printing with variables can be done in two ways:
* print("The {} favorite is {}".format(var1,var2))

Another way is to use f string literals. This is available only in python 3.6 and above. For this you need to provide a letter "f" before the actual string that's being printed:
* print(f"The {var1} favoutite is {var2} ")

## Lists
To append to a list:
* listvariable.append("text")
To insert to a list: 
* listvariable.insert(position,"text")
To delete from a list. position is the number which item you want to delete. If not value is given, it deletes the last item from the list.
* listvariable.pop(position)

--------------------------------------------------------------------------
# Python Advanced

## Scope of a variable
LEGB Rule. Python starts finding a variable in LEGB sequence. These stand for:
L -> Local
E -> Enclosing
G -> Global
B -> Built-in
