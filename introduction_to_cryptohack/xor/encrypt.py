# Function to perform XOR encryption
def xor_encryption(text, key):
    # Initialize an empty string for encrypted text
    encrypted_text = ""
    
    # Iterate over each character in the text
    for i in range(len(text)):
        encrypted_text += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    
    # Return the encrypted text
    return encrypted_text

# The plaintext that we want to encrypt
plain_text = "ESTAMOS FRENTE A UN GRAVE PROBLEMA"
# The secret key used for encryption
key = "barcelona"

# Encrypt the plain_text using the key
encrypted_text = xor_encryption(plain_text, key)
# Print the encrypted text
print(f'Encrypted Text: {encrypted_text}')
