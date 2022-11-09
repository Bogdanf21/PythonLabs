def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, int(x / 2) + 1):
        if x % i == 0:
            return False
    return True


def process_item(x):
    try:
        x += 1
        while True:
            if isPrime(x):
                return x
            else:
                if x % 2 == 0:
                    x += 1
                else:
                    x += 2
    except ValueError:
        print("Not a number")
