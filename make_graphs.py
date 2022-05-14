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
    print_all_graph_p53()