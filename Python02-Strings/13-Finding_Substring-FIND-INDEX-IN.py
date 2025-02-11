# 02 - 031: Finding a Substring in Python with: Find, Index, and In

sentence = 'The quick brown fox jumped over the lazy dog.'

# .find() method
query_find = sentence.find('quick') 
# Returns "4", the 4th index, position where 'quick' starts


# .index() method
query_index = sentence.index('fox')
# Returns '4'. If the query prompt isn't available, it will throw an error

# in method
query_in = 'fox' in sentence
# Returns >True or >False

def noWaySir(sentence):
    if 'oops' not in sentence:
        print("No way, sir")
    elif 'fox' in sentence:
        print("Yeah! There's a match today!")
    else:
        print("Ho Ho Ho")

print(query_find)
print(query_index)  
print(query_in)
noWaySir(sentence)