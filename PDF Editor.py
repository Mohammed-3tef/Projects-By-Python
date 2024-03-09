from PyPDF2 import PdfReader, PdfWriter, PdfMerger
import os

# Merge two files
def merge(pdf1, pdf2):
    pdf1 = pdf1 + ".pdf"                        # Add the extension to the entered file
    pdf2 = pdf2 + ".pdf"                        # Add the extension to the entered file
    pdfs = [pdf1, pdf2]                         # Make a list and add the entered files into it
    merger = PdfMerger()
    for pdf in pdfs:
        merger.append(pdf)                      # Add every pdf in the list to the merger to merge the files
    merger.write("Result.pdf")                  # Make the merged file name result.pdf
    merger.close()                              # End of the merged function
    print("Merging Successfully.\n")


# Extract a page from file
def extract(pdf, num):
    pdf = pdf + ".pdf"                          # Add the extension to the entered file
    file = open(pdf, "rb")                      # Open the pdf o
    reader = PdfReader(file)                    # Use this function to read the content and access to its pages
    num = num -1
    if num in range(0, len(reader.pages)):      # Check if the num in the file
        new_pdf = PdfWriter()                   # Create a new PDF writer
        # Add the specified page to the writer object
        new_pdf.add_page(reader.pages[num])                 # Pages are zero-indexed
        with open("extracted_page.pdf", "wb") as output:    # make the extracted file name as extracted_page.pdf
            new_pdf.write(output)
            print("Extracted Successfully.\n")
    else:                                           # Message error indicate the entered page not in the file
        print(f"Please enter a valid number between 1-{len(reader.pages)}\n")


# Split file into separate pages
def split(pdf: str, page_num: int):
    pdf += '.pdf'                       # Add the extension to the entered file

    with open(pdf, 'rb') as file:       # Opening the PDF file required to split
        reader = PdfReader(file)        # Use this function to read the content and access to its pages
        pages_num = len(reader.pages)   # Getting the total number of pages
        page_num = page_num -1
        if page_num in range(0, len(reader.pages)):             # Check if the page_num in the file
            new_pdf1 = PdfWriter()                              # Create new_pdf1 to add the first pages at it
            for pages1 in range(page_num+1):      # Adding each page to the new_pdf1
                new_pdf1.add_page(reader.pages[pages1])

            with open('SplittedPDF1.pdf', 'wb') as output1:     # Writing the first part to a file
                new_pdf1.write(output1)

            new_pdf2 = PdfWriter()                          # Create new_pdf2 to add the rest pages at it
            for pages2 in range(page_num+1, pages_num):       # Adding each page to the new_pdf2
                new_pdf2.add_page(reader.pages[pages2])

            with open('SplittedPDF2.pdf', 'wb') as output2:     # Writing the second part to a file
                new_pdf2.write(output2)
                print("Splitted Successfully.\n")
        else:                                                   # Message errors indicate the entered page not in the file
            print(f"Please enter a valid number between 1-{len(reader.pages)}\n")

def check_existance(pdf):                               # Check if the file is existed
    return os.path.exists(pdf)

# ============================================== Main Application ============================================== #

while True:
    print("# ===== Welcome To PDf Editor ===== #")
    print("Choose:-")
    print(" 1) Merge two files.\n 2) Extract a page from file.\n 3) Split file into separate pages.\n 4) Exit.")
    choice_menu = str(input("Enter Your Choice: ").strip())

    if choice_menu == "1":                                     # Merge two files
        pdf1 = input("Enter The First PDF's Name: ")           # Take the file name from the user
        if not check_existance(pdf1 + ".pdf"):                 # Check if the entered file is existed
            print("This file is not exist.\n")
            continue
        pdf2 = input("Enter The Second PDF's Name: ")         # Take the file name from the user
        if not check_existance(pdf2 + ".pdf"):                # Check if the entered file is existed
            print("This file is not exist.\n")
            continue
        merge(pdf1, pdf2)                               # Merge two files


    elif choice_menu == "2":                                  # Extract a page from file
        pdf = input("Enter The PDF's Name: ")                 # Take the file name from the user
        if not check_existance(pdf + ".pdf"):                 # Check if the entered file is existed
            print("This file is not exist.\n")
            continue
        while True:                 # Take the page from the user you want to extract and check if the input is integer
            try:
                num = int(input("Enter The Page Number: "))
                break
            except ValueError:
                print("Please enter a valid page number.")
        extract(pdf, num)                               # Extract a page from file


    elif choice_menu == "3":                             # Split file into separate pages
        pdf = input("Enter The PDF's name: ")            # Take the file name from the user
        if not check_existance(pdf + ".pdf"):            # Check if the entered file is existed
            print("This file is not exist.\n")
            continue
        while True:                 # Take the page from the user you want to split at and check if the input is integer
            try:
                page_num = int(input('Enter the page number to split at: '))
                break
            except ValueError:
                print("Please enter a valid page number.")
        split(pdf, page_num)                        # Split file into separate pages

    elif choice_menu == "4":                        # Exit
        break
    else:
        print("Please enter a valid choice.\n")