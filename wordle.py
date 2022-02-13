# PYenchant is used to test if a word is meaningfull or not
import enchant
d = enchant.Dict("en_US")

word='hello'

tempwordlist=["","","","",""]

tries=0

while(tries<6):
    tries+=1
    inword=input("=>").lower()

    if(d.check(inword) and len(inword)==5):
        
        if inword == word:

            print("Correct Answer")
            break

        else:
            for i in range(5):
                if inword[i] == word[i]:
                    tempwordlist[i]=inword[i]

                else:
                    if inword[i] in word:
                        print("'"+inword[i]+"'")
                        
            print(tempwordlist)



    elif inword=='q':

        break

    else:

        print("Not a word, Try Again")
