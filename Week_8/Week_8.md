**Project title:** Healthcare - Persistency of a drug<br>
**Group name:** DG_team_project_PL-RO-KSA-EGY<br>
**Github repo:** [https://github.com/Omar-Safwat/HealthCare_project](https://github.com/Omar-Safwat/HealthCare_project)<br>
**Week:** 8<br>


# Team members
    
| Name | Specialization | Country | Email |
| :--- | --- | --- | --- | 
| Ms. Larisa Popa | Data Science | Romania |Larisapopa4@gmail.com |
| Ms. Afshan Hashmi | Data Science | Kingdom of Saudi Arabia | afshanhashmi786@gmail.com |
| Mr. Omar Safwat | Data Science | Egypt | omarksafwat@gmail.com |
| Mr. Roger Burek-Bors | Data Science | Poland | roger.burek-bors@hotmail.com |


# Problem description 

A machine learning model cannot be built without sufficient data. Quality data is fundamental to any data science engagement. To gain actionable insights, the appropriate data must be sourced and cleansed. There are two key stages of Data Understanding: a Data Assessment and Data Exploration. Our team provides Data Understanding insights within week 9 assignment.<br>

The Pharmaceutical company provided dataset called “Healthcare_dataset” in xlsx format consisting of:
- Basic description of features (Feature Description tab)
- Data (Dataset tab) where we found:
    - 69 features
    - 3424 data points
<br>


# Data understanding

Key dataset characteristic are as following:
- 99% features are provided as categorical data and we need to turn them into numerical before feeding into ML model (e.g. “Yes”/”No” as 1/0, NTM_Speciality as dictionary), only one feature has numerical values ("Count_Of_Risks")
- Data is labelled and “Persistency_Flag” feature will serve as the label for ML model
- There are no duplicating data points
- Missing values are present as "Unknown" in following features: "Race", "Ethnicity", "Region" and "NTM_Speciality"
<br>


What are the problems in the data ( number of NA values, outliers , skewed etc)

What approaches you are trying to apply on your data set to overcome problems like NA value, outlier etc and why?