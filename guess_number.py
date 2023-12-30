from random import randint
r_n = randint(1, 100)
print(r_n)
while True:
    guess = int(input('Введите число: '))
    if guess < r_n:
        print('Ваше число меньше того, что загадано')
    elif guess > r_n:
        print('Ваше число больше того, что загадано')
    else:
        print('Отличная интуиция! Вы угадали чилсло :)')
        break