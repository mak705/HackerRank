def split_and_join(line):
    # write your code here
    letter = line.split(" ")
    return ("-".join(letter))
split_and_join('thie ois')

def split_and_join(line):
    return("-".join(line.split()))
split_and_join('thie ois')

def split_and_join(line):
    return(line.replace(" ","-"))
split_and_join('thie ois')

def split_and_join(line):
    print(*line.split(), sep='-')
split_and_join('thie ois')


