from fpdf import FPDF
import os

# Create instance of FPDF class
pdf = FPDF()

# Add a page


# Specify the directory you want to search
directory = 'animal_txt_files'

# Get the list of txt files
files = [f for f in os.listdir(directory) if f.endswith('.txt')]

# Iterate over the list of files
for i, file in enumerate(files):
    # Split the file name to get the title
    title = os.path.splitext(file)[0]
    
    # Capitalize the title
    title = title.capitalize()

    pdf.add_page()

    pdf.set_font("Arial", size = 15)
    
    # Add the title to the PDF
    pdf.cell(200, 10, txt = title, ln = i+1, align = 'L')

# Save the pdf with name .pdf
pdf.output("titles.pdf")