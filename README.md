# HRConnect Project

    -Download .csv data from following website -https://gist.github.com/kevin336/acbb2271e66c10a5b73aacf82ca82784

## TASK 1:
Write a program to get details of employees who's salary is > 9000. The output should
be in following format
{
"Name": "<first_name last_name>",
"email": "<email>",
"phone number": "<phone number without DOT>"
}
- import csv module
- creating the class of File Handler
- open csv file 
- access the dtat from csv file
- line bye line 
- all file in DictRead mood
  - access data in form of dictionary
  - compare the SALARY with given SALARY
  - access the NAME,EMAIL,PHONE_NUMBER
  - data store in dictionary format
-create class object and class the method of class for access the method

## TASK 2
Write a program to get "HIRE DATE" of employee who's department is within range 30
to 110 AND who's salary is > 4200.
The output should be in following format.

{
"<HIRE DATE in YYYY-MM-DD format>": [
"<first_name last_name>",
...,
"<first_name last_name>"
],
}

- create the module csv for store dictionary value in list format
- import the module
- create the class of different method
- method for access the employees hire date and salary > 4200
  - access of employees DEPARTMENT_ID
  - comapare the id 
  - access the compare id employees name and Hire date 
  - To store in dictionary format acess the method from cs .py file 
  - create class object and call the method of class for details