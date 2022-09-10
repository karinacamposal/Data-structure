"""""subjects = ['Maths', 'Physics', 'Chemestry', 'Programming', 'English']


calif1= int(input(f'¿Qué notas has sacado en {subjects[0]}?'))
calif2= int(input(f'¿Qué notas has sacado en {subjects[1]}?'))
calif3= int(input(f'¿Qué notas has sacado en {subjects[2]}?'))
calif4= int(input(f'¿Qué notas has sacado en {subjects[3]}?'))
calif5= int(input(f'¿Qué notas has sacado en {subjects[4]}?'))
notas=[calif1, calif2, calif3, calif4, calif5]

print(f'En  {subjects[0]} has sacado:{notas[0]}')
print(f'En  {subjects[1]} has sacado:{notas[1]}')
print(f'En  {subjects[2]} has sacado:{notas[2]}')
print(f'En  {subjects[3]} has sacado:{notas[3]}')
print(f'En  {subjects[4]} has sacado:{notas[4]}')"""

"""A programmer devised a program that would find the highest number from a given set of numbers. 
The numbers provided were stored as a list in a list variable called 'number_data'."""

number_data = [323, 209, 5900, 31092, 3402, 39803, 78341, 79843740,
895, 6749, 2870984]
num = 0
for number in number_data:
       if num < number:
        num = number
        
print(f'The highest number is: {num}')