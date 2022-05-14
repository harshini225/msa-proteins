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
    size = len(some_list)
    sum = 0.0
    for i in some_list:
        sum += float(i)
    
    return sum /size


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


def print_control_graph():

    data = [[36.75, 21.665, 36.135, 37.475],
            [35.525, 19.71, 36.01, 36.14],
            [36.07, 21.71, 38.45, 38.445]]
    
    X = np.arange(4)
    fig, ax = plt.subplots()
    ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)
    ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)
    ax.bar(X + 0.50, data[2], color = 'r', width = 0.25)
    ax.set_ylabel('Avg. percent identity')
    ax.set_xlabel('Species')
    ax.set_title('Avg. percent identity amongst the traditional subjects group')
    ax.set_xticks(X, ['danio_rerio', 'drosophila_melanogaster', 'homo_sapiens', 'mus_musculus'])
    ax.set_yticks(np.arange(0, 100, 10))
    ax.legend(labels=['Clustal-Omega', 'MUSCLE', 'T-Coffee'])
    plt.show()


def print_control_graph_p53():

    data = [[36.75, 21.665, 36.135, 37.475],
            [35.525, 19.71, 36.01, 36.14],
            [36.07, 21.71, 38.45, 38.445]]
    
    X = np.arange(4)
    fig, ax = plt.subplots()
    ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)
    ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)
    ax.bar(X + 0.50, data[2], color = 'r', width = 0.25)
    ax.set_ylabel('Avg. percent identity')
    ax.set_xlabel('Species')
    ax.set_title('Avg. percent identity amongst the traditional subjects group p53')
    ax.set_xticks(X, ['danio_rerio', 'drosophila_melanogaster', 'homo_sapiens', 'mus_musculus'])
    ax.set_yticks(np.arange(0, 100, 10))
    ax.legend(labels=['Clustal-Omega', 'MUSCLE', 'T-Coffee'])
    plt.show()


def print_control_graph_nebulin():

    data = [[59.84, 59.4, 59.84],
            [60.19, 59.65, 60.19],
            [59.69, 59.69, 59.96]]
    
    X = np.arange(3)
    fig, ax = plt.subplots()
    ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)
    ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)
    ax.bar(X + 0.50, data[2], color = 'r', width = 0.25)
    ax.set_ylabel('Avg. percent identity')
    ax.set_xlabel('Species')
    ax.set_title('Avg. percent identity amongst the traditional subjects group nebulin')
    ax.set_xticks(X + 0.25, ['danio_rerio', 'homo_sapiens', 'mus_musculus'])
    ax.set_yticks(np.arange(0, 100, 10))
    ax.legend(labels=['Clustal-Omega', 'MUSCLE', 'T-Coffee'])
    plt.show()


def print_all_graph_p53():
    fh = open("results/summary.txt", "r")
    
    need_clustal = False
    need_muscle = False
    need_tc = False
    clustal = []
    muscle = []
    tc = []
    for line in fh: 
        if line:
            if line.startswith("nebulin"):
                break
            if line.startswith("p53 9-all clustal-omega"): 
                need_clustal = True
            elif line.startswith("p53 9-all muscle"): 
                need_clustal = False
                need_muscle = True
            elif line.startswith("p53 9-all t-coffee"): 
                need_muscle = False
                need_tc = True
            else: 
                arr = line.split()
                if need_clustal and len(arr) > 0:
                    clustal.append(float(line.split()[1]))
                elif need_muscle and len(arr) > 0: 
                    muscle.append(float(line.split()[1]))
                elif need_tc and len(arr) > 0:
                    tc.append(float(line.split()[1]))

    fh.close()
    print(clustal)
    print(len(clustal))
    print(muscle)
    print(len(muscle))
    print(tc)
    print(len(tc))
    data = [clustal, muscle, tc]
    
    X = np.arange(12)
    sps = ["b. musculus", "b. physalus", "d. rerio", "d. leucas", "d. melanogaster","h. glaber", "h. sapiens", "l. africana", "m. musculus", "n. galili", "p. macrocephalus", "s. judaei"]
    
    fig, ax = plt.subplots()
    ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)
    ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)
    ax.bar(X + 0.50, data[2], color = 'r', width = 0.25)
    ax.set_ylabel('Avg. percent identity')
    ax.set_xlabel('Species')
    ax.set_title('Avg. percent identity amongst all species p53')
    ax.set_xticks(X + 0.25, sps)
    ax.set_yticks(np.arange(0, 100, 10))
    ax.legend(labels=['Clustal-Omega', 'MUSCLE', 'T-Coffee'])
    plt.show()


if __name__ == "__main__":
    # parse_all_matrix_files()
    # print_control_graph_p53()
    # print_control_graph_nebulin()
    print_all_graph_p53()
    