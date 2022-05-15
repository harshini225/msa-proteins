import matplotlib.pyplot as plt
import numpy as np 


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


def print_any_graph(prefix, num_spec, sps, title, is_nebulin, stop_word):
    fh = open("results/summary.txt", "r")
    
    need_clustal = False
    need_muscle = False
    need_tc = False
    clustal = []
    muscle = []
    tc = []
    for line in fh: 
        if line:
            if is_nebulin and line.startswith("p53"):
                break
            elif (not is_nebulin) and line.startswith("nebulin"):
                break

            if line.startswith(stop_word):
                break

            if line.startswith(prefix + " clustal-omega"): 
                need_clustal = True
            elif line.startswith(prefix + " muscle"): 
                need_clustal = False
                need_muscle = True
            elif line.startswith(prefix + " t-coffee"): 
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

    data = [clustal, muscle, tc]
    
    X = np.arange(num_spec)
    
    fig, ax = plt.subplots()
    ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)
    ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)
    ax.bar(X + 0.50, data[2], color = 'r', width = 0.25)
    ax.set_ylabel('Avg. percent identity')
    ax.set_xlabel('Species')
    ax.set_title(title)
    ax.set_xticks(X + 0.25, sps)
    ax.set_yticks(np.arange(0, 100, 10))
    ax.legend(labels=['Clustal-Omega', 'MUSCLE', 'T-Coffee'])
    plt.show()



def print_any_graph_nebulin(prefix, num_spec, sps, title, is_nebulin, stop_word):
    fh = open("results/summary.txt", "r")
    
    need_clustal = False
    need_muscle = False
    clustal = []
    muscle = []
    for line in fh: 
        if line:
            if line.startswith(stop_word):
                break

            if line.startswith(prefix + " clustal-omega"): 
                need_clustal = True
            elif line.startswith(prefix + " muscle"): 
                need_clustal = False
                need_muscle = True
            else: 
                arr = line.split()
                if need_clustal and len(arr) > 0:
                    clustal.append(float(line.split()[1]))
                elif need_muscle and len(arr) > 0: 
                    muscle.append(float(line.split()[1]))

    fh.close()

    data = [clustal, muscle]
    
    print(data)

    X = np.arange(num_spec)
    
    fig, ax = plt.subplots()
    ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)
    ax.bar(X + 0.25, data[1], color = 'r', width = 0.25)
    ax.set_ylabel('Avg. percent identity')
    ax.set_xlabel('Species')
    ax.set_title(title)
    ax.set_xticks(X + 0.15, sps)
    ax.set_yticks(np.arange(0, 100, 10))
    ax.legend(labels=['Clustal-Omega', 'MUSCLE', 'T-Coffee'])
    plt.show()


if __name__ == "__main__":
    mlrat_human = ["f. damarensis", "h. glaber", "h. sapiens", "n. galili", "s. judaei"]
    mlrat_human_nebulin = ["f. damarensis", "h. glaber", "h. sapiens"]

    giant_human = ["b. musculus", "b. physalus", "d. leucas", "h. sapiens", "l. africana", "p. macrocephalus"]
    giant_human_neb = ["b. musculus", "d. leucas", "h. sapiens", "l. africana"]
    # print_any_graph("p53 5-molerat+human", 5, mlrat_human, 'Avg. percent identity amongst molerat+human p53', False, "p53 6-giant+control")
    # print_any_graph("p53 4-giant+human", 6, giant_human, 'Avg. percent identity amongst giant animals+human p53', False, "p53 5-molerat+human")

    # print_any_graph_nebulin("nebulin 5-molerat+human", 3, mlrat_human_nebulin, 'Avg. percent identity amongst molerat+human nebulin', True, "nebulin 5-molerat+human t-coffee")
    # print_any_graph_nebulin("nebulin 4-giant+human", 4, giant_human_neb, 'Avg. percent identity amongst giant animals+human nebulin', True, "nebulin 4-giant+human t-coffee")