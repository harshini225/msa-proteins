import matplotlib.pyplot as plt
import numpy as np 

result = "results/"
proteins = ["p53", "nebulin"]
names_folders = ["1-control", "2-giant", "3-molerat", "4-giant+human", "5-molerat+human", "6-giant+control", "7-molerat+control", "8-mole+giant", "9-all"]
names_aligners = ["clustal-omega", "muscle", "t-coffee"]


def take_one_100_out(some_list):
    """
    take one 100.00 out of the list to account for similarity to self 
    """
    ct = 0  
    some_copy = []
    for elem in some_list: 
        if elem != "100.00" or (elem == "100.00" and ct == 1):
            some_copy.append(elem)
        else: 
            ct += 1
    return some_copy


def take_average(some_list):
    """
    find avg of stuff in list  
    """
    my_size = len(some_list)
    my_sum = 0.0
    for i in some_list:
        my_sum += float(i)
    
    return my_sum / my_size


def parse_file(fp): 
    """
    parses each file individually 
    """

    read_fh = open(fp, "r")
    to_return = {}

    for ln in read_fh: 
        if ln.strip():
            if ln[0] != "#": 
                ln_array = take_one_100_out(ln.strip().split(":")[1].split())
                spec_name = ln_array[0]
                avg = take_average(ln_array[1:-1])
                to_return[spec_name] = avg
    read_fh.close()

    return to_return


def parse_all_matrix_files(): 
    """
    prints summary stats based on results of alignment
    """
    write_to = open("results/summary.txt", "w")

    for prot in proteins:
        for folder in names_folders: 
            for aligner in names_aligners: 
                full_fp = result + prot + "/" + folder + "/" + aligner + "-matrix.fasta"
                my_dict = parse_file(full_fp)
                my_list = sorted(my_dict.keys())

                write_to.write(prot + " " + folder + " " + aligner + "\n")
                for k in my_list: 
                    write_to.write(k + " " + str(my_dict[k]) + "\n")
                
                write_to.write("\n")

    write_to.close()


if __name__ == "__main__":
    parse_all_matrix_files()
    