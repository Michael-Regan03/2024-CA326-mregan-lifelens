# Life Lens technical Manual
by Michael Regan 22112111

# 1. Introduction
## 1.1. OverView
Lifelens is a web application that visualises its user's life-log data and based on that data alongside other user data, the system predicts the user's current risk of 10 chronic illnesses. It achieves this from its 3 major components. The first is the Django-Backend REST API, where all user data is stored and permission to such data is authenticated, which is a priority due to the sensitive nature of life-log data. The second major component of the life-lens system is the React.js frontend which is the User Interface In which users will interact. The frontend is also responsible for the dynamic life-log data visualisations. The Final component is the Flask Backend, a REST API that queries a chronic illness risk assessment Random Forest Classification model trained using The CDC's Behavioural Risk Factor Servalence Survey Data.


# 2 System Architecture

## 2.1 Overview of system Components

## 2.2 Architectural Diagram

## 2.3 Distrabution of Functions

## 2.4 Reused and Third-Party Components

## 2.5 Security and Scalability Consterations

# 3 High Level Design

## 3.1 Design Overview

## 3.2 Component Interaction Diagram

## 3.3 Data Flow Diagram

## 3.4 Enity Relationship Diagram
![](./images/ERDiagram.jpeg)

## 3.5 Activity Diagrams for Django API requests

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

## 3.6 Sequence Diagrams for React Compnents

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

### Chronic Illness Risk Assessment

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

