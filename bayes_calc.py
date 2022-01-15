#!/usr/bin/env python
"""Bayes Calc: Calculates the value of a bond using Bayes' Rule.
"""

from pyfiglet import Figlet
import numpy as np
from scipy.optimize import newton


def getNumberFromInput(input):
    if "in" in input:
        numbers = input.replace(" ", "").split("in")
        return float(numbers[0]) / float(numbers[1])
    return float(input)

def presentProbabilities(probabilities):
    for key in probabilities.keys():
        print(key + ": " + (8 - len(str(key))) * " " + str(probabilities[key]))

probabilities = dict()
probabilities["P(B)"] = getNumberFromInput(input("Please give the value of P(B): "))
probabilities["P(T|B)"] = getNumberFromInput(input("Please give the value of P(T|B): "))
probabilities["P(T|~B)"] = getNumberFromInput(input("Please give the value of P(T|~B): "))

probabilities["P(~B)"] = 1 - probabilities["P(B)"]
probabilities["P(T)"] = probabilities["P(B)"] * probabilities["P(T|B)"] + probabilities["P(~B)"] * probabilities["P(T|~B)"]
probabilities["P(B|T)"] = (probabilities["P(B)"] * probabilities["P(T|B)"]) / probabilities["P(T)"]

presentProbabilities(probabilities)


