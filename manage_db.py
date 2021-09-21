import MySQLdb as mysql
import time
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.prompt import Prompt
import os
import pprint as pp


console = Console()


def colour_print(colour, string):
    console.print(string, style = f'bold {colour}')
   

def show_database(db):
    cur = db.cursor()
    cmd = "SHOW DATABASES"
    colour_print("#FF00FF", cmd)
    cur.execute(cmd)
    res = cur.fetchall()
    cur.close()
    for db in res:
        colour_print("#FF00FF", db)


def show_status(db):
    cur = db.cursor()
    cmd = "SHOW STATUS"
    colour_print("#0000FF", cmd)
    cur.execute(cmd)
    time.sleep(1)
    res = cur.fetchall()
    cur.close()
    for elem in res:
        if elem[0] == "Threads_connected":
            colour_print("#FF00FF", f"Threads Connected: {elem[1]}")
        elif elem[0] == "Threads_created":
            colour_print("#FF00FF", f"Threads Created: {elem[1]}")
        elif elem[0] == "Threads_running":
            colour_print("#FF00FF", f"Threads Running: {elem[1]}")
        elif elem[0] == "Uptime":
            colour_print("#FF00FF", f"Uptime: {elem[1]}")
        elif elem[0] == "Max_used_connections":
            colour_print("#FF00FF", f"Max used connections: {elem[1]}")
        elif elem[0] == "Queries":
            colour_print("#FF00FF", f"Queries: {elem[1]}")


def show_process_list(db):
    cur = db.cursor()
    cmd = "USE information_schema"
    colour_print("#0000FF", cmd)
    cur.execute(cmd)
    cmd = "select * from PROCESSLIST"
    colour_print("#0000FF", cmd)
    cur.execute(cmd)
    res = cur.fetchall()
    cur.close()
    for elem in res:
        colour_print("#FF00FF", elem)
 

if __name__ == "__main__":
    db = mysql.connect(host = "localhost",user="root",passwd="root",db="INFORMATION_SCHEMA")
    while True:
        colour_print("green", f"{'_'*20}MENU{'_'*20}")
        colour_print("green", "[1] Show database information")
        colour_print("green", "[2] Show database status")
        colour_print("green", "[3] Show process list")
        colour_print("red", "[4] Exit")

        ch = Prompt.ask("Select an option", choices = [str(x) for x in range(1,5)])
        
        if ch == '1':
            show_database(db)
        elif ch == '2':
            show_status(db)
        elif ch == '3':
            show_process_list(db)
        elif ch == '4':
            break
        else:
            colour_print("red", "Wrong option!! Try again")
    db.close()
