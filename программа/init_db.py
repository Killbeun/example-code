import sqlite3
connection = sqlite3.connect('database.db')
cur = connection.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS 'employees' (
	'id_employee' INTEGER PRIMARY KEY AUTOINCREMENT,
	'name' TEXT,
	'email' TEXT,
	'phone_number' TEXT,
	'position' TEXT,
	'department' TEXT,
	'chief_id' INTEGER
)""")
cur.execute("""CREATE TABLE IF NOT EXISTS 'clients' (
	'id_client' INTEGER PRIMARY KEY AUTOINCREMENT,
	'name' TEXT,
	'email' TEXT,
	'phone_number' TEXT,
	'passport' TEXT
)""")
cur.execute("""CREATE TABLE IF NOT EXISTS 'events' (
	'id_event' INTEGER PRIMARY KEY AUTOINCREMENT,
	'address' TEXT,
	'people' INTEGER,
    'date' TEXT,
	'description' TEXT,
	'client_id' INTEGER
)""")
cur.execute("""CREATE TABLE IF NOT EXISTS 'contracts' (
	'id_contract' INTEGER PRIMARY KEY AUTOINCREMENT,
	'number' TEXT,
	'date' TEXT,
	'deal_status' BLOB,
	'price' INTEGER,
	'event_id' INTEGER,
	'client_id' INTEGER,
	'employee_id' INTEGER
)""")
cur.execute("""CREATE TABLE IF NOT EXISTS 'reports' (
	'id_report' INTEGER PRIMARY KEY AUTOINCREMENT,
	'number' TEXT,
	'date' TEXT,
	'report_type' TEXT,
	'description' TEXT,
	'employee_id' INTEGER
)""")

cur.execute("INSERT INTO 'employees' ('name', 'email', 'phone_number', 'position', 'department', 'chief_id')  VALUES (?, ?, ?, ?, ?, ?)",
            ('Ивлев Николай Викторович', 'Ivlev@gmail.ru', '80001234567', 'Старший manager', 'Отдел работы с клиентами', 0))
cur.execute("INSERT INTO 'clients' ('name', 'email', 'phone_number', 'passport')  VALUES (?, ?, ?, ?)",
            ('Кузнецов Иван Иванович', 'Kyznec@gmail.ru', '89151234567', '4050 123456'))
cur.execute("INSERT INTO 'events' ('address', 'people', 'date', 'description', 'client_id')  VALUES (?, ?, ?, ?, ?)",
            ('Москва Ул. Ленина 8', 2,'3.1.2024', ' ', 1))
cur.execute("INSERT INTO 'contracts' ('number', 'date', 'deal_status', 'price', 'event_id', 'client_id', 'employee_id')  VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('2024-1-11', '01.04.2024', True, 1000, 1, 1, 1))

cur.execute("INSERT INTO 'clients' ('name', 'email', 'phone_number', 'passport')  VALUES (?, ?, ?, ?)",
            ('Иванов Евгений Степанович', 'Zeka033@gmail.ru', '89170001234', '4050 001002'))
cur.execute("INSERT INTO 'events' ('address', 'people', 'date', 'description', 'client_id')  VALUES (?, ?, ?, ?, ?)",
            ('Москва Ул. Ленина 7', 1, '2.2.2024', ' ', 2))
cur.execute("INSERT INTO 'contracts' ('number', 'date', 'deal_status', 'price', 'event_id', 'client_id', 'employee_id')  VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('2024-2-12', '04.04.2024', True, 2000, 2, 2, 1))
connection.commit()
connection.close()