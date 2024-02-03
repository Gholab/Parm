import re
#les fichiers en entree/sortie
input_file_name = 'input.txt'
output_file_name = 'output.txt'

dico ={
    #operation de registre
    "lsls": ["00000","0100000010"],
    "lsrs": ["00001","0100000011"],
    "asrs": ["00010","0100000100"],
    
    #opérations arithmétiques
    "adds":["0001100","0001110","00110"],
    "subs":["0001101","0001111","00111"],
    "movs":"00100",
    "cmp":"00101",
    
    #data processing
    "ands":"0100000000",
    "eors":"0100000001",
    "adcs":"0100000101",
    "sbsc":"0100000110",
    "rors":"0100000111",
    "tst":"0100001000",
    "rsbs": "0100001001",
    "cmp": "0100001010",
    "cmn": "0100001011",
    "orrs": "0100001100",
    "muls": "0100001101",
    "bics": "0100001110",
    "mvns": "0100001111",
    "str": "10010",
    "ldr": "10011",
    
    #miscellanous
    
    "add": "101100000",
    "sub": "101100001"

}

categories=["#rr5533","rrr7333","#rr7333","r#538","rr1033","[sp]r#538","#107"]
def compilation(instruction):
    return toHexa(instruction_to_binary(instruction))

def instruction_to_binary(instruction):
    str_binary=""
    separate=re.findall(r'[^, ]+', instruction)
    print(separate)
    print(cptReg(separate))
    print(hasImm(separate))
    forme(separate)
    print(forme(separate))
    
    if (forme(separate)=="#rr5533"): #categories[0] instr rd rm #imm5 
        #4 elements dans la liste
        str_binary+=dico[separate[0]][0]
        str_binary+=toBinary(int(separate[3][1:]), 5) # #imm5
        str_binary+=toBinary(int(separate[2][1:]), 3) #  rm
        str_binary+=toBinary(int(separate[1][1:]), 3) #  rd
    elif (forme(separate)=="rrr7333"): #categories[1] instr rd rn rd 
        #4 elements dans la liste
        str_binary+=dico[separate[0]][0]
        str_binary+=toBinary(int(separate[3][1:]), 3) # rm
        str_binary+=toBinary(int(separate[2][1:]), 3) #  rn
        str_binary+=toBinary(int(separate[1][1:]), 3) #  rd
        
    elif (forme(separate)=="#rr7333"):
        #4 elements dans la liste
        str_binary+=dico[separate[0]][1]
        str_binary+=toBinary(int(separate[3][1:]), 3) # rm
        str_binary+=toBinary(int(separate[2][1:]), 3) #  rn
        str_binary+=toBinary(int(separate[1][1:]), 3) #  rd
    
    elif (forme(separate)=="r#538"):
        #3 elements dans la liste
        if separate[0] in ["adds","subs"]:
            str_binary+=dico[separate[0]][2]
            
        else:
            str_binary+=dico[separate[0]]
            
        str_binary+=toBinary(int(separate[1][1:]), 3) #  rd
        str_binary+=toBinary(int(separate[2][1:]), 3) #  imm8
    
    elif (forme(separate)=="rr1033"):
        #3 elements mn ghir rsbs et muls
        str_binary+=dico[separate[0]]
        str_binary+=toBinary(int(separate[2][1:]), 3) # rm
        str_binary+=toBinary(int(separate[1][1:]), 3) # rdn
    
    elif (forme(separate)=="[sp]r#538"):
        print(separate)
        separate.remove('[sp')
        separate[2]=separate[2].replace(']', '')
        print(separate)
        str_binary+=dico[separate[0]]
        str_binary+=toBinary(int(separate[1][1:]), 3) # rt
        str_binary+=toBinary(int(separate[2][1:]), 8) # imm8
    elif (forme(separate)=="#107"):
        str_binary+=dico[separate[0]]
        str_binary+=toBinary(int(separate[2][1:]), 7) # imm7
        print(str_binary) 
        
        
        
        
    
    
        
    
    
    return str_binary   
    

def cptReg(liste):#compte le nombre de registre dans les instructions dupliquées pour déterminer which decoupage to choose
    cpt=0
    for i in range(1,len(liste)):
        if(liste[i][0]=='r'):
            cpt+=1
    return cpt   
def hasImm(liste): #return vrai si il y'a un imm false sinon;
    cpt=0
    for i in range(1,len(liste)):
        if(liste[i][0]=='#'):
            cpt+=1
    if cpt>0:
        return True
    return False
    
 #categories=["#rr5533","rrr7333","#rr7333","r#538","rr1033","[sp]r#538","#107"]   
def forme(liste):#prend en parametre la liste séparéé
    if(liste[0] in ["str","ldr"]):
        return categories[5] # {[sp]r#538}
    elif(cptReg(liste)==1 and hasImm(liste)):
        return categories[3] # {r#538}
    elif(cptReg(liste)==3):
        return categories[1] # {rrr7333}
    elif(cptReg(liste)==2 and not hasImm(liste)):
        return categories[4] # {rr1033}
    elif(cptReg(liste)==0 and hasImm(liste)):
        return categories[6] # {#1O7}
    elif(cptReg(liste)==2 and hasImm(liste) and liste[0] in ["lsls", "lsrs", "asrs"]):
        return categories[0] # {#rr5533}
    elif(cptReg(liste)==2 and hasImm(liste) and liste[0] in ["adds", "subs"]):
        return categories[2] # {#rr7333}
    else:
        return "compilation error"
    
def toBinary(nb, place): #place que ça prend
    res=""
    while nb!=0:
        res=str(nb%2)+res
        nb=int(nb/2)
    res="0"*(place-len(res))+res
    
    return res

def toHexa(str_nb): #prend en parametre le resultat en string des 16 bits d'instruction en binaire
    place=4
    decimal_number = int(str_nb, 2)
    # Convert integer to hexadecimal
    hexadecimal_representation = hex(decimal_number)
    res=(place-len(hexadecimal_representation[2:]))*"0"+(hexadecimal_representation[2:])
    return res     


with open(input_file_name, 'r') as input_file:
    # Read the contents of the input file
    with open(output_file_name, 'w') as output_file:
        output_file.write("v2.0 raw\n")  # Write header outside the loop
        
        for line in input_file:
            line = line.rstrip() #enlève les "/n"
            content = compilation(line) 
            output_file.write(content)
            output_file.write(" ") 


