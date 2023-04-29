# https://www.blog.pythonlibrary.org/2010/03/08/a-simple-step-by-step-reportlab-tutorial/

def pdf():
    from reportlab.pdfgen import canvas

    c = canvas.Canvas("save_pdf/hello.pdf")
    c.drawString(100,750,"Welcome to Reportlab!")
    c.save()