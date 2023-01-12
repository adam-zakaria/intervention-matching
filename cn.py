import pandas as pd

# load the spreadsheet or dataframe
df = pd.read_excel('your_spreadsheet.xlsx')

# specify the column you want to iterate through
column_name = 'column_name'

# iterate through the cells of the column
for cell in df[column_name]:
    print(cell)

# iterate through every cell
for index, row in df.iterrows():
    for cell in row:
        print(cell)
