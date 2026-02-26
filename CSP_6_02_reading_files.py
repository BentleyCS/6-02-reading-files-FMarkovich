#You must make and submit your own test file and txt file with this assignment.

def toString(fileName):
    #This function returns the text from a given file.
    #Any new lines are written as \n
    f = open(fileName)
    out = ""
    for line in f:
        out += line
    return out
#print(toString("ExampleText.txt")=="Here is the text\ni am another line")

def longestLine(fileName):
    #Given a file return the longest line from within that file
    max = 0
    f=open(fileName)
    for line in f:
        if len(line) > max:
            max = len(line)
    return line

def toBinary(fileName):
    #Given a file that is only 0's and 1's return a list of the file broken into bytes.
    #An example return might be ['01101001', '00101010', '1010']
    f=open(fileName)
    bits = ''.join(f.read().split())
    print ([bits[i:i + 8] for i in range(0, len(bits), 8)])
    return [bits[i:i + 8] for i in range(0, len(bits), 8)]
toBinary("6.02 Binary.txt")