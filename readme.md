#PassCheck

A simple python tool for password security. Np installs needed, just python 3.

#What it does
1. Check Strength: scores a password out of 5 and gives tips.
2. Check Breaches: uses the Have I Been Pwned API to see if the password was leaked. Only the first 5 characters of the password's SHA-1 hash are sent (k-anonymity), so the real password never leaves your computer.
3. Generate: makes a random password with Python's 'secrets' module.
   
#Run it

python PassCheck.py

#What I learned

1. How k-anonymity lets you check breaches privately
2. Why 'secrets' is safer than 'random' for passwords
3. Why long passwords with mixed characters are stronger
