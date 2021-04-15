# Set up your imports here!
from flask import Flask            

app = Flask(__name__)   


@app.route('/') # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    return "<h1> Welcome! Go to /puppy_latin/name to see your name in puppy latin !!</h1>"

@app.route('/puppy_latin/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    last_letter = name[-1]
    if last_letter == 'y':
        return f"<h2> Hi {name} ! Your puppylatin name is " + name[:-1] + "iful </h2>"
    else:
        return f"<h2> Hi {name} ! Your puppylatin name is " + name + "y </h2>"

if __name__ == '__main__':
    # Fill me in!
    app.run(debug=True)
