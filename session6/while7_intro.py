pw = input("Your password:")
while True:
    if pw.isdigit() or pw.isalpha():
        print("login failed")
        print("password can co ca chu va so")
        break
    else:
        print("login seccessful") 
        break