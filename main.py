from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)

    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()

    def create_pass_file(self, path, initial_values=None):
        self.password_file = path
        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key, value)

    def load_pass_file(self, path):
        self.password_file = path
        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()

    def add_password(self, site, password):
        if self.key is None:
            print("Please load or create a key before adding a password.")
            return

        self.password_dict[site] = password
        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")

    def get_password(self, site):
        if site in self.password_dict:
            return self.password_dict[site]
        else:
            return "Password not found for the site: " + site


def main():
    password = {
        "password 1": "password123"
    }

    pm = PasswordManager()

    print("""
    What do you need?
    (1) Create new item
    (2) Load an existing key
    (3) Create new password file
    (4) Load existing password file
    (5) Add a new password
    (6) Get a password
    (q) Quit
    """)

    done = False

    while not done:
        choice = input("Enter your choice: ")

        if choice == "1":
            path = input("Enter a path: ")
            pm.create_key(path)
        elif choice == "2":
            path = input("Enter a path: ")
            pm.load_key(path)
        elif choice == "3":
            path = input("Enter a path: ")
            pm.create_pass_file(path, password)
        elif choice == "4":
            path = input("Enter a path: ")
            pm.load_pass_file(path)
        elif choice == "5":
            site = input("Enter the site: ")
            password = input("Enter the password: ")
            pm.add_password(site, password)
        elif choice == "6":
            site = input("What site do you want: ")
            print(f'Password for {site} is {pm.get_password(site)}')
        elif choice == "q":
            done = True
            print("Good bye!")
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()