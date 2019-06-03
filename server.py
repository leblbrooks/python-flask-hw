

from flask import (
    Flask,
    render_template,
    request
)

import json 
import requests

# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

# Create a URL route in our application for "/multiply"
@app.route('/multiply', methods=['GET', 'POST'])
def multiply():
    """
    This function just responds to the browser ULR
    localhost:5000/multiply 

    :return:        the rendered template 'multiply.html'
    """

    if request.method == "POST":
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        product = num1*num2

        return '''<h1>{} times {} is: {}</h1>'''.format(num1, num2, product)

    return render_template('multiply.html')


 
# Create a URL route in our application for "/statictext"
@app.route('/statictext')
def statictext():
    """
    This function just responds to the browser ULR
    localhost:5000/statictext

    :return:        the rendered template 'statictext.html'
    """
    return render_template('statictext.html')   

# Create a URL route in our application for "/dynamictext"
@app.route('/dynamictext', methods = ['GET', 'POST'])
def dynamictext():
    """
    This function just responds to the browser ULR
    localhost:5000/dynamictext  
    add back button
    """

    if request.method == "POST":
        mood = request.form['mood']
        if mood == 'happy':
            return '''<h1>happy as a clam</h1>'''
        if mood == 'grumpy':
            return '''<h1>take a chill pill</h1>'''
        if mood == 'excited':
            return '''<h1>oo, someone is perky</h1>'''
        if mood == 'content':
            return '''<h1>just keeping it real</h1>'''

        return '''<h1>Your mood is definitely {}</h1>'''.format(mood)


    return render_template('dynamictext.html')  

# Create a URL route in our application for "/jsondictionary"
@app.route('/jsondictionary', methods = ['GET', 'POST'])
def jsondictionary():
    """
    This function just responds to the browser ULR
    localhost:5000/jsondictionary

    :return:        the rendered template 'jsondictionary.html'
    """

    f = open('colors.json', 'r')

    json_obj = json.load(f)

    return '''<h1>Here is a json dictionary: {}</h1>'''.format(json_obj)


    # return render_template('colors.json'), 201, {'Content-Type': 'application/json'}


# Create a URL route in our application for "/jsondictionary"
@app.route('/jsondictionarypretty', methods = ['GET', 'POST'])
def jsondictionarypretty():
    """
    This function just responds to the browser ULR
    localhost:5000/jsondictionary

    :return:        the rendered template 'jsondictionary.html'
    """


    return render_template('colors.json'), 201, {'Content-Type': 'application/json'}


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)