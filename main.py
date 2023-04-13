import random


while(int(input("1. Graj!\n0. Wyjdź\nWpisz: "))):
    def is_valid_number(number):
        try:
            number = int(number)
            if 1 <= number <= 49:
                return True
            else:
                return False
        except:
            return False


    user_numbers = []
    while len(user_numbers) < 6:
        number = input("Podaj liczbę lotto (od 1 do 49): ")
        if is_valid_number(number) and int(number) not in user_numbers:
            user_numbers.append(int(number))
        else:
            print("Nieprawidłowa wartość. Spróbuj ponownie.")

    lotto_numbers = random.sample(range(1, 50), 6)

    print("Twoje liczby lotto:")
    print(user_numbers)

    print("Wylosowane liczby lotto:")
    print(lotto_numbers)

    matched_numbers = set(user_numbers).intersection(set(lotto_numbers))
    #intersection sprawdza które liczby w setcie się pokrywają

    if len(matched_numbers) > 0:
        print("Wygrałeś/łaś! Twoje trafione liczby to:")
        print(matched_numbers)
        with open("matched_numbers.txt", "a") as file:
            for number in matched_numbers:
                file.write(str(number) + "\n")
    else:
        print("Niestety nie trafiłeś/łaś żadnej liczby.")
