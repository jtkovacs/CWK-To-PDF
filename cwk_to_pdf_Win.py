'''
Python script for Mac to convert AppleWorks and ClarisWorks files in a folder to PDF

Original Author: Mathias Beke
Original Date:   August 2019
Modified: May 2020 by Jacob Cannella Kovacs

Example syntax:

>> C:\Python27\python.exe <script.py> <directory_to_convert>

'''



import os
import subprocess
import sys




def file_to_pdf(root, name):
    '''
    file_to_pdf converts a single file to PDF
    '''
    
    filename    = os.path.join(root,name)
    print(filename)
    destination = root
    
    subprocess.call(["C:\Program Files\LibreOffice\program\soffice.exe", "--headless", "--convert-to", "pdf", filename, "--outdir", destination])




def recursive_directory_to_pdf(path):
    '''
    recursive_directory_to_pdf traverses directory recursively and converts all .cwk files to PDF
    
    returns the number of converted documents
    '''
    count = 0
    
    for root, dirs, files in os.walk(path):
    
        for name in files:

            if name.endswith(".cwk"):
                count += 1
                file_to_pdf(root, name)
    
            else:
                pass
    
    return count




if __name__ == "__main__":

    print("AppleWorks to PDF converter\n")
    
    process     = subprocess.Popen('pgrep soffice', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    my_pid, err = process.communicate()
    
    # Check if LibreOffice installed
    if not os.path.exists("C:\Program Files\LibreOffice\program\soffice.exe"):
        print("LibreOffice should be installed in 'Program Files' folder")
        sys.exit(1)
    
    # Check if LibreOffice not running
    if len(my_pid.split()) > 0:
        print("LibreOffice cannot be opened while running this script.\nQuit LibreOffice and run this script again.")
        sys.exit(1)
    
    # Check if input specified
    if len(sys.argv) <= 1:
        print("Usage: python convert.py <path>")
        sys.exit(1) 
    
    path = sys.argv[1]

    # Go!!!
    count = recursive_directory_to_pdf(path)
    
    print("converted " + str(count) + " files")
    


