largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        n = int(num)
        if largest is None and smallest is None:
            largest = n
            smallest = n
        else:
            if n > largest:
                largest = n
            elif n < smallest:
                smallest = n
    except ValueError:
        if num == "done":
            break
        print("Invalid input")
        continue

if largest is not None:  # Add this check
    print("Maximum is", largest)
    print("Minimum is", smallest)