t=int(input())

for _ in range(t):
    n=int(input())
    s=list(input())
    
    freq={}
    for char in s:
        freq[char]=freq.get(char,0)+1
    
    best=None
    max=-1
    for char in freq:
        if freq[char]>=max:
            max=freq[char]
            best=char
    
    for j in range(n):
        if s[j] == best:
            break
        
    for i in range(n):
        if s[i]!=best:
            break
    
    s[i]=s[j]
    print(''.join(s))
