# LAB - Class 18
## Project: Caesar's Cipher
### Author: Brendon and Brian
### Links and Resources
- [back-end server url](#) (when applicable)
- [front-end application](#) (when applicable)
### Setup
`.env` requirements (where applicable)

**i.e.**

- `PORT` - Port Number
- `DATABASE_URL` - URL to the running Postgres instance/db
#### How to initialize/run your application (where applicable)
- run file [Caesar Cipher](ceasar_cypher.py) in your terminal
- e.g. `python ceasar_cypher.py`
#### How to use your library (where applicable)
- this library is used to to encrypt and the decrypt a secret message. 
#### Tests
- How do you run tests?
- in the main root directory run ***Pytest*** 
- Any tests of note?
  - I am very proud of my tests that test for if the shift is working
    - checkout my [Test](./tests/test_clock_queue.py) file
- I built out an entirely new queue that will handle a cipher. it will encrypt and then decrypt if you know the key
  - I built tests to test for if the shifts work
- Describe any tests that you did not complete, skipped, etc