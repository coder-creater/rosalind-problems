import random
def hyp(a, b):
    print((a**2)+(b**2))

def slicer(string, a, b, c, d):
    print(string[a:b+1], string[c:d+1])

string = 'wt89Vgeebkoxj0DxFjvYTd5s6D2GThelodermaNXHSB7NsV3gl7e9zPquFcinereavqLPkq32FbxfvgBlcamD5Wglbeh5T43G1YXjbJCKXiDa6FVWNfmTSCV5GiAJWWnBmbaDkifaHhcRbN0mJ68vZAxycv5IWVzC9p.'
#slicer(string, 28, 37, 58, 64)

def odd_summer(a, b):
    count = 0
    for i in range(a, b+1):
        if i%2 == 1:
            count += i
    print(count)

def even_lines(name):
    with open(f'rosalind-problems/data_files/rosalind_{name}.txt', 'r') as file:
        data = file.read()
    locs = []
    for i in range(0, len(data)):
        if data[i] == '\n':
            locs.append(i)
    locs.append(len(data))
    i = 0
    while i < len(locs)-1:
        print(data[locs[i]+1:locs[i+1]])
        i += 2

def word_count(string):
    diction = {}
    for word in str.split(string):
        if word in diction:
            diction[word] += 1
        else:
            diction[word] = 1
    for key, value in diction.items():
        print(key, value)

#word_count('When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be')

def rand_list(min, max):
    rl = []
    for i in range(min, max):
        rl.append(i)
    random.shuffle(rl)
    print(rl)
    # retl = []
    # for i in range(rl):
    #     retl.append(rl.pop(random.randint(0, len(rl))))
    # print(retl)

rand_list(1, 20)