import re 

cancer_types = ["Adrenal", "Biliary", "Bone", "Brain", "Breast", "Cervix", "Endometrium", "Eye", "Kidney", "LargeIntestine", "Liver", "Lung", "Oesophagus", "Ovary", "Pancreas", "Prostate", "Skin", "Stomach", "Testis", "Thyroid", "Urinary"]
filepath = "./sig-cancers/"


def count_domains():
    """
    This function counts the protein domains from cancer mutant domain data
    and prints the top 10 most common protein domains.
    """
    domains_dict = {}

    for cancer in cancer_types:
        full_path = filepath + cancer + ".txt"
        fh = open(full_path, "r")
        next(fh)
        for line in fh: 
            line_part = line.split("	")
            domain = line_part[0]
            if domain in domains_dict.keys(): 
                domains_dict[domain] += 1
            else: 
                domains_dict[domain] = 1

    print(sorted(domains_dict.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)[0:10])
    # Result: [('P53', 21), ('PI3Ka', 11), ('zf-H2C2_2', 10), ('Nebulin', 10), ('Ras', 8), ('RB_A', 8), ('WD40', 7), ('Pkinase_Tyr', 6), ('KRAB', 6), ('Furin-like', 6)]
    

if __name__ == "__main__":
    count_domains()