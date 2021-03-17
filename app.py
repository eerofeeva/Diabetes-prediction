from flask import Flask, render_template, request, send_file
from flask_bootstrap import Bootstrap
import random
from model import diabetesPrediction

class User:
    def __init__(self, name, age, weight, height, glucose, active, skin, generate):
        if generate == False:
            self.name = name
            self.weight = float(weight)
            self.height = float(height)
            self.age = int(age)
            self.BMI = self.calculateBMI()

            #calculate Blood Pressure
            self.bloodPressure = self.randomInRange(62, 122)
            
            #if user LOVES sugar
            if glucose:
                self.glucose = self.randomInRange(118, 199)
                self.insulin = self.randomInRange(0, 30.5)
            else:
                self.glucose = self.randomInRange(62,117)
                self.insulin = self.randomInRange(31, 846)

            #if user Loves sports
            if active:    
                self.active = self.randomInRange(73,122)
            else:
                self.active = self.randomInRange(30,72)
            
            #if user is thick skinned
            if skin:
                self.skin = self.randomInRange(0, 23)
            else:
                self.skin = self.randomInRange(24, 99)
            
            self.diabetesPedigree = self.diabetesPedigreeCalculate()
            self.prediction = self.predict() 
        else:
            self.generate()

    def diabetesPedigreeCalculate(self):
        return self.randomInRange(0.078, 2.42)

    def calculateBMI(self):
        return 703*(float(self.weight)/(float(self.height)**2)) 

    def generate(self):
        self.name = "sample user"
        self.weight = float(self.randomInRange(120, 300))
        self.height = float(self.randomInRange(60, 96))
        self.age = int(self.randomInRange(12,102))
        self.BMI = self.calculateBMI()
        self.glucose = self.randomInRange(70, 250)
        self.insulin = self.randomInRange(31, 846)
        self.active = self.randomInRange(30,120)
        self.bloodPressure = self.randomInRange(62, 122)
        self.skin = self.randomInRange(20, 70)
        self.diabetesPedigree = self.diabetesPedigreeCalculate()
        self.prediction = self.predict() 

    def predict(self):
        return diabetesPrediction(0, self.glucose, self.bloodPressure, self.skin, 
        self.insulin, self.BMI, self.diabetesPedigree, self.age)

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
    return user.name +' Weight: ' + str(user.weight) + ' Height: ' + str(user.height) \
    + ' Glucose: ' + str(user.glucose) + ' Is Active: '+ str(user.active)  \
    + ' Skin Thickness: ' + str(user.skin) \
    + ' Is Likely To Have Diabetes: ' + ('Yes' if (user.prediction > 0) else 'No')  

@app.route("/userGenerate", methods=['GET','POST'])
def userGenerate():
    user = User('',0,0,0,0,False,False,True)
    rtn_msg = user.name +' Weight: ' + str(user.weight) + ' Height: ' + str(user.height) \
    + ' Glucose: ' + str(user.glucose) + ' Is Active: '+ str(user.active)  \
    + ' Skin Thickness: ' + str(user.skin) \
    + ' Is Likely To Have Diabetes: ' + ('Yes' if (user.prediction > 0) else 'No')
    return {'msg':rtn_msg,
            'name': user.name,
            'weight': user.weight,
            'height': user.height,
            'age': user.age,
            'BMI': user.BMI,
            'glucose': user.glucose,
            'active': user.active,
            'skinthick': user.skin,
            'prediction': float(user.prediction[0])}

if __name__ == "__main__":
    app.run(debug=True)

