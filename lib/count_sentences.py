#!/usr/bin/env python3
class MyString:
    def __init__(self, value=""):
        if isinstance(value, str):
            self.value = value
        else:
            raise ValueError("Value must be a string")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        import re
        sentences = re.split(r'[.!?]+', self.value)
        return len([sentence for sentence in sentences if sentence.strip()])
