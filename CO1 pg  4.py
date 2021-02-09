#Count the occurrences of each word in a line of text.

str1 = input("Enter a string : ")

wordlist = str1.split()

count= []
for w in wordlist:
    count.append(wordlist.count(w))

print("count of the occurrence:" + str(list(zip(wordlist, count))))