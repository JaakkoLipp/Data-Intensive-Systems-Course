import sqlite3
from pymongo import MongoClient

# SQLite connection
SQLITE_DB = "assignment4.db"

# MongoDB connection
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["assignment4"]
mongo_users = mongo_db["users"]

def query_sqlite(query, params=(), fetch=False):
    conn = sqlite3.connect(SQLITE_DB)
    cursor = conn.cursor()
    cursor.execute(query, params)
    data = cursor.fetchall() if fetch else None
    conn.commit()
    conn.close()
    return data

# cli ui
def print_menu():
    print("\nDatabase Management System")
    print("1. View SQLite Users")
    print("2. View MongoDB Users")
    print("3. Insert User into SQLite")
    print("4. Insert User into MongoDB")
    print("5. Delete User from SQLite")
    print("6. Delete User from MongoDB")
    print("7. Update User in SQLite")
    print("8. Update User in MongoDB")
    print("9. View Joined Data (SQLite + MongoDB)")
    print("0. Exit")

##### queries #####

def view_sqlite_users():
    users = query_sqlite("SELECT * FROM users", fetch=True)
    print("\nSQLite Users:")
    for user in users:
        print(user)

def view_mongo_users():
    users = list(mongo_users.find({}, {"_id": 0}))
    print("\nMongoDB Users:")
    for user in users:
        print(user)

def insert_sqlite_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    query_sqlite("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    print("User added to SQLite!")

def insert_mongo_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    mongo_users.insert_one({"name": name, "email": email})
    print("User added to MongoDB!")

def delete_sqlite_user():
    user_id = int(input("Enter user ID to delete: "))
    query_sqlite("DELETE FROM users WHERE id = ?", (user_id,))
    print("User deleted from SQLite!")

def delete_mongo_user():
    name = input("Enter name to delete: ")
    mongo_users.delete_one({"name": name})
    print("User deleted from MongoDB!")

def update_sqlite_user():
    user_id = int(input("Enter user ID to update: "))
    name = input("Enter new name: ")
    email = input("Enter new email: ")
    query_sqlite("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))
    print("User updated in SQLite!")

def update_mongo_user():
    name = input("Enter name to update: ")
    new_email = input("Enter new email: ")
    mongo_users.update_one({"name": name}, {"$set": {"email": new_email}})
    print("User updated in MongoDB!")

def view_joined_data():
    sqlite_users = query_sqlite("SELECT * FROM users", fetch=True)
    mongo_users_data = list(mongo_users.find({}, {"_id": 0}))
    print("\nJoined Data:")
    print("SQLite Users:")
    for user in sqlite_users:
        print(user)
    print("MongoDB Users:")
    for user in mongo_users_data:
        print(user)

# menu loop
def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            view_sqlite_users()
        elif choice == "2":
            view_mongo_users()
        elif choice == "3":
            insert_sqlite_user()
        elif choice == "4":
            insert_mongo_user()
        elif choice == "5":
            delete_sqlite_user()
        elif choice == "6":
            delete_mongo_user()
        elif choice == "7":
            update_sqlite_user()
        elif choice == "8":
            update_mongo_user()
        elif choice == "9":
            view_joined_data()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # run loop
    main()
