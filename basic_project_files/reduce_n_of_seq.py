file = open("Lina_ali_no_dups_reduced_renamed.fasta").readlines()
file = [i.rstrip() for i in file]
names = []
seq = []
seq_temp = ""

for i in file:
    if ">" in i:
        if seq_temp:
            seq.append(seq_temp)
            seq_temp = ""
        names.append(i)
    else:
        seq_temp += i

seq.append(seq_temp)

out = open("Lina_ali_no_dups_reduced_3_rep.fasta", "w")
for i in range(len(seq)):
    if int(names[i].split("_")[-1]) % 4 != 0:
        out.write(names[i] + "\n")
        out.write(seq[i] + "\n")