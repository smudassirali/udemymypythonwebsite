#############################
## Lecture - 145: HTML Templates
#############################

## here we will define an HTL template as our webpage in routes for website.
##  here we will use render method of flask library to access HTLM file and display it.

## following importing flask class from Flask Library
from flask import Flask, render_template

app=Flask(__name__)   ## Initiating Flask class/object

## Following is the route of homepage. Here route is home webpage
@app.route('/')
def home():
    return render_template("home.html")

## Following is the route of page. Here route is for about webpage
@app.route('/about/')
def about():
    return render_template("about.html")

## In following it will check the filename of script and filename in initializing object.
## If it matches it will run application.
    
if __name__=="__main__":
    app.run(debug=True)



