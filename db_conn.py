import mysql.connector
import sys
import datetime


class DBConnection:
    conn = None

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                user="advent_calendar",
                password="Test123456!",
                host="192.168.188.25",
                port=3306,
                database="advent_calendar"
            )
        except mysql.connector.Error as e:
            print(f"Error connecting to MariaDB Platform: {e.msg}")
            sys.exit(1)

    def insert_calendar(self, id, title, msg, from_name, to_name):
        if not self.conn.is_connected(): self.conn.reconnect()
        print("inserting")
        cursor = self.conn.cursor()


        query = f"INSERT INTO calendars (c_id, title, christmas_msg, from_name, to_name) VALUES ('{id}', '{title}', '{msg}', '{from_name}', '{to_name}');"

        try:

            cursor.execute(query)

            self.conn.commit()
            print("success")
        except mysql.connector.Error as e:
            print(query)
            print("")
            pass
