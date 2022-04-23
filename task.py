def days(car):
    rent = car * 50
    if car >= 7:
        print(((rent * 100) - (rent * 30)) / 100, "30%")
    elif car >= 3 and car < 7:
        print(((rent * 100) - (rent * 10)) / 100, "10%")
    else:
        print(rent)
user = int(input())
days(user)




