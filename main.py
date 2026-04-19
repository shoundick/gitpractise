#!/usr/bin/env python3
"""
Simple Python script for Git practice.
This script demonstrates basic Python functionality.
"""

import mymessage
from datetime import date

def main():
    print("Hello, World!")
    print("This is a Git practice repository.")
    print("Current Python version:", __import__('sys').version)
    mymessage.message1(date.today())

if __name__ == "__main__":
    main()
