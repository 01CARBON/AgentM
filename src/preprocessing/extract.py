from docx import Document

class DocxReader:
    """A class to read and convert .docx file content to a string."""

    def __init__(self):
        """
        """

    def read_to_string(self, file_path):
        """
        Reads the .docx file and converts its content to a string.

        Returns:
            str: A string containing the text content of the document,
            with paragraphs separated by double newlines and table rows
            separated by newlines.
        """
        doc = Document(file_path)
        content = ""

        # Loop through document elements in order
        for element in doc.element.body:
            if element.tag.endswith('p'):  # FOr Paragraphs
                para_text = element.text.strip()
                if para_text:
                    content += para_text + "\n\n"

            elif element.tag.endswith('tbl'):  # For Tables
                table = next(t for t in doc.tables if t._element is element)  # Get matching table
                table_text = ""
                for row in table.rows:
                    table_text += " | ".join(cell.text.strip() for cell in row.cells) + "\n"
                content += table_text + "\n"

        return content

if __name__ == "__main__":
    #tests
    file_path = "Manufacturing Expert Manual.docx" 
    reader = DocxReader()
    doc_content = reader.read_to_string(file_path)

    print(doc_content)

