def text_processing(text):
    # Obtener los códigos ASCII de los caracteres en el texto
    ascii_bytes = [ord(char) for char in text]

    # Obtener los bytes en hexadecimal
    hex_bytes = [hex(byte) for byte in ascii_bytes]

    # Convertir los bytes en hexadecimal a una cadena base-16
    base_16 = '0x' + ''.join(byte[2:].zfill(2) for byte in hex_bytes)

    # Convertir la cadena base-16 a base-10
    base_10 = int(base_16, 16)

    print("message:", text.upper())
    print("ascii bytes:", ascii_bytes)
    print("hex bytes:", hex_bytes)
    print("base-16:", base_16)
    print("base-10:", base_10)

# Ejemplo de uso
text = "crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}"
text_processing(text)

