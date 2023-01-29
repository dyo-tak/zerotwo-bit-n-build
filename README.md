# Student Result Predictor

## Problem Statement:
Every class has weak students who need some extra attension from teachers, etc.
There needs to be a ML model which predicts the grades of the student on basis of some important life attributes.
Teachers can therefore give proper guidance to them to improve there performance.

##Process:

Data Set taken from - archive.ics.uci.edu (UCI Machine Learning Repository

### 1) Heat MAP
![image](https://user-images.githubusercontent.com/97503802/215299962-1130dc8f-d19b-43e5-b7ab-4219926ccec5.png)


### 2) Correlation with Grades.
![image](https://user-images.githubusercontent.com/97503802/215296693-c47c0dff-3ca1-4b2b-8609-59ff59cc891b.png)

Above Graph relation gives us top attributes that affect the value of Grades. So we use some of the top attributes to build the model.

### 3) Frequency Of Grades
![image](https://user-images.githubusercontent.com/97503802/215296759-fa1ee93e-7afc-4acf-bc12-df24eef5fa68.png)

Above Graph shows that most of the student got 10/11 grade.

### 4) Studytime VS Grades Relation 
![image](https://user-images.githubusercontent.com/97503802/215296815-68d6083f-8f30-4645-891c-e46b4bf1de1e.png)

The above relation shows the relation between time studied and the grade score associated with it. It will help teacher to ask the student to increase their study 
time to improve there score.

## Algorithms used to build the model

    - Decision Tree Classifier
    - XGBoost Regressor
    - Random Forest Regression
    - Linear Regression [Finalised]
    
## Deployed Website:
![image](https://user-images.githubusercontent.com/97503802/215299355-9f04aeec-8510-4182-94eb-56b6ec671aa1.png)

