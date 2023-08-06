# Simple Password Manager

This Simple Password Manager is a command-line Python application that helps you manage your passwords securely. It uses the `cryptography` library to encrypt and decrypt passwords, ensuring that your sensitive data remains protected.

## Features
- Create and manage a secure encryption key.
- Create and load password files to store your passwords.
- Add new passwords to the password file.
- Retrieve passwords for specific sites.

## Installation
1. Make sure you have Python 3.x installed on your system.
2. Install the required cryptography library using the following command: `pip install cryptography`
3. Download or clone the `main.py` file to your desired directory: `git clone https://github.com/siriusberg/simple-password-manager`

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory where the `main.py` file is located
3. Run the password manager by executing the following command: `python main.py`
4. Follow the on-screen prompts to perform various actions within the password manager.

## Step-by-Step Instruction
1. Create a new password file and generate an encryption key:
```
Enter your choice: 1
Enter a path: pass.key
```
<b>Alert</b>: Before creating a new password file, make sure you have generated an encryption key using option 1. <br>

2. Load the encryption key:
```
Enter your choice: 2
Enter a path: pass.key
```
3. Create a new password file and add a password for a site:
```
Enter your choice: 3
Enter a path: password-database.pass
```
4. Load the password file:
```
Enter your choice: 4
Enter a path: password-database.pass
```
5. Add a new password for a site:
```
Enter your choice: 5
Enter the site: pc
Enter the password: password123
```
<b>Alert</b>: Ensure you have both an encryption key loaded and a password file loaded before adding passwords. <br>

6. Retrieve the password for a specific site:
```
Enter your choice: 6
What site do you want: pc
Password for pc is password123
```
<b>Alert</b>: Make sure you have loaded the correct password file before attempting to retrieve passwords. <br>

7. Quit the password manager:
```
Enter your choice: q
Good bye!
```

## Important Notes
- Keep your encryption key file (`key.key`) safe and secure. <b>Losing this file means you won't be able to decrypt your passwords</b>.

- This is a simple implementation and does not include advanced security features. It is recommended for personal use or as a learning tool.

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request to contribute to the project.

## Future Updates
I'm continuously working to improve the Simple Password Manager and make it even more user-friendly. Here's what you can look forward to in future updates:
- ### Graphical User Interface (GUI)
I'm excited to announce that a graphical user interface (GUI) will be added to the Simple Password Manager. This GUI will provide an intuitive and user-friendly way to manage your passwords, eliminating the need for command-line interactions. With the GUI, you'll be able to perform tasks such as creating and loading keys, managing password files, adding new passwords, and retrieving passwords, all through a visually appealing interface.
Stay tuned for updates as I work on integrating the GUI into the Simple Password Manager. I'm committed to delivering a seamless and secure experience for all users.


