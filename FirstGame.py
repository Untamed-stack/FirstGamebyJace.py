print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name,  "You are", age, "years old")

health: int = 10

if age >= 18:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? (Yes/No): ").lower()
    if wants_to_play == "yes":
        print("Let's play!")
        print('You are starting with', health, "health")

        weapon = input("First choice: Choose a weapon: (Sword/Wooden Bat/Gun): ").lower()
        if weapon == "sword":
            print("You are ready to go!")
        elif weapon == "wooden bat":
            print ("A little shaky but solid choice!")
        elif weapon == "gun":
            print("Smart Choice... Only if you know how to cover your tracks.")
        else:
            print("Please pick one of the 3 weapons listed!")
        left_or_right = input("You had come across two different path, which do you choose? Left or Right (Left/Right): ").lower()
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around (Across/Around)? ").lower()
            if ans == "around":
                    print("You went around and reached the other side of the lake. ")
            elif ans == "across":
                    print("As you approach the lake, You saw a huge fish jumping out of the water! Use your weapon to defeat the fish: ")
                    print("You pulled out your", weapon)
                    if weapon == "sword":
                        print("You stabbed the fish in the head")
                    elif weapon == "wooden bat":
                        print("You bashed the fish head in but the baseball bat is now broken!")
                    elif weapon == "gun":
                        print("You shot the fish in the head! Solid move")
        else:
            print("You went the wrong way. Turn around!")


        river_or_house = input("You noticed a house and a river, which do you go to (River/House)? ").lower()
        if river_or_house == "house":
            print("You go to the house and was greeted by the owner... He offered coffee.")

            accept = input("Do you accept? (Yes/No) ").lower()
            if  accept == "yes":
                print("The coffee was poisoned, you lost 5 health")
                health -= 5
            elif accept == "no":
                print("Good Choice... The old man went into the kitchen.")

            Stay_or_Leave = input("The vibe inside the house began to feel tense. Do you stay or leave? (Stay/Leave) ").lower()
            if Stay_or_Leave == "stay":
                print("You are about to get in a fight with the old man. Get ready! ")

                action = input("Do you engage in the duel? (Yes/No) ").lower()
                if action == "yes":
                    print("You lost the duel against the old man! Game Over!")
            else:
                print("You left the house and survived! you won the game!")
        else:
            print("you fell down the river... Game Over!!")

    else:
        print("Cya!!")
else:
    print("You are not old enough to play this game, BYE!")







