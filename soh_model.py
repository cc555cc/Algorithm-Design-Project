import pandas as pd #tool for opening excel file

# load dataaset
data = pd.read_excel('PulseBat Dataset.xlsx')

raw_data = [] #stores original set of data 
train_data = []
test_data = []

def main():
    read_data();
    split_data();

def read_data():
    for i, row in data.iterrows(): #loop through the rows
        row_data = [];
        for j in range(7, len(data.columns)): # loop through the value from U1 to SOH
            row_data.append(float(data.iloc[i, j]));  #insert value of one battery at a time
        raw_data.append(row_data); #insert the set of values at a time into the data pool

def split_data():
    quota = len(raw_data)*0.2;
    #print(f"Test data quota: {quota}");


# Call the main function
main();

#print(data.head(10));