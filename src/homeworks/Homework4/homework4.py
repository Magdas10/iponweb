# Task 1
# Տրված է թվաբանական պրոգրեսիայի առաջին և երկրորդ անդամները։ Տրված n֊ի
# համար, վերադարձնել այդ պրոգրեսիայի n֊րդ անդամը։

import re


def nth_term(a1, a2, n):
    d = a2 - a1
    return a1 + (n - 1) * d


# print(nth_term(1,5,3))

# Task 2
# CodeMaster-ը նոր է վերադարձել գնումներից։ Նա սկանավորեց իր գնած ապրանքների
# չեկը և ստացված շարանը տվեց Ratiorg֊ին՝ պարզելու գնված ապրանքների
# ընդհանուր թիվը: Քանի որ Ratiorg-ը բոտ է, նա անպայման պատրաստվում է այն
# ավտոմատացնել, ուստի նրան անհրաժեշտ է ծրագիր, որը կամփոփի բոլոր թվերը,
# որոնք հայտնվում են տվյալ մուտքագրում:
# Օգնեք Ratiorg-ին՝ գրելով ֆունկցիա, որը վերադարձնում է տվյալ inputString-ում
# հայտնված թվերի գումարը։
def sumOfNumbers1(inputString):
    i = 0
    size = len(inputString)
    sum = 0
    num = ""
    while i < size:
        while i < size and '0' <= inputString[i] <= '9':
            num += inputString[i]
            i += 1
        if num != "":
            sum += int(num)
        num = ""
        if i < size:
            i += 1
    return sum


def sumOfNumbers2(inputString):
    x = re.findall(r'\b\d+\b', inputString)
    sum = 0
    for i in x:
        sum += int(i)
    return sum


# print(sumOfNumbers1("2 apples,  oranges 28"))
# print(sumOfNumbers2("2 apples, 12 oranges"))

# Task 3
# Մուտքագրեք երեք ամբողջ թիվ: Տպեք «Տեսակավորված» բառը, եթե թվերը նշված են
# ոչ աճող կամ չնվազող հերթականությամբ, իսկ «Չտեսակավորված» հակարակ
# դեփքում:
def isSorted(x, y, z):
    return "sorted" if (x < y and y < z) or (x > y and y > z) else "unsorted"


# print(isSorted(1, 2, 3))
# print(isSorted(1, 3, 2))
# print(isSorted(5, 0, -4))


# Task 4
# Գրել ֆունկցիա, որը տրված բնական թվի համար կստուգի, արդյոք այն
# կատարյալ թիվ է, թե ոչ։


def isPerfect(num):
    sum = 1
    if num != num // 1 or num < 0:
        return "number is not a positive integer"
    for i in range(2, int(num ** 1 / 2 + 1)):
        if num % i == 0:
            sum += i
    return sum == num


# print(isPerfect(6))
# print(isPerfect(6.4))
# print(isPerfect(-6))

# Task 5
# Գրել ծրագիր, որը տրված թվային արժեքներով ցուցակի համար, կհաշվի նրա
# էլեմենտների գումարը։
def sumOfList(list):
    sum = 0
    if len(list) == 0:
        return "list is empty"
    if all(isinstance(x, (int, float)) for x in list):
        for l in list:
            sum += l
        return sum
    return "input is not a number"


#
# print(sumOfList([]))
# print(sumOfList([2, 5, 6]))
# print(sumOfList([2, 5, 6, 'x']))

# Task 6
# Գրել ֆունկցիա, որը տրված թվային արժեքներով ցուցակի համար, կվերադարձնի այդ
# ցուցակի ամենամեծ էլեմենտը։
def maxElement(list):
    if len(list) == 0:
        return "list is empty"
    if all(isinstance(x, (int, float)) for x in list):
        max = list[0]
        for l in list:
            if (max < l):
                max = l
        return max
    return "input is not a number"


# print(maxElement([]))
# print(maxElement([2, 5, 6, 1]))
# print(maxElement([2, 5, 6, 'x']))

# Task 7
# Գրել ֆունկցիա, որը տրված ցուցակից կջնջի տրված արժեքին հավասար բոլոր
# էլեմենտները։
def removeEqualToN(list, N):
    return [l for l in list if l != N]


# print(removeEqualToN([], 5))
# print(removeEqualToN([2, 5, 6, 1, 2, 4, 1, 1, 6], 1))
# print(removeEqualToN([2, 5, 6, 'x'], 'x'))

# Task 8
# Գրեք ֆունկցիա որը կվերադարձնի տրված թվային արժեքներով ցուցակի բոլոր
# էլեմենտների արտադրյալը։
def prod(list):
    if len(list) == 0:
        return "list is empty"
    if all(isinstance(x, (int, float)) for x in list):
        p = 1
        for l in list:
            p *= l
        return p
    return "input is not a number"


# print(prod([]))
# print(prod([2, 5, 6, 1, 1, 6]))
# print(prod([2, 5, 6, 'x']))


# TASK 9
# Գրեք ֆունկցիա՝ տողը հակադարձելու համար, եթե դրա երկարությունը 4-ի
# բազմապատիկ է։
def reverseString(str):
    if len(str) % 4 == 0:
        return str[::-1]
    return "length in not multiple of four"


# print(reverseString("lalalala"))
# print(reverseString("lalalalaaaaaaaa"))

# TASK 10
# Գրեք ֆունկցիա՝ որը տրված բնական n թվի համար վերադարձնում է Ֆիբոնաչիի n-րդ
# անդամը։ Խնդիրը լուծել և ռեկուրսիվ, և իտերատիվ մեթոդներով։

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233

def FibIter(n):
    if n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    t1 = 0
    t2 = 1
    t = 0
    count = 2
    while count < n:
        t = t1 + t2
        t1 = t2
        t2 = t
        count += 1
    return t


# print(FibIter(7))
# print(FibIter(4))

def FibRec(n):
    if n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    return FibRec(n - 1) + FibRec(n - 2)


# print(FibRec(7))
# print(FibRec(4))

# TASK 11
# Գրել ֆունկցիա, որը տրված 2 բնական թվերի համար կվերադարձնի նրանց
# ամենափոքր ընդհանուր բազմապատիկը։

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def leastCommonMultiple(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a * b / gcd(a, b)
    return "input type is wrong"


# print(leastCommonMultiple(6, 18))
# print(leastCommonMultiple(32, 12))
# print(leastCommonMultiple(32, 'azsdc'))


# TASK 12
# Գրեք python ծրագիր՝ նշված թվի հաջորդ ամենափոքր պալինդրոմը գտնելու համար:
def numberFrom(ls, index):
    m = 0
    i = 0
    while i <= index - 1:
        m = m * 10 + ls[i]
        i += 1
    return m


def nextPalindrome(n):
    list = [int(x) for x in str(n)]
    size = len(list)
    s = set(list)
    if len(s) == 1 and 9 in s:
        return n + 2  # if all digits are 9 e.g.99 next is 101, 999 next is 1001
    middleElement = size // 2
    if str(n) == str(n)[::-1]:  # check if number is palindrome
        list[middleElement] = (list[middleElement] + 1) % 10
        if size % 2 == 0:
            list[middleElement - 1] = (list[middleElement - 1] + 1) % 10
        m = numberFrom(list, middleElement - 1 if size % 2 == 0 else middleElement) + 1 if list[
                                                                                               middleElement] == 0 else numberFrom(
            list, middleElement - 1 if size % 2 == 0 else middleElement)
        result = [int(x) for x in str(m)]
        result.append(list[middleElement])
        if size % 2 == 0:
            result.append(list[middleElement - 1])
        result.extend([int(x) for x in str(m)[::-1]])

        return numberFrom(result, size)
    else:
        rightNumber = numberFrom(list[middleElement if size % 2 == 0 else middleElement + 1:], middleElement)
        leftNumber = numberFrom(list[0:middleElement][::-1], middleElement)
        if rightNumber < leftNumber:
            list[middleElement if size % 2 == 0 else middleElement + 1:] = list[0:middleElement][::-1]
        else:
            list[middleElement] = (list[middleElement] + 1) % 10
            if size % 2 == 0:
                list[middleElement - 1] = (list[middleElement - 1] + 1) % 10
            m = numberFrom(list, middleElement - 1 if size % 2 == 0 else middleElement) + 1 if list[
                                                                                                   middleElement] == 0 else numberFrom(
                list, middleElement - 1 if size % 2 == 0 else middleElement)
            result = [int(x) for x in str(m)]
            result.append(list[middleElement])
            if size % 2 == 0:
                result.append(list[middleElement - 1])
            result.extend(result[::-1][middleElement - 1:len(result)])
            list = result
        return numberFrom(list, size)


def normalNextPalindrome(n):
    i = n + 1
    while True:
        if str(i) == str(i)[::-1]:
            return i
        i = i + 1


# print(nextPalindrome(99999))
# print(nextPalindrome(123321))

# print(nextPalindrome(6996))
# print(normalNextPalindrome(6996))


# print(nextPalindrome(199991))
# print(nextPalindrome(123100))
# print(nextPalindrome(12310))
# print(nextPalindrome(723350))
# print(nextPalindrome(729950))
# print(nextPalindrome(72350))


# TASK 13
# Ռոբոտը կանգնած է ուղղանկյուն ցանցի վրա և ներկայումս գտնվում է կետում (X0,
# Y0): Կոորդինատները ամբողջ թիվ են։ Այն ստանում է N հեռակառավարման
# հրամաններ: Յուրաքանչյուր հրաման մեկն է՝ վեր, վար, ձախ, աջ: Ճիշտ հրաման
# ստանալուց հետո ռոբոտը մեկ միավոր է տեղափոխում տվյալ ուղղությամբ։ Եթե
# ռոբոտը սխալ հրաման է ստանում, նա պարզապես անտեսում է այն: Որտե՞ղ է
# գտնվելու ռոբոտը բոլոր հրամաններին հետևելուց հետո:
# Ուշադրություն: աջը՝ x0+1, ձախը՝ x0-1, վերևը՝ y0+1, ներքևը՝ y0-1։

def location(x0, y0, list):
    for l in list:
        if l == 'left':
            x0 = x0 - 1
        if l == 'right':
            x0 = x0 + 1
        if l == 'up':
            y0 = y0 + 1
        if l == 'down':
            y0 = y0 - 1
    return x0, y0


# print(location(1, 1, ['left', 'left', 1, 2, 3, 4, 'up']))


# TASK 14
# Ստուգեք, արդյոք 2 ցուցակները 1-քայլ ցիկլիկ են:

def is1stepCyclic(list1, list2):
    if len(list1) != len(list2):
        return False
    i = 0
    toRight = True
    while i < len(list1) - 1:
        if list1[i] != list2[i + 1]:
            toRight = False
            break
        i += 1
    else:
        return list1[(len(list1) - 1)] == list2[0]
    if not toRight:
        i = 0
        while i < len(list1) - 1:
            if list2[i] != list1[i + 1]:
                return False
            i += 1
        else:
            return list2[(len(list1) - 1)] == list1[0]


# print(is1stepCyclic([1,2,3,4,5],[2,3,4,5,1]))
# print(is1stepCyclic([1,2,3,4,5],[5,1,2,3,4]))
# print(is1stepCyclic([1,2,3,4,5],[2,5,4,5,1]))

# TASK 15
# Գրել ծրագիր, որը ստանւմ է թիվ, գտեք առավելագույն թիվը, որը կարող եք ստանալ՝
# ջնջելով տվյալ թվի ուղիղ մեկ թվանշանը:

def maxN(n):
    list = [int(x) for x in str(n)]
    min = 0
    i = 1
    while i < len(list):
        if (list[i] < list[min]):
            min = i
        i += 1
    del list[min]
    return numberFrom(list, len(list))


# print(maxN(152))
# print(maxN(1001))

# TASK 16
# Գրեք ֆուկցիա որը ստանում է tuple տիպի օբյեկտ և վերադարձնում նոր tuple
# բաղկացած միայն առաջին tuple֊ի թվերից։
def onlyNumbers(tuplee):
    list = []
    for t in tuplee:
        if isinstance(t, (int, float)) and not isinstance(t, bool):
            list.append(t)
    return tuple(list)


# print(onlyNumbers((1, 2, 'dfhjgv', 3, True)))

# TASK 17
# Գրեք Python ֆուկցիա որը ստանում է tuple և ցանկացաց տիպի օբյեկտ և ավելացնում
# է ստացած արժեքը tuple մեջ։

def addElement(t, newValue):
    l = list(t)
    l.append(newValue)
    return tuple(l)


# print(addElement((1, 2, "asdfg", 4), True))

# TASK 18
# Գրեք Python ֆուկցիա որը ստանում է tuple դարձնում է string։ Tuplex֊ի էլեմենտները
# ստրինգում պետք է բաժանված լինեն ‘-’ նշանով։
def toStr(t):
    ls = [str(elem) for elem in t]
    return '-'.join(ls)


# print(toStr((1, 2, 3, 'edfrg')))

# TASK 19
# Գրեք Python ֆուկցիա որը ստանում է list և պետքա գտնել նրա երկարությունը առանց
# len() ֆունկցիա֊ի օգտագորձմամբ։

def length(ls):
    c = 0
    for l in ls:
        c += 1
    return c


# print(length([1, 2, 3, 4, 5, 6]))


# TASK 20
# Ticket numbers usually consist of an even number of digits. A ticket number is considered
# lucky if the sum of the first half of the digits is equal to the sum of the second half.
# Given a ticket number n, determine if it&#39;s lucky or not. Not using: string, list, tuple, set
# types.

def sumAndCountOfDigits(n):
    sum = 0
    count = 0
    while not n == 0:
        sum += n // 1 % 10
        count += 1
        n //= 10
    return sum, count


def isLucky(n):
    t = sumAndCountOfDigits(n)
    if t[1] % 2 == 1:
        return False
    sumOfLeft = sumAndCountOfDigits(n % (10 ** (t[1] / 2)))[0]
    sumOfRight = sumAndCountOfDigits(n // (10 ** (t[1] / 2)) % (10 ** (t[1] / 2)))[0]
    return sumOfRight == sumOfLeft


# print(isLucky(1230))
# print(isLucky(12301))

# TASK 21
# Euler function is return a count of numbers not great than N, which are mutualy simple with N.

def euler(n):
    count = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            # print(i)
            count += 1
    return count


# print(euler(6))


# TASK 22 *
# You are given a 0-indexed string array words, where words[i] consists of lowercase English
# letters. In one operation, select any index i such that 0 < i < words.length and words[i - 1]
# and words[i] are anagrams, and delete words[i] from words. Keep performing this operation
# as long as you can select an index that satisfies the conditions.
# Return words after performing all operations. It can be shown that selecting the indices for
# each operation in any arbitrary order will lead to the same result.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or
# phrase using all the original letters exactly once.


def withoutAnagrams(lst):
    return [lst[i] for i in range(len(lst)) if i == 0 or sorted(lst[i - 1]) != sorted(lst[i])]


# print(withoutAnagrams(['abba', 'baba', 'bbaa', 'cd', 'cd']))
# print(withoutAnagrams(['a','b','c']))

# TASK 23 **
# You are given an array of strings names, and an array heights that consists of distinct
# positive integers. Both arrays are of length n. For each index i, names[i] and heights[i]
# denote the name and height of the ith person. Return names sorted in descending
# order by the people's heights.


def height(list1, list2):
    l = list(zip(list1, list2))
    l.sort(key=lambda x: x[-1], reverse=True)
    return l


# print(height(["Mary", "John", "Emma"], [180, 165, 170]))
# print(height(["Alice", "Bob", "Bob"], [155, 185, 150]))


# TASK 24 ***
# In a special ranking system, each voter gives a rank from highest to lowest to all
# teams participating in the competition.
# The ordering of teams is decided by who received the most position-one votes. If two
# or more teams tie in the first position, we consider the second position to resolve the
# conflict, if they tie again, we continue this process until the ties are resolved. If two or
# more teams are still tied after considering all positions, we rank them alphabetically
# based on their team letter.
# You are given an array of strings votes which is the votes of all voters in the ranking
# systems. Sort all teams according to the ranking system described above.
# Return a string of all teams sorted by the ranking system.

def hTol(lst):
    d = dict()
    ln = len(lst[0])
    rank = []
    for l in range(ln):
        rank.append([])
    for l in rank:
        for i in range(ln):
            l.append(0)
    pair = list(zip(sorted(lst[0]), rank))
    for l in lst:
        for i in range(ln):
            for j in range(ln):
                if l[i] == pair[j][0]:
                    pair[j][1][i] += 1
    result = ''
    for i in range(ln):
        maxE = 0
        for j in range(1, ln):
            if pair[j][1][i] > pair[maxE][1][i]:
                maxE = j
        result += pair[maxE][0]
    return result

# print(hTol(['ABC', "ACB", "ABC", "ACB", "ACB"]))
# print(hTol(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))