from fpdf import FPDF
import glob
from pathlib import Path
import os

files=glob.glob("*txt")# it returns the list of the files
print(files)
pdf=FPDF(orientation="P",unit="mm",format="A4")
for filename in files:
    new=Path(filename).stem.capitalize()#Path accepts object of str , not list
    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=16)
    pdf.cell(w=25,h=12,ln=1,border=0,align="C",txt=new)
    file_path=os.path.abspath(filename)
    string=""
    with open(file_path,"r") as file:
        string=file.read()
    pdf.ln(4)
    pdf.set_font(family="Times",size=12)
    pdf.multi_cell(w=0,h=6,txt=string,border=0)

pdf.output("output.pdf")
