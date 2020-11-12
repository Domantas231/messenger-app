import sqlite3

# TODO error checking
# add hashing with salts or something

def check_authenticity(message):
    pass

def save_message(author, message):
    check_authenticity(message)

    conn = sqlite3.connect("networking/test.db")
    conn.execute(f"insert into messages (sender, message) values ('{author}', '{message}')")

    conn.commit()
    conn.close()
