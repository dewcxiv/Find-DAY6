print(r'''
             _
            /;)
           /;(
           >_/
           |-|
           |-|
           |-|
           |-|
           |-|
           |-|
           |-|
       _   |-|
      / \  |-|   _
     :   `'|-|  /,\
     :   ,`'-'`'/|:
      \  \ ...   ;/
       :  )...  ::
       ; / ...  ::
      / /  ___   \\
     :  `-|||||.  \:
     :        (\`-';
      `._________,'
''')
print("Where\'s is DAY6?")
print("Your mission is to find the member.")
choice1 = input('You\'re at a crossroad, where do you want to go?'
                'Type "left" or "right".').lower()

if choice1 == "right":
    choice2 = input('You see a stairs.'
                    'Shall we go to the 4th floor or go to basement?'
                    'Type "Up".'
                    'Type "basement".').lower()
    if choice2 == "basement":
        choice3 = input("You arrive at the basement. "
                        "There is a door with 3 different colors, one green. "
                        "one black, one red."
                        "Which colour do you choose?").lower()
        if choice3 == "green":
            print("It's DAY6!! They are practicing for their next concert."
                  "If you are here that mean you will get a seat for their next concert!! YAY<3")
        elif choice3 == "yellow":
            print("Uh-oh! someone is here but it's not DAY6! "
                  "it's TWICE you are good, but we are here to find DAY6=_= Game Over")
        elif choice3 == "red":
            print("You enter JYP auditions, you will never meet DAY6. Game Over")
        else:
            print("You choose to leave the building. Game Over.")
    else:
       print("You got caught by JYP and became a trainee by foce. Game Over.")
else:
    print("You see ice cream and forgot to find DAY6. Game Over. ")