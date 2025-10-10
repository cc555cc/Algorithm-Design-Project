import pandas as pd #tool for opening excel file
import random
from sympy import symbols, integrate

# load dataaset
data = pd.read_excel('PulseBat Dataset.xlsx')

raw_data = [] #stores original set of data 
train_data = []
test_data = []

def main():
    read_data();
    analysis_measured_charge();

def read_data():
    for i, row in data.iterrows(): #loop through the rows
        row_data = [];
        for j in range(0, len(data.columns)): # loop through the value from U1 to SOH
            try:
                row_data.append(float(data.iloc[i, j]));  #insert value of one battery at a time
            except (TypeError, ValueError):
                row_data.append(data.iloc[i, j]);

        raw_data.append(row_data); #insert the set of values at a time into the data pool

def split_data():
    quota = int(len(raw_data)*0.2); #number of dataset for testing
    
    #first run for random selection
    for i in range (0,len(raw_data)):
        chance = random.random();
        if chance <= 0.3 and quota > 0:
            test_data.append(raw_data[i]);
            quota -= 1;
        else:
            train_data.append(raw_data[i]);
    
    # second run if the test_data is not exactly 20% of the original data pool(134)
    if quota > 0:
        need = 134 - len(test_data); #the number of dataset need to fill up the the test data pool
        
        #loop through the train data pool
        for i in range(0,need): 
            index = random.randint(0, len(train_data)-1);  #pick a random index 
            test_data.append(train_data.pop(index)); #move the data from train pool to test pool

def analysis_measured_charge():
        for i in range(0,len(raw_data)):
            if raw_data[i][1] == 1.0:
                print (raw_data[i]);


# Call the main function
main();

#print(data.head(10));