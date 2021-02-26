from Shift15.Restart_Function import confirm_restart

Encrypt = {"a": "P", "b": "Q", "c": "R", "d": "S", "e": "T", "f": "U", "g": "V", "h": "W", "i": "X", "j": "Y",
           "k": "Z", "l": "A", "m": "B", "n": "C", "o": "D", "p": "E", "q": "F", "r": "G", "s": "H", "t": "I",
           "u": "J", "v": "K", "w": "L", "x": "M", "y": "N", "z": "O", "A": "p", "B": "q", "C": "r", "D": "s",
           "E": "t", "F": "u", "G": "v", "H": "w", "I": "x", "J": "y", "K": "z", "L": "a", "M": "b", "N": "c",
           "O": "d", "P": "e", "Q": "f", "R": "g", "S": "h", "T": "i", "U": "j", "V": "k", "W": "l", "X": "m",
           "Y": "n", "Z": "o", " ": " ", "1": "4", "2": "5", "3": "6", "4": "7", "5": "8", "6": "9", "7": "0",
           "8": "1", "9": "2", "0": "3", ".": ",", ",": "."}

Decrypt = {v: k for k, v in Encrypt.items()}


def check(answer):
    while True:
        if answer.strip() in "encrypt":
            message = str(input("Please enter the code you'd like to encrypt: "))
            encrypt_check = all(c in Encrypt for c in message)
            if encrypt_check is False:
                print("Invalid input. Please try again.")
                continue
            else:
                break

        else:
            message = input("Please enter the code you'd like to decrypt: ")
            decrypt_check = all(c in Decrypt for c in message)
            if decrypt_check is False:
                print("Invalid input. Please try again.")
                continue
            else:
                break

    return message


class FinalCode:
    def __init__(self, answer, message):
        self.answer = answer
        self.message = message

    def cryptocode(self):
        result = ""
        if self.answer.lower() == "encrypt":
            for e in self.message:
                result += Encrypt[e]
        elif self.answer.lower() == "decrypt":
            for r in self.message:
                result += Decrypt[r]
        return result


print("Please type only letters, numbers, spaces and commas/periods.")

while True:
    def en_or_de():
        while True:
            answer = input("Would you like to encrypt or decrypt a message? Please type encrypt or decrypt: ")
            answer1 = answer.strip().lower()
            if answer1 in ["encrypt", "decrypt"]:
                break
            print("Invalid input. Please try again.")
        return answer1
    FC = FinalCode(en_or_de(), check(""))
    print("Your message translates into: ", FC.cryptocode())

    if "yes" in confirm_restart():
        print("The program has reset.")
        continue
    else:
        break
