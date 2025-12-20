file = open("data.json", "r")
try:
    content = file.read()
    print(content)
except Exception:
    print("Error!")
finally:
    file.close()  # ✅ ALWAYS runs! File gets closed!
