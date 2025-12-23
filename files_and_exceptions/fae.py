class Transaction:
    def __enter__(self):
        print("🔓 BEGIN TRANSACTION")
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type:
            print("↩️ ROLLBACK (error detected)")
        else:
            print("✅ COMMIT")
        print("🔒 END TRANSACTION")

with Transaction():
    print("Updating user balance")
    print("Logging audit entry")
