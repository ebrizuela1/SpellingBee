# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 14:37:19 2025

@author: troy
"""
from sbtrie import SBTrie 
from trie import Trie

# the following functions are to exist with the parameters as written
# the autograder may call these functions

def getNewDictionary(sbt, filename):
  # enter needed code here for command 1
  sbt.clear()
  sbt.getFromFile(filename)

def updateDictionary(sbt, filename):
  # enter needed code here for command 2
  sbt.getFromFile(filename)
  

def setupLetters(sbt, letters):
  # enter needed code here for command 3
  letters_clean = ""
  for char in letters:
    char_clean = char.lower()
    if char_clean.isalpha() and char_clean not in letters_clean:
      letters_clean += char_clean
  if len(letters_clean) != 7:
    print("Invalid letter set")
  else:
    sbt.discovered_words = Trie()
    sbt.current_score = 0
    sbt.pangram_found = False
    sbt.bingo_found = False
    sbt.start_letters = {}
    sbt.central_letter = letters_clean[0]
    sbt.allowed_letters = {}
    for letter in letters_clean:
      sbt.allowed_letters[letter] = True
  
def showLetters(sbt):
  # enter needed code here for command 4
  other_letters = ""
  for char in sbt.allowed_letters:
    if char != sbt.central_letter:
      other_letters += char
  other_letters_sorted = "".join(sorted(other_letters))

  print(f"Central Letter: {sbt.central_letter}") 
  print(f"6 Other Letters: {','.join(other_letters_sorted)}")

def attemptWord(sbt, word):
  # enter needed code here for command 5
  res = sbt.isNewSBWord(word)
  match res:
    case -1:
      print("word is too short")
    case -2:
      print("word is missing central letter")
    case -3:
      print("word contains invalid letter")
    case -4:
      print("word is not in the dictionary")
    case -5:
      print("word has already been found")
    case _:
      sbt.addFoundWord(word)
      sbt.current_score += res

      bingo_message = ""

      if sbt.hasBingo():
        bingo_message = ", Bingo scored"
      pangram_message = ", Pangram found" if sbt.isPangram(word) else ""
      print(f"found {word} {res} {'points' if res>1 else 'point'}, total {sbt.current_score} points{pangram_message}{bingo_message}")

def showFoundWords(sbt):
  # enter needed code here for command 6
  p_msg = ""
  b_msg = ""
  if sbt.pangram_found:
    p_msg = ", Pangram found"
  if sbt.bingo_found:
    b_msg = ", Bingo scored"
  print(f"{sbt.discovered_words.word_count} words found, total {sbt.current_score}{p_msg}{b_msg}")

def showAllWords(sbt):
  # enter needed code here for command 7
  other_letters = ""
  for char in sbt.allowed_letters:
    if char != sbt.central_letter:
      other_letters += char
  all_sb_words = sbt.sbWords(sbt.central_letter,other_letters)

  bingo_dict = {}

  for word in all_sb_words:
    length = len(word)
    bingo_dict[word[0]] = True
    pangram = " Pangram" if sbt.isPangram(word) else ""

    if length > 17:
      print(f"{word} {length}{pangram}")
    else:
      print(f"{word:<19}{length}{pangram}")
  if len(bingo_dict) == 7:
    print("Bingo found")




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