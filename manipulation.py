
#Stores the users input
str_sentence=input("Enter your sentence: ")

#counts the number of chars in the users input
str_length=len(str_sentence)
print(str_length)


#Replaces the last letter of the sentence and every other occurance
str_replace=str_sentence.replace(str_sentence[len(str_sentence)-1],"@")

first_chars0 = str(str_sentence[0])
first_chars1 = str(str_sentence[1])
first_chars2 = str(str_sentence[2])
last_chars3=str(str_sentence[-3])
last_chars2=str(str_sentence[-2])
last_chars1=str(str_sentence[-1])

new_sentence = (first_chars0 + first_chars1 + first_chars2 + last_chars2 + last_chars1)
new_sentence1 = (first_chars0 + "\n" + first_chars1 + "\n" +first_chars2 + "\n" +last_chars2 + "\n" +last_chars1)

print((last_chars3 + last_chars2 + last_chars1)[::-1])

print(new_sentence)
print(new_sentence1)

print(str_sentence[len(str_sentence)-4:len(str_sentence)-1:-1])

print(str_sentence[0:2]+str_sentence[len(str_sentence)-2:len(str_sentence)-1])

print(str_replace)