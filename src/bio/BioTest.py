from Bio import SeqIO

for sequence in SeqIO.parse('example.fasta', "fasta"):
    print(sequence.id)
    print(sequence.seq)
    print(len(sequence))
