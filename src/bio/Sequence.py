import sys
from collections import defaultdict

from Bio import SeqIO

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


def read_fasta(fasta):
    flist = SeqIO.parse(fasta, "fasta")
    for i in flist:
        yield i.description, i.seq


def build_cgr(seq):
    cgr = []
    cgr_marker = CGR_CENTER[:]
    for s in seq:
        cgr_corner = CGR_DICT[s]
        if cgr_corner:
            cgr_marker = (
                (cgr_corner[0] + cgr_marker[0]) / 2,
                (cgr_corner[1] + cgr_marker[1]) / 2
            )
            cgr.append([s, cgr_marker])
        else:
            sys.stderr.write("Bad Nucleotide: " + s + " \n")
    return cgr


if __name__ == '__main__':
    file = 'NC_012920.fasta'
    fasta_seq = read_fasta(file)
    for name, seq in fasta_seq:
        cgr = build_cgr(seq)
        print(cgr)
