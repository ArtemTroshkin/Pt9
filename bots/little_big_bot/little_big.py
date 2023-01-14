number = 100
count_of_attempts = 1

while True:
    try:
        answer = int(input('Введите число: '))

        if answer == number:
            print('Вы угадали!')
            print(f'Количество попыток: {count_of_attempts}')

            with open('high_score.txt', 'w+') as high_score:
                if len(high_score.read()) == 0:
                    high_score.write(f'{count_of_attempts}')
                    break
                elif count_of_attempts < int(high_score.read()):
                    print('Вы установили новый рекорд!')
                    high_score.write(f'{count_of_attempts}')
                    break

        elif number < answer:
            print('Введенное число меньше загаданного')
            count_of_attempts += 1
        else:
            print('Введенное число больше загаданного')
            count_of_attempts += 1

    except ValueError:
        print(f'\n[ERROR] Данные должны иметь числовой тип')
