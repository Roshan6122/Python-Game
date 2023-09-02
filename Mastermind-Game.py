from random import randint

compNumber= str(randint(1000, 9999))
# print(f'Computer Number: {compNumber}')

print('Computer decide a 4 digit number!')
print('Now it\'s your turn to guess that number')

count= 0

while True:
    userNumber= input('\nEnter number: ')
    if compNumber==userNumber:
        print('Great! You successfully guess the number.')
        break
    else:
        for i in range(4):
            if compNumber[i]==userNumber[i]:
                print(f'You guess the number: {userNumber[i]} in {i+1} position')
        count+=1

print(f'You guess the number completely with {count+1} try')