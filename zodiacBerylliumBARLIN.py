birth_year = 0                                                              # Variables to be used in the program
zodiac_number = 0
zodiac_sign = ""


print()
print("Welcome !!! ")
print("This is a code to check what your Chinese Zodiac Sign is !")         # Short introduction
print()


while birth_year < 1900:                                                    # Loop to retry until the user inputs a valid input

    print()                                             #spacing
    birth_year = int(input("Enter your birth year: "))                      # Ask for the user's year of birth

    if birth_year < 1900:                                                   # if function to check if user's input is invalid for the loop to retry                          
        print("="*50)
        print(" Invalid Year, it should not be earlier than 1900")              
        print(" Please enter your birth year again.")                       
        print("="*50)
        print()

    
zodiac_number = (birth_year - 1900) % 12                                    # Calculates the zodiac number 

if zodiac_number == 0:                                                      
    zodiac_sign = "Rat (鼠 / Shǔ)"
elif zodiac_number == 1:
    zodiac_sign = "Ox (牛 / Niú)"
elif zodiac_number == 2:
    zodiac_sign = "Tiger (虎 / Hǔ)"
elif zodiac_number == 3:
    zodiac_sign = "Rabbit (兔 / Tù)"
elif zodiac_number == 4:
    zodiac_sign = "Dragon (龙 / Lóng)"
elif zodiac_number == 5:
    zodiac_sign = "Snake (蛇 / Shé)"
elif zodiac_number == 6:                                                    #Categorizes zodiac number to zodiac sign
    zodiac_sign = "Horse (马 / Mǎ)"
elif zodiac_number == 7:
    zodiac_sign = "Goat (羊 / Yáng)"
elif zodiac_number == 8:
    zodiac_sign = "Monkey (猴 / Hóu)"
elif zodiac_number == 9:
    zodiac_sign = "Rooster (鸡 / Jī)"
elif zodiac_number == 10:
    zodiac_sign = "Dog (狗 / Gǒu)"
elif zodiac_number == 11:
    zodiac_sign = "Pig (猪 / Zhū)"

print("="*52)
print(f"  Your Chinese Zodiac Sign is : {zodiac_sign}")                       # Final output for your Chinese Zodiac Sign
print("="*52)
    
    


