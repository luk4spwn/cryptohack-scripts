import base64

cadena_hexadecimal = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf" # Cadena codificada
bytes_cadena = bytes.fromhex(cadena_hexadecimal) # Pasamos la cadena a hexadecimal
cadena_base64 = base64.b64encode(bytes_cadena) # La encodeamos en base64

print(cadena_base64.decode()) # La mostramos por pantalla

