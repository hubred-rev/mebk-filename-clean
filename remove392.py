import os,sys
for a,b,c in os.walk(sys.path[0]):
    for d in c:
        if d[8]=='_':
            os.rename('%s/%s'%(a,d),'%s/%s'%(a,an:='_'.join(d.split('_')[1:])))
            print(an)
