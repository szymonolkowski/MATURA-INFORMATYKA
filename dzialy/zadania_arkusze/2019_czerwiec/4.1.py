def is_prime(x):
    return all(x % i != 0 for i in range(2, x)) if x > 1 else False


with open("MIN-R2A1P-193_dane/liczby.txt") as file:
    for line in file:
        line = int(line)
        if is_prime(line) and line in range(100, 5001):
            print(line)