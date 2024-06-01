filenames = ["1.Raw Data.txt", "2.Reports.txt","3.Presentations.txt"]
newfilenames = []

for filename in filenames:
    new_filename = filename.replace('.', '-',1)
    newfilenames.append(new_filename)

print(newfilenames)