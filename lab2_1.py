import sqlite3
import generator_mod

if __name__ == "__main__":   
    fio = generator_mod.Generator_name()
    list_fio, list_oms = fio.create_fio()
    print("Connection SQlite DB...")
    try:
        sqlite_connection = sqlite3.connect('sqlite/fio1.db')
        cursor = sqlite_connection.cursor()
        print("Connection SQLite DB - Success")
        print("Load...")
        for name, oms in zip(list_fio, list_oms):

                sqlite_insert_with_param = """INSERT INTO fio_oms
                                    (name, oms)
                                    VALUES (?, ?);"""

                data_tuple = (name, oms)
                cursor.execute(sqlite_insert_with_param, data_tuple)
                sqlite_connection.commit()
        print("Variables added in table fio_oms")

        cursor.close()

    except sqlite3.Error as error:
        print("Connection SQLite DB Failed", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Connection SQLite closed")