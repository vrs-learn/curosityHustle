#
# FLASH TEMPLATES
#

# Flask automatically looks for HTML Templates in the templates directory
# We can render templates simply by importing the render_template function from flask and returning an .html file from our view function.
#

# Once we have imported the render_template from flask, we can use it in the functions.
# render_template by default looks under the template directory for the html files mentioned in the functions to look for.
#

# :::: SENDING VARIABLES TO HTML ::::
# Jinja templating will let us directly insert variables from our python code to the HTML file.
# The syntax for inserting a variable is {{some_variable}}
#
# We can pass in python strings, lists, dictionaires, and more into the templates.
# We set parameters (of our choosing) in the render_template function and then use the {{}} syntax to insert them in the template.
#
# To use it we choose as below, when we call the render_template:

'''
some_variable = "Text"                                      # some_variable is the python variable which we want to pass to the HTML page.
render_template('basic.html',my_variable=some_variable)     # my_variable is the variable which is used in the HTML page. 
'''

# In the HTML page, we use the my_variable as -> {{my_variable}}
# **NOTE : We can have same variable name in python and HTML as well. 
# So below is also valid:

'''
my_variable = "Text"                                     
render_template('basic.html',my_variable=my_variable)  
'''

#
# Similarly we can also send lists, dictionaries etc.
# 
# We also have access to control flow syntax in our templates such as "for loops" and 'if statements'
# These use {% %} syntax
# 
# Example : We are going to create a bulleted list of items in HTML page. For that we have to use as below in the template html page:
#

'''
<ul>                                # HTML tag for unordered list.
    {% for item in mylist %}        # Start of For loop.
    <li> {{item}} </li>             # HTML tag for insert a list item.
    {% endfor %}                    # End of for loop
<ul>
'''

#
# Using If conditional statements in template control flow:
#

'''
{% if 'some_text' in listofitems %}
    <p> Found some_text </p>
{% elif 'some_other_text' in listofitems %}
    <p> Found some_other_text </p>
{% else %}
    <p> Hmm.. some_text is not here </p>
{% endif %}
'''

# Usually pages across a web-application already share a lot of features (eg. navigation bar, footer etc.)
# 
# :::: TEMPLATE INHERITANCE ::::
#
# We setup a base.html template file with teh re-usable aspects of our site.
# Then we use {% extend "base.html" "%} and {% block %} statements to extend these re-usable aspects to other pages.

# The base.html page has something like this..
'''
{% block content %}

{% endblock %}
'''


# The home.html page has something like this, which basically just extends the base.html contents to this page.
'''
{% extends "base.html" %}       # This line does the template inheritance.
{% block content%}


{%endblock %}
'''

# Filters.
# Filtes are a great way to quickly change/edit a variable passed to a template.
# Usage:
# {{ variable | filter }}

# Example:
# {{name}}  - imageine this variable has contents of all lower case "jose"
# jose
# {{ name |capitalize }}    - Using this filter (which is also a Python funtion to a string, it can be used as filter to quickly take action on the name variable.)
# Jose
