import pandas as pd
import numpy as np
import json
import pickle

#Test validation
"""
Load json template, and store it in a dictionary.  
1- Check that all columns are present
2- Iterate through all the columns of the uploaded file and check each column w
your template dictionary.
3- Check that values entered in each columns is valid. (Same for loop as step 2)
"""
def validate_cols(uploaded_document):
    """
    Function args
    -------------
    uploaded_document: Name of the csv file uploaded by the user.
    """
    #Load data using pandas
    user_data = pd.read_excel(uploaded_document, engine='openpyxl', index_col=None)

    if user_data.isnull().any().any():
        return "Dataset validation failed: Data contains missing values"

    #Load JSON schema for the dataframe
    with open('template.json', 'r') as file:
        myTemplate = json.load(file)
    myTemplate = pd.DataFrame(myTemplate)   #Convert it to DataFrame for easier acces
    myTemplate.set_index('Columns', inplace=True)

    list(set(user_data.columns).difference(list(myTemplate.index)))


    #Load dict() mapping from Pickle file
    with open('columns_encode.pickle', 'rb') as file:
        columns_map = pickle.load(file)


    # Validate that columns match in both lists.
    if len(user_data.columns) == len(myTemplate) and (user_data.columns.sort_values() == myTemplate.sort_index().index).all():
        #Validate Dtype and values in each column
        for col in user_data.columns:
            #Compare datatypes with myTemplate
            if str(user_data[col].dtype) != myTemplate.loc[col, :].item():
                return(f"Expected {myTemplate.loc[col, :].item()} Dtype for {col}\nGot {str(user_data[col].dtype)} instead.")
            
            #If the column is categorical, check that values are valid
            if str(user_data[col].dtype) == 'object':
                invalid = np.logical_not(np.isin(user_data[col].unique(), list(columns_map[col].keys()))) #Gathers invvalues not in dictionary
                if invalid.any() == True:
                    return(f"{col} Column Validation failed:\n" \
                        f"The following values are invalid:\n" \
                        f"{user_data[col].unique()[invalid]}")


        return("Columns validation was successful")
    else:
        missing_in_json = list(set(user_data.columns).difference(list(myTemplate.index)))
        if  len(missing_in_json) > 0:
            return('Columns validation has failed\nThe following columns are not needed: ', missing_in_json)
        else:
            missing_in_data = list(set(list(myTemplate.index)).difference(user_data.columns))
            if len(missing_in_data) > 0:
                return('Columns validation has failed\nThe following columns were not in your data: ', missing_in_data)



