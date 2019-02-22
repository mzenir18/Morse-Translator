# Morse-Translator


Morse  Translator is a program coverts English text to Morse code and vice versa.
The text should be read from a file and output should be written to another. 



## Prerequisites

you should install the unit testing framework  using pip in the Terminal 

```
pip install unittest
```
## Morse syntax
Morse code expresses characters as pulses of different durations.Short signals are referred to as "dots", long signals as "dashes".
 We'll refer to "dots" as the character "•" and "dashes" as "-".and the following table will be our dictionary IMAGE
 In this program each charcter of Morse code should be separated with a dot "."  
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
 ## Morse file_manipulator class: 
 this class is used for reading from a text file using the method read that returns "fline" which stores all the content of the input text file.
 <br />
 in this class we have also the method write that will receive parameter data and stores it in the output file.
 <br />
 In addition the class has constructor to initialize the input and output file directory.
 <br />
 finaly we have the read_test that is used for test session.  
 ## Morse main function:
 in the main function and special case for this assignment we would ask the user for input file path and output file path.

 then we pass the values to the "read" and "write" methods.
 <br />
 after we ask the user to choose in which direction the translation wuold be ("1" for English to Morse;"2" for Morse to English )
 and we call the correcpoding method from tranlator class.
 
 ## How to use it:
 in order to compile the code write in terminal (after entring the folder of the code)
 ```
>python code.py
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









## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
