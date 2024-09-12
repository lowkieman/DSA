prev=0;
prev1=1;

print(prev);
print(prev1);

for fibo in range(18):
    newfibo=prev+prev1
    print(newfibo)
    prev1=prev
    prev=newfibo;
