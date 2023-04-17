def main():
    h = int(input("Enter height: "))
    triangle(h)

def triangle(n):
    for i in range(n):
        print("⬜"*(i+1))

if __name__ == "__main__":
    main()