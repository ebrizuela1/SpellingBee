# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 15:22:23 2025

@author: troy
"""

class Node:
    def __init__(self,ch=0,isWord=False):
        self.ch = ch
        self.isWord = isWord
        self.children = {}
        
class Trie:

    """ A class for the Trie """
    def __init__ (self):
        self.word_count = 0
        self.root = Node()
        
    def getFromFile(self,filename: str) -> bool:
        try:
            with open(filename,'r') as file_in:
                for word in file_in:
                    word_clean = word.strip().lower()
                    if word.isalpha():
                        self.insert(word_clean)
                return True
        except Exception as e:
            return False
                
    
    def insert(self,word: str) -> bool:
        if not word.isalpha():
            return False

        cur_node = self.root
        for ch in word:

            if ch.lower() not in cur_node.children:
                cur_node.children[ch.lower()] = Node(ch.lower())

            cur_node = cur_node.children.get(ch.lower())

        if cur_node.isWord == True:
            return False
        else:
            self.word_count += 1
            cur_node.isWord = True
            return True
    
    def search(self,word:str) -> bool:
        cur_node = self.root
        for ch in word:
            if ch.lower() not in cur_node.children:
                return False
            else:
                cur_node = cur_node.children[ch.lower()]
        return cur_node.isWord

    def remove(self,word:str) -> bool:
        cur_node = self.root
        for ch in word:
            if ch.lower() not in cur_node.children:
                return False
            else:
                cur_node = cur_node.children[ch.lower()]
        if cur_node.isWord:
            cur_node.isWord = False
            self.word_count -= 1
            return True
        else:
            return False
    
    def clear(self) -> bool:
        if self.word_count == 0:
            return False
        self.word_count = 0
        self.root = Node()
        return True
    
    def wordCount(self) -> int:
        return self.word_count
    

    def words(self) -> [str]:
        cur_node = self.root
        wordsList = []
        for cur in cur_node.children:
            self.wordsHelper(cur_node.children[cur],cur,wordsList)
        return wordsList

    def wordsHelper(self, curNode, curString, wordList:[str]):
        if curNode.isWord:
            wordList.append(curString)

        for cur in curNode.children:
            self.wordsHelper(curNode.children[cur],curString + cur.ch,wordList)