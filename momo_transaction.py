
charge1 = 2
charge2 = 5
charge3 = 10
print('MTN Mobile Money Transaction \n')
amount = int (input('Enter Amount '))
if amount <= 100:
    print(f'The Receiver gets GHS:',amount - charge1)
elif amount > 100 and amount < 500:
    print(f'The Receiver gets GHS:', amount - charge2)
elif amount > 500:
    print(f'The Receiver gets GHS:', amount-charge3)