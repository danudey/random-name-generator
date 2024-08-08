#!/usr/bin/env python3

import string
import random
import argparse

from collections import namedtuple

parser = argparse.ArgumentParser()
parser.add_argument("--matching-letters", "--ubuntu", "-m", action="store_true", default=False, help="Choose words with matching initial letters (similar to Ubuntu's release names)")

def random_letter():
    return random.choice(string.ascii_lowercase)

def choose_random_with_letter(source, letter=None):
    if letter:
        return random.choice([s for s in source if s.startswith(letter)])
    else:
        return random.choice(source)

def get_random_data(letter=None):
    Pair = namedtuple("Pair", "adjective noun")
    adjectives = open("adjectives.txt").read().splitlines()
    nouns = open("nouns.txt").read().splitlines()
    
    adjective = choose_random_with_letter(adjectives, letter)
    noun = choose_random_with_letter(nouns, letter)

    result = Pair(adjective, noun)

    return result

def main():
    args = parser.parse_args()

    if args.matching_letters:
        letter = random_letter()
    else:
        letter = None

    result = get_random_data(letter=letter)
    print(f"{result.adjective} {result.noun}")

if __name__ == "__main__":
    main()

