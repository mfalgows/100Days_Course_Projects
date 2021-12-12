MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

MORSE_CODE_REVERSED = {value: key for key, value in MORSE_CODE_DICT.items()}

print('''

███╗░░░███╗░█████╗░██████╗░░██████╗███████╗  ░█████╗░░█████╗░██████╗░███████╗
████╗░████║██╔══██╗██╔══██╗██╔════╝██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██╔════╝
██╔████╔██║██║░░██║██████╔╝╚█████╗░█████╗░░  ██║░░╚═╝██║░░██║██║░░██║█████╗░░
██║╚██╔╝██║██║░░██║██╔══██╗░╚═══██╗██╔══╝░░  ██║░░██╗██║░░██║██║░░██║██╔══╝░░
██║░╚═╝░██║╚█████╔╝██║░░██║██████╔╝███████╗  ╚█████╔╝╚█████╔╝██████╔╝███████╗
╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝  ░╚════╝░░╚════╝░╚═════╝░╚══════╝

░█████╗░░█████╗░███╗░░██╗██╗░░░██╗███████╗██████╗░████████╗███████╗██████╗░
██╔══██╗██╔══██╗████╗░██║██║░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██║░░╚═╝██║░░██║██╔██╗██║╚██╗░██╔╝█████╗░░██████╔╝░░░██║░░░█████╗░░██████╔╝
██║░░██╗██║░░██║██║╚████║░╚████╔╝░██╔══╝░░██╔══██╗░░░██║░░░██╔══╝░░██╔══██╗
╚█████╔╝╚█████╔╝██║░╚███║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║
░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝''')

print('\nWelcome to the Morse Code Converter.\nWould you like to convert text to Morse Code or Unscramble it?')
choice1 = input('Convert(c) or Unscramble(u)?').lower()

while choice1 != 'convert' and choice1 != 'unscramble' and choice1 != 'u' and choice1 != 'c':
    print('Please type Convert or Unscramble or C/U for your choice')
    choice1 = input('Please try again\n').lower()

while choice1 != 'exit':
    if choice1 == 'convert' or choice1 == 'c':
        text_to_convert = input('What text do you want to convert to Morse Code?:').upper()
        list_to_convert = []
        for i in text_to_convert:
            if i != ' ':
                list_to_convert.append(MORSE_CODE_DICT[i])
        converted_string = ' '.join(list_to_convert)
        print(converted_string)
        list_to_convert.clear()
        choice1 = input('Type Exit to quit, C to Convert again or U to Unscramble').lower()

    elif choice1 == 'unscramble' or choice1 == 'u':
        text_to_unscramble = input('Input Morse Code you wish to unscramble:')
        list_to_unscramble=text_to_unscramble.split(' ')
        unscrambled_list=[]
        for i in list_to_unscramble:
            unscrambled_list.append(MORSE_CODE_REVERSED[i])
        unscrambled_string=''.join(unscrambled_list)
        print(unscrambled_string)
        list_to_unscramble.clear()
        choice1 = input('Type Exit to quit, C to Convert again or U to Unscramble').lower()

    elif choice1=='exit' or choice1=='e':
        break
