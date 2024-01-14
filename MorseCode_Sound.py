import time
from playsound import playsound

morse = {'a': '._', 'b': '_...', 'c': '_._.', 'd': '_..', 'e': '.', 'f': '.._.', 'g': '__.', 'h': '....', 'i': '..', 'j': '.___',  'k': '_._', 'l': '._..', 'm': '__', 'n': '_.', 'o': '___', 'p': '.__.', 'q': '__._', 'r': '._.', 's': '...', 't': '_', 'u': '.._', 'v': '..._', 'w': '.__', 'x': '_.._', 'y': '_.__', 'z': '__..', '1': '.____', '2':'..___', '3': '...__', '4': '...._', '5': '.....', '6': '_....', '7': '__...', '8': '___..', '9': '____.', '0': '____'}

def decode(user):
    for i in user.lower():
        time.sleep(.5)
        if i == ' ':
            print('/', end=' ') 
        elif i in morse.keys():
            print(morse[i], end=' ')
            for j in morse[i]:
                if j == ".":
                    playsound('audio/morse_E.wav')
                else:
                    playsound('audio/morse_T.wav')
        else:
            print("Hein ji??")

    print()

def code(user):    
    for i in user.split():
        if i == '/':
            print(' ', end ='')
        for keys, values in morse.items():
            if i == values:
                print(keys.upper(), end='')
    print()
    
def main():
    count = 0
    agr = 0
    while True:
        print("\n1. For English to Morse")
        print("2. For Morse to English")
        print("3. Quit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            count = 0
            user = input("Please enter you english sentance/word: ")
            decode(user)
        elif choice == 2:
            count = 0
            user = input("Please enter you morse code: ")
            code(user)
        elif choice == 3:
            print("Exiting the program!!!")
            break
        else:
            count += 1
            if count == 5:
                print("You've reached the maximum amounst to attemps please restart the program!")
                break
            else:
                print("\nOOPS! Wrong input\nPlease try again and Enter the right input......\n")
                continue            
        
            
        ch = input("Want to continue(Y/N): ")
        
        if ch.upper() == 'N':
            break    


if  __name__ == "__main__":
    main()