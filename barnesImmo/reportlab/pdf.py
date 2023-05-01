# https://www.blog.pythonlibrary.org/2010/03/08/a-simple-step-by-step-reportlab-tutorial/
# https://stackoverflow.com/questions/53529173/how-to-draw-a-table-on-a-canvas-in-python-using-report-lab
# https://docs.reportlab.com/reportlab/userguide/ch6_paragraphs/
# https://docs.reportlab.com/reportlab/userguide/ch7_tables/#tablestyle-user-methods

# heigth = 841.8897637795277, width: 595.2755905511812    A4

from .imports import *

def pdf():
    
    c = canvas.Canvas("save_pdf/test.pdf", pagesize=A4)
    c.drawString(100,800,"Welcome to Reportlab!")

    title = "Hello world"
    # pageinfo = "platypus example"

    data = [
        ['(0,0)', '(1,0)', '(2,0)', '(3,0)'],
        ['(0,1)', '(1,1)', '(2,1)', '(3,1)'],
        ['(0,2)', '(1,2)', '(2,2)', '(3,2)'],
        ['(0,3)', '(1,3)', '(2,3)', '(3,3)'],
    ]

    tableau = Table(data, 
                    colWidths = [ 3*cm, 3*cm, 3*cm, 3*cm ],
                    rowHeights= [ 2*cm, 2*cm, 2*cm, 2*cm ]
                    )
    # les indices negatifs repr les fins de listes as list[-1]
    # les indices positifs repr les coordonnées
    # ce qui crée un range 
    tableau.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-3,-3), colors.palegreen),
        ('BACKGROUND', (2,2), (3,3), colors.pink),
        ('BOX', (0,0), (-1,-1), 0.1*cm, colors.black),
        ('INNERGRID', (0,0), (4,4), 0.05*cm, colors.black),
        ('BOX', (1,1), ( 1,3), 0.3*cm, colors.red),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'), # tout le tab
        ('ALIGN', (0,0), (0,0), 'LEFT'), # puis certains champs
        ('ALIGN', (3,3), (3,3), 'RIGHT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('VALIGN', (0,0), (0,0), 'TOP'),
        ('VALIGN', (3,3), (3,3), 'BOTTOM'),
        ('LINEABOVE',(2,0), (2,1), 0.3*cm, colors.blue),
        ('LINEBEFORE',(3,2), (3,3), 0.3*cm, colors.orange),
        ('LINEAFTER',(3,3), (3,3), 0.3*cm, colors.gray),
        # ('TEXTCOLOR',(0,0),(1,-1),colors.red)
    ]))
    tableau.wrapOn(c, 400, 100)
    tableau.drawOn(c, 100, 400)

    c.save()

    def myFirstPage(canvas, doc):
        canvas.saveState()
        canvas.setFont('Times-Bold',16)
        canvas.drawCentredString(width/2.0, height-25, title)
        canvas.setFont('Times-Roman',9)
        canvas.drawString(cm, 0.75 * cm, f"First Page ")
        canvas.restoreState()

    def myLaterPages(canvas, doc):
        canvas.saveState()
        canvas.setFont('Times-Roman',9)
        canvas.drawString(cm, 0.75 * cm, f"Page {doc.page}" )
        canvas.restoreState()

    def go():
        doc = SimpleDocTemplate("save_pdf/hello.pdf")
        data = [
            ['(0,0)', '(1,0)', '(2,0)', '(3,0)'],
            ['(0,1)', '(1,1)', '(2,1)', '(3,1)'],
            ['(0,2)', '(1,2)', '(2,2)', '(3,2)'],
            ['(0,3)', '(1,3)', '(2,3)', '(3,3)'],
        ]

        tableau = Table(data, 
                        colWidths = [ 3*cm ] * 4,
                        rowHeights= [ 2*cm, 2*cm, 2*cm, 2*cm ]
                        )
        # les indices negatifs repr les fins de listes
        # les indices positifs repr les coordonnées
        # ce qui crée un range 
        tableau.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-3,-3), colors.palegreen),
            ('BACKGROUND', (2,2), (3,3), colors.pink),
            ('BOX', (0,0), (-1,-1), 0.1*cm, colors.black),
            ('BOX', (1,1), ( 1,3), 0.3*cm, colors.red),
            ('INNERGRID', (0,0), (4,4), 0.05*cm, colors.black),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'), # tout le tab
            ('ALIGN', (0,0), (0,0), 'LEFT'), # puis certains champs
            ('ALIGN', (3,3), (3,3), 'RIGHT'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('VALIGN', (0,0), (0,0), 'TOP'),
            ('VALIGN', (3,3), (3,3), 'BOTTOM'),
            ('LINEABOVE',(2,0),(2,1), 0.3*cm, colors.blue),
            ('LINEBEFORE',(3,2),(3,3), 0.3*cm, colors.orange),
            # ('TEXTCOLOR',(0,0),(1,-1),colors.red)
        ]))

        Story = [Spacer(1,2*cm)]
        style = styles["Normal"]
        bogustext = "This is Paragraph ! "
        for i in range(1020):
            bogustext += (f"This is Paragraph number {i}. ") 
        p = Paragraph(bogustext, style)
        Story.append(p)        
        Story.append(Spacer(1, 1.5*cm))
        Story.append(tableau)        
        Story.append(Spacer(1, 0.2*cm))
        doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)

    go()
