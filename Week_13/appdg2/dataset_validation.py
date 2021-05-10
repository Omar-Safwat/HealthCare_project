import pandas as pd
import json

#Test validation
"""
Load json template, and store it in a dictionary.  
1- Check that all columns are present
2- Iterate through all the columns of the uploaded file and check each column w
your template dictionary.
"""
def validate_cols(user_data):
    """
    Function args
    -------------
    user_data: A pandas dataframe for uploaded data by the user.
    """

    #Load JSON schema for the dataframe
    with open('template.json', 'r') as file:
        myTemplate = json.load(file)
    myTemplate = pd.DataFrame(myTemplate)   #Convert it to DataFrame for easier acces
    myTemplate.set_index('Columns', inplace=True)
    # Validate that columns match in both lists.
    if len(user_data.columns) == len(myTemplate) and (user_data.columns.sort_values() == myTemplate.sort_index().index).all():
        #Validate Dtype in each column
        for col in user_data.columns:
            if str(user_data[col].dtype) != myTemplate.loc[col, :].item():
                return(f"Expected {myTemplate.loc[col, :].item()} Dtype for {col}\nGot {str(user_data[col].dtype)} instead.")
                 
        return("Columns validation was successful")
    else:
        missing_in_json = list(set(user_data.columns).difference(list(myTemplate.index)))
        if not missing_in_json:
            return('Columns validation has failed\nThe following columns are not needed: ', missing_in_json)
        else:
            missing_in_data = list(set(list(myTemplate.index)).difference(user_data.columns))
            return('Columns validation has failed\nThe following columns were not in your data: ', missing_in_data)



