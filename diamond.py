from string import ascii_uppercase as letters

def rows(letter):
    u = letters.index(letter) + 1
    result = []
    for char in letters[:u]:
        s = letters.index(char)
        ap = 2 * u - 1
        p = (u - s)
        line = f"{char: ^{ap}}" if char == 'A' else f"{char: >{p}}{' ':{s*2-1}}{char: <{p}}"
        result.append(line)

    return result[:-1] + result[::-1]
