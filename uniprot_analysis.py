from Bio import SeqIO

uniprot_data = "raw-prot-data/uniprot.fasta"
proteins = ["p53", "smu1", "rb", "nebulin", "pi3k"]

def analyze_uniprot(): 
    """
    This function organises the protein sequences from Uniprot for Multiple Sequence Alignment. 
    """
    # maps protein types (p53, etc.) to a tuple of their organism name and sequence
    uniprot_dict = {} 
    for prot in proteins: 
        uniprot_dict[prot] = set()

    # opens the file as fasta for parsing 
    fasta_sequences = SeqIO.parse(open(uniprot_data),'fasta')
    
    # iterates through sequences to populate dictionary 
    for fasta in fasta_sequences:
        sequence, description = str(fasta.seq), fasta.description.lower()
        species = "".join(x + " " for x in description.split("=")[1].split()[0:2]).strip()

        if "p53" in description: 
            uniprot_dict["p53"].add((species, sequence))
        elif "smu1" in description: 
            uniprot_dict["smu1"].add((species, sequence))
        elif "nebulin" in description: 
            uniprot_dict["nebulin"].add((species, sequence))
        elif "rb" in description: 
            uniprot_dict["rb"].add((species, sequence))
        else: 
            uniprot_dict["pi3k"].add((species, sequence))
    
    return uniprot_dict


def write_seq_to_file(): 
    output_file = ""


if __name__ == "__main__":
    analyze_uniprot()