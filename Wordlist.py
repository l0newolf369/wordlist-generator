# this code is used to create probable password with the given inputs like alphabates,special character or symbol and number of digits
# this code create passwords then store them in a file which needed to be named and then it store the file in a given location


import os
import colorama
from colorama import init,Fore,Back,Style 

init()


# code to save the passwod in a .txt file 
def sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4):
    filenm = str(input(Fore.LIGHTBLUE_EX + "  Name the file in which the passwords will be stored : "))
    print(Fore.RESET)
    current_dir = os.path.dirname(__file__)
     

    #output = "code to save the out put as a file in the file system ."

    output_file = os.path.join(current_dir,filenm)

    with open(output_file, "w") as file:
        for pswd1 in pswds1:
            file.write(pswd1 + "\n")
            
        for pswd2 in pswds2:
            file.write(pswd2 + "\n")
            
        for pswd3 in pswds3:
            file.write(pswd3 + "\n")
        
        for pswd4 in pswds4:
            file.write(pswd4 + "\n")
    
    print(f"Output saved to the file{output_file}")
        


# the codes of the functions to generate multipule passwords as optioned 


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#                                                          numbers + alphabate + special character


def _4dgtnum_nm_spc():             # 4 digit number + name + special char
    pswds1 = []
    pswds2 = []
    pswds3 = []
    pswds4 = []
    
    
    n1 = 0
    while(n1 < 10):
        p1 = "000"+str(n1)+name+spclchar
        pswds1.append(str(p1))
        n1 += 1
            
    n2 = 10
    while(n2 < 100):
        p2 = "00"+str(n2)+name+spclchar
        pswds2.append(str(p2))
        n2 += 1
        
    n3 = 100
    while(n3 < 1000):
        p3 = "0"+str(n3)+name+spclchar
        pswds3.append(str(p3))
        n3 += 1
    
    n4 = 1000
    while(n4 < 10000):
        p4 = str(n4)+name+spclchar
        pswds4.append(str(p4))
        n4 += 1
    
    return pswds1,pswds2,pswds3,pswds4

def _3dgtnum_nm_spc():                # 3 digit number + name + special character
    
    pswds1 = []
    pswds2 = []
    pswds3 = []
    pswds4 = []
    
    n1=0
    while(n1 < 10):
        p1 = "00"+str(n1)+name+spclchar
        pswds1.append(str(p1))
        n1 += 1
            
    n2 = 10
    while(n2 < 100):
        p2 = "0"+str(n2)+name+spclchar
        pswds2.append(str(p2))
        n2 += 1
        
    n3 = 100
    while(n3 < 1000):
        p3 = str(n3)+name+spclchar
        pswds3.append(str(p3))
        n3 += 1
    
    return pswds1,pswds2,pswds3,pswds4

def _2dgtnum_nm_spc():                # 2 digit number + name + special character
    
    pswds1 = []
    pswds2 = []
    pswds3 = []
    pswds4 = []
    
    
    n1=0
    while(n1 < 10):
        p1 = "0"+str(n1)+name+spclchar
        pswds1.append(str(p1))
        n1 += 1
            
    n2 = 10
    while(n2 < 100):
        p2 = str(n2)+name+spclchar
        pswds2.append(str(p2))
        n2 += 1
        
    
    return pswds1,pswds2,pswds3,pswds4

def _1dgtnum_nm_spc():                # 1 digit number + name + special character
    
    pswds1 = []
    pswds2 = []
    pswds3 = []
    pswds4 = []
    
    
    n1=0
    while(n1 < 10):
        p1 = str(n1)+name+spclchar
        pswds1.append(str(p1))
        n1 += 1
        
    
    return pswds1,pswds2,pswds3,pswds4




#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


#                                                              numbers + special character + alphabate

def _4dgtnum_spc_nm():                   #  4 digit number + special character + name
    
    pswds1 = []
    pswds2 = []
    pswds3 = []
    pswds4 = []
 
    n1 = 0
    while(n1 < 10):
        p1= "000"+str(n1)+spclchar+name
        pswds1.append(str(p1))
        n1 += 1
            
    n2 = 10
    while(n2 < 100):
        p2= "00"+str(n2)+spclchar+name
        pswds2.append(str(p2))
        n2 += 1
        
        
    n3 = 100
    while(n3 < 1000):
        p3= "0"+str(n3)+name+spclchar
        pswds3.append(str(p3))
        n3 += 1
        
    
    n4 = 1000
    while(n4 < 10000):
        p4= str(n4)+spclchar+name
        pswds4.append(str(p4))
        n4 += 1
        
    return pswds1,pswds2,pswds3,pswds4


def _3dgtnum_spc_nm():                   #  3 digit number + special character + name
    
    pswds1 = []
    pswds2 = []
    pswds3 = []
    pswds4 = []
 
    n1 = 0
    while(n1 < 10):
        p1= "00"+str(n1)+spclchar+name
        pswds1.append(str(p1))
        n1 += 1
            
    n2 = 10
    while(n2 < 100):
        p2= "0"+str(n2)+spclchar+name
        pswds2.append(str(p2))
        n2 += 1
        
        
    n3 = 100
    while(n3 < 1000):
        p3= str(n3)+name+spclchar
        pswds3.append(str(p3))
        n3 += 1
        
    return pswds1,pswds2,pswds3,pswds4

def _2dgtnum_spc_nm():                   #  2 digit number + special character + name
    
    pswds1 = []
    pswds2 = []
    pswds3 = []
    pswds4 = []
 
    n1 = 0
    while(n1 < 10):
        p1= "0"+str(n1)+spclchar+name
        pswds1.append(str(p1))
        n1 += 1
            
    n2 = 10
    while(n2 < 100):
        p2= str(n2)+spclchar+name
        pswds2.append(str(p2))
        n2 += 1
        
    return pswds1,pswds2,pswds3,pswds4

def _1dgtnum_spc_nm():                   #  1 digit number + special character + name
    
    pswds1 = []
    pswds2 = []
    pswds3 = []
    pswds4 = []
 
    n1 = 0
    while(n1 < 10):
        p1= str(n1)+spclchar+name
        pswds1.append(str(p1))
        n1 += 1
        
    return pswds1,pswds2,pswds3,pswds4



    

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


#                                                              alphabater + special character + numbers 



def nm_spc_4dgtnum():                   # name+ 2 digit number  + special char
    
    pswds1 = []
    pswds2 = []
    pswds3 = []
    pswds4 = []
 
    n1 = 0
    while(n1 < 10):
        p1= name+spclchar+"000"+str(n1)
        pswds1.append(str(p1))
        n1 += 1
            
    n2 = 10
    while(n2 < 100):
        p2= name+spclchar+"00"+str(n2)
        pswds2.append(str(p2))
        n2 += 1
        
        
    n3 = 100
    while(n3 < 1000):
        p3= name+spclchar+"0"+str(n3)
        pswds3.append(str(p3))
        n3 += 1
        
    
    n4 = 1000
    while(n4 < 10000):
        p4= name+spclchar+str(n4)
        pswds4.append(str(p4))
        n4 += 1
        
    return pswds1,pswds2,pswds3,pswds4


def nm_spc_3dgtnum():                   # name+ 2 digit number  + special char 
    
    pswds1 = []
    pswds2 = []
    pswds3 = []
    pswds4 = []
 
    n1 = 0
    while(n1 < 10):
        p1= name+spclchar+"00"+str(n1)
        pswds1.append(str(p1))
        n1 += 1
            
    n2 = 10
    while(n2 < 100):
        p2= name+spclchar+"0"+str(n2)
        pswds2.append(str(p2))
        n2 += 1
        
        
    n3 = 100
    while(n3 < 1000):
        p3= name+spclchar+str(n3)
        pswds3.append(str(p3))
        n3 += 1
        
    return pswds1,pswds2,pswds3,pswds4


def nm_spc_2dgtnum():                   # name+ 2 digit number  + special char  
    
    pswds1 = []
    pswds2 = []
    pswds3 = []
    pswds4 = []
 
    n1 = 0
    while(n1 < 10):
        p1= name+spclchar+"0"+str(n1)
        pswds1.append(str(p1))
        n1 += 1
            
    n2 = 10
    while(n2 < 100):
        p2= name+spclchar+str(n2)
        pswds2.append(str(p2))
        n2 += 1
        
    return pswds1,pswds2,pswds3,pswds4


def nm_spc_1dgtnum():                   # name+ 1 digit number  + special char 
    
    pswds1 = []
    pswds2 = []
    pswds3 = []
    pswds4 = []
 
    n1 = 0
    while(n1 < 10):
        p1= name+spclchar+str(n1)
        pswds1.append(str(p1))
        n1 += 1
            
    return pswds1,pswds2,pswds3,pswds4




#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


#                                                               alphabates + numbers + special character




def nm_4dgtnum_spc():                   # name + 4 digit number + special character 
    
    pswds1 = []
    pswds2 = []
    pswds3 = []
    pswds4 = []
 
    n1 = 0
    while(n1 < 10):
        p1= "000"+str(n1)+spclchar+name
        pswds1.append(str(p1))
        n1 += 1
            
    n2 = 10
    while(n2 < 100):
        p2= "00"+str(n2)+spclchar+name
        pswds2.append(str(p2))
        n2 += 1
        
        
    n3 = 100
    while(n3 < 1000):
        p3= "0"+str(n3)+name+spclchar
        pswds3.append(str(p3))
        n3 += 1
        
    
    n4 = 1000
    while(n4 < 10000):
        p4= str(n4)+spclchar+name
        pswds4.append(str(p4))
        n4 += 1
        
    return pswds1,pswds2,pswds3,pswds4


def nm_3dgtnum_spc():                   # name + 3 digit number + special character 
    
    pswds1 = []
    pswds2 = []
    pswds3 = []
    pswds4 = []
 
    n1 = 0
    while(n1 < 10):
        p1= "00"+str(n1)+spclchar+name
        pswds1.append(str(p1))
        n1 += 1
            
    n2 = 10
    while(n2 < 100):
        p2= "0"+str(n2)+spclchar+name
        pswds2.append(str(p2))
        n2 += 1
        
        
    n3 = 100
    while(n3 < 1000):
        p3= str(n3)+name+spclchar
        pswds3.append(str(p3))
        n3 += 1
        
    return pswds1,pswds2,pswds3,pswds4

def nm_2dgtnum_spc():                   # name + 2 digit number + special character 
    
    pswds1 = []
    pswds2 = []
    pswds3 = []
    pswds4 = []
 
    n1 = 0
    while(n1 < 10):
        p1= "0"+str(n1)+spclchar+name
        pswds1.append(str(p1))
        n1 += 1
            
    n2 = 10
    while(n2 < 100):
        p2= str(n2)+spclchar+name
        pswds2.append(str(p2))
        n2 += 1
        
    return pswds1,pswds2,pswds3,pswds4

def nm_1dgtnum_spc():                   # name + 1 digit number + special character 
    
    pswds1 = []
    pswds2 = []
    pswds3 = []
    pswds4 = []
 
    n1 = 0
    while(n1 < 10):
        p1= str(n1)+spclchar+name
        pswds1.append(str(p1))
        n1 += 1
        
    return pswds1,pswds2,pswds3,pswds4



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


#                                                               special character + alphabates + numbers


def spc_nm_4dgtnum():                   # special character + name + 4 digit number 
    
    pswds1 = []
    pswds2 = []
    pswds3 = []
    pswds4 = []
 
    n1 = 0
    while(n1 < 10):
        p1= spclchar+name+"000"+str(n1)
        pswds1.append(str(p1))
        n1 += 1
            
    n2 = 10
    while(n2 < 100):
        p2= spclchar+name+"00"+str(n2)
        pswds2.append(str(p2))
        n2 += 1
        
        
    n3 = 100
    while(n3 < 1000):
        p3= spclchar+name+"0"+str(n3)
        pswds3.append(str(p3))
        n3 += 1
        
    
    n4 = 1000
    while(n4 < 10000):
        p4= spclchar+name+str(n4)
        pswds4.append(str(p4))
        n4 += 1
        
    return pswds1,pswds2,pswds3,pswds4


def spc_nm_3dgtnum():                   # special character + name + 3 digit number 
    
    pswds1 = []
    pswds2 = []
    pswds3 = []
    pswds4 = []
 
    n1 = 0
    while(n1 < 10):
        p1= spclchar+name+"00"+str(n1)
        pswds1.append(str(p1))
        n1 += 1
            
    n2 = 10
    while(n2 < 100):
        p2= spclchar+name+"0"+str(n2)
        pswds2.append(str(p2))
        n2 += 1
        
        
    n3 = 100
    while(n3 < 1000):
        p3= spclchar+name+str(n3)
        pswds3.append(str(p3))
        n3 += 1
        
    return pswds1,pswds2,pswds3,pswds4


def spc_nm_2dgtnum():                   # special character + name + 2 digit number 
    
    pswds1 = []
    pswds2 = []
    pswds3 = []
    pswds4 = []
 
    n1 = 0
    while(n1 < 10):
        p1= spclchar+name+"0"+str(n1)
        pswds1.append(str(p1))
        n1 += 1
            
    n2 = 10
    while(n2 < 100):
        p2= spclchar+name+str(n2)
        pswds2.append(str(p2))
        n2 += 1
        
    return pswds1,pswds2,pswds3,pswds4


def spc_nm_1dgtnum():                   # special character + name + 1 digit number 
    
    pswds1 = []
    pswds2 = []
    pswds3 = []
    pswds4 = []
 
    n1 = 0
    while(n1 < 10):
        p1= spclchar+name+str(n1)
        pswds1.append(str(p1))
        n1 += 1
        
    return pswds1,pswds2,pswds3,pswds4



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



#                                                                special character + numbers + alphabates



def spc_4dgtnum_nm():                   # special character +  4 digit number + name
    
    pswds1 = []
    pswds2 = []
    pswds3 = []
    pswds4 = []
 
    n1 = 0
    while(n1 < 10):
        p1= spclchar+"000"+str(n1)+name
        pswds1.append(str(p1))
        n1 += 1
            
    n2 = 10
    while(n2 < 100):
        p2= spclchar+"00"+str(n2)+name
        pswds2.append(str(p2))
        n2 += 1
        
        
    n3 = 100
    while(n3 < 1000):
        p3= spclchar+"0"+str(n3)+name
        pswds3.append(str(p3))
        n3 += 1
        
    
    n4 = 1000
    while(n4 < 10000):
        p4= spclchar+str(n4)+name
        pswds4.append(str(p4))
        n4 += 1
        
    return pswds1,pswds2,pswds3,pswds4

 
def spc_3dgtnum_nm():                   # special character +  3 digit number + name
    
    pswds1 = []
    pswds2 = []
    pswds3 = []
    pswds4 = []
 
    n1 = 0
    while(n1 < 10):
        p1= spclchar+"00"+str(n1)+name
        pswds1.append(str(p1))
        n1 += 1
            
    n2 = 10
    while(n2 < 100):
        p2= spclchar+"0"+str(n2)+name
        pswds2.append(str(p2))
        n2 += 1
        
        
    n3 = 100
    while(n3 < 1000):
        p3= spclchar+str(n3)+name
        pswds3.append(str(p3))
        n3 += 1
        
    return pswds1,pswds2,pswds3,pswds4


def spc_2dgtnum_nm():                   # special character +  2 digit number + name
    
    pswds1 = []
    pswds2 = []
    pswds3 = []
    pswds4 = []
 
    n1 = 0
    while(n1 < 10):
        p1= spclchar+"0"+str(n1)+name
        pswds1.append(str(p1))
        n1 += 1
            
    n2 = 10
    while(n2 < 100):
        p2= spclchar+str(n2)+name
        pswds2.append(str(p2))
        n2 += 1
        
    return pswds1,pswds2,pswds3,pswds4

def spc_1dgtnum_nm():                   # special character +  1 digit number + name
    
    pswds1 = []
    pswds2 = []
    pswds3 = []
    pswds4 = []
 
    n1 = 0
    while(n1 < 10):
        p1= spclchar+str(n1)+name
        pswds1.append(str(p1))
        n1 += 1
        
    return pswds1,pswds2,pswds3,pswds4



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX








def start():
    print(Style.BRIGHT + Fore.LIGHTRED_EX + Back.GREEN  +"")
    
    print(" _________________________________________________")
    print("|                                                 |")
    print("|        -----------------------------            |")
    print("|        :    WORDLISTS GENERATOR    :            |")
    print("|        -----------------------------            |")
    print("|_________________________________________________|")
    print(Style.RESET_ALL)
    print(Fore.RESET+"")
    print(Fore.LIGHTYELLOW_EX)
    print('''
                                                                                
                 Look the options carefully.... then choose the passwordtype
                 which you need and enter the respective number contained in
                 the squre braces just left to  your choosen option .
            __________________________________________________________________
            ------------------------------------------------------------------  
             _______________________________________________________________ 
            |                                                               |      
            |     [ 1]  4 digit numbers + alphabates + special character    | 
            |     [ 2]  3 digit numbers + alphabates + special character    |
            |     [ 3]  2 digit numbers + alphabates + special character    |
            |     [ 4]  1 digit numbers + alphabates + special character    |
            |                                                               |
            |     [ 5]  4 digit numbers + special character + alphabates    |
            |     [ 6]  3 digit numbers + special character + alphabates    |
            |     [ 7]  2 digit numbers + special character + alphabates    |
            |     [ 8]  1 digit numbers + special character + alphabates    |
            |                                                               |
            |     [ 9]  alphabates + special character + 4 digit numbers    |
            |     [10]  alphabates + special character + 3 digit numbers    |
            |     [11]  alphabates + special character + 2 digit numbers    |
            |     [12]  alphabates + special character + 1 digit numbers    |
            |                                                               |
            |     [13]  alphabates + 4 digit numbers + special character    |
            |     [14]  alphabates + 3 digit numbers + special character    |
            |     [15]  alphabates + 2 digit numbers + special character    |
            |     [16]  alphabates + 1 digit numbers + special character    |
            |                                                               |
            |     [17]  special character + alphabates + 4 digit numbers    |
            |     [18]  special character + alphabates + 3 digit numbers    |
            |     [19]  special character + alphabates + 2 digit numbers    |
            |     [20]  special character + alphabates + 1 digit numbers    |
            |                                                               |
            |     [21]  special character + 4 digit numbers +alphabates     |
            |     [22]  special character + 4 digit numbers +alphabates     |
            |     [23]  special character + 4 digit numbers +alphabates     |
            |     [24]  special character + 4 digit numbers +alphabates     |
            |                                                               |
            |---------------------------------------------------------------|
            |                                                               |
            |       all 4 digit number pins                                 |
            |       all 6 digit number passwords                            |
            |       all 8 digit number passwords                            |
            |                                                               |
            |     You can get these passwords file in default password      |
            |        file folder...navigate there if you need these...      |  
            |                                                               |
            |                                                               |
            |     [0]  exit                                                 |
            |                                                               |
            |_______________________________________________________________|
            
            ''')
    
    print("")
    print(Fore.RESET)

    print("")
    chs = str(input(Fore.LIGHTGREEN_EX + "     Enter your choice : "))
    print(" ")
    print(Fore.RESET)
    
    
    if chs == "1":
        
        pswds1,pswds2,pswds3,pswds4 = _4dgtnum_nm_spc()
        
        sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4)

        os.system('clear')
        
        start()
        
    
    elif chs == "2":
        
        pswds1,pswds2,pswds3,pswds4 = _3dgtnum_nm_spc()
        
        sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4)
        
        os.system('clear')
        
        start()
    
    
    elif chs == "3":
        
        pswds1,pswds2,pswds3,pswds4 = _2dgtnum_nm_spc()
        
        sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4)
        
        os.system('clear')
        
        start()
    
    
    elif chs == "4":
        
        pswds1,pswds2,pswds3,pswds4 = _1dgtnum_nm_spc()
        
        sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4)
        
        os.system('clear')
        
        start()
    
    

        
    
    elif chs == "5":
        
        pswds1,pswds2,pswds3,pswds4 = _4dgtnum_spc_nm() 
        
        sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4)
        
        os.system('clear')
        
        start()
        
        
    elif chs == "6":
        
        pswds1,pswds2,pswds3,pswds4 = _3dgtnum_spc_nm()
        
        sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4)
        
        os.system('clear')
        
        start()


    elif chs == "7":
        
        pswds1,pswds2,pswds3,pswds4 = _2dgtnum_spc_nm()
        
        sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4)
        
        os.system('clear')
        
        start()


    elif chs == "8":
        
        pswds1,pswds2,pswds3,pswds4 = _1dgtnum_spc_nm()
        
        sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4)
        
        os.system('clear')
        
        start()
   
     
    
        
    elif chs == "9":
        
        pswds1,pswds2,pswds3,pswds4 = nm_spc_4dgtnum()
        
        sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4)
        
        os.system('clear')
        
        start()
    
    elif chs == "10":
        
        pswds1,pswds2,pswds3,pswds4 = nm_spc_3dgtnum()
        
        sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4)
        
        os.system('clear')
        
        start()
    
    elif chs == "11":
        
        pswds1,pswds2,pswds3,pswds4 = nm_2dgtnum_spc()
        
        sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4)
        
        os.system('clear')
        
        start()
    
    elif chs == "12":
        
        pswds1,pswds2,pswds3,pswds4 = nm_spc_1dgtnum()
        
        sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4)
        
        os.system('clear')
        
        start()
        



    elif chs == "13":
        
        pswds1,pswds2,pswds3,pswds4 = nm_4dgtnum_spc()
        
        sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4)
        
        os.system('clear')
        
        start()
    
    elif chs == "14":
        
        pswds1,pswds2,pswds3,pswds4 = nm_3dgtnum_spc()
        
        sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4)
        
        os.system('clear')
        
        start()
    
    elif chs == "15":
        
        pswds1,pswds2,pswds3,pswds4 = nm_2dgtnum_spc()
        
        sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4)
        
        os.system('clear')
        
        start()
        
    elif chs == "16":
        
        pswds1,pswds2,pswds3,pswds4 = nm_1dgtnum_spc()
        
        sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4)
        
        os.system('clear')
        
        start()
        


    
    elif chs == "17":
        
        pswds1,pswds2,pswds3,pswds4 = spc_nm_4dgtnum()
        
        sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4)
        
        os.system('clear')
        
        start()
    
    elif chs == "18":
        
        pswds1,pswds2,pswds3,pswds4 = spc_nm_3dgtnum()
        
        sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4)
        
        os.system('clear')
        
        start()
    
    elif chs == "19":
        
        pswds1,pswds2,pswds3,pswds4 = spc_nm_2dgtnum()
        
        sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4)
        
        os.system('clear')
        
        start()
        
    elif chs == "20":
        
        pswds1,pswds2,pswds3,pswds4 = spc_nm_1dgtnum()
        
        sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4)
        
        os.system('clear')
        
        start()
    
    
    
    
    elif chs == "21":
        
        pswds1,pswds2,pswds3,pswds4 = spc_4dgtnum_nm()
        
        sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4)
        
        os.system('clear')
        
        start()
        
    elif chs == "22":
        
        pswds1,pswds2,pswds3,pswds4 = spc_3dgtnum_nm()
        
        sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4)
        
        os.system('clear')
        
        start()
    
    elif chs == "23":
        
        pswds1,pswds2,pswds3,pswds4 = spc_2dgtnum_nm()
        
        sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4)
        
        os.system('clear')
        
        start()
    
    elif chs == "24":
        
        pswds1,pswds2,pswds3,pswds4 = spc_1dgtnum_nm()
        
        sv_pswd_as_txt(pswds1,pswds2,pswds3,pswds4)
        
        os.system('clear')
        
        start()
        
        


    elif chs == "0":
        os.system('clear')
        print(Fore.LIGHTCYAN_EX)
        print("                   _______________________________________________")
        print("                  |                                               |")
        print("                  |       -:THANK YOU TO RUN THIS CODE :-         |")
        print("                  |_______________________________________________|")
        print("")
        print("")
        print(Fore.RESET)

    else:
        print(Fore.LIGHTRED_EX + "  ..Please , enter a choice from the options only.........")
        print(Fore.RESET)
        os.system('clear')
        start()


    
print(Fore.LIGHTCYAN_EX + '''  INSTRUCTIONS : 
      
    >> Here you have to enter alphabates which is the name or any word phrase of target.
    >> Then you have to enter a special symbol or character of , if he has.
    >> If you don't have any special character then just pree enter without typing anything.
    >> Then you have to enter the number of digit according it's need.
      
    ... Read these instructions and use the tool carefully. ''')
print(Fore.RESET)
print(" ")
print(Fore.LIGHTGREEN_EX + " ")

name = str(input("    Enter the name or the name :  "))
print(" ")
spclchar = str(input("    Enter the special character or symbols if you have :  "))   
print(" ")
print(Fore.RESET)
start()


