
import mysql.connector


my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sqlok2002",
    database="w6"
    )

mycursor = my_db.cursor()
query = "create table if not exists twenty (student_id int unsigned auto_increment primary key, student_name varchar(20) not null, student_score int(3) not null)"
mycursor.execute(query)
my_db.commit()
quit = "e"
while quit != 'q':
    student_name = input("Ismi: ").strip()
    while not student_name:
        student_name = input("Ismi?: ").strip()
    student_score = input("Ball: ").strip()
    while not student_score or not student_score.isnumeric():
        student_score = input("Ball?: ").strip()
    query = f"insert into twenty (student_name, student_score) values ('{student_name}', {student_score})"
    mycursor.execute(query)
    my_db.commit()
    quit = input("Top ball olgan studentni ko'rish uchun [q] ni bosing: ")
query = "select max(student_score) from twenty"
mycursor.execute(query)
maxx = mycursor.fetchall()
query = f"select * from twenty where student_score={maxx[0][0]}"
mycursor.execute(query)
stud = mycursor.fetchall()
for _ in stud[0]:
    print(f"| {_} |", end="")