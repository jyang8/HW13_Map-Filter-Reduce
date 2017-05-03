# converts txt file to list of strings
with open('wilde.txt', 'r') as f:
    text = f.read().split()

# Find the frequency of a single word
def freq(word):
    return len(filter(lambda x: x.lower() == word, text))
    
# Find the total frequency of a group of words
def tFreq(words):
    return reduce(lambda a, b: a + b, map(lambda x: 1 if x.lower() in words else 0, text))
    
# Find the most frequently occurring word
def mFreq():
    return reduce(lambda a, b: a if freq(a) > freq(b) else b, text)

# Checks that the num from tFreq matches the sum of freq of each word
def tFreqCheck(words):
    s = 0
    for word in l:
        print 'Frequency of \"' + word + '\":'
        print freq(word)
        s += freq(word)
    print 'Total frequency:'
    return s

l = ['the','importance','of','being','earnest']
w = 'and'

#print text
print 'Frequency of \"' + w + '\":'
print freq(w)
print 'Frequency of [' + ', '.join(l) + ']:'
print tFreq(l)
print 'Check tFreq():'
print tFreqCheck(l)
print 'Most frequently occuring word: '
print mFreq()
