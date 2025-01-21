def split_string(s, length):
    for i in range(0, len(s), length):
        yield s[i:i + length]


class Ddu64:
    def __init__(self, ddu_char=None, padding_char="뭐"):
        if ddu_char is None:
            ddu_char = ["뜌", "땨", "이", "우", "야", "!", "?", "."]
        self.ddu_char = ddu_char
        self.padding_char = padding_char

    def encode(self, string: bytes) -> str:
        encoded_bin = ""
        for char in string:
            char_raw = str(bin(char))[2:]
            encoded_bin += ("0" * (8 - len(char_raw)) + char_raw)

        encoded = []
        for chunk in split_string(encoded_bin, 6):
            encoded.append(chunk)

        padding = 6 - len(encoded[len(encoded) - 1])
        encoded[len(encoded) - 1] = encoded[len(encoded) - 1] + "0" * padding

        result = ""

        for char in encoded:
            char_int = int(char, 2)
            result += self.ddu_char[char_int // 8] + self.ddu_char[char_int % 8]
        result += self.padding_char * int(padding / 2)
        return result

    def decode(self, string: str) -> bytes:
        padding_count = string.count(self.padding_char)
        string = string[:len(string) - padding_count]

        decoded_bin = ""
        for chunk in split_string(string, 2):
            char = bin(int("0o" + str(self.ddu_char.index(chunk[0])) + str(self.ddu_char.index(chunk[1])), 8))[2:]
            char = "0" * (6 - len(char)) + char
            decoded_bin += char
        decoded_bin = decoded_bin[:len(decoded_bin) - padding_count * 2]

        decoded = []
        for chunk in split_string(decoded_bin, 8):
            decoded.append(int("0b" + chunk, 2))

        return bytes(decoded)


if __name__ == "__main__":
    ddu64 = Ddu64()
    encode = input("Encode: ").encode("utf-8")
    print(ddu64.encode(encode))
    decode = input("Decode: ")
    print(ddu64.decode(decode).decode("utf-8"))
