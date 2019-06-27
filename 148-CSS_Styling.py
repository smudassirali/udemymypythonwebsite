## here we will define an HTML template as our webpage in routes for website.
##  here we will use render method of flask library to access HTLM file and display it.
## Here we will use navigation menu.

## following importing flask class from Flask Library
from flask import Flask, render_template

app=Flask(__name__)   ## Initiating Flask class/object

## Following is the route of homepage. Here route is home webpage
@app.route('/')
def home():
    ## Now our webpage templates will be child templates so we will remove all normal tags and add link of this webpage to it.
    return render_template("myhome.html")

## Following is the route of page. Here route is for about webpage
@app.route('/about/')
def about():
    ## Now our webpage templates will be child templates so we will remove all normal tags and add link of this webpage to it.
    return render_template("myabout.html")

## In following it will check the filename of script and filename in initializing object.
## If it matches it will run application.
    
if __name__=="__main__":
    app.run(debug=True)



