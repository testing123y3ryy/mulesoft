
from tabulate import tabulate
from sqlite3 import *


def show():
	conn = connect('muldb.db')
	print("Database Created / Opened")
	cur = conn.cursor()
	cur.execute("SELECT name, releaseDate, director, leadActor, leadActress FROM movies ORDER BY releaseDate ASC")
	records = cur.fetchall()
	head = ["Name", "Release Date","Director","Actors","Actress"]
	print("All Movies: ")
	print(tabulate(records, headers=head, tablefmt="grid"))
	conn.commit()
	conn.close()

def find(queryse):
	conn = connect('muldb.db')
	cur = conn.cursor()
	cur.execute("SELECT name, releaseDate, director, leadActor, leadActress FROM movies where leadActor LIKE '%{}%'".format(queryse))
	records = cur.fetchall()
	head = ["Name", "Release Date","Director","Actors","Actress"]
	print("Search Results: ")
	print(tabulate(records, headers=head, tablefmt="grid"))
	conn.commit()
	conn.close()

def insert(name,releasedate,director,leadactor,leadactress):
	conn = connect('muldb.db')
	cur = conn.cursor()
	cur.execute("INSERT INTO movies (name, releaseDate, director, leadActor, leadActress) values (?,?,?,?,?)", (name,releasedate,director,leadactor,leadactress))
	print("Data Inserted!!!")
	conn.commit()
	conn.close()

def delete(name):
	conn = connect('muldb.db')
	cur = conn.cursor()
	sql = 'DELETE FROM movies WHERE name=?'
	cur.execute(sql, (name,))
	print("Data Deleted!!!")
	conn.commit()
	conn.close()


print('ENTER FOLLOWING NUMBERS TO DO ANY OPERATION:')
repeat = 1
while(repeat):
	print("\n")
	print("**MENU***")
	print("1. Show all Movies")
	print("2. Search by name")
	print("3. Insert a movie")
	print("4. Delete a movie")
	print("5. Enter '-1' to exit")
	choice = int(input("Enter Your Choice: "))
	print("\n")
	if choice==1:
		show()
		
	elif choice==2:
		query = input("Enter your query: ")
		find(query)
		
	elif choice==3:
		name = input("Enter Movie Name: ")
		release_date = input("Release date in YYYY-MM-DD format: ")
		director = input("Director Name: ")
		actor = input("Lead Actor Name: ")
		actress = input("Actress Name: ")
		insert(name,release_date,director,actor,actress)
	elif choice==4:
		name=input("Enter name of movie to delete")
		delete(name)
	elif choice==-1:
		repeat=0
	else:
		print("Invalid Choice")