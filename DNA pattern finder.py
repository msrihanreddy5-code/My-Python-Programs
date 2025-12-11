dna = input("Enter DNA sequence: ").upper()

bases = {x: dna.count(x) for x in "ATCG"}

print("Base Count:", bases)
print("GC Content:", (bases["G"] + bases["C"]) / len(dna) * 100, "%")
