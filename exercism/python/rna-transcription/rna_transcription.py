'''
Given an DNA sequence, return and RNA sequence.
G -> C
C -> G
T -> A
A -> U
'''


def to_rna(dna_strand):
    rna = ''
    transcription = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    # if value not in dict -> raise ValueError
    for nucleotide in dna_strand:
        if nucleotide not in transcription.keys():
            raise ValueError("Value not present.")
    # must include ValueError
        else:
            rna += transcription[nucleotide]
    return rna
