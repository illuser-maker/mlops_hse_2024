import random

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total/count

def greet(name:str)->str:
    return f"Hello, {name}!"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

def main():
    numbers = [1, 2, 3, 4, 5]
    avg = calculate_average(numbers)
    print(f"The average is: {avg}")

    name = input("Enter your name: ")
    greeting = greet(name)
    print(greeting)

    person = Person("Alice", 30)
    person.introduce()

    # Unused import
    random_number = random.randint(1, 10)

if __name__ == "__main__":
    main()