#
#
# Passwords should be hashed.
# We can use a hash function to help with this.
# A hash funtion is an algorithm that can take in a document (password) and return back a secure hash digest
# 
# There are two important libraries for hashing:
# - Bcrypt  (pip install flask-bcrypt)
# - Werkzeug    
#
''' Using Bcrypt

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = 'somepassword'

hashed_password = bcrypt.generate_password_hash(password=password)  # Hashing of the password

#print(hashed_password)

check = bcrypt.check_password_hash(hashed_password,'somepassword')  # To chek the hashed password with the password the user has provided.
print(check)
'''
#
#   Using Werkzeug  (already comes installed with flask) if not, then --> pip install Werkzeug
#
'''
from werkzeug.security import generate_password_hash, check_password_hash

hashed_password = generate_password_hash('somepassword')

print(hashed_password)

check = check_password_hash(hashed_password,'wrong')
print(check)
'''
#
#
# Flask login library makes adding user to authentication to our web applications very easy.
# flask-login library has easily callable decorators for adding user functionality. Lets explore it

from flask_login import LoginManager

login_manager = LoginManager()


#
# Flask Dance to use OAuth
#
# OAuth is an open standard authorization protocol or framework that describes how unrelated servers and services can safely allow authenticated access
# to their assets without actually sharing the initial, related, single logon credential.
#

#
# 
# https://flask-dance.readthedocs.io/en/latest/