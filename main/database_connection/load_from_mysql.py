import json
import mysql.connector as mysql


class LoadFromMySQL:
    __conn = None
    __user: str = ''
    __database: str = ''
    __password: str = ''
    __host: str = ''

    def __init__(self):
        pass

    def load_settings_from_json(self, path: str):
        with open(path) as json_file:
            data = json.load(json_file)
        self.__user = data['user']
        self.__database = data['database']
        self.__password = data['password']
        self.__host = data['host']
        if self.__user and self.__database and self.__host != "":
            print("Import from JSON sucessfull")
        else:
            raise Exception("Error while reading from JSON")

    def establish_connection(self):
        try:
            self.__conn = mysql.connect(user=self.__user,
                                                  password=self.__password,
                                                  host=self.__host,
                                                  database=self.__database)
        except mysql.Error as err:
            if err.errno == mysql.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == mysql.errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def close_connection(self):
        self.__conn.close()