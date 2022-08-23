def greet(name, location):
    print(f"Hello {name}!")
    print("Where are you from?")
    print(f"I'm from {location}")

name = input("Enter your name: ")
location = input("Enter your location: ")

greet(name, location)

greet(location="Lisbon", name="Me")