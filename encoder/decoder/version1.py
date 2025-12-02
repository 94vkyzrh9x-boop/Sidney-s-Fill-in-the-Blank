#!/usr/bin/env python3 
print ("Welcome to the Binary Encoder/Decoder v1!")
print ("Enter your text below to encode it into binary, or enter binary code to decode it back into text.")
# Mapping from character to hex code
def encode_text_to_binary(text: str) -> str:
    """Convert a string to space-separated 8-bit binary codes.
    Example: 'A' -> '01000001'"""
    """Encode text to binary using the hex lookup tables."""
    binary_codes = []

    for char in text:
        ascii_val = ord(char)
        binary_code = format(ascii_val, '08b')
        binary_codes.append(binary_code)
    return ' '.join(binary_codes)

def decode_binary_to_text(binary_string: str) -> str:
    chars = []
    binary_parts = binary_string.split()

    for b in binary_parts:
        number = int(b, 2)
        char = chr(number)
        chars.append(char)
    return ''.join(chars)


print ("If you would like to encode text to binary, type 'encode'. If you would like to decode binary to text, type 'decode'. If you would like to exit, type 'exit'.")
user_answer = input("Type your choice here: ")
if user_answer == "encode":
    encode_text = input("Enter your chosen text to encode: ")
    print("\nEncoded:\n")
    print(encode_text_to_binary(encode_text))
    
elif user_answer == "decode":
    decode_binary = input("Enter your chosen binary code to decode: ")
    print("\nDecoded:\n")
    print(decode_binary_to_text(decode_binary))

elif user_answer == "exit":
    print ("Goodbye!")

else:
    print ("Invalid choice. Please restart the program and choose 'encode' or 'decode'.")

print ("What would you like to do next?")
print ("If you would like to encode text to binary, type 'encode'. If you would like to decode binary to text, type 'decode'. If you would like to exit, type 'exit'.")
user_answer = input("Type your choice here: ")
if user_answer == "encode":
    encode_text = input("Enter your chosen text to encode: ")
    print("\nEncoded:\n")
    print(encode_text_to_binary(encode_text))

elif user_answer == "decode":
    decode_binary = input("Enter your chosen binary code to decode: ")
    print("\nDecoded:\n")
    print(decode_binary_to_text(decode_binary)) 

elif user_answer == "exit":
    print ("Goodbye!")

print ("Thank you for using the Binary Encoder/Decoder v1!")