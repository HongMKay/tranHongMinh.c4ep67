text=input("Enter your text: ").lower()
word=input("Choose a word from the previously entered text: ").lower()
def censor(text,word):
    t=text.split()
    n=[]
    for i in t:
        if(i==word):
            n.append("*"*len(word))
        else:
            n.append(i)
    return " ".join(n)
print (censor(text,word))
