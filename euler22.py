
def name_score(name, position):
    val = sum(ord(it) - ord('A') + 1 for it in name)
    return val*position

with open('euler22_data') as fil:
    dat = fil.read().split(',')
    dat = [it.strip('"') for it in dat]
    dat.sort()

    total_Score = sum( name_score(name, pos+1) for pos, name in enumerate(dat))

    print(total_Score)

    
    
    
    
