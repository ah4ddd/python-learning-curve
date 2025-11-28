class Database:
    def connect(self):
        raise NotImplementedError()

    def query(self, sql):
        raise NotImplementedError()

class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL...")
        return True

    def query(self, sql):
        print(f"Executing MySQL query: {sql}")
        return [("row1",), ("row2",)]

class PostgresDatabase(Database):
    def connect(self):
        print("🔌 Connecting to PostgreSQL...")
        return True

    def query(self, sql):
        print(f"Executing PostgreSQL query: {sql}")
        return [("row1",), ("row2",)]

class MongoDatabase(Database):
    def connect(self):
        print("🔌 Connecting to MongoDB...")
        return True

    def query(self, sql):
        print(f"Executing MongoDB query: {sql}")
        return [{"_id": 1}, {"_id": 2}]

class UserService:
    def __init__(self, database):
        self.db = database

    def get_all_users(self):
        self.db.connect()
        results = self.db.query("SELECT * FROM users")
        return results

print("--- Using MySQL ---")
mysql = MySQLDatabase()
service = UserService(mysql)
service.get_all_users()

print("\n--- Using PostgreSQL ---")
postgres = PostgresDatabase()
service = UserService(postgres)
service.get_all_users()

print("\n--- Using MongoDB ---")
mongo = MongoDatabase()
service = UserService(mongo)
service.get_all_users()


