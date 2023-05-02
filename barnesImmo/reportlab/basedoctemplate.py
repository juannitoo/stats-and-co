"""
examples of reportlab document using
BaseDocTemplate with
2 PageTemplate (one and two columns)

"""
import os
from reportlab.platypus import BaseDocTemplate, Frame, Paragraph, NextPageTemplate, PageBreak, PageTemplate
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

styles=getSampleStyleSheet()
Elements=[]

doc = BaseDocTemplate('basedoc.pdf', showBoundary=1, pagesize=A4)

def foot1(canvas,doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "Page %d" % doc.page)
    canvas.restoreState()

def foot2(canvas,doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "Page %d" % doc.page)
    canvas.restoreState()

# normal frame as for SimpleFlowDocument, equivalent d'un template
# frameT = format pleine page ici, format 1 et 2 en colonnes, repr 1 col chacune
# c'est les frames qui déterminent la taille de la zone d'écriture
# j'ai rajouté -20 et +40 ici
frameT = Frame(doc.leftMargin-20, doc.bottomMargin, doc.width+40, doc.height, id='normal')

#Two Columns
frame1 = Frame(doc.leftMargin, doc.bottomMargin, doc.width/2-6, doc.height, id='col1')

frame2 = Frame(doc.leftMargin+doc.width/2+6, doc.bottomMargin, doc.width/2-6,
               doc.height, id='col2')

# elements equivaut a story
Elements.append(Paragraph("Frame one column, "*500,styles['Normal']))
Elements.append(NextPageTemplate('TwoCol')) # pour changer de template à la page suivante, le 1er est induit
Elements.append(PageBreak()) # obligatoire pour éviter que les paragraphes ne se suivent
Elements.append(Paragraph("Frame two columns,  "*500,styles['Normal']))

# ici on rebascule sur le 1er template
# Elements.append(NextPageTemplate('OneCol'))
# Elements.append(PageBreak())
# Elements.append(Paragraph("Une colonne",styles['Normal']))

# on ajoute les frames aux PagesTemplate, qu'on ajoute au doc
doc.addPageTemplates([PageTemplate(id='OneCol',frames=frameT,onPage=foot1),
                      PageTemplate(id='TwoCol',frames=[frame1,frame2],onPage=foot2),
                      ])

#start the construction of the pdf
doc.build(Elements)

# use external program xpdf to view the generated pdf
# os.system("xpdf basedoc.pdf")