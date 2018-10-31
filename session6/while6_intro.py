print("how much money i have left??")
print("1. A lot")
print("2. Not much")
print("3. NONE")
print("4. huhuhuhuhuhuhuhuhu")
while True:
    ans = input("Your answer:")
    if ans.isdigit() == True:
        if ans == "3":
            print("corect")
            break
        else:
            print("wrong")
        
    else:
        print("the answer must be 1; 2; 3 or 4")
        
