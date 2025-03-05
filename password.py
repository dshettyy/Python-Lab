import random
import string

def generate_password(length=12):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_chars = letters + digits + symbols
    password = random.choice(letters) + random.choice(digits) + random.choice(symbols)
    password += ''.join(random.choices(all_chars, k=length - 3))
    password = list(password)
    random.shuffle(password)
    return ''.join(password)

def main():
    length = int(input("Enter password length: "))
    print("Generated Password:", generate_password(length))

if __name__ == "__main__":
    main()
