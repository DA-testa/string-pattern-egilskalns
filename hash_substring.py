# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose
    # which input type will follow
    text = input().rstrip()
    if text == "I":
        pattern = input().rstrip()
        data = input().rstrip()

    elif text == "F":
        file = open("tests/06","r")
        text3 = file.read().rstrip().split("\n")
        file.close()
        pattern = text3[0].rstrip()
        data = text3[1].rstrip()
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern,data)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    # and return an iterable variable
    pattern_len = len(pattern)
    text_len = len(text)
    pattern_hash = get_hash(pattern)
    occurances=[]

    for i in range(text_len-pattern_len+1):
        if pattern_hash == get_hash(text[i:i+pattern_len]):
            if pattern == text[i:i+pattern_len]:
                occurances.append(i)
    return occurances

def get_hash(pattern: str) -> int:
    result = 0
    for i in pattern:
        result = (37 * result + ord(i)) % 256
    return result

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
