cocoa_price = 850
bonus = 2000
bags = int (input(f'How many bags of Coca do you want to sell? '))
total = bags * cocoa_price
if bags >= 100:
    print(f'Your Cocoa is Worth GHS:',total+bonus,' Including GHS2,000 bonus')
else:
    print('Your Cocoa is Worth GHS',total)
