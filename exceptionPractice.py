try:
    with open("app.py") as file:
        print("file opened")

    file = open("app.py")
    age = int(input("Age: "))
    xfacter = 10 / age


except (ValueError, ZeroDivisionError) as ex:
    print("You didn't enter a valid age")

else:
    print("No exceptions were thrown")
