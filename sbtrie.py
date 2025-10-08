# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 15:17:47 2025

@author: troy
"""
from trie import Trie

class SBTrie(Trie):
    """ A class for the Spelling Bee Trie """
    def __init__ (self):
        super().__init__()
        self.central_letter = ''
        self.allowed_letters = {}
        self.discovered_words = Trie()
        self.current_score = 0
        self.pangram_found = False
        self.bingo_found = False
        self.start_letters = {}
        
    
    def getLetters(self) -> str:
        letters = []
        for char in self.allowed_letters:
            if char != self.central_letter:
                letters.append(char)
        sorted_letters = "".join(sorted(letters))

        return self.central_letter + sorted_letters

    def isNewSBWord(self, word:str) ->int:
        if len(word) < 4:
            return -1
        if self.central_letter not in word:
            return -2
        for char in word:
            if char not in self.allowed_letters:
                return -3

        if not self.search(word):
            return -4

        if self.discovered_words.search(word):
            return -5
        
        score = 0
        if len(word) == 4:
            score = 1
        else:
            score = len(word)

        if self.isPangram(word):
            score += 7

        return score

    def isPangram(self, word:str) -> bool:
        for char in self.allowed_letters:
            if char not in word:
                return False
        return True

    def hasBingo(self) -> bool:
        if self.bingo_found:
            return True

        if len(self.start_letters) == len(self.allowed_letters):
            self.bingo_found = True
            return True
        return False

    def getFoundWords(self) -> [str]:
        return self.discovered_words.words()
        
    def sbWords(self, centralLetter: str, otherLetters:str) -> [str]:
        self.central_letter = centralLetter
        self.allowed_letters[centralLetter] = True
        for char in otherLetters:
            self.allowed_letters[char] = True

        

        word_list = []
        for char in self.root.children:
            if char in self.allowed_letters:
                self._sbWordsHelper(self.root.children[char],char, word_list)

        return sorted(word_list)
    
    def _sbWordsHelper(self, curNode, curString, word_list):
        if curNode.isWord and len(curString) >= 4 and self.central_letter in curString:
            word_list.append(curString)
        
        for char in curNode.children:
            if char in self.allowed_letters:
                self._sbWordsHelper(curNode.children[char],curString + char,word_list)
    
    def addFoundWord(self, word:str):
        self.discovered_words.insert(word)
        if self.isPangram(word):
            self.pangram_found = True
        self.start_letters[word[0]] = True