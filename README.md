<h1>Diabetes & You</h1>

<h3>About the Data:</h3>

The Akimel O’odham (“River People”, known formerly as the Pima) are a group of first nations people that since the 1960’s the have donated their time and information to various scientists that have greatly increased global understanding of the factors relate to type 2 diabetes. The reason for the intense interest is that they have the highest known prevalence of type 2 diabetes among any identified community on the planet and relatively homogenous.
The data we have for these 768 individuals is just a small snapshot of what has been collected over the years, but it has been used for numerous studies and data science projects.

<h3>About the Application:</h3>

<h5>Application on Heroku: https://diabetesprediction2021.herokuapp.com/</h5>

![image](https://user-images.githubusercontent.com/70925750/111548683-0f0ffb00-8749-11eb-898b-cd99ed9a9433.png) 

For this project we created an application that allows a user to compare their data to that of the dataset after we filtered out users who had null values in fields where that would not be possible. Since not everyone knows their glucose and insulin levels off hand the system generates random numbers within a certain range based off some lighthearted questions. This is meant to be an interesting but fun tool for comparison.

![image](https://user-images.githubusercontent.com/70925750/111548530-d8d27b80-8748-11eb-82d9-91a781dac2ea.png)

The generated user data also includes the results of running the user data through a machine learning model (with a roughly 75% accuracy) to predict the likelihood of diabetes. Not shockingly, since this dataset is a group of people for having the highest incident of type 2 diabetes in the world, the results may come back as a “Yes” even though the user may not be at risk for diabetes. In addition to the model results, the application also generates a plotly chart of the cleaned data for a comparison of age and BMI of the study participants with the user inputs included for comparison.

![image](https://user-images.githubusercontent.com/70925750/111548857-58f8e100-8749-11eb-8e96-8374a97f7dfd.png)

Under the “Graphs” tab of the site, there are two correlation matrices and two tableau graph stories comparing the participant data to illustrate various trends. Under the “Jupyter Notebook” tab a user would be able to examine the machine learning model and learn about how the diabetes prediction was made. Under the “About” section you can learn more about the data itself.

![image](https://user-images.githubusercontent.com/70925750/111549671-990c9380-874a-11eb-8033-cec324b894e3.png)
![image](https://user-images.githubusercontent.com/70925750/111548951-762daf80-8749-11eb-905c-ababf6f8f46f.png)

The application runs on Heroku and uses a combination of python and javascript to bring together the various elements of the site for an interactive experience.
Thank you for checking out this project!

![image](https://user-images.githubusercontent.com/70925750/111549145-b55c0080-8749-11eb-9537-36afb83ae923.png)

<h3>Team & Roles:</h3>
<p>Elena Erofeeva: Created site infastructure and input form, made sure input data flowed to the model and user graph, and linked the various parts of the site together.</p>
<p>Kelly Olien: Created the machine learning predictive model displayed in jupyter notebook.</p>
<p>Kylie Malcolm: Wrote the about section, created matplotlib correlative matrices, and the four tableau graphs comparing multiple attribures in the dataset.</p>
<p>Kory Harris: Created tableau scatter charts.</p>
