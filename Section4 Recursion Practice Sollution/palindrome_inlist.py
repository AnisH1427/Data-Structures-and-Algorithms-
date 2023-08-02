def palindrome_recursive(words):
    if len(words)<=1:#if the length of the word is less than or equal to 1
        return 'is a palindrome'
    l=1# -*- coding: latin-1 -*# 
    if words[l-1]==words[l*-1]:#if the first letter of the word is equal to the last letter of the word
        return palindrome_recursive(words[l:l*-1])#return the word without the first and last letter
    return 'is not a palindrome'
words=['wow','Anish','loves','madam','Sulochana','Khadka']#list of words
for i in words:#loop for the words
    spac=i.replace(' ','').lower()#remove the spaces and convert the word to lower case
    print(i,palindrome_recursive(spac),'\n')#print the word and the result
