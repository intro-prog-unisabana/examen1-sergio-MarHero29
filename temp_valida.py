while True:
    try:
        temp = int(input("Please enter the temperature: "))
        
        if 55 <= temp <= 100:
            print("Valid input.")
            break
        else:
            print("Invalid input, try again.")
    
    except:
        print("Invalid input, try again.")