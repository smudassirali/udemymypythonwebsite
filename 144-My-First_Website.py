#############################
## Lecture - 144: Your First Website
#############################

## Here we will build a simple website

from flask import Flask   ## importing flask class from Flask Library

app=Flask(__name__)   ## Initiating Flask class/object

## Following is the route of page. Here route is home webpage
@app.route('/')
def home():
    return "Website Content Goes Here."

## Following is the route of page. Here route is for about webpage
@app.route('/about/')
def about():
    return "This is about us page."

## In following it will check the filename of script and filename in initializing object.
## If it matches it will run application.
    
if __name__=="__main__":
    app.run(debug=True)