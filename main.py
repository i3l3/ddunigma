def split_string(s, length):
    for i in range(0, len(s), length):
        yield s[i:i + length]


dduchar = ["뜌", "땨", "이", "우", "야", "!", "?", "."]
spacing = "="

string = input("Enter a string: ").encode("utf-8")
encoded_bin = ""
for char in string:
    char_raw = str(bin(char))[2:]
    encoded_bin += ("0" * (8 - len(char_raw)) + char_raw)

encoded = []
for chunk in split_string(encoded_bin, 6):
    encoded.append(chunk)

print(len(encoded_bin[0]))
print(encoded)
