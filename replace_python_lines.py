file_path = "earning_python.txt .md"

language = "C++"

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        modified = line.replace("Python", language)
        print(modified, end="")

