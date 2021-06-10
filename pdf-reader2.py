import pyttsx3
import PyPDF2

book = open('(Ebook - Pdf) Napoleon Hill - Think And Grow Rich (Recommend.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
speaker = pyttsx3.init()

for num in range(0, pages):
    page = pdfReader.getPage(9)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()


