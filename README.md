

# **End-to-End Machine Learning Project: Student Performance Indicator**



## **Author: Muhammad Adil Naeem**

[![GitHub](https://img.shields.io/badge/GitHub-Profile-green?style=for-the-badge&logo=github)](https://github.com/muhammadadilnaeem) 
[![Twitter/X](https://img.shields.io/badge/Twitter-Profile-red?style=for-the-badge&logo=twitter)](https://twitter.com/adilnaeem0) 
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/muhammad-adil-naeem-26878b2b9/)

---

## **Lifecycle of this Machine Learning Project**

1. **Understanding the Problem Statement**
2. **Data Exploration**
3. **Data Visualization**
4. **Data Cleaning**
5. **Data Preprocessing**
6. **Model Building**
7. **Model Evaluation**
8. **Choosing Best Machine Learning Model**
9. **Save the Best Machine Learning Model**
10. **Make prediction with Best Machine Learning Model**
11. **Creating a Web Interface for User Predictions**

---

## **Understanding Problem Statement**
This project explores how students' performance (exam scores) is influenced by variables such as **Gender**, **Ethnicity**, **Parental Level of Education**, **Lunch Type**, and **Test Preparation Course**.

## **Data Exploration**

- The dataset used in this project is obtained from [Kaggle](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977).
- The dataset contains **8 columns** and **1000 rows**.

### Dataset Attributes:

| **Attribute**                    | **Description**                                      | **Possible Values**                                                |
|----------------------------------|------------------------------------------------------|--------------------------------------------------------------------|
| **gender**                       | Sex of students                                      | Male, Female                                                       |
| **race_ethnicity**               | Ethnicity of students                                | Group A, Group B, Group C, Group D, Group E                        |
| **parental_level_of_education**  | Parents' final education                             | Bachelor's degree, Some college, Master's degree, Associate's degree, High school |
| **lunch**                        | Type of lunch before test                            | Standard, Free/reduced                                             |
| **test_preparation_course**      | Completion of test preparation course                | Complete, Not complete                                             |
| **math_score**                   | Score in math                                        | Numeric value                                                      |
| **reading_score**                | Score in reading                                     | Numeric value                                                      |
| **writing_score**                | Score in writing                                     | Numeric value                                                      |

## **Libraries Used**

- setuptools
- numpy
- pandas
- matplotlib
- seaborn
- openpyxl
- scikit-learn
- xgboost
- catboost

---

## **Working of the Code**

The project code includes data ingestion, preprocessing, model building, evaluation, and deployment steps. A web interface is provided to allow users to input their data and receive predictions.

https://github.com/muhammadadilnaeem/ML-Project/assets/162784706/bd642b58-792b-43f9-94e8-9e1302df4c80

---

## **Web Interface**

The web interface built using Flask allows users to input various parameters to predict a student's math score. The interface is designed to be user-friendly and interactive.

![112233](https://github.com/muhammadadilnaeem/ML-Project/assets/162784706/2e5bc1df-448e-42c0-9cab-76e8d7e432db)



Feel free to explore the project and use the interface to see how different variables can affect student performance in exams.