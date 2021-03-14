from flask import Flask, render_template, request, send_file
from flask_bootstrap import Bootstrap
import random

class User:
    def __init__(self, name, age, weight, height, glucose, active, skin, generate):
        if generate == False:
            self.name = name
            self.weight = weight
            self.height = height
            self.age = age
            self.BMI = self.calculateBMI
            
            #if user LOVES sugar
            if glucose:
                self.glucose = self.randomInRange(118, 199)
                self.insulin = self.randomInRange(0, 30.5)
            else:
                self.glucose = self.randomInRange(62,117)
                self.insulin = self.randomInRange(31, 846)

            #if user Loves sports
            if active:    
                self.active = self.randomInRange(30,72)
            else:
                self.active = self.randomInRange(73,122)
            
            #if user is thick skinned
            if skin:
                self.skin = self.randomInRange(0, 23)
            else:
                self.skin = self.randomInRange(24, 99)
            self.diabetesPedigreeCalculate()
        else:
            self.generate()

    def diabetesPedigreeCalculate(self):
        self.randomInRange(0.078, 2.42)

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
        self.insulin = self.randomInRange(31, 846)
        self.active = self.randomInRange(30,120)
        self.skin = self.randomInRange(20, 70)
        self.diabetesPedigreeCalculate()


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
    return send_file("Resources/about_section.txt")

@app.route("/userUpload", methods=['GET','POST'])
def userUpload():
    user = User(request.form.get('userName',''),
    request.form.get('age',''),
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
    user = User('',0,0,0,False,False,False, True)
    print("userUpload: " + user.name)
    return user.name +' Weight: ' + str(user.weight) + ' Height: ' + str(user.height) \
    + ' Glucose: ' + str(user.glucose) + ' Is Active: '+ str(user.active)  \
    + ' Skin Thickness: ' + str(user.skin)

if __name__ == "__main__":
    app.run(debug=True)

