def update_database(query):
    """Update database with guaranteed cleanup."""
    connection = None
    try:
        print("🔌 Connecting to database...")
        # connection = connect_to_database()  # Simulate
        connection = "DB_CONNECTION"  # Mock

        print(f"📝 Executing query: {query}")
        # result = connection.execute(query)  # Simulate

        # Simulate error on certain queries
        if "DROP" in query:
            raise ValueError("❌ DROP commands not allowed!")

        print("✅ Query executed successfully!")

    except ValueError as e:
        print(f"❌ Error: {e}")
        # Rollback changes
        print("↩️ Rolling back transaction...")

    finally:
        # ALWAYS close connection, even if error occurred
        if connection:
            print("🔌 Closing database connection...")
            # connection.close()  # In real code
        print("🧹 Cleanup complete!")

# Test
update_database("INSERT INTO users VALUES ('Ahad', 20)")
print()
update_database("DROP TABLE users")  # This will fail!
