#testing file
import unittest
import sys
import os
from code import Translator
from code import file_manipulator



class Test_Translator(unittest.TestCase):
    '''
    Class for testing the methods  of translator. starts first with the "encrypt" method
    tested here by the funtion "test_encrypt" where it take 3 different tests
    the second method "decrypt" tested through "test_decrypt" function covering
    4 diffrent tests

    '''
    ''' 
    VARIABLE KEY 
    'self.input_test' -> 'stores the input test file content' 
    'self.output_test' -> 'stores the output test file content' 
    'read_test' -> 'function impoted fro the original code to read the test files  ' 
    
    '''


    def test_encrypt(self):
        #test a correct English text
        self.input_test=file_manipulator.read_test(self,"encrypt_test\\test _ english text input.txt")
        self.output_test=file_manipulator.read_test(self,"encrypt_test\\test _ english text output.txt")
        self.assertEqual(Translator.encrypt(self,self.input_test,True),self.output_test)



        #test all Valid English character
        self.input_test=file_manipulator.read_test(self,"encrypt_test\\test_valid character English_input.txt")
        self.output_test=file_manipulator.read_test(self,"encrypt_test\\test_valid character English_output.txt")
        self.assertEqual(Translator.encrypt(self,self.input_test,True),self.output_test)

        #test invalid English character
        self.input_test=file_manipulator.read_test(self,"encrypt_test\\test_invlid character English.txt")
        for letter in self.input_test:
            self.assertEqual(Translator.encrypt(self,self.input_test,True),-1)


    def test_decrypt(self):

        #test a text writen in morse code
        self.input_test=file_manipulator.read_test(self,"decrypt_test\\test_text Morse input.txt")
        self.output_test=file_manipulator.read_test(self,"decrypt_test\\test_text Morse output.txt")
        self.assertEqual(Translator.decrypt(self,self.input_test,True),self.output_test)

        #test all Valid Morse character
        self.input_test=file_manipulator.read_test(self,"decrypt_test\\test_valid characters Morse_input.txt")
        self.output_test=file_manipulator.read_test(self,"decrypt_test\\test_valid characters Morse_output.txt")
        self.assertEqual(Translator.decrypt(self,self.input_test,True),self.output_test)

        #test invalid Morse character
        self.input_test=file_manipulator.read_test(self,"decrypt_test\\test_invalid character Morse.txt")
        for letter in self.input_test:
            self.assertEqual(Translator.decrypt(self,self.input_test,True),-2)

        #test The result of double dots consecutive
        self.input_test=file_manipulator.read_test(self,"decrypt_test\\test_consecutive double dot.txt")
        self.assertEqual(Translator.decrypt(self,self.input_test,True),-3)
