for k in range(1, 11):
    f = open(f'input{k}.txt')
    result = []
    for line in f:
        a = ''
        potion = line.split()
        for i in range(1, len(potion)):
            try:
                number = int(potion[i])
                a += result[number - 1]
            except ValueError:
                a += potion[i]
        if potion[0] == 'MIX':
            a = 'MX' + a + 'XM'
        elif potion[0] == 'WATER':
            a = 'WT' + a + 'TW'
        elif potion[0] == 'DUST':
            a = 'DT' + a + 'TD'
        elif potion[0] == 'FIRE':
            a = 'FR' + a + 'RF'
        result.append(a)
    print(k, a == open(f'output{k}.txt').readline())
