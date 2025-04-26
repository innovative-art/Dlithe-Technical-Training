def is_disarium(num):
    s = str(num)
    return sum(int(digit) ** (i + 1) for i, digit in enumerate(s)) == num

print("1. First n Disarium numbers")
print("2. Disarium numbers between two numbers")
choice = int(input("Enter choice (1 or 2): "))

if choice == 1:
    n = int(input("Enter n: "))
    num = 0
    count = 0
    while count < n:
        if is_disarium(num):
            print(num, end=" ")
            count += 1
        num += 1

elif choice == 2:
    start = int(input("Enter start number: "))
    end = int(input("Enter end number: "))
    for num in range(start, end + 1):
        if is_disarium(num):
            print(num, end=" ")
else:
    print("Invalid choice!")

