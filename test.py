fin = open("clean_output6.txt")
fout = open("clean_output7.txt", "wt")
for line in fin:
    fout.write( line.replace(line[7:13],str(int(line[7:13])*2)))
    print(line[7:13])
fin.close()
fout.close()
fin = open("clean_output7.txt")
fout = open("clean_output8.txt", "wt")
for line in fin:
    fout.write( line.replace(line[14:19],str(int(line[14:19])*2)))
    print(line[13:19])
fin.close()
fout.close()
