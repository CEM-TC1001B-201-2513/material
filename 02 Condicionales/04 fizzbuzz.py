# Ingresar un número entero n
# Si el número es divisible entre 3 -> Fizz
# Si el número es divisible entre 5 -> Buzz
# Si el número es divisible entre 3 y entre 5 -> FizzBuzz
# Si el número no es divisible ni entre 3 ni entre 5 -> n
n = int(input("Ingresa un número n: "))
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)