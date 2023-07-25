import sqlite3

conn = sqlite3.connect('quotes_db.db')
curr = conn.cursor()

# curr.execute("""create table quotes_tb(
#                 title text,
#                 author text,
#                 tag text
#                 )""")

curr.execute("""insert into quotes_tb values('Python is awesome', 'John Doe', 'python')""")

conn.commit()
conn.close()