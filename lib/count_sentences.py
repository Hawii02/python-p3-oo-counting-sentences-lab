#!/usr/bin/env python3
class MyString:
    def __init__(self, value=''):
        self.value = value
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value =value
        else:
            print("The value must be a string.")
    def is_sentence(self):
        if self.value.endswith('.'):
            return True
        else:
            return False
    def is_question(self):
        if self.value.endswith('?'):
            return True
        else:
            return False
    def is_exclamation(self):
        if self.value.endswith('!'):
            return True
        else:
            return False
    # def count_sentences(self):
    #     count = 0
    #     for char in self.value:
    #         if char == '.':
    #             count += 1
    #     return count
        
    # def count_sentences(self):
    #     return len([sentence for sentence in re.split(r'[.!?]', self._value.strip()) if sentence])
        
    def count_sentences(self):
        partially_replaced = self.value.replace('!', '.')
        fully_replaced = partially_replaced.replace('?', '.')
        sentences_list = fully_replaced.split('.')
        no_empty_sentences = list(filter(None, sentences_list))
        return len(no_empty_sentences)
          
    

            
