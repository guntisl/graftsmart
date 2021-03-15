#!/usr/bin/env python












correct_output = []                       # The list where we will store results.

linenum = 0
substr = "peri".lower()          # Substring to search for.
with open ('first_output.txt', 'rt') as myfile:
    for line in myfile:
        linenum += 1
        if line.lower().find(substr) != -1:    # if case-insensitive match,
            correct_output.append(line.rstrip('\n'))

target = open("clean_output2.txt", 'wb')
for output_correct in correct_output:
    
#    print(output_correct)

    target.writelines(output_correct + '\n')
target.close()

fin = open("clean_output2.txt")
fout = open("clean_output3.txt", "wt")
for line in fin:
    fout.write( line[11:] )
fin.close()
fout.close()


fin = open("clean_output3.txt")
fout = open("clean_output4.txt", "wt")
for line in fin:
    fout.write( line.replace("top_y:", "Y"))
fin.close()
fout.close()


fin = open("clean_output4.txt")
fout = open("clean_output5.txt", "wt")
for line in fin:
    fout.write( line.replace("left_x:", "X"))
fin.close()
fout.close()
fin = open("clean_output5.txt")
fout = open("clean_output6.txt", "wt")
for line in fin:
    fout.write( line.replace("width:", ""))
fin.close()
fout.close()





fin = open("clean_output6.txt")
fout = open("clean_output7.txt", "wt")
for line in fin:
    fout.write( line.replace(line[3:8],str(int(line[3:8])*2)))
fin.close()
fout.close()

fin = open("clean_output7.txt")
fout = open("clean_output8.txt", "wt")
for line in fin:
    fout.write( line.replace(line[10:15],str(int(line[10:15])*2)))
fin.close()
fout.close()








fin = open("clean_output8.txt")
fout = open("clean_output9.txt", "wt")
for line in fin:
    fout.write( line.replace("height:", ""))
fin.close()
fout.close()





fin = open("clean_output9.txt")
fout = open("clean_output10.txt", "wt")
for line in fin:
    fout.write( line.replace(line[16:],'\n'))
fin.close()
fout.close()

fin = open("clean_output10.txt")
fout = open("clean_output11.txt", "wt")
for line in fin:
    fout.write( line.replace(" ",''))
fin.close()
fout.close()


fin = open("clean_output11.txt")
fout = open("clean_output12.txt", "wt")
for line in fin:
    fout.write( line.replace(line[:2],''))
fin.close()
fout.close()


fin = open("clean_output12.txt")
fout = open("clean_output13.txt", "wt")
for line in fin:
    fout.write( line.replace("X", "G0 X"))
fin.close()
fout.close()

fin = open("clean_output13.txt")
fout = open("clean_output14.txt", "wt")
for line in fin:
    fout.write( line.replace("Y",' Y'))
fin.close()
fout.close()




#cell_str = '' 
# define the function blocks
def cell1():
    return "G1 Z10 E1000 F1000\nG0 Z100 E1000 F1000'+'\n"

def cell2():
    return "G2 Z10 E1000 F1000\nG0 Z100 E1000 F1000'+'\n"

def cell3():
    return "G3 Z10 E1000 F1000\nG0 Z100 E1000 F1000'+'\n"

def cell4():
    return "G4 Z10 E1000 F1000\nG0 Z100 E1000 F1000"+"\n"

def cell5():
    return "G5 Z10 E1000 F1000\nG0 Z100 E1000 F1000'+'\n"

def cell6():
    return "G6 Z10 E1000 F1000\nG0 Z100 E1000 F1000'+'\n"

def cell7():
    return "G7 Z10 E1000 F1000\nG0 Z100 E1000 F1000'+'\n"

def cell8():
    return "G8 Z10 E1000 F1000\nG0 Z100 E1000 F1000"+"\n"

def cell9():
    return "G9 Z10 E1000 F1000\nG0 Z100 E1000 F1000'+'\n"

def cell10():
    return "G10 Z10 E1000 F1000\nG0 Z100 E1000 F1000'+'\n"

def cell11():
    return "G11 Z10 E1000 F1000\nG0 Z100 E1000 F1000"+"\n"

def cell12():
    return "G12 Z10 E1000 F1000\nG0 Z100 E1000 F1000'+'\n"

def cell13():
    return "G13 Z10 E1000 F1000\nG0 Z100 E1000 F1000'+'\n"

def cell14():
    return "G14 Z10 E1000 F1000\nG0 Z100 E1000 F1000"+"\n"

def cell15():
    return "G15 Z10 E1000 F1000\nG0 Z100 E1000 F1000'+'\n"

def cell16():
    return "G16 Z10 E1000 F1000\nG0 Z100 E1000 F1000'+'\n"

def cell17():
    return "G17 Z10 E1000 F1000\nG0 Z100 E1000 F1000"+"\n"

def cell18():
    return "G18 Z10 E1000 F1000\nG0 Z100 E1000 F1000'+'\n"

def cell19():
    return "G19 Z10 E1000 F1000\nG0 Z100 E1000 F1000'+'\n"

def cell20():
    return "G20 Z10 E1000 F1000\nG0 Z100 E1000 F1000"+"\n"
# map the inputs to the function blocks
options = {0 : cell1,
           1 : cell2,
           2 : cell3,
           3 : cell4,
           4 : cell5,
           5 : cell6,
           6 : cell7,
           7 : cell8,
           8 : cell9,
           9 : cell10,
           10 : cell11,
           11 : cell12,
           12 : cell13,
           13 : cell14,
           14 : cell15,
           15 : cell16,
           16 : cell17,
           17 : cell18,
           18 : cell19,
           19 : cell20,
           20 : cell1,
           21 : cell2,
           22 : cell3,
           23 : cell4,
           24 : cell5,
           25 : cell6,
           26 : cell7,
           27 : cell8,
           28 : cell9,
           29 : cell10,
           30 : cell11,
           31 : cell12,
           32 : cell13,
           33 : cell14,
           34 : cell15,
           35 : cell16,
           36 : cell17,
           37 : cell18,
           38 : cell19,
           39 : cell20,
           40 : cell1,
}



















linenumber2 = 0
linenus = 0
substr = "X".lower()          # Substring to search for.
with open ('clean_output14.txt', 'rt') as myfile:
    with open('main_cutput.txt','w') as output:
        for line in myfile:
            linenumber2 = linenumber2 + 1
 #           linenum += 1
           
            if line.lower().find(substr) != -1:
                output.write(line + options[linenumber2-1]())

with open('main_cutput.txt', 'r+') as fp:
    lines = fp.readlines()     # lines is list of line, each element '...\n'
    lines.insert(0, "G28\n")  # you can use any index if you know the line index
    fp.seek(0)                 # file pointer locates at the beginning to write the whole file again
    fp.writelines(lines)
linenum = 0
