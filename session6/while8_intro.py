pw = input("Your password:")
while True:
    if pw.isdigit() or pw.isalpha() or len(pw) <= 8:
        print("login failed")
        break
    else:
        print("login seccessful") 
        break