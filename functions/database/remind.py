from functions.database import utils


def getAllRows():
    connection = utils.connect()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM remind")
    return cursor.fetchall()


def getOrAddUser(userid):
    connection = utils.connect()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM remind WHERE userid = %s", (int(userid),))
    res = cursor.fetchall()

    if not res:
        cursor.execute("INSERT INTO remind(userid) VALUES %s", (int(userid),))
        connection.commit()

        return getOrAddUser(userid)

    return res[0]


def switchReminder(userid, column):
    connection = utils.connect()
    cursor = connection.cursor()

    columns = ["id", "nightly", "les"]

    res = getOrAddUser(userid)

    # Switch the column value
    to = not (res[columns.index(column)])

    cursor.execute("UPDATE remind SET %s = %s WHERE userid = %s", (column, to, int(userid),))
    connection.commit()

    return to

