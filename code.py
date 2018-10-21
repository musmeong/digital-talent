"""This program is supposed to be a BMI-count tool that need user's weight and height
as a user-defined input and will show BMI and its condition as an output.
This program is created to fulfill the Digital Talent assignment.

Created by : Muhamad Musta'in
"""

#User Defined Input
weight = float(input('Input your weight (in kg) = ')) #weight input in kg
print('kg')
height = float(input('Input your height (in cm) = ')) #height input in cm
hm = height/100 #convert the height from cm to m
#--------------------------------

#Count the BMI
BMI = weight/(hm**2)  #BMI formula
#--------------------------------

#Show the output
print('Your weight is', weight,'kg')
print('Your height is', height, 'cm')
print('Your BMI score is',BMI)
#--------------------------------

#Conditional statement
if BMI <= 15:
    print ('You are very severely underweight.')
elif 15 < BMI <= 16 :
    print ('You are severely underweight.')
elif 16 < BMI <= 18.5 :
    print ('You are underweight.')
elif 18.5 < BMI <= 25 :
    print ('You are normal (healthy weight).')
elif 25 < BMI <= 30 :
    print ('You are overweight.')
elif 30 < BMI <= 35 :
    print ('You are moderately obese.')
elif 35 < BMI <= 40 :
    print ('You are severely obese.')
elif BMI > 40 :
    print ('You are very severely obese.')