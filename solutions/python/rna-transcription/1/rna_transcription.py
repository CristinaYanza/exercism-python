"""Transcribe DNA to RNA."""

def to_rna(dna_strand):
    """Return the RNA complement of a DNA strand."""

    result = ""

    for nucleotide in dna_strand:
        if nucleotide == "G":
            result += "C"
        elif nucleotide == "C":
            result += "G"
        elif nucleotide == "T":
            result += "A"
        elif nucleotide == "A":
            result += "U"

    return result