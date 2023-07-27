#!/usr/bin/python3
def multiple_returns(sentence):
    
    phrase = tuple(sentence)
    length = len(sentence)
    
    if len(sentence) != 0:
        package = (length, phrase[0])
        return package
    else:
        packages = (length, None)
        return packages
    
    