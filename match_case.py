a=int(input("enter a number:"))
match a:
    case 1:
        print("you have won 10$")
    case 5:
        print("you got an iphone")
    case 6:
        print("you won the jackpot")
    case _:
        print("better luck next time")
        
# match_case is newer version of if_elif_else conditons.