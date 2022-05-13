from Bio import SeqIO

uniprot_data = "./sequences/uniprot-results.fasta"
proteins = ["p53", "smu1", "rb", "nebulin", "pi3k"]
edited_proteins = ["p53", "nebulin"]

GIANT_ANIMALS = "giant_animals"
MOLERATS = "mole_rats"
CONTROL = "control"

def classify_species(): 
    species_dict = {} # maps species to their analysis category 
    species_dict["balaenoptera_musculus"] = GIANT_ANIMALS
    species_dict["loxodonta_africana"] = GIANT_ANIMALS
    species_dict["physeter_macrocephalus"] = GIANT_ANIMALS
    species_dict["delphinapterus_leucas"] = GIANT_ANIMALS
    species_dict["balaenoptera_physalus"] = GIANT_ANIMALS

    species_dict["spalax_judaei"] = MOLERATS
    species_dict["nannospalax_galili"] = MOLERATS
    species_dict["heterocephalus_glaber"] = MOLERATS
    species_dict["fukomys_damarensis"] = MOLERATS
    species_dict["spalax_ehrenbergi"] = MOLERATS
    
    species_dict["mus_musculus"] = CONTROL
    species_dict["danio_rerio"] = CONTROL
    species_dict["homo_sapiens"] = CONTROL
    species_dict["drosophila_melanogaster"] = CONTROL

    return species_dict

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
        species = "".join(x + "_" for x in description.split("=")[1].split()[0:2])[:-1]

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


# def write_all_prot_to_file(seq_dict): 
#     output_folder = "sequences"
#     for key, set_of_seqs in seq_dict.items(): 
#         fh = open(output_folder + key + ".fasta", "w")
#         for species, sequence in set_of_seqs:
#             fh.write(">" + species + "\n")
#             fh.write(sequence + "\n")
#         fh.close()


def write_p53_nebulin_files(uniprot_dict, species_dict):
    output_folder = "sequences/"
    for prot in edited_proteins:
        file_prefix = output_folder + prot + "/"
        giant_output_file = open(file_prefix + GIANT_ANIMALS + ".fasta", "w")
        molerat_output_file = open(file_prefix + MOLERATS + ".fasta", "w")
        control_output_file = open(file_prefix + CONTROL + ".fasta", "w")
        for species, sequence in uniprot_dict[prot]:
            if species_dict[species] == GIANT_ANIMALS:
                giant_output_file.write(">" + species + "\n")
                giant_output_file.write(sequence + "\n")
            elif species_dict[species] == MOLERATS: 
                molerat_output_file.write(">" + species + "\n")
                molerat_output_file.write(sequence + "\n")
            else: 
                control_output_file.write(">" + species + "\n")
                control_output_file.write(sequence + "\n")
        giant_output_file.close()
        molerat_output_file.close()
        control_output_file.close()


if __name__ == "__main__":
    spec_dict = classify_species() 
    dict_with_seq = analyze_uniprot()
    write_p53_nebulin_files(dict_with_seq, spec_dict)