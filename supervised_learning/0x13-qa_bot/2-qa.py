#!/usr/bin/env python3
"""
Answer Questions
"""

question_answer = __import__('0-qa').question_answer


def answer_loop(reference):
    """
    Bot Question
    """
    in_qa = ''
    while (in_qa is not None):
        in_qa = input("Q: ")
        if in_qa.lower() in ['bye', 'exit', 'quit', 'goodbye']:
            print("A: Goodbye")
            break
        answer = question_answer(in_qa, reference)
        if answer is None or answer == '':
            print("A: Sorry, I do not understand your question.")
            continue
        print("A: {}".format(answer))
