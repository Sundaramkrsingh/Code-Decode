'''Write a python program to translate a message into secret code 
language.Use the rules below to translate normal English into secret
code language'''

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

opt=int(input(">>> Enter '1' to code (or) '0' to decode <<<\n"))

if opt==1:
    txt=input("Enter the text to you want to code\n")
    with open('decoded file.txt','w') as txt_in:
        txt_in.write(txt)
    
    with open('decoded file.txt','r') as ctxt_in:
        ctxt=ctxt_in.read()
        words=ctxt.split(" ")
        cwords=[]
        for word in words:
            if len(word)>=3:
                r1='uch'
                r2='pwq'
                cword=r1+word[1:]+word[0]+r2
                cwords.append(cword)
            else: 
                cwords.append(word[::-1])

    with open('coded file.txt','w') as cdtxt_in:
        cdtxt_in.write(" ".join(cwords))


else:
    with open('coded file.txt','r') as cddtxt_in:
        cddtxt=cddtxt_in.read()
    with open('coded file.txt','w') as cddtxt_in:
        cddtxt_in.write(cddtxt)
    
    with open('coded file.txt','r') as codetxt_in:
        codetxt=codetxt_in.read()
        words=codetxt.split(" ")
        dcdwords=[]
        for word in words:
            if len(word)>2:
                new_word=word[-4]+word[3:-4]
                dcdwords.append(new_word)
            else:
                dcdwords.append(word[::-1])

    with open('decoded file.txt','w') as decoded_txt:
        decoded_txt.write(" ".join(dcdwords))