f = open('input3.txt', 'r', encoding='utf-8')
c = f.read()
def translate_to_whistling_language(text):
    glas = 'аеёиоуыэюя'
    res = []
    i = 0
    while i < len(text):
        char = text[i]
        if char in glas:
            res.append(char)
            if i > 0 and text[i - 1] not in glas:
                res.append('с' + char)
        else:
            res.append(char)
        i += 1
    return ''.join(res)
translated_c = translate_to_whistling_language(c)
print(translated_c)
