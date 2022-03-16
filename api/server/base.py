import disnake as discord
import sqlite3


def clan(guild):
    connection = sqlite3.connect('data/db/main/Database.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM clans WHERE guild = {guild.id}")
    result = cursor.fetchone()

    return result

def guild(guild):
    connection = sqlite3.connect('data/db/main/Database.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM config WHERE id = {guild.id}")
    result = cursor.fetchone()

    return result   

def user(user):
    connection = sqlite3.connect('data/db/main/Database.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM users WHERE guild = {user.guild.id} AND id = {user.id}")
    result = cursor.fetchone()

    return result

def send(result):
    connection = sqlite3.connect('data/db/main/Database.db')
    cursor = connection.cursor()
    print(result)
    cursor.execute(result)
    connection.commit()