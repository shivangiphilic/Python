#tuple is immutable list

def main():
    person = get_person()
    print(f"{person[0]} from {person[1]}")

def get_person():
    name = input("Enter name: ").title()
    country = input("Enter country: ").title()
    return (name,country)     #returning a tuple 'person' with 2 values

if __name__ == "__main__":
    main()

