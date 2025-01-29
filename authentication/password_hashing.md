# Password hashing

- Hash functions are a one way function which turns any given data into a hash of fixed length which are irreversible called the fingerprint.
- Always tell the user both the username or the password is invalid when the hash doesn't match with the hash stored in the database.
- Hash functions designed to create data structure are made to be fast while cryptographic hash functions are designed to implement password hashing.
- SHA256, SHA512, RipeMD and WHIRLPOOL are a few cryptographic hash functions.

## Attacks used to crack plain password

1. Dictionary Attack

- A text file containing a list of passwords is hashed and each hash is used to check against the password hash in the database.
- Leet Speak equivalents are used to make the process more effective.

2. Brute Force Attack

- It tries all the possible combination to find the password, though the password can be eventually found, it takes exceeding long time and are computationally expensive.

3. Lookup tables

- An effective way is to use the lookup table method, where the hash of the password list is computed and stored as a password dictionary then compared against the corresponding password in a lookup data structure.

- It can process hundreds of hash lookups per second.

4. Reverse Lookup tables

- A lookup table that maps each password hash from the compromised user account database to a list of users who had that hash.

## Salting

- The advantage of lookup tables and rainbow tables is the exact hash is used to compare against the password hashes, it can be avoided by randomizing each hash. So, hash of two passwords will never be the same.
- Ranomization is nothing but appending or prepending a string called _Salt_ to the password before hashing.
- The salt is usually stored in the user's db or it is mostly part of the hash itself.

## Wrong implementations of Salt

- Usage of same salt in each hash, a new random salt must be generated each time a user creates an account or changes thier password.
- The salt should be short, an ideal size would be size of the hash and the salt should be same.
- Never combine multiple hash functions with the notion that it would make the password more secure, in reality it offers little benefit. Also, it sometimes lead to less secure hash functions.

## How to Hash

- Salt should be generated using a _Crytpgraphically Secure Pseudo-Random Number Generator_, since they provide high level of randomness and are completely unpredictable. _os.urandom_ for python
- The salt needs to be unique per user per password.
- Always hash on the server

## Resources

[Salted Hashing - Doing it right](https://www.codeproject.com/Articles/704865/Salted-Password-Hashing-Doing-it-Right)
