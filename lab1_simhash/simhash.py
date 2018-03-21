import sys
import hashlib

scale = 16 # hexadecimal
num_of_bits = 4

def hexconvert(hex):
    return bin(int(hex, scale))[2:].zfill(num_of_bits)

def comparehash(first,second,diff):
    dif = 0
    zipper = zip(hexconvert(first),hexconvert(second))
    for tup in zipper:
        if tup[0] != tup[1]:
            dif+=1
        if dif > diff:
            return False
    return True

def simhash(text):
    sh = [0] * 128
    member_dict = dict()
    hexnum_dict = dict()
    members = text.split()
    for member in members:
        binary = ""
        if(member not in member_dict):
            hash = hashlib.md5(member.encode('utf-8'))
            member_dict[member] = hash.hexdigest()
        for c in member_dict[member]:
            if(c not in hexnum_dict):
                # solving the left-side trailing zero problem
                hexnum_dict[c] = bin(int(c, scale))[2:].zfill(num_of_bits)
            binary+=str(hexnum_dict[c])
        i = 0
        for c in binary:
            if c == '1':
                sh[i]+=1
            else:
                sh[i]-=1
            i+=1
    for i in range(0,128):
        if sh[i] >= 0:
            sh[i] = 1
        else:
            sh[i] = 0
    simhash = ''.join(str(x) for x in sh)
    return hex(int(simhash,2))

def main():
    hashes = []
    src = open("a.in", 'r')
    # src = sys.stdin
    # read number of input lines
    input_lines = int(src.readline())
    # read input lines
    for i in range(0,input_lines):
        hashes.append(simhash(src.readline()))
    # read number of queries
    queries = int(src.readline())
    # read queries
    for i in range(0,queries):
        query = [int(x) for x in src.readline().split()]
        exhash = hashes[query[0]]
        diff = query[1]
        cntr = 0
        for h in hashes:
            if h == exhash or comparehash(h,exhash,diff):
                cntr+=1
        cntr -= 1
        print(cntr)


# print(simhash("fakultet elektrotehnike i racunarstva"))
main()