

with open('euler13_data', 'r') as fil:
    dat = fil.read()
    num_li = dat.split('\n')
    if num_li[-1] == '':
        num_li = num_li[:-1]

    num_li = map(int, num_li)

    sm = sum(num_li)

    print(str(sm)[:10])
    
    
    
