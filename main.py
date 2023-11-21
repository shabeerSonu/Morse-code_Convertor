# dict of all letters, numbers and symbols to morse
letter_to_morse = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
                   "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
                   "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",  "x": "-..-",
                   "y": "-.--", "z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
                   "5": ".....", "6": "-....", "7": "-....", "8": "---..", "9": "----.", "!": "-.-.--", "@": ".--.-.",
                   "&": ".-...", "(": "-.--.", ")": "-.--.-", "+": ".-.-.", "=": "-...-", ":": "---...", ",": "--..--",
                   "?": "..--..", "/": "-..-.", "'": ".----.", '"': '.-..-.'}

string = []
invalid = False

# Taking input from user and converting to list.
user_sentence = list(input("Enter the sentence to translate to morse code:\n").lower())


# changing user string to morse.
for letter in user_sentence:
    if letter in letter_to_morse:
        string.append(letter_to_morse[letter])
    elif letter == " ":
        string.append("/")
    else:
        print(f"Invalid Character '{letter}'.")
        invalid = True
        break

# joining the morse code to a single string.
result = " ".join(string)

# printing output if valid.
if not invalid:
    print(result)
