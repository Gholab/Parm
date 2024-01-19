import re
input_file_name = 'input.txt'
output_file_name = 'output.txt'


    
    
dico ={
    #operation de registre
    "lsls": "00000",
    "lsrs": "00001",
    "asrs": "00010", 

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
    
    
    
    
        
def instruction_ToBinary(instruction): #instruction est une String
    #separate=re.findall(r'[^\W\d_]+(?<!r)|\d+', instruction) #separation est une liste
    separate=re.findall(r'[^, ]+', instruction)
    
    
    str_binary=""
        
    if(separate[0] in dico):
        str_binary+=dico[separate[0]] #mettre l'operation en premier
    
    i=len(separate)-1
    while(i!=0):
        
        if((separate[i][1:]).isdigit()):
            
            if(separate[i][0]=='#'):
                str_binary+=toBinary(int(separate[i][1:]),5) #ajouter le imm
            elif(separate[i][0]=='r'):
                str_binary+=toBinary(int(separate[i][1:]),3) #ajouter le registre
        i-=1 #l'ordre est inversé
        
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
