# Morse-Translator


Morse  Translator is a program converts English text to Morse code and vice versa.
The text should be read from a file and output should be written to another. 



## Prerequisites

you should install the unit testing framework  using pip in the Terminal 

```
pip install unittest
```
## Morse syntax
Morse code expresses characters as pulses of different durations.Short signals are referred to as "dots", long signals as "dashes".
 We'll refer to "dots" as the character "•" and "dashes" as "-".and the following table will be our dictionary 
 ![Alt text](img/Morse_Dic.png?raw=true "Title")


<br />In this program each character of Morse code should be separated with a dot "."  
example we have in English 

```
sos
```
the result after translation should be 
```
•••.−−−.•••
```
In addition the words are separated with a normal space " " as the following example shows 
```
hello world
```
would be :
```
••••.•.•-••.•-••.--- •--.---.•-•.•-••.-•• 
```


## Morse Translator Classes:
the code contain 2 classe which are 
## Translator class:
this class is for translating the text to Morse or backwards .infact this class is constructed by two fundamnetal method:
### Translator Encrypt method:
this function is responsible for encrypting English text to Morse code taking "MORSE_CODE_DICT" as reference dictionary.
the method works as the following:<br />
    <br />*convert all the string(message) entred to upper case<br />
    <br />*check the letter of the message 1 by one <br />
         <br />-if it has equivalent in dictionary then it stors the value in cipher varible and add a point to sparate the characters
         <br />-otherwise it stops the program 
   
    *in case we have new line the output is kept constant.
    *in case there is a tab we interpret it as a space.
    *in case the letter is a space then we add a space to the morse code.

at last the function retun the morse code that is identical to the English text entred. 

### Translator decrypt  method:
this method is used for converting the morse code to its corresponding English text.
<br />
the method works as the following:<br />
*we add space to the message entred in case it does not ontain one at the end ; this is used to allow the function convert the last character<br /> 
<br />
*check each letter of the message one by one <br />
                   
    *in case  letter is neither space nor dot'.' and has a value in the dictionary the it will be stored in citext 
    *in case the letter is a point or a space then we know that we have collected al the parts of the character then we pass it to the  <br />dictionary to give its equivalent English character
    *in case the is a double dot consecutive  the program will stop and exit 
 at the End(if all characters are valid) it returns the string but in upper case.
 ## Morse file_manipulator class: 
 this class is used for reading from a text file using the method "read" that returns "fline" which stores all the content of the input text file.
 <br />
 in this class we have also the method "write" that will receive parameter data and stores it in the output file.
 <br />
 In addition the class has constructor to initialize the input and output file directory.
 <br />
 finaly we have the read_test that is used for test session.  
 ## Morse main function:
 in the main function and special case for this assignment we would ask the user for input file path and output file path.

 then we pass the values to the "read" and "write" methods.
 <br />
 after we ask the user to choose in which direction the translation would be ("1" for English to Morse;"2" for Morse to English )
 and we call the correcpoding method from tranlator class.
 
 ## How to use it:
 in order to compile the code write in terminal (after entring the folder of the code)
 ```
python code.py
 ```
 then enter the input file path and output file path for example:
 ```
Enter the input file path : input.txt
Enter the output file path : output.txt
 ```
after that you should select which direction of translation do you want (English to Morse or Morse to English) by just typing 1 or 2
```
could you select which kind of translation do you want ?
 1-English to morse
 2-Morse to English

Enter the corresponding number :
 ```
at the end if there was no problem during the translation the output data should be in the output file where you indicate its path at the beginning.









## The Test
We used unit test framework .In the test_code file we created a class named "Test_Translator" where we try t test the most important class of this program which is the "translator" class
###test_encrupt method :
In this method we were able to generate 3 kinds of tests on the "encrypt" method of the original code.
```
*test an english text that contain only valid character using the file "test _ english text input.txt"
*test all the valid English characters using the file "test_valid character English_input.txt"
*test all the invalid English characters using the file "test_invlid character English.txt"


 ```     
 
###test_decrypt method :
In this method we were able to generate 4 kinds of tests on the "dncrypt" method of the original code.
```
*test a text writen in morse code using the file "test_text Morse input.txt"
*test test all Valid Morse character in morse code using the file "test_valid characters Morse_input.txt"
*test test all inValid Morse character in morse code using the file "test_invalid character Morse.txt"
*test The result of double dots consecutive

 ```   
   



### Running the tests

after installing unit testing framework we should write the following command in the terminal.  

```
python -m unittest test_code
```
the result is :
```
Ran 2 tests in 0.281s

OK
```
this means that the two function were tested correctly and no problem has been noticed.

## Limitations and suggestion to the user:
-you should avoid closing input file with a space at the end that should output a correct code but with additional space or dot'.' that won't affect the meaning. 
<br />
-try to not make two spaces in the morse code this may let the program add a separation dot.



