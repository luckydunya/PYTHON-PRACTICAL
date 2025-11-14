nationality = str (input('Enter nationality ')).lower()
name = str (input('Enter your name '))
age = int (input('Enter your age '))
if age >=18 and nationality == 'ghanaian':
    print('Eligible')
else:
    print('Not Eligible')