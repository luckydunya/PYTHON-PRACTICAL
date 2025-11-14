fare1 =  5
fare2 = 10
fare3 =  8
destination =  str (input('Tell us your destination (Madina/Kasoa/Tema) ')).lower()
if destination == 'madina':
 passenger = int (input('How many of you are Boarding '))
 print(f"Your estimated fare is GHS:",passenger * fare1)
elif destination == 'kasoa':
    passenger = int(input('How many of you are Boarding '))
    print(f"Your estimated fare is GHS:", passenger * fare2)
elif destination == 'tema':
        passenger = int(input('How many of you are Boarding '))
        print(f"You estimated fare is GHS:", passenger * fare3)
else:
    print('Sorry,We are not going to your destination.')


