def rm_char(n1, n2):
    for i in n1[:]:
        if i in n2:
            n1.remove(i)
            n2.remove(i)
    return n1 + n2


def calc_flames(l):
    flame = ['Friends','Love','Affection','Marriage','Enemies','Sister']
    while len(flame)>1:
        pos = (l % len(flame)) - 1
        if pos==-1:
            t = flame[-1]
            flame.remove(t)
        else:
            left = flame[0:pos]
            right = flame[pos + 1:]
            flame = right + left
    print(flame)


calc_flames(len(rm_char(list(input("Enter Your Name : ").lower().strip().replace(' ', '')),
            list(input("Enter Your Partner Name : ").lower().strip().replace(' ', '')))))
