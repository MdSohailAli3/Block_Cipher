# CIPHER BLOCK CODE
import random as rd
KEY = None
isEncrypted = False
LE = None
RE = None
LAYERS_COUNT = 0
def func(RE,KEY):# using OR
    data = []
    for i in range(len(RE)):
        data.append(RE[i] | KEY[i])
    return data
    
def clearAll():
    global isEncrypted,LE,RE,KEY
    isEncrypted = False
    LE = None
    RE = None
    KEY = None

def binary_to_string(binary_string):
   

    bytes_list = []
    for i in range(0, len(binary_string), 8):
        chunk = binary_string[i:i+8]
        decimal_value = int(chunk, 2) # Convert 8-bit binary chunk to an integer (decimal)
        character = chr(decimal_value) # Convert the integer (ASCII/Unicode code point) to a character
        bytes_list.append(character)

    return ''.join(bytes_list)


def encryption():
    global isEncrypted, LE, RE, KEY, LAYERS_COUNT
    LAYERS_COUNT += 1
    isEncrypted = True
    newLE = RE[:] #this is the final LE
    newRE = []
    # now for RE
    modifiedRE = func(RE,KEY)
    for i in range(len(RE)):
        newRE.append(LE[i] ^ modifiedRE[i])
    
    encrypted_message = "".join(map(str,newLE + newRE))
    enc = binary_to_string(encrypted_message)
    print(f"Encrypted message: {enc}")
    print(f"Current Layer : {LAYERS_COUNT}")
    LE = newLE[:]
    RE = newRE[:]
    return

def decryption():
    global RE, LE, KEY, LAYERS_COUNT
    LAYERS_COUNT -= 1
    newRE = LE[:]
    newLE = []
    modifiedLE = func(LE,KEY)

    for i in range(len(RE)):
        newLE.append(RE[i] ^ modifiedLE[i])

    decrypted_message = "".join(map(str,newLE + newRE))
    dyc = binary_to_string(decrypted_message)
    print(f"Decrypted Message : {dyc}")
    print(f"Current Layer is : {LAYERS_COUNT}")
    return

def string_to_bits_bytearray(text, encoding='utf-8'):
    """
    Converts a string to a binary string using bytearray for efficient
    conversion to bytes first.
    """
    # Encode the string to bytes with a specified encoding
    encoded_bytes = text.encode(encoding)
    # Format each byte as an 8-bit binary string
    binary_representation = ''.join(format(byte, '08b') for byte in encoded_bytes)

    return [int(i) for i in binary_representation]


def main():
    global LE, RE, KEY
    input_string = input("Enter message: ")
    bits_array = string_to_bits_bytearray(input_string, 'utf-8')
   
    LE = bits_array[:int(len(bits_array)/2)]
    RE = bits_array[int(len(bits_array)/2):]

    KEY = [(i ^ rd.choice(bits_array) ) for i in LE]
   
    while(True):
        print("\n1. Encrypt Data\n2. Decrypt Data\n3. New Message\n4. Exit")
        choice = int(input("Enter Choice: "))
        if choice == 1:
            encryption()
        elif choice == 2:
            if not isEncrypted:
                print("First Encrypt the message !!!")
                continue
            decryption()
        elif choice == 3:
            clearAll()
            main()

        elif choice == 4:
            exit()
        else : print("Wrong Choice entered !!!")


if __name__ == '__main__':

    main()

