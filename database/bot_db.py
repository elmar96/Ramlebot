import sqlite3
from config import bot


def sql_create():
    global connection, cursor
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    if connection:
        print("Database connected successfully")
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS tvshow 
        (photo TEXT, title TEXT PRIMARY KEY, description TEXT)
        """
    )
    connection.commit()

    connection.execute("""
    CREATE TABLE IF NOT EXISTS user
    (telegram_account_id TEXT,
    user_name TEXT PRIMARY KEY,first_name TEXT,last_name TEXT)
    """)

    connection.commit()


async def sql_insert_telegram_account_id(state):
    async with state.proxy() as data:
        cursor.execute("""INSERT INTO user VALUES(?,?, ?, ?)
        """, tuple(data.values()))
        connection.commit()


async def sql_insert(state):
    async with state.proxy() as data:
        cursor.execute("""
        INSERT INTO tvshow VALUES (?, ?, ?)
        """, tuple(data.values()))
        connection.commit()


async def sql_select(message):
    for result in cursor.execute("""SELECT * FROM tvshow""").fetchall():
        await bot.send_photo(message.chat.id,
                             result[0],
                             caption=f'Title {result[1]}\n'
                                     f'Description: {result[2]}')


async def sql_casual_select():
    return cursor.execute("""SELECT * FROM tvshow""").fetchall()

async def sql_casual_select_user():
    return cursor.execute("""SELECT * FROM user""").fetchall()


async def sql_delete(data):
    cursor.execute("""
    DELETE FROM tvshow WHERE title == ?
    """, (data,))
    connection.commit()


async def sql_delete_user(data):
    cursor.execute("""
    DELETE FROM user WHERE user_name == ?
    """, (data,))
    connection.commit()
