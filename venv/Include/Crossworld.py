import string
import re
def regex_crossword_check(horizontal_patterns, vertical_patterns, width, height, candidate, alphabet=string.ascii_uppercase):
    for pattern, horiz_line in zip(horizontal_patterns, candidate):
        line = ''.join(horiz_line)
        if re.match(pattern, line) is None:
            return False

    for pattern, vert_line in zip(vertical_patterns, zip(*candidate)):
        line = ''.join(vert_line)
        if re.match(pattern, line) is None:
            return False

    return True



horiz = [r'HE|LL|O+', r'[PLEASE]+']
vert = [r'[^SPEAK]+', r'EP|IP|EF']
candidate = [
	['H', 'E'],
	['L', 'P']
]
print(regex_crossword_check(horiz, vert,vert.__sizeof__(),horiz.__sizeof__(), candidate))  # => True
