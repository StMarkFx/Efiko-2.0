from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_RIGHT
from io import BytesIO

def create_pdf_from_chat(messages: list) -> bytes:
    """Create a PDF document from chat messages"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Create custom styles
    styles.add(ParagraphStyle(
        name='User',
        parent=styles['Normal'],
        spaceAfter=10,
        textColor='blue'
    ))
    styles.add(ParagraphStyle(
        name='Assistant',
        parent=styles['Normal'],
        spaceAfter=10,
        textColor='green',
        alignment=TA_RIGHT
    ))

    for message in messages:
        style = styles['User'] if message['role'] == 'user' else styles['Assistant']
        story.append(Paragraph(
            f"{message['role'].title()}: {message['content']}",
            style
        ))
        story.append(Spacer(1, 12))

    doc.build(story)
    return buffer.getvalue()
