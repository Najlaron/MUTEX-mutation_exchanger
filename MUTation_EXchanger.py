#|  WELCOME TO MUTEX, SIMPLE SCRIPT TO INTRODUCE POINT MUTATIONS TO YOUR SEQUENCE |
#|                        ---------  MUTEX  ---------                             |
#|--------------------------------------------------------------------------------|

import os

def mutate(seq, mutations, fasta_name = ">mutated_sequence"):
    seq = seq.replace("\n", "")
    mutex_seq = ""
    mut_list = trim_mutations(mutations)
    j = 0
    count = [0,0]
    for i, char in enumerate(seq):
        if (j < len(mut_list) and i+1 == mut_list[j][1]):
            count[1] += 1
            if (char == mut_list[j][0]):
                mutex_seq += mut_list[j][2].lower()
                count[0] += 1
            else:
                mutex_seq += char
                j += 1
                i += 1
                continue
            j += 1
        else:
            mutex_seq += char
    print("Your mutated sequence: ")
    print(mutex_seq)
    print("Mutations were found successfully in: " + str(count[0]) + "/" + str(count[1]))
    mutex_seq = mutex_seq.replace("-", "")
    return mutex_seq, fasta_name

def trim_mutations(mutations):
    mut_list = []
    mutations = mutations.upper()
    ln = len(mutations)
    this = ""
    j = 1
    while(j < ln):
        c1 = mutations[j-1]
        c2 = mutations[j]
        i = 0
        if (ord(c1) >=  65 and ord(c1) <= 90 and ord(c2) >=  48 and ord(c2) <= 57):
            this = c1
            nm_s = c2
            mutation = ""
            for i in range(j+1, ln):
                c = mutations[i]
                if (c == '\n'):
                    break
                if (ord(c) >=  48 and ord(c) <= 57):
                    nm_s += c
                elif(ord(c) >=  65 and ord(c) <= 90 or ord(c) == 45):
                    mutation += c
                else:
                    break
            if (mutation != ""):
                mut_list.append([this, int(nm_s), mutation])
                i = 0
        j += i + 1
    mut_list = sorted(mut_list, key = lambda x: x[1], reverse = False)
    print(mut_list)
    return mut_list

def from_fasta(path):
    with open(path, 'r') as f:
        lines = ""
        name = ">mutated_sequence"
        for line in f:
            if (line == "\n"):
                continue
            if (line[0] == '>'):    
                name = line
            else:
                lines += line
    lines = lines.replace('\n','')
    print(lines)
    return lines, name

def save_as_fasta(path, sequence, fasta_name):
    f = open(path + ".fasta", 'w')
    ln = len(sequence)
    f.write(str(fasta_name) + "\n")
    k = 0
    for i in range(ln):
        f.write(sequence[i])
        k += 1
        if(k == 60):
            f.write("\n")
            k = 0        
    f.close()
    return True

def input_lines():
    lines = ""
    line = input()
    while (line != ''):
        lines += line + '\n' 
        line = input()
    return lines[:-1]

def main_menu():
    welcome()
    fasta_name = ""
    command = 'Y'
    while(command != 'N'):
        print("----------------------------------------------------------------------------------------------")
        print("Input sequence as raw text. | Or input 'F' to import fasta or text file.")
        sequence = input_lines()
        command = sequence.upper()
        if (command == 'F'):
            try:
                print("Input the path (name) of your fasta/txt file.")
                path = input()
                sequence, fasta_name = from_fasta(path)
            except:
                command = 'Y'
                print("Couldn't find file with given name.")
                print("Be sure to add file type, such as: .fasta or .txt")
                print("Check that your file is in correct directory or input whole path.")
                print("Your parent directory is: " + str(os.path.abspath(os.pardir)))
                continue
        print("Input mutations as text in some form such as: AA1 index AA2")
        mutations = input_lines()
        mutex_seq, fasta_name = mutate(sequence, mutations, fasta_name)
        print("----------------------------------------------------------------------------------------------")
        print("Input:     'Y', if you wanna mutate another sequence.\n           'S', if you wanna save result as fasta file.\n           'C', if you wanna print out result sequence without '-' for deletion.\n           'N', if you wanna end MUTEX.")
        command = input().upper()
        if (command == 'C'):
            print(mutex_seq)
        elif (command == 'S'):
            print("Input the path (name) to save your result as fasta.")
            path = input()
            if(fasta_name == ""):
                fasta_name = ">"+str(path)
            save_as_fasta(path, mutex_seq, fasta_name)
            print("Input:     'Y', if you wanna mutate another sequence.\n           'N', if you wanna end MUTEX.")
            command = input().upper()            
    print("Goodbye and thanks for using MUTEX!")
    input()
    return True

def welcome():
    print(" _ _ _       _                           _         _    __ __  _ _  ___  ___ __  _  ")
    print("| | | | ___ | | ___  ___ ._ _ _  ___   _| |_  ___ <_>  |  \  \| | ||_ _|| __>\ \/   ")
    print("| | | |/ ._>| |/ __'/ . \| ' ' |/ ._>   | |  / . \ _   |     || ' | | | | _>  \ \   ")
    print("|__/_/ \___.|_|\___.\___/|_|_|_|\___.   |_|  \___/<_>  |_|_|_|`___' |_| |___>_/\_\  ")
    print("                                                                                    ")
    print("               _           _    _                            _                            ")
    print("._ _ _  _ _  _| |_  ___  _| |_ <_> ___ ._ _    ___ __   ___ | |_  ___ ._ _  ___  ___  _ _ ")
    print("| ' ' || | |  | |  <_> |  | |  | |/ . \| ' |  / ._>\ \// __'| . |<_> || ' |/ . |/ ._>| '_>")
    print("|_|_|_|`___|  |_|  <___|  |_|  |_|\___/|_|_|  \___./\_\\___.|_|_|<___||_|_|\_. |\___.|_|  ")
    print("                                                                           <___'          ")
    return True

#---------------------------------------------------------------
#MAIN
main_menu()
