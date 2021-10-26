#this program will add new chars to a string stored in a variable

#Stores the string
hero= "super man"

#Uses the upper() function to change the word stored in the variable to uppercase
hero=hero.upper()

#adds the wanted chars to the string stored in the hero variable
hero= hero[:1] + "^" + hero[1:]
hero= hero[:3] + "^" + hero[3:]
hero= hero[:5] + "^" + hero[5:]
hero= hero[:7] + "^" + hero[7:]
hero= hero[:11] + "^" + hero[11:]
hero= hero[:13] + "^" + hero[13:]

#Display the string in the varible with the new added chars
print (hero)


