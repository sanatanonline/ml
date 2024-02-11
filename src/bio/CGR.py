import re
import sys
from collections import defaultdict

import matplotlib.pyplot as plt
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


def slugify(value):
    value = re.sub(r'[^\w\s-]', '', value).strip()
    value = re.sub(r'[-\s]+', '-', value)
    return value


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


def fasta_reader(fasta):
    flist = SeqIO.parse(fasta, "fasta")
    for i in flist:
        yield i.description, i.seq


def mk_cgr(seq):
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


def mk_plot(cgr, name, figid):
    x_axis = [i[1][0] for i in cgr]
    y_axis = [i[1][1] for i in cgr]
    plt.figure(figid)
    plt.title("Chaos Game Representation\n" + name, wrap=True)
    plt.plot([CGR_CENTER[0], CGR_CENTER[0]], [0, CGR_Y_MAX], 'k-')
    plt.plot([CGR_Y_MIN, CGR_X_MAX], [CGR_CENTER[1], CGR_CENTER[1]], 'k-')
    plt.scatter(x_axis, y_axis, alpha=0.5, marker='.')
    return {'fignum': figid, 'title': name, 'fname': slugify(name)}


if __name__ == '__main__':
    fig_id = 1
    files = ['NC_012920.fasta', 'HQ287892.1.fasta']
    my_plots = []
    mycgr = []
    for i in files:
        fasta_seq = fasta_reader(i)
        for name, seq in fasta_seq:
            cgr = mk_cgr(seq)
            my_plots.append(mk_plot(cgr, name, fig_id))
            fig_id += 1
    plt.show()
