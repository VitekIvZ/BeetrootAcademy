import sqlite3
from sqlite3 import Error, OperationalError


def create_db_connection(db):
    con = None
    try:
        con = sqlite3.connect(".\\learn.db")
        print(sqlite3.version)
    except Error as err:
        print(f"{err.__class__.__name__}: {err}")
        if con:
            con.rollback()
    else:
        con.commit()
    finally:
        if con: 
            con.close()


def create_db_connection_m():
    con = None
    try:
        with sqlite3.connect(":memory:") as con: 
            print(sqlite3.version)
    except OperationalError as err:
        print(f"{err.__class__.__name__}: {err}")


def create_conn(db):
    conn = None
    try:
        conn = sqlite3.connect(".\\learn.db")
        print(sqlite3.version)
    except Error as err:
        print(f"{err.__class__.__name__}: {err}")
    return conn


def create_table(conn, sql):
    """
    """
    try:
        # conn.execute(sql)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    except Error as err:
        print(f"{err.__class__.__name__}: {err}")


def insert_data(conn, sql, data):
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid
    except Error as err:
        print(f"{err.__class__.__name__}: {err}")


def insert_project(conn, data):
    """
    """
    sql = """INSERT INTO projects(name,begin_date,end_date)
                VALUES(?,?,?)"""
    
    return insert_data(conn, sql, data)


def insert_task(conn, data):
    """
    """
    sql = """INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
             VALUES(?,?,?,?,?,?)"""
    return insert_data(conn, sql, data)


def update_data(conn, sql, data):
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid
    except Error as err:
        print(f"{err.__class__.__name__}: {err}")


def manipulate_data(conn, sql, data):
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid
    except Error as err:
        print(f"{err.__class__.__name__}: {err}")


def select(conn, sql, mode='all', size=None):
    try:
        cur = conn.cursor()
        cur.execute(sql)
        if mode == 'all':
            return cur.fetchall()
        elif mode == 'one':
            return cur.fetchone()
        elif mode == 'many' and size:
            return cur.fetchmany(size)
    except Error as err:
        print(f"{err.__class__.__name__}: {err}")


def close_conn(conn):
    if conn is not None:
        conn.close()


def insertion_section(conn):
    if conn:
        with conn:
            project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30')
            project_id = insert_project(conn, project)

            print(f'Created a project with the id {project_id}')

            tasks = [
                ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02'),
                ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')
            ]

            for task in tasks:
                task_id = insert_task(conn, task)
                print(f'Created task with the id {task_id}')


def updating_section(conn):
    if conn:
        with conn:
            sql = """UPDATE projects
                    SET begin_date = ?, end_date = ?
                    WHERE id = ?"""
            project = ('2016-03-01', '2016-03-30', '1')
            update_data(conn, sql, project)

            sql = """UPDATE tasks
                    SET begin_date = ?, end_date = ?
                    WHERE id = ?"""
            tasks = [('2016-03-01', '2016-03-15', '1'), 
                     ('2016-03-16', '2016-03-30', '2')]
            for task in tasks:
                update_data(conn, sql, task)
                # print(f'Updated a task with the id {task_id}')


def deleting_data(conn):
    if conn:
        with conn:
            sql = """DELETE FROM projects WHERE id = ?"""
            project = ('2', )
            update_data(conn, sql, project)


def select_section(conn):
    if conn:
        with conn:
            sql = """SELECT * FROM tasks"""
            data = select(conn, sql, 'many', size=1)
            print(data)


if __name__ == '__main__':
    # con = sqlite3.connect(".\\learn.db")
    # con.close()
    conn = create_conn(".\\learn.db")

    # 1. Table creation
    sql_project_table = """CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY, 
            name text NOT NULL, 
            begin_date DATE, 
            end_date DATE
        );"""
    
    sql_task_table = """CREATE TABLE IF NOT EXISTS tasks (
                            id INTEGER PRIMARY KEY, 
                            name text NOT NULL, 
                            priority INT, 
                            project_id INT NOT NULL, 
                            status_id INT NOT NULL, 
                            begin_date DATE NOT NULL, 
                            end_date DATE NOT NULL, 
                            FOREIGN KEY (project_id) 
                            REFERENCES projects (id) 
                                ON DELETE CASCADE 
                                ON UPDATE CASCADE
                        );"""

    # if conn is not None:
    #     create_table(conn, sql_project_table)
    #     create_table(conn, sql_task_table)
    # close_conn(conn)

    # 2. Data inssertion
    # insertion_section(conn)

    # 3. Update data
    # updating_section(conn)

    # 4. Deleting data
    # sql = """INSERT INTO projects(name,begin_date,end_date)
    #             VALUES(?,?,?)"""
    # project = ('2 App with SQLite & Python', '2018-01-01', '2018-01-30')
    # project_id = manipulate_data(conn, sql, project)

    # print(f'Created a project with the id {project_id}')
    # deleting_data(conn)

    # 5. Selection section
    select_section(conn)



