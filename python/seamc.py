#create number
strings=[]
s_new = 0
a=1
while(a<=9):
    b=0
    while(b<=9):
        c=0
        while(c<=9):
            d=0
            while(d<=9):
                e=0
                while(e<=9):
                    f=0
                    while(f<=9):
                        strings.append(str(a)+str(b)+str(c)+str(d)+str(e)+str(f))
                        f+=1
                    e+=1
                d+=1
            c+=1
        b+=1
    a+=1

for s in strings:
    s_new = int(s[2:6]+s[0:2])
    if(s_new==(2*int(s))):
        print s_new
