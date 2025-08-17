def decimals_to_binary(decimals, bits_per_digit=4):
    binary = ""
    for d in decimals:
        if not d.isdigit():
            continue
        b = bin(int(d))[2:].zfill(bits_per_digit)
        binary += b
    return binary

def binary_to_ascii(binary_str):
    chars = []
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        if len(byte) < 8:
            continue
        chars.append(chr(int(byte, 2)))
    return "".join(chars)

def search_word_in_file(file_path, word, block_size=1000):
    total_digits_processed = 0
    with open(file_path, "r") as f:
        buffer = ""
        while True:
            chunk = f.read(block_size)
            if not chunk:
                break
            buffer += chunk.strip()
            binary_block = decimals_to_binary(buffer)
            ascii_block = binary_to_ascii(binary_block)
            idx = ascii_block.find(word)
            total_digits_processed += sum(c.isdigit() for c in buffer)
            if idx != -1:
                return total_digits_processed, idx
            buffer = "" 
    return None, None

# ======================

word_to_search = "ASCII"
file_path = "pi_digits.txt"

digits_processed, ascii_index = search_word_in_file(file_path, word_to_search)

if digits_processed is not None:
    print(f"La palabra '{word_to_search}' se encontró después de procesar {digits_processed} dígitos.")
else:
    print(f"No se encontró la palabra '{word_to_search}' en el archivo.")
