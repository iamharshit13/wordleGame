from distutils.text_file import TextFile
import enchant
d = enchant.Dict("en_US")

txtf=open('wordlist.txt',"w")

wordl=[]

fullstr = 'abcdefghijklmnopqrstuvwxyz'
# fullstr = 'shghaeiou'

for l1 in fullstr:
    for l2 in fullstr:
        for l3 in fullstr:
            for l4 in fullstr:
                for l5 in fullstr:
                    temp=l1+l2+l3+l4+l5
                    if(d.check(temp)):
                        wordl.append(temp)
                        # txtf.write(temp+"\n")


for ele in wordl:
    txtf.write(ele+"\n")

# l1="a"
# l2="b"
# l3="c"

# print(l1+l2+l3)