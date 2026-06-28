from typing import List

histories = []

def add(history):
    histories.insert(0, history)

def get_all():
    return histories