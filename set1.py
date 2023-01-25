def sub(s1,s2):
    m=len(s1)
    n=len(s2)
    ans=0
    e=0
    lookup=[[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                lookup[i][j]=0
            elif s1[i-1]==s2[j-1]:
                lookup[i][j]=lookup[i-1][j-1]+1
                if lookup[i][j]>ans:
                    ans=lookup[i][j]
                    e=i-1
                else:
                    lookup[i][j]=0
    if ans==0:
        return ""
    else:
        return s1[e-ans+1:e+1]
