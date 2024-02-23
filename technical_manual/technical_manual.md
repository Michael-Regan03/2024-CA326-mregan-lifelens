# Life Lens technical Manual
by Michael Regan 22112111

# 1. Introduction
## 1.1. OverView
Lifelens is a web application that visualises its user's life-log data and based on that data alongside other user data, the system predicts the user's current risk of 10 chronic illnesses.


# 2. System Architecture
## 2.1 Overview of system Components
Life Lens achieves its functionality from its 3 major components. The first is the Django-Backend REST API, where all user data is stored and permission to such data is authenticated, which is a priority due to the sensitive nature of life-log data. The second major component of the life-lens system is the React.js frontend which is the User Interface In which users will interact. The frontend is also responsible for the dynamic life-log data visualisations. The Final component is the Flask Backend, a REST API that queries a chronic illness risk assessment Random Forest Classification model trained using The CDC's Behavioural Risk Factor Servalence Survey Data.

## 2.2 Architectural Diagram

## 2.3 Distrabution of Functions
### 2.3.1 Dango Backend
- **Role**: Serves as the backbone of the server-side application, and handles data processing, formatting and storage. Handles API requests and authentication.
- **Responsibilities**:
- **Data Processing**: Processes CSV files containing lifelog data,
-**Data Storage** Stores data in an SQLite database. This data includes user data, life-log data and illness data.
- **RESTFUL API**: Offers RESTFUL API for the frontend to interact with, facilitating data exchanges using HTTP GET and POST requests.
- **Authentication**: Handles Authentication using Json Web Tokens(JWT) supplied by the Djoser library. Security must be a priority of the system given the sensitive nature of Life Log Data.

### 2.3.1 React Frontend
- **Role**: Provides the User Interface. Maintains user authentication on the client side. Serves dynamic visualisations of lifelog data and displays users with a risk assessment of 10 chronic illnesses.
- **Responsibilities**:
- **User Interface**: User Interface is the gateway in which the user can access the functionality of the Life Lens system.
- **Maintaining Authorization on Client Side**: To improve user experience, the React app implements `useContext` for managing the global state and stores access and refresh tokens locally. This ensures that user sessions can be maintained seamlessly using a static API, allowing for efficient authentication checks without the need to constantly re-authenticate the user.
- **Dynamic Data Visualisations**: Frontend handles lifelog data processing for dynamic visualisation of lifelog data across different periods.
-**Chronic Illness Risk Assessment View**: Displays the user's current risk for 10 different chronic illnesses.

### 2.3.1 Flask Backend
- **Role**: Hosts the random forest classification model that classifies chronic illness.
- **Responsibilities**:
- **API**: Handles requests to query the machine learning model.
- **Host Model**: Hosts model to be queried by frontend


## 2.4 Third-Party Components

### 2.4.1 sklearn

### 2.4.2 Djoser

### 2.4.3 Chart.js

### 2.4.4 Moment

## 2.5 Devations from SRS




# 3 High Level Design

## 3.1 Design Overview

## 3.2 Component Interaction Diagram

## 3.3 Data Flow Diagram

## 3.4 Database Design
### 3.4.1 Storing Life Log Data
This is how Lifelog Data is represented in a CSV file where every entry represents a minute in time recorded with a unix timestamp.

|ts|action|actionOption|actionSub|actionSubOption| condition|conditionSub1Option|conditionSub2Option|place| emotionPositive | emotionTension | activity |
|-|-|-|-|-|-|-|-|-|-|-|-|
|1598713200.0|sleep|111|||WITH_ONE|2|1|other_indoor|4|2|3|
|1598713260.0|sleep|111|||WITH_ONE|2|1|other_indoor|4|2|3|
|1598713320.0|sleep|111|||WITH_ONE|2|1|other_indoor|4|2|3|
|1598713380.0|sleep|111|||WITH_ONE|2|1|other_indoor|4|2|3|

This is what each column means

|ts|action|actionOption|actionSub|actionSubOption| condition|conditionSub1Option|conditionSub2Option|place| emotionPositive | emotionTension | activity |
|-|-|-|-|-|-|-|-|-|-|-|-|
|Unix time stamp|activity class|activity|metric to distinguse actionSubOption|Travel method or Meal Amount|People in users presence|social interaction|conversation engagment|place| emotionPositive (1=negative, 7=Positive) | emotionTension (1=relaxed, 7=aroused) |activity status|

The Life Lens System stores data from such a file by creating an instances of a day entity with the date of the first timestamp. That day is associated with the user who uploaded the file. The database then stores actions as one instance with a start time, end time and duration. That action is stored in a table called DailyActivity. Each daily activity is assocated with sub actions which aslo have a start time, end time and duration. Sub actions include actionSubOption, condition, conditionSub1Option, conditionSub1Option, place emotionPositive, emotionTension and activity. Each of these actions represent

### 3.4.2 Entity Relationship Diagram
![](./images/ERDiagram.jpeg)


## 3.5 API design
### 3.5.1 Daily Activity CSV Upload

![](../code/plantUML/Backend/images/DailyActivityCSVUpload.png)

### 3.5.2 Daily Activity View

![](../code/plantUML/Backend/images/DailyActivityView.png)

### 3.5.3 Day View

![](../code/plantUML/Backend/images/DayView.png)

### 3.5.4 Day View For Survey

![](../code/plantUML/Backend/images/DayViewForSurvey.png)

### 3.5.5 Survey AM Upload

![](../code/plantUML/Backend/images/SurveyAMUpload.png)

### 3.5.5 Survey PM Upload

![](../code/plantUML/Backend/images/SurveyPMUpload.png)

### 3.5.6 Chronic Illness Parameters View

![](../code/plantUML/Backend/images/ChronicIllnessParametersView.png)

### 3.5.7 Chronic Illness Parameters View

![](../code/plantUML/Backend/images/ChronicIllnessFormatedView.png)

### 3.5.8 Illness Description View

![](../code/plantUML/Backend/images/IllnessDesciptionView.png)

## 3.6 Frontend Design

### 3.6.1 Authorisation system
#### 3.6.1.1 Authorisation Context

![](../code/plantUML/React/images/AuthContext.png)

#### 3.6.1.2 Log In

![](../code/plantUML/React/images/LogIn.png)

#### 3.6.1.23 Log out

![](../code/plantUML/React/images/LogOut.png)

#### 3.6.1.4 Sign up

![](../code/plantUML/React/images/SignUp.png)

#### 3.6.1.5 Navbar Contol

![](../code/plantUML/React/images/Header.png)


### 3.6.2 Fetch Components
#### 3.6.2.2 Fetch Component with Authorisation

![](../code/plantUML/React/images/AuthFetchComp.png)

#### 3.6.2.3 Load Data with Automatic Authorisation

![](../code/plantUML/React/images/LoadData.png)

### Visualisation Menu

#### 3.6.3.1 Create Data Structure Containing Dates in which the User has Uploaded Data
![](../code/plantUML/React/images/getYearsMonthsDays.png)

#### 3.6.3.2 Load Menu for Visualisations
![](../code/plantUML/React/images/DaysDropDownMenu.png)

#### 3.6.3.3 Date Select for visualistations

![](../code/plantUML/React/images/MenuSelect.png)


### 3.6.4 Accumulate Activity Durations
![](../code/plantUML/React/images/AdditemOrUpdateDuration.png)


### 3.6.5 Time Series Data Visualisation
#### 3.6.5.1 Determine Time Span
![](../code/plantUML/React/images/DetermineTimeSpan.png)

#### 3.6.5.2 Graph Data over a day
![](../code/plantUML/React/images/TimeSeriesGraphDay.png)

#### 3.6.5.3 Graph Averages over time
![](../code/plantUML/React/images/TimeSeriesGraphAverage.png)

### 3.6.6 Surveys

#### 3.6.6.1 Survey Form
![](../code/plantUML/React/images/SurveyForm.png)

#### 3.6.6.2 Render Option Tags From Dictionary
![](../code/plantUML/React/images/RenderSelectOptions.png)

### 3.6.7 Chronic Illness Risk Assessment

#### 3.6.7.1 View Risk Assessment
![](../code/plantUML/React/images/ChronicIllnessRiskAssessment.png)

#### 3.6.7.1 View Risk
![](../code/plantUML/React/images/RiskView.png)




# 4 Machine Learning 
# 4.1 Machine Leaning Overview

![](../code/Risk_Assessment/images/correlation_heatmap.png)


![](../code/plantUML/Risk-Assessment/images/preprocessing.png)


# 4.2 Data Decoding and Cleaning
![](../code/Risk_Assessment/images/bar_chart.png)



# 4.3 Data Balancing

[](../code/Risk_Assessment/images/Multi_Ilness_Distrabution.png)


![](../code/plantUML/Risk-Assessment/images/DataBalancing.png)

![](../code/plantUML/Risk-Assessment/images/AddingNoneIllness.png)



[](../code/Risk_Assessment/images/IllnessDistrabution.png)

[](../code/Risk_Assessment/images/BalancedIllnessDistrabution.png)




# 4.4 Data Normalisation
![](../code/plantUML/Risk-Assessment/images/normalisation.png)

# 4.5 Model Training 

# 4.6 Model Selection

# 5 Problems and Resolutions

## 5.1 Identfied Issues

## 5.2 Resolution Strategies

## 5.3 Lessons Learned

## 5.4 Future Consideration

