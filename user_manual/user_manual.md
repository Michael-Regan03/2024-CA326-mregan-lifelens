# Life Lens User Manual
Michael Regan 22112111




## Introduction


When you first access the Life Lens web app you will encounter the homepage which includes a short description of Life Lens. It's worth reading this if it is your first time on the site.


![](./images/HomePage.png)


You'll notice a blue bar at the top of the page, this is the navbar and can be used to navigate the web page. It is used by clicking on the buttons. They will become visible when you hover over the text. The mouse pointer will change to a hand, indicating that the object is clickable.


## Create an Account


You can create an account by clicking on 'Create an account'


![](./images/HoverOverCreteAnAccount.png)


After clicking on 'Create an account" you will be presented with the sign-up form. Here you need to enter your email, name, age, gender, password and re-password to create an account.


![](./images/CreateAnAccount.png)


Fill it in as such:


![](./images/SignUpFilledIn.png)


If you fail to enter your credentials correctly or perhaps your email is already associated with an account you will receive an error message. This is ok, just try again.


![](./images/SignUpFail.png)


## Log In


After Successfully Creating an account you will be redirected to the login page where you must enter your credentials again to access your account.


![](./images/LogIn.png)




![](./images/LogInFilled.png)


If you fail to enter your credentials correctly you will receive an error message.


![](./images/LogInFailed.png)


Once you log In you'll be redirected to the Homepage. This time however your name is displayed in the header and the navar has more options.


![](./images/LoggedInHomepage.png)


## LogOut


If you wish to return to a logged-out state you can press logged out on the navbar.


![](./images/LogOut.png)


## Upload Life Log Data


Before you upload life log data you will notice in visualisations that you are unable to select a date. That is because there are no uploaded days.


![](./images/NoDaysMenu.png)


Each file you upload is associated with one day's worth of data. To access all of the visualisations its advised you upload multiple CSV files.


Click on 'Upload LifeLog Data' in the navbar and you will find the form where you can upload your lifelog data,


![](./images/UploadCSV.png)


Click on 'Upload CSV Containing the lifelog data spanning across a day'


Your data should be formatted as such


|ts|action|actionOption|actionSub|actionSubOption| condition|conditionSub1Option|conditionSub2Option|place| emotionPositive | emotionTension | activity |
|-|-|-|-|-|-|-|-|-|-|-|-|
|1598713200.0|sleep|111|||WITH_ONE|2|1|other_indoor|4|2|3|
|1598713260.0|sleep|111|||WITH_ONE|2|1|other_indoor|4|2|3|
|1598713320.0|sleep|111|||WITH_ONE|2|1|other_indoor|4|2|3|
|1598713380.0|sleep|111|||WITH_ONE|2|1|other_indoor|4|2|3|




![](./images/HoverOverCSV.png)


Select a file containing your life log data


![](./images/SelectFile.png)


Click 'Upload CSV'


![](./images/HoverOverUploadCSV.png)


If your CSV is successfully uploaded you will see this response.


![](./images/SuccessfulCSVUpload.png)


Else an error message will be displayed


![](./images/FailedCSVSend.png)




## Visualise Life Log Data


Now that you've uploaded life log data you will see you can now select a year. This is because Life Lens can derive the date of your CSV files uploaded.


![](./images/YearAppear.png)


Select a year and see the data visualised.


![](./images/2020Data.png)


You will see time series visualisations of emotionPositive and emotionTension graphed across months as you selected a year. Life Lens displays the average associated with that month.


![](./images/2020-Time-Series-Data.png)


If you scroll down the page you will also see visualisations of 'Time Spent Travelling' and 'Time Spent with Others'.


![](./images/Traveling_Others.png)


If you scroll down further you will a visualisation of 'Social Interaction Distribution'.


![](./images/SocialInteractionDistribution.png)


If you keep scrolling you will see a visualisation of 'Conversation Distribution'


![](./images/ConversationDistrabution.png)


Finally, at the bottom of the page, you will see visualisations of Places and activity Statuses


![](./images/Places_Activity_Statuses.png)


Back at the top of the page, you will now see the option to Select a Month.


![](./images/MonthSelect.png)


After selecting a month Life Lens will then visualise YYYY-MM data


![](./images/MonthSelected.png)


While Months is selected time series visualisations will now average values across days


![](./images/MonthDataVisualisation.png)


Finally, you can select to visualise data associated with a specific date


![](./images/DaySelection.png)


Time series visualisations, when a specific date is selected, will graph specific time stamps across that day


![](./images/DayVisualisation.png)


## Survey


To fill out a survey you need to click on 'Fill Out Survey' on Navabr


![](./images/SelectForm.png)


You will be given the option to fill out the pm survey and the am survey. The AM survey is supposed to be filled in at the start of the day and the PM survey is supposed to be filled in at the end of the day.


At the top of both surveys, there will be an option to select a date. These dates are dates that are associated with lifelog data. Once an am or pm survey is submitted you cannot select that data again for that survey.




Here is the survey AM form and it includes questions about your sleep from the previous night.


![](./images/SurveyAm.png)


Here is the survey PM form and it includes questions about tour day such as stress, fatigue and alcohol consumption


![](./images/SurveyPM.png)


Once these forms are submitted you will be redirected to the home page


## Chronic Illness Risk Assessment


If you want to view your chronic illness risk assessment click on 'Chronic Illness Risk Assessment' in the navbar.


At the top of the page, you will see the data that was given to the machine learning model. This data includes age, average sleep, average alcohol consumption approximation, average time spent being active, and smoking status.


Your age is derived when you create your account, Your alcohol consumption comes from the PM survey, and the rest is derived from your life log data


![](./images/Risk1.png)


Your risk of chronic illnesses will appear green for 'low risk', orange for 'mid risk' and red for 'high risk'. Each Illness comes attached with a short description from the CDC as well as a link to their website for more resources


![](./images/Risk2.png)
