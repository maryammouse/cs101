def cellular_automaton(nes, pn, n):
    alist = ['...','..x','.x.', '.xx', 'x..', 'x.x', 'xx.', 'xxx']
    blist = [int(x) for x in list('{0:0b}'.format(pn))]
    blist.reverse()
    blist += [0] * (8 - len(blist))
    blist = map(lambda x: '.' if x == 0 else 'x', blist)
    adict = dict(zip(alist, blist))
    nstr = ''
    for y in range(0,n):
        nstr = adict[''.join([nes[len(nes) - 1],nes[0],nes[1]])]
        for x in range(1, len(nes) -1):
            nstr += adict[''.join([nes[x-1],nes[x],nes[x+1]])]
        nstr += adict[''.join([nes[len(nes) -2], nes[len(nes) - 1], nes[0]])]
        nes = nstr
    return nstr


#1st line: the patterns in a list
#2nd line: turns the pattern number into binary number list, ex 10 = [1, 0, 1, 0]
#3rd line: reverses blist to match alist
#4th line: pads blist to 8 elements
#5th line: converts the 1's and 0's into x's and .'s
#6th line: makes a dictionary with alist as keys and blist as values
#7th line: new string
#8th line: loop n times
#9th line: joins last, first, and second elements of the string and looks up the rule in the dictionary
#10th - 11th lines: loop that joins 3 elements and looks them up in the dictionary
#12th line: same as 9th except second to last, last, and firs elements
#13th line: prepares for next iteration of loop
#14th line: shows that confused0617 can't count properly


print cellular_automaton('.x.x.x.x.', 17, 2)
#>>> xxxxxxx..
print cellular_automaton('.x.x.x.x.', 249, 3)
#>>> .x..x.x.x
print cellular_automaton('...x....', 125, 1)
#>>> xx.xxxxx
print cellular_automaton('...x....', 125, 2)
#>>> .xxx....
print cellular_automaton('...x....', 125, 3)
#>>> .x.xxxxx
print cellular_automaton('...x....', 125, 4)
#>>> xxxx...x
print cellular_automaton('...x....', 125, 5)
#>>> ...xxx.x
print cellular_automaton('...x....', 125, 6)
#>>> xx.x.xxx
print cellular_automaton('...x....', 125, 7)
#>>> .xxxxx..
print cellular_automaton('...x....', 125, 8)
#>>> .x...xxx
print cellular_automaton('...x....', 125, 9)
#>>> xxxx.x.x
print cellular_automaton('...x....', 125, 10)
#>>> ...xxxxx
