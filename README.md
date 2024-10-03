# Password Manager

## Project Description
A secure and user-friendly password manager that allows users to store, retrieve, and manage passwords for various platforms and services. The application includes features such as password generation, encryption, and secure storage in a PostgreSQL database, all managed through a PyQt5 GUI interface.

## Features
- **Secure Password Storage**: Stores passwords in a PostgreSQL database with encryption.
- **Password Retrieval**: Allows users to search and retrieve passwords by platform and username.
- **User Authentication**: Password protection for accessing the manager.
- **GUI Interface**: Uses PyQt5 for a user-friendly graphical interface.

## Technologies Used
- **Languages**: Python 3.12.6
- **Database**: PostgreSQL (using Docker for setup)
- **Libraries**:
  - PyQt5 for the GUI
  - `psycopg2` for database interaction
  - `secrets` for password generation
  - `bcrypt` and `cryptography` for encryption and hashing
- **Version Control**: Git




## Currently working on adding:
- setting up backend for registering and login functions


## Files not included:
- cryptography.py which stores the encryption and decryption functions for the passwords.