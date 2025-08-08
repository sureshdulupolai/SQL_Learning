import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="BankManagement",
    user="postgres",
    password="646464"
)

my_cursor = conn.cursor()

def tableSelect(a):
    my_cursor.execute("SELECT * FROM {}".format(a))
    my_result = my_cursor.fetchall()
    return my_result

def sum(a):
    var = tableSelect(a)
    sum = 0
    for i in var:
        sum += i[10]
    return ("Total Value of Bank Management System is : {}".format(sum))

# order by asc
def orderByAsc(a, n1):
    var = tableSelect(a)
    for i in range(len(var) - 1):
        for j in range(len(var) - 1):
            if var[i][n1][0] < var[j][n1][0]:
                var[i], var[j] = var[j], var[i]
            else:
                continue
    return var

def lineByLine(lst):
    for i in lst:
        print(i)

var = orderByAsc('user_data', 1)
lineByLine(var)

# create a Dict of ID : ( userid : [userName, userMoney, userDetails, etc.] ) , value as list form
def dct(a):
    var = tableSelect(a)
    dct = {}
    for i in var:
        dct[i[0]] = [*i[1:]] 
    return dct

# sum of all state
def sumOfState(a,c,b):
    var = tableSelect(a)
    sum = 0
    for i in var:
        if b in i[c]:
            sum += i[10]
    return ("The Total Valuation of '{}' is : {}".format(b, sum))

# var = sumOfState("user_data", 7, 'maharashtra')
# print(var)

# 
def lineByLineReturn(lst):
    v2 = tuple()
    for i in lst:
        v2 += i
    return v2

# EMPTY VALUE IS NULL 
def emptySpace(a):
    lst = []
    var = tableSelect(a)
    for i in var:
        tpl = ()
        for j in i:
            if j == "":
                tpl += "NUll",
            else:
                tpl += j,
        lst += [tpl]
    return lst

# v1 = emptySpace("user_data")
# v2 = lineByLineReturn(v1)
# print(v2)

# addText
def addText(a):
    if isinstance(a, tuple):
        print("hello")
    elif isinstance(a, str):
        print("Hi")

# addText()

# count function
def countBy(a, b, c, d):
    var = tableSelect(a)
    count = 0
    lst = []
    for i in var:
        if d == 1:
            if i[b] == c:
                count += 1
        elif d == 2:
            if i[b] == c:
                lst += [i]
                lineByLine(lst)
    return count
# var = countBy("user_data", 7, 'Uttar Pradesh', 2)
# print(var)

# --------------------------------------
# sum of all city

# get value by id

# change name or update value

# check data of user by id

# ---------------------------------------------
# var = orderByAsc("user_data")
# lineByLine(var)



# var1 = sum("user_data")
# print(var1)

# var = dct("user_data")
# print(var[1234567][9])      # price

# 


my_cursor.close()
conn.close()