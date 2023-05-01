from .imports import *

def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold',16)
    canvas.drawCentredString(width/2.0, height-25, "Les aliments riches en oxalate")
    canvas.setFont('Times-Bold', 11)
    canvas.drawCentredString(width/2.0, height-50, "Données obtenues sur lanutrition.fr")
    canvas.drawCentredString(width/2.0, height-65, "* plus de 50 mg ** plus de 100 mg *** plus de 200 mg")
    canvas.setFont('Times-Roman', 10)
    canvas.drawString(cm, 0.75 * cm, f"First Page")
    canvas.restoreState()

def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(cm, 0.75 * cm, f"Page {doc.page} ----- * plus de 50 mg ** plus de 100 mg *** plus de 200 mg " )
    canvas.restoreState()


def lanutrition_pdf(data):
    doc = SimpleDocTemplate("save_pdf/lanutrition.pdf")
    # canva = canvas.Canvas("save_pdf/lanutrition.pdf", pagesize=A4)

    Story = []
    style = styles["Normal"]

    for key, value in data.items():
        tableau = Table(value, 
                        colWidths = 6*cm, 
                        rowHeights= 0.6*cm
                        )
        
        # les indices negatifs repr les fins de listes
        # les indices positifs repr les coordonnées
        # ce qui crée un range 
        tableau.setStyle(TableStyle([
            ('BOX', (0,0), (-1,-1), 0.07*cm, colors.black),
            ('INNERGRID', (0,0), (-1,-1), 0.05*cm, colors.black),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('SPAN',(0,0),(-1,1)),
            ('BACKGROUND', (0,0), (-1,1), colors.Color(red=(245/255),green=(245/255),blue=(240/255))),
            ('FONTSIZE', (0,0), (-1,1), 14),
            ('SPAN',(0,2),(0,3)),
            ('SPAN',(1,2),(1,3)),
            ('SPAN',(2,2),(2,3)),
            ('BACKGROUND', (0,2), (0,-1), colors.Color(red=(255/255),green=(220/255),blue=(220/255))),
            ('BACKGROUND', (-1,2), (-1,-1), colors.Color(red=(169/255),green=(248/255),blue=(228/255))),
            # ('TEXTCOLOR',(0,0), (-1,1),colors.white),
            # ('BOTTOMPADDING',(0,0),(0,-1), 1*cm),
        ]))

        # tableau.wrapOn(canva, 400, 100)
        # tableau.drawOn(canva, 0, 50)
      
        # ici je determine l'espace sous les tableaux
        Story.append(tableau) 
        if key=="tableau1":      
            Story.append(Spacer(1, 4*cm))
        elif key =="tableau2":
            Story.append(Spacer(1, 0.8*cm))
        elif key =="tableau3":
            pass
        else:
            Story.append(Spacer(1, 1.5*cm))


    # canva.save()

    doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)
