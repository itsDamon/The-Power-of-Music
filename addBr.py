with open("addBr.txt", "r") as f:
    with open("addedBr.txt", "w") as f2:
        for line in f:
            line = "<li>" +line.strip() + ("</li>")
            f2.write(line + "\n")
