#!/usr/bin/env python3
"""
Multi-reference Question Answering
"""

question_answer = __import__('0-qa').question_answer
semantic_search = __import__('3-semantic_search').semantic_search


def qa_bot(corpus_path):
    """
    Bot Question
    """
    in_qa = ''
    while (in_qa is not None):
        in_qa = input("Q: ")
        if in_qa.lower() in ['bye', 'exit', 'quit', 'goodbye']:
            print("A: Goodbye")
            break
        reference = semantic_search(corpus_path, in_qa)
        answer = question_answer(in_qa, reference)
        if answer == '':
            print("A: Sorry, I do not understand your question.")
            continue
        print("A: {}".format(answer))
