contents = ["a", "b", "c"]
filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../bonusfiles/{filename}", "w")
    file.write(content)
