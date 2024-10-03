***NOTES***

* work on encryption and decryption of the data going inside the database (cryptography library)
*  clean up un-used code that serves no purpose , consolidate other code.

***RESOURCES:***

https://www.youtube.com/watch?v=VXNMYTzVyfM

***Removed:***

- Authenticate.py:
- we did this because now in our create_hash.py we have a verify_password function
  - taking the functionality of what authenticate did with less hardcoding 
  - since we stored the hashed password into our users table in our database
- create_hash.py: 
  - deleted the function gen_secret_key I believe this was from the old code where things were hard coded



