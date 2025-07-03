import random 
import string

def gen(length=12):
    char = string.ascii_letters + string.digits + string.punctuation
    paswo = ''. join(random.choice(char) for _ in range(length))
    return paswo

def main():
    print("Generate password random")
    try:
        user_input = input("input password length  you(password length  <= 12) :")
        length = int(user_input) if user_input else 12

        if length < 8:
            print("Warning: You must input your password length  >= 8 ")
        paswo = gen(length)
        print(f"your password is : {paswo}")
    except ValueError:
        print("input invalid . password length must be numbers ")
if __name__ == "__main__":
    main()