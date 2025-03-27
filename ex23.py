import sys

script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
    
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)


# Exercise not complete. BREAK THE CODE
string = b"""
Ram Sita Ram Sita Ram Sita Ram
Ram Sita Ram Sita Ram Sita Ram
Ram Sita Ram Sita Ram Sita Ram
Ram Sita Ram Sita Ram Sita Ram 
Ram Sita Ram Sita Ram Sita Ram
Ram Sita Ram Sita Ram Sita Ram
Ram Sita Ram Sita Ram Sita Ram
Ram Sita Ram Sita Ram Sita Ram
Ram Sita Ram Sita Ram Sita Ram
"""
import codecs

code = codecs.encode(string, encoding = "base64", errors = "strict")
#code = string.encode("base64", "strict")
print(code, "\nDecode the text")
codec = input("> ")
text = codecs.decode(code, encoding = codec, errors = "strict")
#text = code.decode(codec.strip(), "strict")
print(text)