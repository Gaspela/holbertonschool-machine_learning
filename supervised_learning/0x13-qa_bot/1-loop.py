#!/usr/bin/env python3
"""
Create the loop
"""

in_q = ''
while (in_q is not None):
    """
    Bot Question
    """
    in_q = input("Q: ")
    if in_q.lower() in ['bye', 'exit', 'quit', 'goodbye']:
        print("A: Goodbye")
        break
    print("A: ")
