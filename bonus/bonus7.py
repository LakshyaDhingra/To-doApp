filenames = ["1.doc", "1.report", "1.presentation"]

filenames2 = [filename.replace('.', '-') + ".txt" for filename in filenames]

print(filenames2)
