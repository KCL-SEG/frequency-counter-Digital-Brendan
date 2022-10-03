"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
from collections import Counter

def frequencies(items):
    frequencies = Counter([str(x) for x in items])
    return frequencies
