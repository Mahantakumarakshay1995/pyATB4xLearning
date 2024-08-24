browser_name=input("Enter browser name")
browser_name=browser_name.lower()

match browser_name:
    case"firefox":
        print("Execute the Firefox Code")
    case "chrome":
        print("Execute the chrome Code")
    case "safari":
        print("Execute the safari Code")
    case _:
        print("Browser not found")