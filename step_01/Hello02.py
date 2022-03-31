def numZ(num):
    if num<10: return ' '+str(num)
    else: return str(num)

print('-'*100)
for i in range(1,11):
    for j in range(1,11):
        print(numZ(i)+'+'+numZ(j)+'='+numZ(i+j)+'  ',end='')
    print()
print('-'*100)