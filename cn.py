# imports

import pandas as pd

# Helper functions


def compare(cell, celll, type='bert'):
    # bert is the default comparsion method
    if type == 'bert':
        return
    if type == 'token_based':
        # find and count the tokens that each cell has in common
        # remove stopwords?
        return

# This will replace all NaN values in the DataFrame with the specified value.
# And there are a lot of other functions to replace NaN with something else.
df = df.fillna(value)


# Main execution


# load the spreadsheets 
# note: run print(df0) to see the spreadsheets (useful for troubleshooting)
df_pd = pd.read_excel('program descriptions.xlsx')
df_i = pd.read_excel('interventions.xlsx')

# Remove columns with nans
df_pd = df_pd.dropna(axis=1)

# a column to iterate through
column_name = 'program descriptions'
#column_name = 'c'

# iterate through the cells of a column
for cell in df_pd[column_name]:
    print(cell)
    # iterate through every cell of a spreadsheet
    for index, row in df_i.iterrows():
        for celll in row:
            print(celll)
            similarity = compare(cell, celll)
            # write the similarity score to the last column


"""
Notes
    1/13/23
        For next time, start by figuring out what should be done about NaNs.

"""

