import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%) :":
    "Utwórz klasę o nazwie %%%, która jest %%%.",
    "class %%%(object): \n\tdef__init__(self, ***)":
    "Klasa %%% ma __init__, które przyjmuje parametry self i ***.",
    "class %%%(object):\n\tdef***(self, @@@)":
    "Klasa %%% ma funkcję ***, któa przyjmuje parametry self i @@@.",

}

#kontynuacja...