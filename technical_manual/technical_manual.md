# Life Lens technical Manual
by Michael Regan 22112111

# 1. Introduction
## 1.1. OverView
Life Lens is a web application that helps its user's extract meaningful insight from their lifelog data through visualisations. It also uses that lifelog data alongside user information to run a chronic illness risk assessments of 10 diffrent chronic illnesses ranking the user either 'low-risk', 'mid-risk' or 'high-risk' of each illness. In this way Life Lens can be used to help its users prevent chronic illness and maintain good health.


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
- **RESTful API**: Offers RESTul API for the frontend to interact with, facilitating data exchanges using HTTP GET and POST requests.
- **Authentication**: Handles Authentication using Json Web Tokens(JWT) and Djoser RESTful APIs. Security must be a priority of the system given the sensitive nature of Life Log Data.

### 2.3.1 React Frontend
- **Role**: Provides the User Interface. Maintains user authentication on the client side. Serves dynamic visualisations of lifelog data and displays users with a risk assessment of 10 chronic illnesses.
- **Responsibilities**:
- **User Interface**: User Interface is the gateway in which the user can access the functionality of the Life Lens system.
- **Maintaining Authorization on Client Side**: To improve user experience, the React app implements `useContext` for managing the global state and stores access and refresh tokens locally. This ensures that user sessions can be maintained seamlessly using a static API, allowing for efficient authentication checks without the need to constantly re-authenticate the user.
- **Dynamic Data Visualisations**: Frontend handles lifelog data processing for dynamic visualisation of lifelog data across different periods.
- **Chronic Illness Risk Assessment View**: Displays the user's current risk for 10 different chronic illnesses.

### 2.3.1 Flask Backend
- **Role**: Hosts the random forest classification model that classifies chronic illness.
- **Responsibilities**:
- **API**: Handles requests to query the machine learning model.
- **Host Model**: Hosts model to be queried by frontend


## 2.4 Third-Party Components  
### 2.4.1 Scikit-learn
- **Role**: Scikit learn assists in ml model training and validation.
- **Responsibilities**:
- **Train Test Split**: Handles splitting of dataset for training and validation.
- **Machine learning Algorithms**: Provides *Logistic Regression*and *Random Forest Classification* algorithms for creating ml models.
- **Model Evaluation**: Provides evaluation the scores *accuracy score*, *precisison score*, *recall score* and *f1-score*.

### 2.4.2 Djoser
- **Role**: Provides a set of RESTful APIs for user Authentication, and registration and also offers flexibility with custom user models.
- **Responsibilities**:
- **Authentication**: Provides a set of Restful APIs for Authentication which is a priority when dealing with sensitive life log data.
- **Registration**: Provides a set of RESTful APIs for registration.
- **Custom User Models**: Djoser provides flexibility with its RESTful API with its incorporation with custom user accounts.

### 2.4.3 React Chartjs 2
- **Role**: React chartjs 2 is a react wrapper for the javascript library Chart.js. React chartjs 2 was used for dynamic visualisations of life log data.
- **Responsibilities**:
- **Data Visualisation**: Visualisations are implemented using React chartjs 2's `pie` , `bar` and `line`.
- **Responsive Design**: Reacht chartjs 2 handles responsive design that will adapt to screen size.
- **Integration with React**: Facilites the integration of Chart.js charts in a React application.

### 2.4.4 Moment
- **Role**: Time Zone Conversion and Date Time Formatting on the frontend inside the component `KoreanTimeConverter`
- **Responsibilities**:
- **Time Zone Conversion**: Handles converting timestamps to Asia/Seoul time as an example dataset is from Korea.
- **Date Time Formatting**: Provides flexible date time formats which are used to visualise data on different timespans.


## 2.5 Deviations from SRS
### 2.5.1 Activity Suggestions
- **Description**: The feature in which the Life Lens system suggests future activities to the user was excluded from the final Life Lens application.
- **Reasoning**: This feature was removed due to time constraints and also it offered no further technical difficulty given it would simply be prompting for activity suggestions from frontend to backend.


### 2.5.2 Text Generation API
- **Description**: The feature in which the Life Lens system prompts a text generation API was excluded from the final Life Lens application.
- **Reasoning**: This feature was removed due to time constraints and also it didn't seem to seamlessly fit in with Life Len's other functionality


# 3 High Level Design
## 3.1 Design Overview

## 3.2 Component Interaction Diagram

## 3.3 Database Design
### 3.3.1 Storing Life Log Data
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

### 3.3.2 Entity Relationship Diagram
![](./images/ERDiagram.jpeg)


## 3.4 API design
### 3.4.1 Daily Activity CSV Upload

![](../code/plantUML/Backend/images/DailyActivityCSVUpload.png)

### 3.5.2 Daily Activity View

![](../code/plantUML/Backend/images/DailyActivityView.png)

### 3.4.3 Day View

![](../code/plantUML/Backend/images/DayView.png)

### 3.4.4 Day View For Survey

![](../code/plantUML/Backend/images/DayViewForSurvey.png)

### 3.4.5 Survey AM Upload

![](../code/plantUML/Backend/images/SurveyAMUpload.png)

### 3.4.5 Survey PM Upload

![](../code/plantUML/Backend/images/SurveyPMUpload.png)

### 3.4.6 Chronic Illness Parameters View

![](../code/plantUML/Backend/images/ChronicIllnessParametersView.png)

### 3.4.7 Chronic Illness Parameters View

![](../code/plantUML/Backend/images/ChronicIllnessFormatedView.png)

### 3.4.8 Illness Description View

![](../code/plantUML/Backend/images/IllnessDesciptionView.png)

## 3.5 Frontend Design
### 3.5.1 Authorisation system
#### 3.5.1.1 Authorisation Context

![](../code/plantUML/React/images/AuthContext.png)

#### 3.5.1.2 Log In

![](../code/plantUML/React/images/LogIn.png)

#### 3.5.1.3 Log out

![](../code/plantUML/React/images/LogOut.png)

#### 3.5.1.4 Sign up

![](../code/plantUML/React/images/SignUp.png)

#### 3.5.1.5 Navbar Contol

![](../code/plantUML/React/images/Header.png)


### 3.5.2 Fetch Components
#### 3.5.2.2 Fetch Component with Authorisation

![](../code/plantUML/React/images/AuthFetchComp.png)

#### 3.5.2.3 Load Data with Automatic Authorisation

![](../code/plantUML/React/images/LoadData.png)

### Visualisation Menu
#### 3.5.3.1 Create Data Structure Containing Dates in which the User has Uploaded Data

![](../code/plantUML/React/images/getYearsMonthsDays.png)

#### 3.5.3.2 Load Menu for Visualisations
![](../code/plantUML/React/images/DaysDropDownMenu.png)

#### 3.5.3.3 Date Select for visualistations

![](../code/plantUML/React/images/MenuSelect.png)


### 3.5.4 Accumulate Activity Durations
![](../code/plantUML/React/images/AdditemOrUpdateDuration.png)


### 3.5.5 Time Series Data Visualisation
#### 3.5.5.1 Determine Time Span
![](../code/plantUML/React/images/DetermineTimeSpan.png)

#### 3.5.5.2 Graph Data over a day
![](../code/plantUML/React/images/TimeSeriesGraphDay.png)

#### 3.5.5.3 Graph Averages over time
![](../code/plantUML/React/images/TimeSeriesGraphAverage.png)

### 3.5.6 Surveys

#### 3.5.6.1 Survey Form
![](../code/plantUML/React/images/SurveyForm.png)

#### 3.5.6.2 Render Option Tags From Dictionary
![](../code/plantUML/React/images/RenderSelectOptions.png)

### 3.5.7 Chronic Illness Risk Assessment

#### 3.5.7.1 View Risk Assessment
![](../code/plantUML/React/images/ChronicIllnessRiskAssessment.png)

#### 3.5.7.1 View Risk
![](../code/plantUML/React/images/RiskView.png)


## 3.6 Machine Learning Design
### 3.6.1 Machine Leaning Overview
The data that Life-lens is using for its risk assessment algorithm is from the CDC’s Behavioural Risk Factor Analysis Surveillance System. The data is of American adults and includes relevant data to me such as age, sleep, alcohol, tobacco consumption and activity. Life-lens uses this data to train a model that can take behaviour and user data and perform a risk assessment on a series of chronic illnesses.

![](../code/Risk_Assessment/images/correlation_heatmap.png)

Overview of the preprocessing steps to prepare the data to train the model

![](../code/plantUML/Risk-Assessment/images/preprocessing.png)


### 3.6.2 Data Pre-Processing
#### 3.6.2.1 Data Decoding and Cleaning
Pandas was used to concatenated BRSS data from 5 years(2010, 2012, 2013, 2014, 2015). This resulted total of *43211* rows,


Relevant columns where decoded by mapping the values of each column to a dictionary that contained a string representation of the value.

An Overview oof the distrabution of both chronic ilnesses and behaviours

![](../code/Risk_Assessment/images/bar_chart.png)



#### 3.6.2.2  Data Balancing
Data balancing began by adding two new columns to the data frame, one was the number of illnesses the user is suffering from, and the other column was a list representation of the user's chronic illnesses. 

Visualisation of multi-illness distribution.


![](../code/Risk_Assessment/images/Multi_Ilness_Distrabution.png)

Visualisation of Illness Distribution


![](../code/Risk_Assessment/images/IllnessDistrabution.png)


The mean being much larger than the median signifies a rightward skew, which means there are a few outliers that have an overwhelming majority. This intuitively makes sense that some diseases will be more prevalent than others.  To handle multi-illness patients when balancing the data set was devided by the number of illnesses in each row. The mean number of people inflicted by each combination of Illnesses in each division was found up to combinations of 5 illnesses. Each combination of illnesses was then under and over-sampled to the mean in their division. For reproducible, I used a seed in sampling which adds determinism to the function. 

![](../code/plantUML/Risk-Assessment/images/DataBalancing.png)

To prevent overfitting the model the mean number of illnesses after balancing was calulated and entries without illnesses where sampled to that mean and inserted that into the balanced df


![](../code/plantUML/Risk-Assessment/images/AddingNoneIllness.png)


Visualtisation of Illness Distrabution after balancing


![](../code/Risk_Assessment/images/BalancedIllnessDistrabution.png)



#### 3.6.2.3 Data Normalisation
Finally, I normalised both the balanced distribution data frame and the natural distribution data frame. The normalised data frames have two columns (Behaviour, Illness) which are both bit lists where a 1 represents the presence of that Behaviour/Illness and 0 represents an absence. This form makes the dataset machine-readable for future machine-learning models.

Process of Normalisation


![](../code/plantUML/Risk-Assessment/images/normalisation.png)

Normalised Data Set Example

|Behaviour|Illnesses|
|-|-|
|"[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]"|"[1, 0, 0, 0, 0, 0, 0, 0, 0, 1]"|


### 3.6.3 Model Training 


### 3.6.4 Model Selection

## 3.6.5 Model Evaluation and Results
#### 4.6.5.1 Accuracy

| ML Algorithm | Accurancy |
| ---- | ---- |
| Logistical Regression | 0.22663185378590078  | 
| Random Forest Classification | 0.3199303742384682 | 


#### 4.6.5.2  Precison, Recall, F1-Score

<table>
  <tr>
    <td colspan="4">
      ML-Algorithm
    </td>
    <td colspan="1" >
      Ilnessess
    </td>
    <td >
      Metrics
    </td>
    <td colspan="4">
      Values
    </td>
  </tr>
<td rowspan="30" colspan="4" > 
        Logistic Regression
    </td>    
    <td rowspan=3>
        Diebetes
    </td>
    <td>
        Precision
    </td>
    <td>
        0.18421053
    </td>
  </tr>
  <tr>
     <td>
        Recall
     </td>
     <td>
        0.00558214
     </td>
  </tr>
  <tr>
    <td>
        F1-score
    </td>
    <td>
        0.01083591
  </tr>
   <td rowspan=3>
        Pre_Diebetes
    </td>
    <td>
        Precision
    </td>
    <td>
        0.
    </td>
  </tr>
  <tr>
     <td>
        Recall
     </td>
     <td>
        0.
    </td>
  </tr>
  <tr>
    <td>
        F1-score
    </td>
    <td>
        0.
    </td>
  </tr>
   <td rowspan=3>
        Depression
    </td>
    <td>
        Precision
    </td>
    <td>
        0.62776025
    </td>
  </tr>
  <tr>
     <td>
        Recall
     </td>
     <td>
        0.15706393
    </td>
  </tr>
  <tr>
    <td>
        F1-score
    </td>
    <td>
        0.25126263
    </td>
  </tr>
   <td rowspan=3>
        COPD
    </td>
    <td>
        Precision
    </td>
    <td>
        0.66573034
    </td>
  </tr>
  <tr>
     <td>
        Recall
     </td>
     <td>
        0.22170253
    </td>
  </tr>
  <tr>
    <td>
        F1-score
    </td>
    <td>
        0.33263158
    </td>
  </tr>
   <td rowspan=3>
        Kidney Disease
    </td>
    <td>
        Precision
    </td>
    <td>
        0.61562021
    </td>
  </tr>
  <tr>
     <td>
        Recall
     </td>
     <td>
        0.24202288
    </td>
  </tr>
  <tr>
    <td>
        F1-score
    </td>
    <td>
        0.3474503
    </td>
  </tr>
   <td rowspan=3>
        Angina/Coronary heart disease
    </td>
    <td>
        Precision
    </td>
    <td>
        0.65471884
    </td>
  </tr>
  <tr>
     <td>
        Recall
     </td>
     <td>
        0.72007233
    </td>
  </tr>
  <tr>
    <td>
        F1-score
    </td>
     <td>
        0.68584223
    </td>
  </tr>
   <td rowspan=3>
        Myocardial infarction
    </td>
    <td>
        Precision
    </td>
    <td>
        0.6779661
    </td>
  </tr>
  <tr>
     <td>
        Recall
     </td>
     <td>
        0.61840121
    </td>
  </tr>
  <tr>
    <td>
        F1-score
    </td>
    <td>
        0.64681522
    </td>
  </tr>
   <td rowspan=3>
        Stroke
    </td>
    <td>
        Precision
    </td>
    <td>
        0.55305466
    </td>
  </tr>
  <tr>
     <td>
        Recall
     </td>
     <td>
        0.3733044
    </td>
  </tr>
  <tr>
    <td>
        F1-score
    </td>
    <td>
        0.4457402
    </td>
  </tr>
   <td rowspan=3>
        Arthritis Gout Lupus Fibromyalgia
    </td>
    <td>
        Precision
    </td>
    <td>
        0.62117235
    </td>
  </tr>
  <tr>
     <td>
        Recall
     </td><td>
        0.33793432
    </td>
  </tr>
  <tr>
    <td>
        F1-score
    </td><td>
       0.4377312
    </td>
  </tr>
 <td rowspan=3>
        Skin Cancer
    </td>
    <td>
        Precision
    </td>
    <td>
        0.52185609
    </td>
  </tr>
  <tr>
     <td>
        Recall
     </td>
     <td>
        0.41342568
    </td>
  </tr>
  <tr>
    <td>
        F1-score
    </td>
    <td>
        0.46135553
    </td>
  </tr>




  <td rowspan="30" colspan="4" > 
        Random Forest Classification 
    </td>    
    <td rowspan=3>
        Diebetes
    </td>
    <td>
        Precision
    </td>
    <td>
        0.7063197
    </td>
  </tr>
  <tr>
     <td>
        Recall
     </td>
     <td>
        0.3030303
     </td>
  </tr>
  <tr>
    <td>
        F1-score
    </td>
    <td>
      0.42410714
  </tr>
   <td rowspan=3>
        Pre_Diebetes
    </td>
    <td>
        Precision
    </td>
    <td>
        0.64044944
    </td>
  </tr>
  <tr>
     <td>
        Recall
     </td>
     <td>
        0.33187773
    </td>
  </tr>
  <tr>
    <td>
        F1-score
    </td>
    <td>
        0.43720038
    </td>
  </tr>
   <td rowspan=3>
        Depression
    </td>
    <td>
        Precision
    </td>
    <td>
        0.69170579
    </td>
  </tr>
  <tr>
     <td>
        Recall
     </td>
     <td>
        0.34885556
    </td>
  </tr>
  <tr>
    <td>
        F1-score
    </td>
    <td>
        0.46379853
    </td>
  </tr>
   <td rowspan=3>
        COPD
    </td>
    <td>
        Precision
    </td>
    <td>
        0.78830645
    </td>
  </tr>
  <tr>
     <td>
        Recall
     </td>
     <td>
        0.36576239
    </td>
  </tr>
  <tr>
    <td>
        F1-score
    </td>
    <td>
        0.49968051
    </td>
  </tr>
   <td rowspan=3>
        Kidney Disease
    </td>
    <td>
        Precision
    </td>
    <td>
        0.70096852
    </td>
  </tr>
  <tr>
     <td>
        Recall
     </td>
     <td>
        0.34858519
    </td>
  </tr>
  <tr>
    <td>
        F1-score
    </td>
    <td>
        0.46562123
    </td>
  </tr>
   <td rowspan=3>
        Angina/Coronary heart disease
    </td>
    <td>
        Precision
    </td>
    <td>
        0.70536618
    </td>
  </tr>
  <tr>
     <td>
        Recall
     </td>
     <td>
        0.75587703
    </td>
  </tr>
  <tr>
    <td>
        F1-score
    </td>
     <td>
        0.7297486
    </td>
  </tr>
   <td rowspan=3>
        Myocardial infarction
    </td>
    <td>
        Precision
    </td>
    <td>
        0.70802377
    </td>
  </tr>
  <tr>
     <td>
        Recall
     </td>
     <td>
        0.71870287
    </td>
  </tr>
  <tr>
    <td>
        F1-score
    </td>
    <td>
        0.71332335
    </td>
  </tr>
   <td rowspan=3>
        Stroke
    </td>
    <td>
        Precision
    </td>
    <td>
        0.69310345
    </td>
  </tr>
  <tr>
     <td>
        Recall
     </td>
     <td>
        0.43624525
    </td>
  </tr>
  <tr>
    <td>
        F1-score
    </td>
    <td>
        0.53546454
    </td>
  </tr>
   <td rowspan=3>
        Arthritis Gout Lupus Fibromyalgia
    </td>
    <td>
        Precision
    </td>
    <td>
        0.68888889
    </td>
  </tr>
  <tr>
     <td>
        Recall
     </td><td>
        0.51642075
    </td>
  </tr>
  <tr>
    <td>
        F1-score
    </td><td>
          0.59031556
    </td>
  </tr>
 <td rowspan=3>
        Skin Cancer
    </td>
    <td>
        Precision
    </td>
    <td>
        0.66165414
    </td>
  </tr>
  <tr>
     <td>
        Recall
     </td>
     <td>
        0.56259989
    </td>
  </tr>
  <tr>
    <td>
        F1-score
    </td>
    <td>
        0.60811978
    </td>
  </tr>


</table>

# 5 Problems and Resolutions

## 5.1 Identfied Issues

## 5.2 Resolution Strategies

## 5.3 Lessons Learned

## 5.4 Future Consideration

