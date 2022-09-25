#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None or len(sentence) == 0:
        size = 0
        char_1 = None
    else:
        size = len(sentence)
        char_1 = sentence[0]
    return (size, char_1)


if __name__ == '__main__':
    print(multiple_returns('i am a boy'))
    print(multiple_returns(None))
    print(multiple_returns(''))
