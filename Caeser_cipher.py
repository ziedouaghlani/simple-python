import art

print(art.logo_caesar)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,shift,method):
    result=[]
    for char in text :
        if method == "encode":
            p=alphabet.index(char) + shift % 26
            if p > 25 :
                p = p % 26
            result.append(alphabet[p])
        else:
           p=alphabet.index(char) - shift % 26
           if p < 0:
                p= p + 26 
           result.append(alphabet[p]) 
    return ''.join(result)

while(True):
    method = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    print(caesar(text,shift,method))
    continu = input("Type yes if you want to go again ")
    if continu != "yes":
        break






