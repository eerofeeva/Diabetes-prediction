from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap


# class User:
#     def __init__(name, weight, height, age ):
#         self.name = name
#         self.weight = weight
#         self.height = height
#         self.name = name

#     def calculateBMI():
#         print("test bmi")    

#     def isLikely():
#         pass

#     def generate():
#         pass


app=Flask(__name__)
Bootstrap(app)
objects = {}

@app.route("/")
def index():
    print("Running index function")
    return render_template("index.html")

@app.route("/userUpload", methods=['GET','POST'])
def userUpload():
    theName = request.form.get('userName','')
    print("userUpload: "+theName)
    return theName


if __name__ == "__main__":
    app.run(debug=True)

