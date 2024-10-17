# Password Manager

## Project Description
A secure and user-friendly password manager that allows users to store, retrieve, and manage passwords for various platforms and services. 
The application includes features such as separate user accounts, encryption/decryption, and secure storage in a PostgreSQL database, all managed through a PyQt5 GUI interface.

## Features
- **Secure Password Storage**: Stores passwords in a PostgreSQL database with encryption.
- **Accounts**: Allows for multiple users to use the password manager. Separating data for each user.
- **Password Retrieval**: Allows users to search and retrieve passwords by platform and username.
- **User Authentication**: Password protection for accessing the manager.
- **GUI Interface**: Uses PyQt5 for a user-friendly graphical interface.

## Technologies Used
- **Languages**: Python 3.12.6
- **Database**: PostgreSQL (using Docker for setup)
- **Libraries**:
  - `PyQt5` for the GUI
  - `psycopg2` for database interaction
  - `bcrypt`, `cryptography`, and `base64`' for encryption/decryption and hashing
- **Version Control**: Git

## Youtube resources used:
- Python cryptography using fernet: https://www.youtube.com/watch?v=VXNMYTzVyfM
- password manager tutorial: https://www.youtube.com/watch?v=8e6HQvy7ggU
  - helped with giving myself clear starting parameters
- This video is what the previous youtuber was inspired by: https://www.youtube.com/watch?v=hkhyKJj28Ac&t=554s
- Docker and PostgreSQL setup video: https://www.youtube.com/watch?v=TfJ8YD7sfsI


## Files not included:
- encryption_key.key holds my one time generated encryption key 
  - I understand that having a rotating encryption key is fundamentally more secure than a static never changing key
  - but from a personal project but for a personal project standpoint I don't think it is necessary
- password.py which holds my password for accessing my database


## Setup:
- Start by downloading docker desktop application for your specific system:
  - https://www.docker.com/products/docker-desktop/
- Follow this video for the Docker Desktop setup with postgreSQL image: https://www.youtube.com/watch?v=TfJ8YD7sfsI
  - be careful with the username you are using
  - password.py is where I currently store my password for my database
  - inside the database_connect.py you will see use of a variable rather than hard coding database password.
  - To create an encryption key for use you can use this:
    - `new_encryption_key = Fernet.generate_key()`
    - `print("New Encryption Key:", new_encryption_key.decode('utf-8'))`
    - store inside a file called encryption_key.key
  