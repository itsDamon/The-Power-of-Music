with open("addBr.txt", "r") as f:
    with open("addedBr.txt", "w") as f2:
        for line in f:
            line = line.strip() + ("<br>")
            f2.write(line + "\n")
