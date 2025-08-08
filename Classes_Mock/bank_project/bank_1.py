import psycopg2
VariableName = psycopg2.connect(
    host="localhost",
    database="BankManagement",
    user="postgres",
    password="646464"
)

my_cursor = VariableName.cursor()

# Creating a Bank_Management Database System 
# my_cursor.execute("CREATE DATABASE BANK_MANAGEMENT")

# my_cursor.execute("USE BankManagement;")

# create table USER_DATA
# my_cursor.execute("CREATE TABLE user_data( userid INT PRIMARY KEY, userFirstName VARCHAR(15) NOT NULL, userMiddleName VARCHAR(15), userLastName VARCHAR(12) NOT NULL, userMobileNo VARCHAR(10) NOT NULL UNIQUE, userGmail VARCHAR(40));")


# inserting column in existing table
# my_cursor.execute("ALTER TABLE user_data ADD COLUMN userCurrentValue VARCHAR(20);")

# MODIFY COLUMN
# my_cursor.execute("ALTER TABLE user_data ALTER COLUMN userCurrentValue BIGINT;")

# add column
# my_cursor.execute('ALTER TABLE user_data Add COLUMN userContry VARCHAR(20), ADD COLUMN userState VARCHAR(30), ADD COLUMN userCity VARCHAR(30), ADD COLUMN userPincode VARCHAR(10);')

# --------------------------------------------------------
# Modify columns with separate operations for type and constraints
# my_cursor.execute("ALTER TABLE user_data ALTER COLUMN userContry TYPE VARCHAR(10);")
# my_cursor.execute("ALTER TABLE user_data ALTER COLUMN userContry SET NOT NULL;")

# my_cursor.execute("ALTER TABLE user_data ALTER COLUMN userState TYPE VARCHAR(25);")
# my_cursor.execute("ALTER TABLE user_data ALTER COLUMN userState SET NOT NULL;")

# my_cursor.execute("ALTER TABLE user_data ALTER COLUMN userCity TYPE VARCHAR(30);")
# my_cursor.execute("ALTER TABLE user_data ALTER COLUMN userCity SET NOT NULL;")

# my_cursor.execute("ALTER TABLE user_data ALTER COLUMN userPincode TYPE VARCHAR(6);")
# my_cursor.execute("ALTER TABLE user_data ALTER COLUMN userPincode SET NOT NULL;")
# --------------------------------------------------------------------------------

# modify column
# my_cursor.execute("ALTER TABLE user_data ALTER COLUMN userid TYPE BIGINT;")
VariableName.commit()

def conditionThree():
    print(); print("Thank You For Using Our Bank Management System")

def userShowId(a):
    print(); my_cursor.execute(f"SELECT userCurrentValue FROM user_data WHERE userid = '{a}'")
    current_value = my_cursor.fetchone(); print(f"Your Total is: {current_value[0]}")
    return current_value[0]

def anotherCondiion(userId, var2):
    print(); userValue = input("Do Need To Do another Process y/n: ").lower()
    if userValue in "yes":
        upDownMoney(userId, var2)
    else:
        conditionThree()

def upDownMoney(userId, var2):
    var = int(var2)
    print(); userEnter = input("What You Need To Do, \n1. Add Balance \n2. Withdraw Balance \n3. Exit \nEnter Your Choice : ").lower()
    if userEnter == "1" or userEnter in "add balance":
        useramt = input("Enter Your Cash Amount Insert : ").lower()
        my_cursor.execute("UPDATE user_data SET userCurrentValue = userCurrentValue + %s WHERE userid = %s", (useramt, userId))
        VariableName.commit()
        print("Balance Added Successfully")
        userShowId(userId)
        anotherCondiion(userId, var)
    
    elif userEnter == "2" or userEnter in "withdraw balance":
        useramt = int(input("Enter Amount To Widthdrawal : "))
        if ((var - useramt) >= 0):
            my_cursor.execute("UPDATE user_data SET userCurrentValue = userCurrentValue - %s WHERE userid = %s", (useramt, userId))
            VariableName.commit()
            print("Balance Withdraw Successfully")
            userShowId(userId)
            anotherCondiion(userId, var)
        else:
            print()
            print("Insufficient Balance")
            var3 = userShowId(userId)
            print("Your Current Balance is : {}".format(var3))
            anotherCondiion(userId, var)
    else:
        conditionThree()

def conditionTwo():
    a1 = 0; print(); print("Continue With Your Process Now!")
    var1 = int(input("Enter Your Bank ID : ")); var2 = input("Enter Your Mobile No : ")
    my_cursor.execute("SELECT * FROM user_data"); lst1 = my_cursor.fetchall()
    for i in lst1:
        if ((i[0] == var1) and (i[4] == var2)):
            a1 += 1
            # print("Your Account is Active")
            var2 = userShowId(var1)
            upDownMoney(var1, var2)
            break

    if (a1 == 0):
        print("Your Account is Inactive")
        userEnterValue = input("Do You Need To Activate Your Account y/n: ").lower()
        if userEnterValue in "yes":
            conditionOne()
        else:
            conditionThree()

def createId():
    lst = []; my_cursor.execute("SELECT * FROM user_data"); lst = my_cursor.fetchall()
    if lst:
        var1 = lst[len(lst) - 1]; var2 = var1[0] + 1
        return var2
    
    else:
        var2 = 1234
        return var2

def conditionOne():
    print("Welcome To Our Bank")
    id = createId(); first = input("Enter First Name : ").lower(); middle = input("Enter Middle Name : ").lower()
    last = input("Enter Last Name : ").lower(); mob = input("Enter Your Mobile No : ").lower()
    gml = input("Enter Your Gmail Id : ").lower(); cnt = input("Enter Your Contry : ").lower()
    state = input("Enter Your State : ").lower(); city = input("Enter Your City : ").lower()
    pin = int(input("Enter PinCode : ")); cbl = int(input("Enter Your Deposit : "))

    lst = [id, first, middle, last, mob, gml, cnt, state, city, pin, cbl]
    var1 = "INSERT INTO user_data(userid, userFirstName, userMiddleName, userLastName, userMobileNo, userGmail, userContry, userState, userCity, userPincode, userCurrentValue) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    my_cursor.execute(var1, lst)
    VariableName.commit()
    print()
    print("Your Bank Id : {}".format(id))
    print('{} Registration Successfully'.format(first))
    # conditionTwo()

def printOne():
    print(); print("Welcome To My Bank Management System"); print("1. User Registration"); print("2. User Login"); print("3. Exit")
    choice = input("Enter Your Choice: ")
    if choice == "1":
        conditionOne()   
    elif choice == "2":
        conditionTwo()
    elif choice == "3":
        conditionThree()
    else:
        print("Invalid Choice Between ( 1. User Registration, 2. User Login, 3. Exit )")
        printOne()

# Start Program Line
# ----------------------------------------------------------------------------------
# using bank_management system
# my_cursor.execute("USE bank_management")

# ----------------------------------------
printOne()

# ---------------------------------------------------------------------------------------
# my_cursor.execute("ALTER TABLE user_data ALTER COLUMN userCurrentValue TYPE BIGINT USING userCurrentValue::BIGINT;")
# VariableName.commit()


# my_cursor.fetchall() 

# To Drop Table User_Data
# my_cursor.execute("DROP TABLE IF EXISTS User_Data")
my_cursor.close()
VariableName.close()

