#Simple Program that convert text from English to Morse and vice versa
#read the Input to be translated from an input  file and append the result of translation in an output file 

import sys  
import os
class Translator:
    """
    Class to encapsulate mapping of A-Z, 0-9 and the symboles(',' '.' '?' '/' '@')  to their corresponding morse value 
    and vise versa.
    Morse code expresses characters as pulses of different durations.
    Short signals are referred to as "dots", long signals as "dashes".
    We'll refer to "dots" as the character "•" and "dashes" as "-"
    Example:  "A" translates to "dot", "dash" in morse.
              In our dictionary, we'll store the key "A" with value "•-"
    Dictionary transcribed from international morse code
    
    """
    ''' 
    VARIABLE KEY 
    'cipher' -> 'stores the morse translated form of the english string' 
    'decipher' -> 'stores the english translated form of the morse string' 
    'citext' -> 'stores morse code of a single character' 
    'i' -> 'keeps count of the dot separator(.) between morse characters' 
    'message' -> 'stores the string to be encoded or decoded' 
    '''
   # Dictionary representing the morse code chart 

    # Function to encrypt the string 
    # according to the morse code chart
    def encrypt(self,message,testing=False): 
        self.MORSE_CODE_DICT = { 'A':'•-', 'B':'-•••',
                        'C':'-•-•', 'D':'-••', 'E':'•',
                        'F':'••-•', 'G':'--•', 'H':'••••',
                        'I':'••', 'J':'•---', 'K':'-•-',
                        'L':'•-••', 'M':'--', 'N':'-•',
                        'O':'---', 'P':'•--•', 'Q':'--•-',
                        'R':'•-•', 'S':'•••', 'T':'-',
                        'U':'••-', 'V':'•••-', 'W':'•--',
                        'X':'-••-', 'Y':'-•--', 'Z':'--••',
                        '1':'•----', '2':'••---', '3':'•••--',
                        '4':'••••-', '5':'•••••', '6':'-••••',
                        '7':'--•••', '8':'---••', '9':'----•',
                        '0':'-----', ',':'--••--', '.':'•-•-•-',
                        '?':'••--••', '/':'-••-•', '@':'•--•-•',
                        }




        self.message=message.upper()+' '

        self.cipher = ''

        
        for letter in self.message:
            if letter != ' ':
                # Looks up the dictionary and adds the 
                # correspponding morse code 
                # along with a dot(.) to separate 
                # morse codes for different characters 
                if letter in self.MORSE_CODE_DICT:
                    #check if the letter exist in the dictionary
                    #then it stores that letter 
                    self.cipher += self.MORSE_CODE_DICT[letter] +'.'
                #case of New line we keep the cipher as it is
                elif letter == "\n":
                    self.cipher ==self.cipher
                #case of tab we add a space
                elif letter == "\t":
                    self.cipher +=" "

                else:
                    #letter does not exist in the dictionary 
                    
                    if(testing):
                     #For Testing Purpose   
                        return -1
                    else:
                    #orginary usage
                    #stop the program and exit 
                        print("there is invalid character\n")
                        print(letter)
                   
                        sys.exit() 

            # 1 space indicates different word 
            # then we separate the two words with a space 
            else :
                #in case of a space we should delete the separation
                # dot(.) of the last letter in the word
                self.cipher = self.cipher[:-1]
                #we add here a space to the result
                #to separate the words
                self.cipher += ' '

        return self.cipher

    # Function to decrypt the string
    #from morse to english
    
    def decrypt(self,message,testing=False): 
        # Dictionary representing the morse code chart
        self.MORSE_CODE_DICT = { 'A':'•-', 'B':'-•••',
                        'C':'-•-•', 'D':'-••', 'E':'•',
                        'F':'••-•', 'G':'--•', 'H':'••••',
                        'I':'••', 'J':'•---', 'K':'-•-',
                        'L':'•-••', 'M':'--', 'N':'-•',
                        'O':'---', 'P':'•--•', 'Q':'--•-',
                        'R':'•-•', 'S':'•••', 'T':'-',
                        'U':'••-', 'V':'•••-', 'W':'•--',
                        'X':'-••-', 'Y':'-•--', 'Z':'--••',
                        '1':'•----', '2':'••---', '3':'•••--',
                        '4':'••••-', '5':'•••••', '6':'-••••',
                        '7':'--•••', '8':'---••', '9':'----•',
                        '0':'-----', ', ':'--••--', '.':'•-•-•-',
                        '?':'••--••', '/':'-••-•', '@':'•--•-•',
                        }
    # extra space added at the end to access the 
    # last morse code 
        if message[-1]==" ":
            self.message=message
        else:
            self.message=message+' '

        self.decipher = ''
        self.citext = ''
        self.decipher = ''
        self.citext = ''
        for letter in self.message:

            # checks for space 
            #check for dot(.)
            if (letter != ' ' and letter != '.'): 
                if letter in iter(self.MORSE_CODE_DICT.values()):
                #check if the letter exist in the dictionary
                #then it stores that letter 
               
                # counter to keep track of dots 
                    i = 0

                # storing morse code of a single character 
                    self.citext += letter
                else:
                #letter does not exist in the dictionary
                    
                    if (testing):
                    #For Testing Purpose  
                        return -2
                    else:
                        print ("there is invalid Morse character\n")
                        print (letter)
                    
                        sys.exit()

            # in case of space 
            elif letter ==' ':
                if self.citext=='':
                    print("invalid space character")
                else:
                    i = 0
                    self.decipher += list(self.MORSE_CODE_DICT.keys())[list(self.MORSE_CODE_DICT
                        .values()).index(self.citext)]
                    self.citext = ''
                    self.decipher += ' '



            # in case of a dot(.)
            elif letter=='.': 
                # if i = 1 that indicates a new character 
                i += 1

                # if i = 2 that indicates an invalid morse code 
                if i == 2 : 
                    
                    if (testing):
                    #For Testing Purpose  
                        return -3
                    else:
                    #normal usage 
                    #stop the program and exit 
                        print ("there  is an invalid morse code due to double dot in a single row \n")

                    
                        sys.exit()                     
                #here we confirm that the dot(.) indicates 
                #word reading is finnished 
                
                else: 


                    #check if citext is not empty
                    if self.citext=='':
                        print("invalid space character")

                    else:
                        # accessing the keys using their values (reverse of encryption)
                        self.decipher += list(self.MORSE_CODE_DICT.keys())[list(self.MORSE_CODE_DICT
                            .values()).index(self.citext)]
                        self.citext = ''

        return self.decipher

    


# In[2]:


class file_manipulator:
    '''
  class for file manupilation contains constructor to intialise 
  the input file path and output file path then passing those 
  data to read method and write method
  
    '''
    ''' 
    VARIABLE KEY 
    'self.input_path' -> 'stores the input file directory' 
    'self.output_path' -> 'stores the output file directory' 
    'line' -> 'stores single line of the input file content ' 
    'fline' -> 'stores the all  line of the input file content'
    'data' -> 'stores the data wanted to be written  '
    
    '''    
    
    
    input_path=""
    output_path=""
    def __init__(self, input_path, output_path):
        self.input_path= input_path
        self.output_path= output_path 
    
    
    
    #Reading from the input file
    def read (self):
        
        fline = ""
        if not os.path.isfile(self.input_path):
            
            print("File path {} does not exist. Exiting...".format(self.input_path))
            sys.exit()
    
        with open(self.input_path) as fp:  
            #read the first line
            line = fp.readline()
            #check iff there are more lines in the file
            while line:
                fline +=line
                line = fp.readline()
            #add a space to the string
            #when we finnish reading the file

        return fline 
    #test reading file
    def read_test (self,input_path):

        fline = ""
        self.input_path=input_path
        if not os.path.isfile(self.input_path):

            print("File path {} does not exist. Exiting...".format(self.input_path))
            sys.exit()

        with open(self.input_path) as fp:
            #read the first line
            line = fp.readline()
            #check iff there are more lines in the file
            while line:
                fline +=line
                line = fp.readline()
            #add a space to the string
            #when we finnish reading the file

        return fline


    #write to the output file
    def write (self,data):
        f= open(self.output_path,"a+")
        f.write(data)
        f.close()
    


# In[3]:


def main():
    '''
  Main function start by asking the user for input and output file path .
  according to user decision the function call either encrypt funtion (English To Morse)
  or decrypt funtion (Morse To English)
    '''

    ''' 
    VARIABLE KEY 
    'input_path' -> 'stores the input file directory' 
    'output_path' -> 'stores the output file directory' 
    'decision' -> 'stores tanslation direction  chosen by the user   ' 
    'translation' -> 'object of Translator class '
    'txt' -> 'object of file_manipulator class   '
    
    '''
    print(" welcome to morse english translator \n")
    #Ask the User for Input and output file path
    input_path=input('Enter the input file path : ')
    output_path=input('Enter the output file path : ') 
    #ask the user in which direction do you want to translate
    print("could you select which kind of translation do you want ?\n 1-English to morse \n 2-Morse to English \n  ")
    decision=input('Enter the corresponding number : ')
    #create object of each class
    translation = Translator()
    txt = file_manipulator(input_path,output_path)       
    
    input_data=txt.read()
    #translate from English to Morse
    if decision=='1' :
        output_data = translation.encrypt(input_data)
        txt.write(output_data)
        print("your translation(ENGLISH to MORSE ) is successful")
    
    #translate from Morse to English
    elif decision=='2' :
        output_data=translation.decrypt(input_data)
        txt.write(output_data)
        print("your translation (MORSE to ENGLISH ) is successful")

    else:
        print("invalid decision input ")
  

     # Executes the main function 
if __name__ == '__main__': 
    main() 







