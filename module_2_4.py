numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for numbers in numbers:
    if numbers > 1:
        for i in  range(2,numbers):
            if (numbers % i) == 0:
                not_primes .append(numbers)
                break
            else:
                primes.append(numbers)
        else:
            not_primes.append(numbers)

print('Список простых чисел:' , primes)
print('Список не простых чисел:', not_primes)
