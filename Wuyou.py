import time
import random


ores = [
    "COPPER",
    "BRONZE",
    "CALCITE",
    "AMBER",
    "IRON",
    "AVENTURINE",
    "LAPIS LAZULI",
    "QUARTZ",
    "JADE",
    "SILVER",
    "AMETHYST",
    "MOONSTONE",
    "TOURMALINE",
    "AGATE",
    "GOLD",
    "PLATINUM",
    "TITANIUM",
    "SAPPHIRE",
    "SMOKY QUARTZ",
    "EMERALD",
    "RUBY",
    "JADEITE",
    "DIAMOND",
    "MYTHRIL",
    "ADAMANTINE"
]

ore_prices = {
    "COPPER": "$4.76/lb",
    "BRONZE": "$2.50/lb",
    "CALCITE": "$2/lb - $40/lb",
    "AMBER": "Estimated $2/lb - $200/lb",
    "IRON": "$0.04/lb",
    "AVENTURINE": "$5/carat - $100+/carat",
    "LAPIS LAZULI": "$1/carat - $100+/carat",
    "QUARTZ": "$1/carat - $4/carat",
    "JADE": "$5/carat - $150+/carat",
    "SILVER": "$277.45/Troy lb",
    "AMETHYST": "$20/carat - $50+/carat",
    "MOONSTONE": "$20/carat - $125+/carat",
    "TOURMALINE": "$1/carat - $700+/carat",
    "AGATE": "$1/carat - $200+/carat",
    "GOLD": "$39,818/Troy lb",
    "PLATINUM": "$10,642/Troy lb",
    "TITANIUM": "$20/Troy lb",
    "SAPPHIRE": "$25/carat - $11000+/carat",
    "SMOKY QUARTZ": "$1/carat - $20+/carat",
    "EMERALD": "$1/carat - $100,000+/carat",
    "RUBY": "$1/carat - $100,000+/carat",
    "JADEITE": "$50/carat - $30,000+/carat",
    "DIAMOND": "$1,000/carat - $220,000+/carat",
    "MYTHRIL": "N/A",
    "ADAMANTINE": "N/A"
}

ore_descr = {
    "COPPER": "Copper is a soft, malleable, and ductile metal "
    "with very high thermal and electrical conductivity.",
    "BRONZE": "Bronze is an alloy consisting primarily of copper, "
    "commonly with about 12–12.5% tin and often with the addition "
    "of other metals (including aluminium, manganese, nickel, or zinc) "
    "and sometimes non-metals (such as phosphorus) or metalloids "
    "(such as arsenic or silicon).",
    "CALCITE": "Calcite is a common carbonate mineral that is widespread "
    "and found in many crystal shapes and colors. It is typically colorless "
    "or white, however impurities can color calcite shades of red, yellow, "
    "orange, green, blue, purple, brown and black, and "
    "it can be multicolored or banded.",
    "AMBER": "Amber is fossil tree resin that has achieved a stable state "
    "through loss of volatile constituents and chemical change after burial "
    "in the ground. Amber occurs as irregular nodules, rods, "
    "or droplike shapes in all shades of yellow with nuances of "
    "orange, brown, and, rarely, red.",
    "IRON": "Iron is a chemical element; it has symbol Fe and atomic number "
    "26. It is, by mass, the most common element on Earth, forming much of "
    "Earth's outer and inner core.",
    "AVENTURINE": "Aventurine is a form of quartzite, characterised by its "
    "translucency and the presence of platy mineral inclusions that give "
    "it a shimmering or glistening effect termed aventurescence.",
    "LAPIS LAZULI": "Lapis lazuli, or lapis for short, is a deep-blue "
    "metamorphic rock that has been prized since antiquity for its intense "
    "color. Lapis lazuli is a rock composed primarily of the minerals "
    "lazurite, pyrite and calcite.",
    "QUARTZ": "Quartz is the second most abundant mineral in Earth's "
    "crust. It occurs in nearly all acid igneous, "
    "metamorphic, and sedimentary rocks.",
    "JADE": "Jade is often referred to by either of two different "
    "silicate mineral names: nephrite, or jadeite. The more highly "
    "prized of the two jadestones is jadeite; the other is nephrite.",
    "SILVER": "Silver is a chemical element; it has symbol Ag and "
    "atomic number 47. A soft, white, lustrous transition metal, it "
    "exhibits the highest electrical conductivity, thermal conductivity, "
    "and reflectivity of any metal.",
    "AMETHYST": "Amethyst usually is a transparent variety of quartz that "
    "comes in shades of purple. Some translucent to opaque amethyst is also "
    "found and the purplish zones alternate with white or grayish areas.",
    "MOONSTONE": "Moonstone is a sodium potassium aluminium silicate of "
    "the feldspar group that displays a pearly and opalescent schiller.",
    "TOURMALINE": "Tourmaline is a crystalline silicate mineral group in "
    "which boron is compounded with elements such as aluminium, iron, "
    "magnesium, sodium, lithium, or potassium. This gemstone comes in a "
    "wide variety of colors.",
    "AGATE": "Agate is a banded variety of chalcedony. Agate stones "
    "are characterized by alternating bands of different colored "
    "chalcedony and sometimes include macroscopic quartz.",
    "GOLD": "Gold is a chemical element; it has chemical symbol Au "
    "and atomic number 79. In its pure form, it is a bright, slightly "
    "orange-yellow, dense, soft, malleable, and ductile metal.",
    "PLATINUM": "Platinum is one of the least reactive metals. It "
    "has remarkable resistance to corrosion, even at high temperatures, "
    "and is therefore considered a noble metal.",
    "TITANIUM": "Titanium is a chemical element; it has symbol Ti and "
    "atomic number 22. Found in nature only as an oxide, it can be reduced "
    "to produce a lustrous transition metal with a silver color, low density, "
    "and high strength, resistant to corrosion.",
    "SAPPHIRE": "Sapphire is a precious gemstone, a variety of the mineral "
    "corundum, consisting of aluminium oxide with trace amounts of "
    "elements such as iron, titanium, cobalt, lead, chromium, vanadium, "
    "magnesium, boron, and silicon.",
    "SMOKY QUARTZ": "Smoky quartz is a brownish grey, translucent variety "
    "of quartz that ranges in clarity from almost complete transparency to "
    "an almost-opaque brownish-gray or black crystals. The color of smoky "
    "quartz is produced when natural radiation, emitted from the "
    "surrounding rock, activates color centers around aluminum impurities "
    "within the crystalline quartz.",
    "EMERALD": "Emerald is the bluish green to green variety of beryl, "
    "a mineral species that includes aquamarine. Highly saturated green "
    "color defines high quality emerald.",
    "RUBY": "Ruby is a pinkish-red to blood-red-colored gemstone, a "
    "variety of the mineral corundum. Ruby is one of the most popular "
    "traditional jewelry gems and is very durable.",
    "JADEITE": "Jadeite is one of the two types of jade, know for being "
    "more expensive than nephrite for its deep green hues",
    "DIAMOND": "Diamond is a solid form of the element carbon with "
    "its atoms arranged in a crystal structure called diamond cubic. "
    "Diamond as a form of carbon is tasteless, odourless, strong, brittle "
    "solid, colourless in pure form, a poor conductor of electricity, and "
    "insoluble in water. Diamond has the highest hardness and thermal "
    "conductivity of any natural material, properties that are used in "
    "major industrial applications such as cutting and polishing tools.",
    "MYTHRIL": "N/A",
    "ADAMANTINE": "N/A"
}


# --------------- functions begin here


def welcome():
    num_delay = random.randint(2, 4)
    time.sleep(1)
    print("          -+-")
    time.sleep(.25)
    print("        *     *")
    time.sleep(.25)
    print("     *   .       *")
    time.sleep(.25)
    print("   /         .     \\")
    time.sleep(.25)
    print("  *    .          . *")
    time.sleep(.25)
    print(" *   Welcome to the  *")
    time.sleep(.5)
    print("{ .       ORE    .    }")
    time.sleep(.5)
    print(" *  .  INSPECTOR     *")
    time.sleep(.25)
    print("  *        .        *")
    time.sleep(.25)
    print("   \\ .       .     /")
    time.sleep(.25)
    print("     *           *")
    time.sleep(.25)
    print("        * .   *")
    time.sleep(.25)
    print("          -+-")
    print(" ")
    print(" ")
    time.sleep(1)
    print("    / ------------- \\")
    print("   [ Loading  Assets ]")
    print("    \\ ------------- /")
    time.sleep(1)
    print(" ")
    print(" ")
    for dashes in range(num_delay):
        # making this delay a bit quicker
        print("           ...")
        print(" ")
        time.sleep(.5)
    time.sleep(1)
    print(" ")
    print(" ")

def selectOre():
    """Asking for what ore the user wants to inspect"""
    while True:
            place_valid = False
            while not place_valid:
                # asking for the place
                print("___________________________________")
                print("                                   ")
                target = input("What ore would you like to inspect?\n"
                              "For the list of ores, enter ' ? '\n"
                              ).upper().strip()
                # checking for correct values
                if target.isalpha() or target == "?" or target in ores:
                    if target not in ores and target != "?":
                        print("\nMake sure the input is "
                              "a valid ore or ' ? '.")
                        print(" ")
                    else:
                        if target == "?":
                            print(" ")
                            print("_____________")
                            print(" ")
                            for ore in ores:
                                print(f"-{ore.lower().capitalize()}")
                            print("_____________")
                            print(" ")
                            print(" ")
                        else:
                            showOre(target)
                            printOre(target)
                        # this value changes no matter what
                        place_valid = True
                # more checking
                else:
                    print("\nMake sure the input is a valid option.")
                    print(" ")
            continue

def printOre(item):
    print(f"Price: {ore_prices[item]}\n")
    print(f"{ore_descr[item]}\n")

    print(" ")
    print(" ")

def showOre(ore):
    print(" ")
    print(" ")
    if ore in [ores[0], ores[1], ores[2], ores[3]]:
        if ore == ores[0]:
            print("     _")
            print("   /  **\\")
            print(" /\\*  *  \\")
            print("*  ***  * | ")
            print("\\____/\\__/ ")
        elif ore == ores[1]:
            print("     ___")
            print("   /     \\")
            print(" /\\       \\")
            print("|          | ")
            print(" \\____/\\__/ ")
        elif ore == ores[2]:
            print("     ___")
            print("   /=====\\")
            print(" /\\=======\\")
            print("|==========| ")
            print(" \\____/\\__/ ")
        elif ore == ores[3]:
            print("     ___")
            print("   /=-=-=\\")
            print(" /\\-=-=-=-\\")
            print("|=-=-=-=-=-| ")
            print(" \\____/\\__/ ")
    elif ore in [ores[5], ores[6], ores[8]]:
        if ore == ores[5]:
            print("    ( /-\\ )")
            print("    |/---\\|    ")
            print("   <*  *  *>      ")
            print("    |\\---/|   ")
            print("    ( \\-/ )")
        elif ore == ores[6]:
            print("   +{ /-\\ }+")
            print("   | /---\\ |    ")
            print("  <-*  *  *->      ")
            print("   | \\---/ |   ")
            print("   +{ \\-/ }+")
        else:
            print("   /{*/-\\*}\\")
            print("  |- /---\\ -|    ")
            print("  <-*  *  *->      ")
            print("  |- \\---/ -|   ")
            print("   \\{*\\-/*}/")
    elif ore in [ores[4], ores[9], ores[14], ores[15], ores[16]]:
        if ore == ores[4]:
            print("    ________________________")
            print("  / \\    *     #     ###    \\")
            print(" / # \\  ##   *WROUGHT*   #  #\\")
            print(" \\   *\\_______________________\\")
            print("  \\ * /     ###    *  #   ##  /")
            print("   \\_/_______________________/")
        elif ore == ores[9]:
            print("    ________________________")
            print("  / \\    *           * *    \\")
            print(" / * \\  *    *STERLING*     *\\")
            print(" \\   *\\_______________________\\")
            print("  \\ * /      *     *      **  /")
            print("   \\_/_______________________/")
        elif ore == ores[14]:
            print("    ________________________")
            print("  / \\                       \\")
            print(" /   \\         *24K*         \\")
            print(" \\    \\_______________________\\")
            print("  \\   /                       /")
            print("   \\_/_______________________/")
        elif ore == ores[15]:
            print("    ________________________")
            print("  /-\\- - - - - - - - - - - -\\")
            print(" /- -\\- - - - *NOBLE* - - - -\\")
            print(" \\- - \\_______________________\\")
            print("  \\- -/- - - - - - - - - - - -/")
            print("   \\_/_______________________/")
        else:
            print("    ________________________")
            print("  /_\\_______________________\\")
            print(" /___\\_______*LUSTROUS*______\\")
            print(" \\____\\_______________________\\")
            print("  \\___/_______________________/")
            print("   \\_/_______________________/")
    elif ore in [ores[7], ores[10], ores[12], ores[18], ores[24]]:
        if ore == ores[7]:
            print("     ^")
            print("    / \\")
            print("   /  |\\")
            print("  /   | \\")
            print(" /|   |  \\")
            print("| |   |   |")
            print("| |   |   |")
            print("| |   |   |")
            print(" \\|___|/\\_|")
        elif ore == ores[10]:
            print("     ^")
            print("    /+\\")
            print("   /++|\\")
            print("  /+++|+\\")
            print(" /|+++|++\\")
            print("|+|+++|+++|")
            print("|+|+++|+++|")
            print("|+|+++|+++|")
            print(" \\|___|/\\_|")
        elif ore == ores[12]:
            print("   _____")
            print("  /###|#\\")
            print(" /| ##|##\\")
            print("|#|# #|###|")
            print("|#|###|# #|")
            print("|#| ##|# #|")
            print(" \\|___|/\\_|")
        elif ore == ores[18]:
            print("    ___")
            print("   /##|\\       __")
            print("  /###| \\     /|#\\")
            print(" /|###|  \\   / |##\\")
            print("| |###|   |_/  |###\\")
            print("| |###|   |    |####|")
            print("| |###|   |    |###/")
            print(" \\|___|/\\_|____|__|")
        else:
            print("                     ^")
            print("                    / \\")
            print("                   / /#\\")
            print("                  / /_##\\")
            print("     ^           / /___##\\")
            print("    /_\\         / /____###\\")
            print("   /__|\\       / /_____###|\\")
            print("  /___|_\\     / /|______##|#\\")
            print(" /|___|__\\   | /_|_______#|##|")
            print("|_|___|___|_/_/__|________|##|")
            print("|_|___|___|______|________|_#|")
            print("|_|___|___|______|________|__|")
            print(" \\|___|___|______|________|_/")
            print("  \\___|___|______|________|/")
            print("   \\__|___|______|________/")
            print("    |__/\\_/\\____/\\__/\\___/")
    elif ore in [ores[11], ores[13], ores[21]]:
        if ore == ores[11]:
            print("            ***")
            print("         ***/-\\***")
            print("      ***  /   \\  ***")
            print("    **    /     \\    **")
            print("  <*     |   *   |     *>")
            print("    **    \\     /    **")
            print("      ***  \\   /   ***")
            print("         ***\\-/***")
            print("            ***")
        elif ore == ores[13]:
            print("            ***")
            print("         ***/-\\***")
            print("      ***/ /   \\ \\***")
            print("    **  / /     \\ \\  **")
            print("  <*   | |  {+}  | |   *>")
            print("    **  \\ \\     / /  **")
            print("      ***\\ \\   / /***")
            print("         ***\\-/***")
            print("            ***")
        else:
            print("            ***")
            print("         ***/-\\***")
            print("      ***/-/ | \\-\\***")
            print("    **  /-/  |  \\-\\  **")
            print("  <*---|-|--{=}--|-|---*>")
            print("    **  \\-\\  |  /-/  **")
            print("      ***\\-\\ | /-/***")
            print("         ***\\-/***")
            print("            ***")
    elif ore == ores[22]:
        print(" ________")
        print("< \\/\\/\\/ >")
        print("  \\\\/\\//")
        print("   \\\\//")
        print("    \\/")
    elif ore in [ores[17], ores[19], ores[20]]:
        if ore == ores[17]:
            print("     /------------\\")
            print("    / /          \\ \\")
            print("   / /    ----    \\ \\")
            print("  | |     |<>|     | |")
            print("   \\ \\    ----    / /")
            print("    \\ \\          / /")
            print("     \\------------/")
        elif ore == ores[19]:
            print("     /------------\\")
            print("    / /    /\\    \\ \\")
            print("   / /    /||\\    \\ \\")
            print("  | |   < |<>| >   | |")
            print("   \\ \\    \\||/    / /")
            print("    \\ \\    \\/    / /")
            print("     \\------------/")
        else:
            print("     /------------\\")
            print("    / / }- /\\ -{ \\ \\")
            print("   / / }- /||\\ -{ \\ \\")
            print("  | | }-<=|++|=>-{ | |")
            print("   \\ \\ }- \\||/ -{ / /")
            print("    \\ \\ }- \\/ -{ / /")
            print("     \\------------/")
    else:
        print("         *         *         *")
        print("        ***       ***       ***")
        print("       *****     *****     *****")
        print("      *******   *******   *******")
        print("     ********* ********* *********")
        print("    *******************************")
        print("    *******************************")
        print("    *******************************")
        print("       *************************")
        print("          *******************")
        print("             *************")
        print("                *******")
        print("                   *")
    print(" ")
    print(" ")

def main():
    welcome()
    selectOre()

if __name__ == "__main__":
    main()