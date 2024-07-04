from pypdf import PdfReader
import sys

input_arg = sys.argv[1]
# print(f"Recieved argument: {input_arg}")
def scrape_PDF(fileName):   
    # reader = PdfReader('3936-60L FT.pdf')
    reader = PdfReader(fileName)

    unitNumber = reader.pages[0]
    signOffPage = reader.pages[11]
    unitInfoPage = unitNumber.extract_text().split(' ')
    unitInfo = unitInfoPage[37] + '-' + unitInfoPage[39] # + ' ' + unitInfoPage[40]
    technicianInfo = signOffPage.extract_text().split('SIGNATURE  DATE')
    signedOffBy = technicianInfo[1]

    outputData = unitInfo + ' ' + signedOffBy


    print(outputData)
    return outputData

scrape_PDF(input_arg)
