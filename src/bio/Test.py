from collections import defaultdict

CGR_X_MAX = 1
CGR_Y_MAX = 1
CGR_X_MIN = 0
CGR_Y_MIN = 0
CGR_A = (CGR_X_MIN, CGR_Y_MIN)
CGR_T = (CGR_X_MAX, CGR_Y_MIN)
CGR_G = (CGR_X_MAX, CGR_Y_MAX)
CGR_C = (CGR_X_MIN, CGR_Y_MAX)
CGR_CENTER = ((CGR_X_MAX - CGR_Y_MIN) / 2, (CGR_Y_MAX - CGR_Y_MIN) / 2)


def empty_dict():
    return None


CGR_DICT = defaultdict(
    empty_dict,
    [
        ('A', CGR_A),  # Adenine
        ('T', CGR_T),  # Thymine
        ('G', CGR_G),  # Guanine
        ('C', CGR_C),  # Cytosine
        ('U', CGR_T),  # Uracil demethylated form of thymine
        ('a', CGR_A),  # Adenine
        ('t', CGR_T),  # Thymine
        ('g', CGR_G),  # Guanine
        ('c', CGR_C),  # Cytosine
        ('u', CGR_T)  # Uracil/Thymine
    ]
)

if CGR_DICT['D']:
    print("in if")
else:
    print("in else")

