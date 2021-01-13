path = "Lina_ali_no_dups_reduced_3_rep.fasta"
file = open(path).readlines()
out = open("Lina_ali_no_dups_reduced_renamed_3_rep.fasta", "w")

used = {}
for i in file:
    if ">" in i:
        text = i
        family = text
        for i1 in range(len(text)):
            if text[i1] == "P" and text[i1+1] == "F":
                family = text[i1:i1+7]
                break
        if family in used:
            used[family] += 1
        else:
            used[family] = 0
        out.write(f">{family}_{used[family]}\n")
    else:
        out.write(i)



