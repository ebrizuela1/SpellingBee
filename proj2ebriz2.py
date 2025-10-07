# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 14:37:19 2025

@author: troy
"""
from sbtrie import SBTrie 

# the following functions are to exist with the parameters as written
# the autograder may call these functions

def getNewDictionary(sbt, filename):
  # enter needed code here for command 1
  pass

def updateDictionary(sbt, filename):
  # enter needed code here for command 2
  pass

def setupLetters(sbt, letters):
  # enter needed code here for command 3
  pass

def showLetters(sbt):
  # enter needed code here for command 4
  pass

def attemptWord(sbt, word):
  # enter needed code here for command 5
  pass

def showFoundWords(sbt):
  # enter needed code here for command 6
  pass

def showAllWords(sbt):
  # enter needed code here for command 7
  pass

def displayCommands():
  print( "\nCommands are given by digits 1 through 9\n")
  print( "  1 <filename> - read in a new dictionary from a file")
  print( "  2 <filename> - update the existing dictionary with words from a file")
  print( "  3 <7letters> - enter a new central letter and 6 other letters")
  print( "  4            - display current central letter and other letters")
  print( "  5 <word>     - enter a potential word")
  print( "  6            - display found words and other stats")
  print( "  7            - list all possible Spelling Bee words from the dictionary")
  print( "  8            - display this list of commands")
  print( "  9            - quit the program")
  print()


def spellingBee():
  print("Welcome to Spelling Bee Game")
  
  sbt = SBTrie()

  displayCommands()

  while (True):
    line = input ("cmd> ")
    command = line[0]
    #print ("Debug 0:" + line + "***" + command + "***")
    
    # clear input from any previous value
    args = ""

    
    if(command == '1'):
        args = line[1:].strip()
        #print ("Debug 1:" + args + "***")
        getNewDictionary(sbt, args)

    if(command == '2'):
        args = line[1:].strip()
        #print( "Debug 2:" + args + "***")
        updateDictionary(sbt, args)
        
    if(command == '3'):
        args = line[1:].strip()
        #print( "Debug 3:" + args + "***")
        setupLetters(sbt, args)


    if(command == '4'):
        showLetters(sbt)

    if(command == '5'):
        args = line[1:].strip()
        #print ( "Debug 5:" + args + "***")
        attemptWord(sbt, args)

    if(command == '6'):
        showFoundWords(sbt)

    if(command == '7'):
        showAllWords(sbt)

    
    if(command == '8' or command == '?'):
        displayCommands()
    
    if(command == '9' or command == 'q'):
        break
    

  return

if __name__=="__main__":
  spellingBee()