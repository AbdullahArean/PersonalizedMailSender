from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# Function to create the PDF grid
def create_participants_grid(participants):
    doc = SimpleDocTemplate("participants_grid.pdf", pagesize=letter)

    # Prepare data for the table
    data = []
    styles = getSampleStyleSheet()
    paragraph_style = ParagraphStyle(name='TableCell', parent=styles['Normal'], fontName='Helvetica-Bold')
    for i, participant in enumerate(participants):
        participant_details = f"DUSACH Admission Guideline Program Season 4<br/>{participant.name}<br/>{participant.collegeName}<br/>Sit Number: <font size='16'>{participant.sitNum}</font>"
        if i % 4 == 0:
            data.append([Paragraph(participant_details, paragraph_style), '', '', ''])
        elif i % 4 == 1:
            data[-1][1] = Paragraph(participant_details, paragraph_style)
        elif i % 4 == 2:
            data[-1][2] = Paragraph(participant_details, paragraph_style)
        else:
            data[-1][3] = Paragraph(participant_details, paragraph_style)

    # Define table style
    table_style = TableStyle([
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, '#aaaaaa'),
    ])

    # Create the table and apply the style
    table = Table(data, colWidths=[150, 150, 150, 150])
    table.setStyle(table_style)

    # Build the PDF
    elements = [table]
    doc.build(elements)

    print("participants_grid.pdf created successfully!")

