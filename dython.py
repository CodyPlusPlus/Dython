# Filename:         dython.py
# Author:           Cody Stuck
# Purpose:          Dython is a console die parser and roller designed for rpg tabletop games. 
#
# Instructions:     Multiple die-pool rolls with variable sides and integer bonuses/penalties are supported.
#                   The parser uses Dijkstra's two-stack algorithm, and is quite picky about syntax.
#                   Terms should be supplied in the format of "(n)d(x)" where (n) is the number of dice
#                   and (x) is the number of sides on each dice. Bonuses/penalties are simply integers.
#                   Spaces should surround each term and operator, and the terms should be surrounded in parentheses.
#                   ex. "( 1d20 + 2 )"
#                   ex. "( ( 1d20 + 2d4 ) - 2 )" 
#               

import sys
import random

def isNum(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

class Roller:
    def __init__(self):
        self.pool = []
        self.rolls = []
        self.total = 0

    def roll(self):
        self.rolls = [random.randint(1, s) for s in self.pool]
        self.total = sum(self.rolls)

    def printRolls(self):
        for i in range(len(self.rolls)):
            print(self.rolls[i],"(d", self.pool[i],")")
        
    def printTotal(self):
        print("Total", self.total)
            
def rollAllTerms(termList):
    for t in termList:
        if 'd' in t:
            t = str(evaluateTerm(t))

def evaluateTerm(raw):
    if type(raw) == 'int':
        return raw
    elif isNum(raw):
        return int(raw)
    else:
        poolArgs = raw.split("d")
        dicePool = Roller()
        dicePool.pool = [int(poolArgs[1]) for d in range(int(poolArgs[0]))]
        dicePool.roll()
        dicePool.printRolls()
        return dicePool.total

def evaluateRoll(raw):
    args = raw.split()
    ops = []
    terms = []
    
    for s in args:
        if s == "(":
            pass
        elif s == "+":
            ops.append(s)
        elif s == "-":
            ops.append(s)
        elif s == ")":
            o = ops.pop()
            t = terms.pop()
            if o == "+":
                t = int(terms.pop()) + int(t)
            elif o == "-":
                t = int(terms.pop()) - int(t)
            terms.append(int(t))
        else:
            terms.append(int(evaluateTerm(s)))
    return terms.pop()

print(evaluateRoll("( 1d20 + 2 )"))

# start of script

args = str(sys.argv)

