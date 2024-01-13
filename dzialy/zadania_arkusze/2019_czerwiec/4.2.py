def is_prime(x):
    return all(x % i != 0 for i in range(2, x)) if x > 1 else False


with open("MIN-R2A1P-193_dane/pierwsze.txt") as file:
    for line in file:
        line = line.strip()
        liczba = int(line[::-1])
        if is_prime(liczba):
            print(line)