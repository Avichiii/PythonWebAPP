import sqlite3
import hashlib

def hashfunction(password:str) -> str:
    return hashlib.sha512(bytes(password, 'utf-8')).hexdigest()

def varify(username, passowrd) -> bool:
    passwordsha512 = hashfunction(passowrd)
    conn = sqlite3.connect('database.sqlite')
    cur = conn.cursor()

    cur.execute('SELECT password FROM Credentials WHERE user= ?', (username,))
    database_passowrd = cur.fetchone()[0]
    cur.close()

    if database_passowrd is None: 
        return False
    else:
        if database_passowrd == passwordsha512: return True
        else: return False

    

def store(username:str, password:str) -> bool:
    passwordsha512 = hashfunction(password)
    conn = sqlite3.connect('database.sqlite')
    cur = conn.cursor()

    cur.executescript(
        '''CREATE TABLE IF NOT EXISTS Credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            user TEXT NOT NULL,
            password TEXT NOT NULL
        )'''
    )
    cur.execute('SELECT id FROM Credentials WHERE user= ?', (username,))
    row = cur.fetchone()

    status = False
    if row is None:
        cur.execute('''INSERT OR IGNORE INTO Credentials (user, password)
                    VALUES (?,?)''', (username, passwordsha512))

        conn.commit()
        cur.close()
        
        status = True

    else:
        pass

    if status: return True
    else: return False