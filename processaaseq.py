#!/usr/bin/python -w
# open the input file
file = open("PK01-ROUND1_Unique_aaSeqonly")
# open the output file
output = open("PK01_7aaseq_10152020", "w")
# go through the input file one line at a time
for aa in file:
    trimmed_aa = aa[2:9]
    output.write(trimmed_aa)
    output.write("\n")
output.close()