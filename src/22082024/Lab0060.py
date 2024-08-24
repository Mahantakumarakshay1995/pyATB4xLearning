user_type = input("Enter your profile\n")
user_type = user_type.lower()
match user_type:
    case "manager" | "admin":
        print("welcome sir")
    case "guest" | "new joine" :
        print("Welcome guest")
    case _:
        print("Not Welcome")
