# Author: Shepard Berry
# Class: MIS 4322
# Due: 2/13/2023
# Quiz 1
'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
with open("employee_data.csv", 'r') as f:
    reader = csv.reader(f)

    #create an empty dictionary
    employee_dict = {}

    #use a loop to iterate through the csv file
    for line in reader:
        #check if the employee fits the search criteria
        if reader.line_num != 1 and line[3] == "Marketing" and line[4] == "CSR":
            print(f'Manager Name: {line[1]} {line[2]} Current Salary: ${float(line[5]):,.2f}')
            employee_dict[f'{line[1]} {line[2]}'] = float(line[5]) * 1.10
    print()
    print('=========================================')
    print()

    #iternate through the dictionary and print out the key and value as per printout
    #print all values in dict
    for k, v in employee_dict.items():
        print(f'Manager Name: {k} New Salary: ${v:,.2f}')



          
        

        
    
