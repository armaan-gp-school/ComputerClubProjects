import random

moneyTalks = 100.00  # Start with a float for proper rounding

print("Welcome to the Jackpot Spinner!")
ye_or_ne = input("Do you want to play? (Y/N)").lower().strip()

def input_checker(value):
    while True:
        try:
            value = float(value)
            if value < 0:
                print("Invalid input. Please enter a number greater than 0.")
                return False
            return True
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return False

values = ["   7  ", "Banana", "  Bar ", " Apple"]

def display_slots(slot1, slot2, slot3):
    print(" ________________________________")
    print("|                                |")
    print(f"|  {slot1}  |  {slot2}  |  {slot3}  |")
    print("|________________________________|\n")

def main():
    print("You can choose the amount of money you want to gamble.")
    print("1) If 2 of the three slots match then you lose a quarter of your money\n2) If 0 slots match then you lose half of your money\n3) If all 3 of the slots match then you multiply your money by 10!\n4) If all 3 of your slots are 7 then you multiply your money by 100!")
    money = moneyTalks
    while True:
        def picker(money2):
            decision1 = random.choices(values, weights=[1, 2, 3, 2], k=1)[0]
            decision2 = random.choices(values, weights=[1, 2, 3, 2], k=1)[0]
            decision3 = random.choices(values, weights=[1, 2, 3, 2], k=1)[0]
           
            # Display the slots
            display_slots(decision1, decision2, decision3)

            if decision1 == "7" and decision2 == "7" and decision3 == "7":
                print("YOU GOT THE LEGENDARY ALL 7s!")
                print("You just multiplied your gambling money by 100!")
                money2 = money2 * 100
                return f"+{round(money2, 2)}"
            elif decision1 == decision2 and decision2 == decision3:
                print("Winner winner chicken dinner!")
                print("You just multiplied your gambling money by 10!")
                money2 = money2 * 10
                return f"+{round(money2, 2)}"
            elif decision1 == decision2 or decision1 == decision3 or decision2 == decision3:
                print("You lost! Say good bye to a quarter of your gambling money!")
                money2 = money2 - (money2 / 4)
                return f"-{round(money2, 2)}"
            else:
                print("You lost! Say good bye to half of your gambling money!")
                money2 = money2 - (money2 / 2)
                return f"-{round(money2, 2)}"

        print(f"You have: ${round(money, 2)}")
   
        yah_or_nah = input("How much money do you want to gamble? ")
        if not input_checker(yah_or_nah): continue
        yah_or_nah = float(yah_or_nah)

        # Check if the gamble amount is greater than the current money
        if yah_or_nah > money:
            print(f"You cannot gamble more than you have! You currently have ${round(money, 2)}.")
            continue
       
        result = picker(yah_or_nah)
        print(result)

        # Update the money based on the result
        if result.startswith("+"):
            money += float(result[1:])  # Add the winnings
        else:
            money -= float(result[1:])  # Subtract the losses

        money = round(money, 2)  # Round the money after updating

        if money <= 0:
            print("You have 0 dollars, GAME OVER")
            break
        else:
            continue
       

if ye_or_ne == "y":
    print("Let's Go!")
    main()
elif ye_or_ne == "n":
    print("Ok, bye!")
else:
    print("That is not an option.")