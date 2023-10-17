import sqlite3


class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   telegram_id INTEGER,
                   full_name TEXT,
                   phone_number TEXT,
                   age INTAGER,
                   work_longitude INTAGER NULL,
                   work_latitude INTAGER NULL,
                   home_longitude INTAGER NULL,
                   home_latitude INTAGER NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   telegram_id INTEGER,
                   order_name TEXT,
                   quantity INTAGER,
                   price INTAGET
            )
        """)
        self.conn.commit()

    def append_user(self, data):
        user_id = data.get("user_id")
        full_name = data.get("full_name")
        phone_number = data.get("phone_number")
        age = data.get("age") 
        work_longitude = data.get("work_longitude")
        work_latitude = data.get("work_latitude")
        home_longitude = data.get("home_longitude")
        home_latitude = data.get("home_latitude")

        try:
            self.cursor.execute(f"""
                INSERT INTO users (telegram_id, full_name, phone_number, age, work_longitude, work_latitude, home_longitude, home_latitude)
                VALUES (?,?,?,?,?,?,?,?)
            """, (user_id, full_name, phone_number, age, work_longitude, work_latitude, home_longitude, home_latitude))
            self.conn.commit()
            return True
        except Exception as exc:
            print(exc)
            return False

    def drop_table(self, table_name):
        self.cursor.execute(f"DROP TABLE {table_name}")

    def get_user(self, message):
        return self.cursor.execute(f"SELECT * FROM users WHERE telegram_id={message.chat.id}").fetchone()

    def close(self):
        self.conn.close()
