#pyodbc is an open source Python module that makes accessing ODBC databases simple
import pyodbc

#Is a collection of functions that make matplotlib work
import matplotlib.pyplot as plt

#Is a Python library used for working with arrays
import numpy as np

#Is an open-source python package/module which is used to print tabular data in nicely formatted tables
from tabulate import tabulate

#Is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit
import tkinter as tk

#Is a module that is used to style the tkinter widgets. Just like CSS is used to style an HTML element
from tkinter import ttk
from tkinter import *

#Pandas is a Python library used for working with data sets
import pandas as pd

'''
    Program that gives Statistics of the project.
'''
#דרך הרשאה של ווינדוס
# Connection_Str = ("Driver={SQL Server Native Client 11.0};"
#                   "Server=DESKTOP-QSLPRED\SQLEXPRESS;"
#                   "Database=SQLPROJ;"
#                   "Trusted_Connection=yes;")
# conn = pyodbc.connect(Connection_Str)


##חיבור לSQL
#דרך שרת רופין
'''
    connecting to SQL Server.
'''
Connection_Str=pyodbc.connect(
                   "Driver={SQL Server Native Client 11.0};"
                   "Server=DESKTOP-QSLPRED\SQLEXPRESS;"
                   "Database=SQLPROJ;"
                   "Trusted_Connection=yes;")
#חיבור על ידי שרת
                   # 'Driver={SQL Server Native Client 11.0};'
                   # 'Server=sql5108.site4now.net;'
                   # 'Database=db_a79b5b_proj10;'
                   # 'UID=db_a79b5b_proj10_admin;'
                   # 'PWD=zbVK8D2AB29kT7q3;'
                   # 'Trusted_Connection=no;')


cursor = Connection_Str.cursor()

cursor.execute('''
                    SET DATEFORMAT dmy
                 ''')
cursor.commit()


def InsertData():
    '''
        Function that add data to the database.
    :return:
    '''
    cursor.execute('''
                      INSERT INTO USERS (pass,user_name,user_mail) VALUES ('Omer1234', N'עומר','o@gmail.com')
                     ''')
    Connection_Str.commit()

    cursor.execute('''
                      INSERT INTO CATEGORY (category_name) VALUES (N'אפייה')
                      ''')
    Connection_Str.commit()

    cursor.execute('''
                     INSERT INTO PRODUCT ([category_code],[product_name],[descrept],[image_product])
                      VALUES (4,N'בצק עלים',N'בצק לשימוש למאפים','https://imgs.search.brave.com/LWTA6sYnqaE8xP4MlZedZ5Dyfv5glKqZByR9yJFGE0o/rs:fit:1170:660:1/g:ce/aHR0cHM6Ly93d3cu/eWVodWRpdC1hdml2/LmNvLmlsL3dwLWNv/bnRlbnQvdXBsb2Fk/cy90aHVtYnMvRFND/XzAwMjYtJUQ3JUEy/JUQ3JUE4JUQ3JTk1/JUQ3JTlBLTQtMzc3/aXFpaDRrdjJ4bjV4/NGsxajd5OC5qcGc')
                       INSERT INTO PRODUCT ([category_code],[product_name],[descrept],[image_product])
                      VALUES (4,N'קורנפלור',N'שימוש בקינוחים ואפיה','https://imgs.search.brave.com/mq6NitOWwx5x_TuKNyJ_na3ykl4yjN7hMC8IpiTIp8I/rs:fit:600:600:1/g:ce/aHR0cHM6Ly93d3cu/ZWdvemhha2Zhci5j/by5pbC93cC1jb250/ZW50L3VwbG9hZHMv/MjAyMC8wMS8lRDcl/QTclRDclOTUlRDcl/QTglRDclQTAlRDcl/QTQlRDclOUMlRDcl/OTUlRDclQTguanBn')
                    INSERT INTO PRODUCT ([category_code],[product_name],[descrept],[image_product])
                      VALUES (3,N'שמנת לבישול',N'שמנת לבישול ואפייה','https://imgs.search.brave.com/xbi6WDqTav1omz9Ope2GTqLVCDlvv75klq6329x0t0s/rs:fit:1024:1024:1/g:ce/aHR0cDovL2ltZzIu/dGFwdXouY28uaWwv/Zm9ydW1zLzFfMTU5/MDQ2NjEzLmpwZw')
                     ''')
    Connection_Str.commit()

    cursor.execute('''
                     INSERT INTO INGRIDENTS ([ing_name],[descript])
                      VALUES (N'קמח',N'חומר גלם המופק מחיטה')
                     ''')
    Connection_Str.commit()

    cursor.execute('''
                        INSERT PRODUCTS_TO_USER ([id],[product_code],[date_of_scan],[name_of_product])
                        VALUES (4,7,'12/3/2019',N'שמנת לבישול')
                        INSERT PRODUCTS_TO_USER ([id],[product_code],[date_of_scan],[name_of_product])
                        VALUES (4,5,'22/4/2019',N'בצק עלים')
                        INSERT PRODUCTS_TO_USER ([id],[product_code],[date_of_scan],[name_of_product])
                        VALUES (4,4,'1/10/2017',N'קורנפלור')
                        INSERT PRODUCTS_TO_USER ([id],[product_code],[date_of_scan],[name_of_product])
                        VALUES (3,4,'12/3/2021',N'בצק עלים')
                     ''')
    Connection_Str.commit()

    cursor.execute('''
                     INSERT INTO ING_IN_PRODCUT ([product_code],[ing_code],[descript])
                      VALUES (5,6,'מכיל גלוטן')
                      INSERT INTO ING_IN_PRODCUT ([product_code],[ing_code],[descript])
                      VALUES (7,2,'מכיל לקטוז')
                     ''')
    Connection_Str.commit()


def show_All_Ingredints():
    '''
        Function that show all the Ingredints.
        Output a table with all the data
    '''
    ingName=[]
    ingDescription=[]
    ing_index = 0
    query = "SELECT*FROM INGRIDENTS"
    df = cursor.execute(query)
    row = df.fetchone()
    #loop that add the data to lists
    while row:
        ingName.append(str(row[1]))
        ingDescription.append(str(row[2]))
        #method is used when you want to select only the first row from the table.
        row = cursor.fetchone()
        ing_index += 1

    data = {'שם': ingName, 'תאור': ingDescription}
    #create a 2 dimensional data structure and load data
    df = pd.DataFrame(data)
    df.index.name = 'מוצר'
    #print a module that allows you to display table data beautifully
    print(tabulate(df, headers='keys', tablefmt='grid', maxcolwidths=[None, None, 50]))


def show_User_Table_In_Window():
    '''
        Function that show all the users.
        Output the data in a window with table insinde.
    '''
    UsersTemp=[]
    Labels = ["ID", "PASS", "USER NAME", "EMAIL"]
    #create GUI window to show the data
    my_window = tk.Tk()
    my_window.geometry("400x250")

    #fill the first row of headers with data from database.
    r_set = cursor.execute("SELECT * from USERS")
    e = Label(my_window, width=13, text='id', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=0)
    e = Label(my_window, width=13, text='Pass', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=1)
    e = Label(my_window, width=13, text='User Name', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=2)
    e = Label(my_window, width=13, text='Email', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=3)

    #loop on all the users and put the data into a table
    for index, user in enumerate(r_set):
        for row in range(len(user)):
            e = Label(my_window, width=13, text=user[row], borderwidth=2, relief='ridge', anchor="w")
            e.grid(row=index + 1, column=row)
        UsersTemp.append(user)

    #print a module that allows you to display table data beautifully
    print(tabulate(UsersTemp, headers=Labels, tablefmt="fancy_grid"))

    #open the window and output the table.
    my_window.mainloop()


def line_Charts_Products_Scan_By_Year():
    '''
        Function that show all the Products that scan by year.
    '''
    plt.close()
    Years = []
    amount_per_year = []
    #activate the proc of products that scans by year.
    stored = "EXEC Scan_by_year"
    cursor.execute(stored)
    row = cursor.fetchone()
    while row:
        Years.append(str(row[0]))
        amount_per_year.append(row[1])
        row = cursor.fetchone()
    #usage of Line chart.
    plt.plot(Years, amount_per_year, label='Amount', marker='o')
    plt.xlabel('Years')
    plt.ylabel('Amount')
    plt.title('Amount per year')
    plt.show()


def graph_Of_Amount_Of_Products_Scaned():
    '''
    Function that show the amount of each product that scanned.
    '''
    plt.close()
    products=[]
    amount=[]
    #activate the proc of the amount of scan.
    storedProc = "EXEC AmountOfScan"
    cursor.execute(storedProc)
    row = cursor.fetchone()

    #loop that fill the lists.
    while row:
        products.append(row[0][::-1])
        amount.append(row[2])
        row = cursor.fetchone()

    #insert data into table and output.
    print("==================================================")
    x = np.array(products)
    y = np.array(amount)
    plt.title('Amount of scans')
    plt.xlabel('Products')
    plt.ylabel('Amount')
    plt.bar(x, y, color="red", width=0.6)
    plt.show()


def graph_of_amount_of_scans_per_category():
    '''
        Function that show all the amount of scannes by category.
    '''
    query = "SELECT * from CATEGORY"
    df = cursor.execute(query)
    row = df.fetchone()
    category_dict = {}

    #loop that fill the dictonary with data from database.
    while row:
        category_json = {"id": row[0], "name": str(row[1]), "amount": 0}
        category_dict[category_json["id"]] = category_json
        row = cursor.fetchone()

    query = "SELECT * from PRODUCT"
    df = cursor.execute(query)
    row = df.fetchone()
    #loop that count the number of times that category scanned.
    while row:
        category_code = row[1]
        category_json = category_dict[category_code]
        category_json["amount"] += 1
        category_dict[category_code] = category_json
        row = cursor.fetchone()

    #fill the lists in data.
    category_names_to_show = [category["name"][::-1] for category in category_dict.values()]
    category_amount_to_show = [category["amount"] for category in category_dict.values()]
    x = np.array(category_names_to_show)
    y = np.array(category_amount_to_show)
    #define bar graph and make 2 subplot to output in the same window
    plt.subplot(122)
    plt.title('כמות סריקות לפי קטגוריה'[::-1])
    plt.xlabel('קטגוריה'[::-1])
    plt.ylabel('כמות'[::-1])
    plt.bar(x, y, color="blue", width=0.6)
    #define pie chart and second subplot
    plt.subplot(121)
    plt.pie(y, labels=category_names_to_show, wedgeprops={'edgecolor': 'black'}, autopct='%1.1f%%')
    plt.legend(title="קטגוריות"[::-1], loc=(0.3,1))
    plt.show()




def showDialog():
    # Create an instance of Tkinter frame
    win = Tk()
    # Set the geometry of the Tkinter frame
    win.geometry("450x250")
    # Create Multiple Buttons with different commands
    button_dict = {}
    option = ["show users", "show Ingredints", "Products Scan By Year", "Amount Of Products Scaned",
              "amount of scans per category"]

    for i in option:
        def func(x=i):
            if x == "show users":
                show_User_Table_In_Window()
            elif x == "show Ingredints":
                show_All_Ingredints()
            elif x == "Products Scan By Year":
                line_Charts_Products_Scan_By_Year()
            elif x == "Amount Of Products Scaned":
                graph_Of_Amount_Of_Products_Scaned()
            else:
                graph_of_amount_of_scans_per_category()

        button_dict[i] = ttk.Button(win, text=i, command=func)
        button_dict[i].pack()

    win.mainloop()


def main():
    # InsertData()
    showDialog()


if __name__ == "__main__":
    main()
