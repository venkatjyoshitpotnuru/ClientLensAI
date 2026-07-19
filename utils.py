from docx import Document


def read_docx(file):
    """
    Read all text from a DOCX file.
    """

    document = Document(file)

    text = []

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            text.append(paragraph.text)

    return "\n".join(text)