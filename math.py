import pdb

outputformat1 = 0
outputformat2 = 0
cache = 0

def Factorization(key):
    factor = []
    
    i = 2
    while(key > 1):
        
        if(key % i == 0):
            factor.append(i)
            while(key % i == 0):
                key /= i
        i += 1
    return factor

def Intersection(a, b):
    t= []
    for i in a:
        if i in b:
            t.append(i)
    return t

def Findgoal(key, limit, avoid):
    isReversed = False
    rightKey = key * limit
    goal = 0

    
    for i in range(2, limit + 1):
        maybeReversed = False
        t = key * i
        k = len(str(t))
        
        if k == 1  or Intersection(Factorization(int(str(t)[0])), avoid) != []:
            print "\x1b[1;35m[*] pass \x1b[1;m" + str(t)
            continue
        print "\x1b[1;35m[*] Test \x1b[1;m" + str(t)

        test = t % 10**(k - 1)
        
        if 5 < test and int(str(t)[0]) < 9:
            maybeReversed = True
            test = 10**(k - 1) - test

        if test < rightKey:
            rightKey = test
            isReversed = maybeReversed

            goal = t

    return isReversed, goal

def DecideOutputFormat(target, goal):
    k = len(str(goal))

    t1 = target / 10**(k - 1)
    t2 = target % 10**(k - 1)
    return len(str(t1)) + 1, len(str(t2)) + 1

def findFormula(goal, isReversed):
    k = len(str(goal))
    multi = goal / 10**(k - 1)
    add = goal % 10**(k - 1)
    if isReversed is True:
        multi += 1
        add = add - 10**(k-1)
        add = -add

    return multi, add

def mod(target, key, goal, multi, add, isReversed, stage):
    global outputformat1, outputformat2, cache
    #cache = target

    k = len(str(goal))

    t1 = target / 10**(k - 1)
    t2 = target % 10**(k - 1)

    print "\x1b[1;32m[*] Stage {}\x1b[1;m".format(stage)
    string = "\x1b[1;33mN0 : {:%d}    a0 : {:%d}\x1b[1;m" %(outputformat1, outputformat2)
    print string.format(t1, t2)

    t1 = t1 * add
    t2 = t2 * multi
    if isReversed is False:
        target = t1 - t2
        print "{0}N0 - {1}a0 = {2}".format(add, multi, target)
    else :
        target = t1 + t2
        print "{0}N0 + {1}a0 = {2}".format(add, multi, target)
    print ""

    if abs(target) <= goal:# or target % 10 == 0:
        return target
    
    stage +=1
    return mod(target, key, goal, multi, add, isReversed, stage)


def __main__():
    global outputformat1, outputformat2
    target = int(raw_input('\x1b[1;39mtarget : \x1b[1;m'))
    #target = 1337

    key = int(raw_input('\x1b[1;39mkey : \x1b[1;m'))
    #key = 7
    avoid = Factorization(key)

    print ""
    limit = 9
    isReversed, goal = Findgoal(key, limit, avoid)
    outputformat1, outputformat2 = DecideOutputFormat(target, goal)

    print ""
    print "\x1b[1;31m[*] Key digit is \x1b[1;m" + str(goal)

    multi, add = findFormula(goal, isReversed)
    #print "\x1b[1;33m[*] multi %d times add %dN0 and minus %dN0 \x1b[1;m" %(multi, add, add)
    print ''

    k = len(str(goal)) - 1
    k = 10**k
    print "\x1b[1;33mN = %dN0 + a0 \x1b[1;m" %(k)
    print "\x1b[1;33m{0}N = {1}N0 + {0}a0 \x1b[1;m".format(multi, multi * k)
    
    if isReversed == False:
        print "\x1b[1;33m{0}N = {1}N0 - ({2}N0 - {0}a0) \x1b[1;m".format(multi, goal, add)
    else :
        print "\x1b[1;33m{0}N = {1}N0 + ({2}N0 + {0}a0) \x1b[1;m".format(multi, goal, add)
    print ""
    #print isReversed

    result = mod(target, key, goal, multi, add, isReversed, 1)
    print ""

    while result < 0:
        result += key

    while result >= key:
        result -= key
    
    if result == 0:
        print "\x1b[1;36mSo %d mod %d == 0\x1b[1;m" % (target, key)
    else: 
        print "\x1b[1;31m%d != 0\x1b[1;m" % result
        print "\x1b[1;36mSo %d mod %d != 0\x1b[1;m" % (target, key)

if __name__ == '__main__':
    __main__()
