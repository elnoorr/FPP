from application.config import db

import mysql.connector

class Query:
    
    def __init__(self, statement):
        self.statement = statement
        self.db = self.connection(db.HOST, db.USER, db.PASS, db.NAME)
        self.cursor = self.db.cursor(buffered=True)
        self.commands = ('INSERT', 'SELECT', 'UPDATE', 'DELETE')
        
    def connection(self, host, user, password, database):
        return mysql.connector.connect(
            host        = host,
            user        = user,
            password    = password,
            database    = database
        )
    
    def checkConnection(self):
        return self.db.is_connected()
    
    def commandIsExists(self):
        
        if not self.statement:
            raise Exception('Command is not found')
        
        getCommand = self.statement.split(" ")[0].upper()
        return True if getCommand in self.commands else False
        
    def get(self, rows:bool = False):
        
        if self.checkConnection() == False:
            raise Exception('Connection error')
        
        if self.commandIsExists() == False:
            raise Exception('Command not found')
        
        self.cursor.execute(self.statement)
        return self.cursor.fetchall() if rows else self.cursor.fetchone()
    
    def exec(self):
        if self.checkConnection() == False:
            raise Exception('Connection error')

        if self.commandIsExists() == False:
            raise Exception('Command not found')

        self.cursor.execute(self.statement)
        return self.db.commit()
    
    def count(self):
        if self.checkConnection() == False:
            raise Exception('Connection error')

        if self.commandIsExists() == False:
            raise Exception('Command not found')

        self.cursor.execute(self.statement)
        # self.db.commit()
        # allData = self.cursor.fetchall()
        return self.cursor.rowcount

        
    
     

# mysql.Query("...").get()
# mysql.Query("...").all()
# mysql.Query("...").exec()
# mysql.Query("...").count()
# mysql.Query("...").errors()

# mysql.Query("..", rows:True, errors:True)


# mysql.Table('cedvel').create({
#     "name": "John",
#     "surname": "Doe"
# })

# insert into `cedvel` () values ()


class Table:
    def __init__(self, table_name:str):
        self.tableName = table_name
    
    def create(self, data:dict = {}):
        
        if data == {}:
            raise Exception("Data failed")
    
        statement = f"INSERT INTO `{self.tableName}` "
        
        dataKeys, dataValues = data.keys(), data.values()
        dataKeyList, dataValueList = [], []
        
        for datakey in dataKeys:
            dataKeyList.append(f"`{datakey}`")
            
        for dataValue in dataValues:
            dataValueList.append(f"'{dataValue}'")
            
        fieldList = ','.join(dataKeyList)
        statement += f"({fieldList})"
        
        valuesList = ','.join(dataValueList)
        statement += f" VALUES ({valuesList})"
        
        return Query(statement).exec()
    
    def update(self, data:dict, id:int):
        self.data = data
        self.id  = id
        
        if data  == {}:
            raise Exception("Data failed")
        
        statement = f"UPDATE `{self.tableName}` SET "
        
        list = []
        
        for item in data:
            list.append(f" `{item}` = '{data[item]}' ")
        
        statement += ",".join(list)
        statement += f" WHERE `id` = {id}"
        return Query(statement).exec()       
        
    def delete(self, id:int):
        return Query(f"DELETE FROM `{self.tableName}` WHERE `id` = {id}").exec()       
    
        
        
        """_summary_
        mysql.Table(cedvel).update({
           name: "jane",
           surname: "doe"
        }, 6)
        
        update `cedvel` set `name` = 'Jane', `surname` = 'Doe' where `id` = 1
        """