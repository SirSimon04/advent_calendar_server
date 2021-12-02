import mysql.connector
import sys
import emoji
import re


def remove_emojis(text):
    text = emoji.demojize(text)
    text = re.sub(r'(:[!_\-\w]+:)', '', text)
    return text


class DBConnection:
    conn = None

    def __init__(self):
        print(remove_emojis("hallo😀"))
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

    def insert_calendar(self, id, title, msg, from_name, to_name, bgId, doorId):
        if not self.conn.is_connected():
            self.conn.reconnect()
        print("inserting")
        cursor = self.conn.cursor(prepared=True)

        query = f"INSERT INTO calendars (c_id, title, christmas_msg, from_name, to_name, bg_id, door_id) VALUES ('{id}', '{title}', '{msg}', '{from_name}', '{to_name}', '{bgId}', '{doorId}');"

        insert = "INSERT into calendars (c_id, title, christmas_msg, from_name, to_name, bg_id, door_id) VALUES (%s, %s, %s, %s, %s, %s, %s, )"

        data = (id, remove_emojis(title), remove_emojis(msg), from_name, to_name, bgId, doorId)

        try:

            cursor.execute(insert, data)

            self.conn.commit()
            print("success")
        except mysql.connector.Error as e:
            print(query)
            print("")
            pass

    def get_calendar(self, id):
        if not self.conn.is_connected():
            self.conn.reconnect()
        cursor = self.conn.cursor()

        query = f"SELECT * FROM calendars WHERE c_id='{id}'"

        cursor.execute(query)

        data = {}
        print(cursor)
        for(id, title, msg, _, _, bgId, doorId) in cursor:
            data = {"id": id, "title": title, "msg": msg,
                    "bgId": bgId, "doorId": doorId, }

        return data
