import getpass
import hashlib
import secrets
import string
import urllib.request

common_passwords = ["password", "123456", "12345678", "qwerty", "abc123", "pakistan123", "iloveyou", "letmein", "welcome", "admin"]

def check_strength (password):
    score = 0
    tips = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        tips.append("Use at least 12 characters. ")

    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("Mix uppercase and lowercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("Add some numbers.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        tips.append("Add a symbol like ! or #.")

    if password.lower() in common_passwords:
        score = 0
        tips.append("This is a very common password!")

    return score, tips

def check_breach(password):
    hash_value = hashlib.sha1(password.encode()).hexdigest().upper()
    first5, rest = hash_value[:5], hash_value[5:]

    url = "https://api.pwnedpasswords.com/range/" + first5
    response = urllib.request.urlopen(url, timeout = 10).read().decode()

    for line in  response.splitlines():
        suffix, count = line.split(":")
        if suffix == rest:
            return int(count)
    return 0

def generate_password(length = 12):
    letters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(secrets.choice(letters) for _ in range(length))

def main():
    while True:
        print("\n 1) check strength 2) check breach 3) Generate 4) Quit")
        choice = input("Choose: ")

        if choice == "1":
            password = getpass.getpass("password (hidden): ")
            score, tips = check_strength(password)
            print(f"Score: {score}/5")
            for tip in tips:
                print(" -", tip)

        elif choice == "2":
            password = getpass.getpass("Password (hidden): ")
            try:
                count = check_breach(password)
            except OSError:
                print("Could not connect. Check your internet. ")
                continue
            if count:
                print(f"Found in {count:,} breaches. Do not use it!")
            else:
                print("Not found in known breaches.")

        elif choice == "3":
            print("Your password: ", generate_password())

        elif choice == "4":
            break

if __name__ == "__main__":
    main()