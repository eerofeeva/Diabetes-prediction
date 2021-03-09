from flask import Flask, render_template, request, send_file
from flask_bootstrap import Bootstrap
import random

class User:
    def __init__(self, name, weight, height, glucose, active, skin, generate):
        if generate == False:
            self.name = name
            self.weight = weight
            self.height = height
            self.BMI = self.calculateBMI
            self.glucose = self.randomInRange(0, 199)
            self.active = self.randomInRange(0,122)
            self.skin = self.randomInRange(0, 99)
        else:
            self.generate()


    def calculateBMI(self):
        return 703*self.height/self.weight**2   

    def isLikely(self):
        pass

    def generate(self):
        self.name = "sample user"
        self.weight = self.randomInRange(120, 300)
        self.height = self.randomInRange(60, 96)
        self.BMI = self.calculateBMI
        self.glucose = self.randomInRange(70, 250)
        self.active = self.randomInRange(30,120)
        self.skin = self.randomInRange(20, 70)
    
    def randomInRange(self, x,y):
        return round(random.uniform(x,y), 3)    


app=Flask(__name__)
Bootstrap(app)
objects = {}

@app.route("/")
def index():
    print("Running index function")
    return render_template("index.html")

@app.route("/about")
def about():
    return send_file("../Resources/about_section.txt")

@app.route("/userUpload", methods=['GET','POST'])
def userUpload():
    user = User(request.form.get('userName',''),
    request.form.get('weight',''),
    request.form.get('height',''),
    request.form.get('sugar',''),
    request.form.get('active',''),
    request.form.get('skinThickness',''), False)
    print("userUpload: " + user.name)
    return user.name +' Weight: ' + str(user.weight) + ' Height: ' + str(user.height) \
    + ' Glucose: ' + str(user.glucose) + ' Is Active: '+ str(user.active)  \
    + ' Skin Thickness: ' + str(user.skin)

@app.route("/userGenerate", methods=['GET','POST'])
def userGenerate():
    user = User(request.form.get('userName',''),
    request.form.get('weight',''),
    request.form.get('height',''),
    request.form.get('sugar',''),
    request.form.get('active',''),
    request.form.get('skinThickness',''), True)
    print("userUpload: " + user.name)
    return user.name +' Weight: ' + str(user.weight) + ' Height: ' + str(user.height) \
    + ' Glucose: ' + str(user.glucose) + ' Is Active: '+ str(user.active)  \
    + ' Skin Thickness: ' + str(user.skin)

if __name__ == "__main__":
    app.run(debug=True)

