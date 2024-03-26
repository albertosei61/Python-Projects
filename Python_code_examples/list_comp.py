filenames = ['1.doc', '1.report', '1.presentation']
# for file in filenames:
#     print(file)
filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]
print(filenames)