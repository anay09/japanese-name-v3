alphabet_map = {
    'A': 'ka',
    'B': 'tu',
    'C': 'mi',
    'D': 'te',
    'E': 'ku',
    'F': 'lu',
    'G': 'ji',
    'H': 'ri',
    'I': 'ki',
    'J': 'zu',
    'K': 'me',
    'L': 'ta',
    'M': 'rin',
    'N': 'to',
    'O': 'mo',
    'P': 'no',
    'Q': 'ke',
    'R': 'shi',
    'S': 'ari',
    'T': 'chi',
    'U': 'do',
    'V': 'ru',
    'W': 'mei',
    'X': 'na',
    'Y': 'fu',
    'Z': 'zi',
}

inp_name = 'Anay'
output_name = list()
[output_name.append(alphabet_map[i.upper()]) for i in inp_name]
print('Original Name: {i}, Translated Name: {o}'.format(
        o=''.join(output_name),
        i=inp_name)
)