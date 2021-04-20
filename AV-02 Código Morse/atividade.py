Morse = {"a": ".-",
         "b": "-...",
         "c": "-.-.",
         "d": "-..",
         "e": ".",
         "f": ".._.",
         "g": "--.",
         "h": "....",
         "i": "..",
         "j": ".---",
         "k": "-.-",
         "l": ".-..",
         "m": "--",
         "n": "-.",
         "o": "---",
         "p": ".--.",
         "q": "--.-",
         "r": ".-.",
         "s": "...",
         "t": "-",
         "u": "..-",
         "v": "...-",
         "w": ".--",
         "x": "-..-",
         "y": "-.--",
         "z": "--..",
         "0": "-----",
         "1": ".----",
         "2": "..---",
         "3": "...--",
         "4": "....-",
         "5": ".....",
         "6": "-....",
         "7": "--...",
         "8": "---..",
         "9": "----.",
         " ": " "}

print ("Codificando a Frase:")
FraseEscolhida = input("Escreva o que você quer traduzir pra código morse: ")
FraseEmCodigo = ''

for x in FraseEscolhida:
        if x.lower() in Morse:
            FraseEmCodigo += Morse[x.lower()]

print("Frase Escolhida: ", FraseEscolhida)  
print("Frase em Código: ", FraseEmCodigo)
         