# Mathews Milian
# Lab 12_3 files IO - guest book

print("Enter 'quit' when you are finished.")

while True:
    name = input("What's your name? ").strip()

    if name.lower() == "quit":
        break

    print(f"Hi {name}, you've been added to the guest book.")

    with open("guest_book.txt", "a", encoding="utf-8") as f:
        f.write(f"{name}\n")

