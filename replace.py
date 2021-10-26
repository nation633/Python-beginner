#This program will replace occurances in the sentence stored in the varible and display it in reverse

#Stores the sentences that has occurances
invalid_sentence="The!quick!brown!fox!jumps!over!the!lazy!dog!"

#replaces all the occurances in the string stored in the variable created
invalid_sentence=invalid_sentence.replace("!"," ")
invalid_sentence= invalid_sentence.upper()

print (invalid_sentence)
print (invalid_sentence)
print (invalid_sentence[:: -1])
