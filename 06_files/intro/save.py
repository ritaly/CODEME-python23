items = ['latarka', 'woda', 'namiot', 'źdźbło', 'gąbka']

with open('example.txt', 'w') as fopen:
    print(fopen)
    fopen.write('\n'.join(items))
