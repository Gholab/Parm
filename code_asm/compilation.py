import re
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
    

}
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
       
def instruction_ToBinary(instruction): #instruction est une String
    #separate=re.findall(r'[^\W\d_]+(?<!r)|\d+', instruction) #separation est une liste
    separate=re.findall(r'[^, ]+', instruction)
    
    
    str_binary=""
    cpt=cptReg(separate)
    Imm=hasImm(separate)
    casPart=False
    casReverse=True
    if(separate[0] in {"adds","subs"}):
        casPart=True
        if(cpt==3): #cas il y'a 3 registres ex: adds r2, r3, r2
           str_binary+=dico[separate[0]][0]
        elif(cpt==2): #cas il y'a 2 registres ex: adds r2, r3, #2
           str_binary+=dico[separate[0]][1]
        elif(cpt==1): #cas il y'a 2 registres ex: adds r2, r3, #2
           str_binary+=dico[separate[0]][2]
           casReverse=False
    elif(separate[0] in {"lsls","lsrs","asrs"}):
        if(Imm):
           str_binary+=dico[separate[0]][0]
        else:
           str_binary+=dico[separate[0]][1]
    elif(separate[0] in dico): #cas il y'a 1 registres ex: adds r2, #154
        str_binary+=dico[separate[0]] #mettre l'operation en premier
        if(cpt==1): 
            casReverse=False
        
       
    i=len(separate)-1
    j=1 #pour le cas pas reverse, on commence à 1 parce que on a déja rempli pour le separate[0]
    if(casReverse):
        while(i!=0):
            if(casPart):     
                if(cpt==3 or cpt==2):
                    str_binary+=toBinary(int(separate[i][1:]),3) #ajouter le registre ou l'imm
                if(cpt==1):
                    if(separate[i][0]=='#'):
                        str_binary+=toBinary(int(separate[i][1:]),8) #ajouter le imm
                        
                    elif(separate[i][0]=='r'):
                        
                        str_binary+=toBinary(int(separate[i][1:]),3) #ajouter le registre
                        
                
            
            elif((separate[i][1:]).isdigit()):
                
                if(separate[i][0]=='#'):
                    str_binary+=toBinary(int(separate[i][1:]),5) #ajouter le imm
                elif(separate[i][0]=='r'):
                    str_binary+=toBinary(int(separate[i][1:]),3) #ajouter le registre
            i-=1 #l'ordre est inversé
    else:
        #pas de reverse; instruction de type adds r5, #218
        while(j!=len(separate)):
            #if(cpt==1):
            if(separate[j][0]=='#'):
                        
                str_binary+=toBinary(int(separate[j][1:]),8) #ajouter le imm
                        
            elif(separate[j][0]=='r'):
                        
                str_binary+=toBinary(int(separate[j][1:]),3) #ajouter le registre
                        
            j+=1
       
    return str_binary
    
        
def compilation(instruction):
    return toHexa(instruction_ToBinary(instruction)) 




with open(input_file_name, 'r') as input_file:
    # Read the contents of the input file
    with open(output_file_name, 'w') as output_file:
        output_file.write("v2.0 raw\n")  # Write header outside the loop
        
        for line in input_file:
            line = line.rstrip() #enlève les "/n"
            content = compilation(line) 
            output_file.write(content)
            output_file.write(" ")      
