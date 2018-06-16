alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
types = {1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', 2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE', 3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO', 4: 'ESOVPZJAYQUIRHXLNFTGKDCMWB', 5: 'VZBRGITYUPSDNHLXAWMJQOFECK'}
rtypes = {'A': 'EJMZALYXVBWFCRQUONTSPIKHGD', 'B': 'YRUHQSLDPXNGOKMIEBFZCWVJAT', 'C': 'FVPJIAOYEDRZXWGCTKUQSBNMHL'}
class Rotor:
    def __init__(self, num, start):
        self.output = types[num]
        self.type = numerals[num]
        self.start = start
        self.offset = ord(start) - ord('A')
    def use(self, letter):
        self.offsetLetter = chr(ord(letter) + self.offset)
        if ord(self.offsetLetter) > 90:
            self.offsetLetter = chr(ord(self.offsetLetter)-90 + 65)
        self.pos = list(alphabet).index(self.offsetLetter)
        return list(self.output)[self.pos]
    def rotate(self):
        self.offset += 1

class Reflector:
    def __init__(self, rtype):
        self.output = rtypes[rtype]
    def reflect(self, letter):
        self.index = list(alphabet).index(letter)
        return list(self.output)[self.index]
    
class Enigma:
    def __init__(self):
        print('print what number rotors u want and their starting pos then type a, b or d for the reflector type')
        print('----------- EXAMPLE -----------')
        print('          1B 4Z 3H A          ')
        print('-------------------------------')
        raw = input()
        l = raw.split()
        self.rotors = []
        for i in l:
            if len(i) != 1:
                self.rotors.append(Rotor(int(i[0]), i[1]))
            else:
                self.reflector = Reflector(i)

    def updateRotors(self):
        print('print what number rotors u want and their starting pos then type a, b or d for the reflector type')
        print('----------- EXAMPLE -----------')
        print('          1B 4Z 3H A          ')
        print('-----------------------------')
        raw = input()
        l = raw.split()
        self.rotors = []
        for i in l:
            if len(i) != 1:
                self.rotors.append(Rotor(int(i[0]), i[1]))
            else:
                self.reflector = Reflector(i)
        
        
    def encode(self):
        self.letter = input('input letter: ').upper()
        self.crypt = self.rotors[0].use(self.letter)
        self.crypt = self.rotors[1].use(self.crypt)
        self.crypt = self.rotors[2].use(self.crypt)
        self.crypt = self.reflector.reflect(self.crypt)
        self.crypt = self.rotors[2].use(self.crypt)
        self.crypt = self.rotors[1].use(self.crypt)
        self.crypt = self.rotors[0].use(self.crypt)

        self.rotors[0].rotate()
        if chr(self.rotors[0].offset + ord('A')) == self.rotors[0].start:
            self.rotors[1].rotate()
            if chr(self.rotors[1].offset + ord('A')) == self.rotors[1].start:
                self.rotors[2].rotate()

        return chr(ord(self.crypt))
e = Enigma()
while 1:
    print(e.encode())
    




