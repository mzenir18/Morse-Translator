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
### Morse Encrypt method:
this function is responsible for encrypting English text to Morse code taking "MORSE_CODE_DICT" as reference dictionary.
the method works as the following:
    \n*convert all the string(message) entred to upper case
    \n*check the letter of the message 1 by one 
         \n-if it has equivalent in dictionary then it stors the value in cipher varible and add a point to sparate the characters
         \n-otherwise it stops the program 
   
    *in case we have new line the output is kept constant 
    *in case there is a tab we interpret it as a space
    *in case the letter is a space then we add a space to the morse code

at last the function retun the morse code that is identical to the English text entred 

### Morse decrypt  method:






Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

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
