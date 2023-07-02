from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# Function to create the PDF grid
def create_participants_list(participants):
    doc = SimpleDocTemplate("participants_list.pdf", pagesize=letter)

    # Prepare data for the table
    data = [['Seat', 'Name', 'College', 'Mobile', '','','']]
    styles = getSampleStyleSheet()
    paragraph_style = ParagraphStyle(name='TableCell', parent=styles['Normal'], fontName='Helvetica-Bold')
    for participant in participants:
        participant_details = [
            Paragraph(participant.sitNum, paragraph_style),
            Paragraph(participant.name, paragraph_style),
            Paragraph(participant.collegeName, paragraph_style),
            Paragraph(participant.mobileNumber, paragraph_style),
            '', '', ''  # Empty columns
        ]
        data.append(participant_details)

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
    table = Table(data, colWidths=[75, 150, 150, 100, 25, 25, 25])
    table.setStyle(table_style)

    # Build the PDF
    elements = [table]
    doc.build(elements)

    print("participants_list.pdf created successfully!")
