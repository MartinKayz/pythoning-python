﻿secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = int(input("Enter your guessing number: "))

while number != secret_number:
    print("Ha ha! You\'re stuck in my loop!")
    
    number = int(input("Enter your guessing  number: "))
    
    if number ==secret_number:
        print(str(secret_number), " Well done, muggle! You are free now.")
        
