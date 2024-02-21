contents = ['Documents contents', 'Report contents', 'Presentation Content']
filenames = ['docs.txt', 'report.txt', 'presentation.txt']

for content, filename in zip(contents, filenames):
    file = open(f"../files\{filename}", 'w')
    file.write(content)
