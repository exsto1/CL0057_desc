file = open("Lina_ali_not_modified.fasta").readlines()
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

print(len(names), len(seq))

counter = 0
excluded = []
for i in range(len(seq)):
    if i not in excluded:
        for i1 in range(i + 1, len(seq)):
            if seq[i] == seq[i1]:
                print(i, i1, names[i], names[i1], seq[i], seq[i1])
                excluded.append(i1)
                counter += 1

print(counter)

out = open("Lina_ali_no_dups.fasta", "w")
for i in range(len(seq)):
    if i not in excluded:
        if "PF7181" in names[i]:
            out.write("PF07181".join(names[i].split("PF7181")) + "\n")
        else:
            out.write(names[i] + "\n")
        out.write(seq[i] + "\n")
