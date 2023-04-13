import random

lotto_numbers = random.sample(range(1, 50), 6)

with open("lotto_numbers.txt", "w") as file:
    for number in lotto_numbers:
        file.write(str(number) + " ")

print("Wylosowane liczby zostały zapisane do pliku lotto_numbers.txt")
