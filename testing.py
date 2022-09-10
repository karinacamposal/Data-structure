# Exercise 1
"""Write a program that stores your subjects (e.g. Math, Physics, Chemistry, Programming, English) in a list, 
asks the user for the grade he/she got in each subject, and then displays them on screen with the message In 
<subject> you got <grade> where <subject> is each of the subjects in the list and <grade> each of the 
corresponding 

notes entered by the user. """

subjects = ['Math', 'Physics', 'Chemistry', 'Programming', 'English']
grades = [ ]

grades.append (int(input(f'What grade did you get in {subjects[0]}? ')))
grades.append((input(f'What grade did you get in {subjects[1]}? ')))
grades.append (int(input(f'What grade did you get in {subjects[2]}? ')))
grades.append (int(input(f'What grade did you get in {subjects[3]}? ')))
grades.append (int(input(f'What grade did you get in {subjects[4]}? ')))


print(f'In  {subjects[0]} you scored: {grades[0]}')
print(f'In  {subjects[1]} you scored: {grades[1]}')
print(f'In  {subjects[2]} you scored: {grades[2]}')
print(f'In  {subjects[3]} you scored: {grades[3]}')
print(f'In  {subjects[4]} you scored: {grades[4]} \n \n')


# Exercise 2 

"""A programmer devised a program that would find the highest number from a given set of numbers. 
The numbers provided were stored as a list in a list variable called 'number_data'."""

number_data = [323, 209, 5900, 31092, 3402, 39803, 78341, 79843740,
895, 6749, 2870984]
Num = 0
for numb in number_data:
       if Num < numb:
        Num = numb
        
print(f'The highest number is: {Num}')