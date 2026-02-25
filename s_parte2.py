counter = 0

for i in range(10):
    message = input("Enter your message:\n")
    
    contains_s = "s" in message.lower()
    print(contains_s)
    
    if contains_s:
        counter += 1

print(f"{counter}/10 messages contained the letter \"s\"")