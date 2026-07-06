import fitz # type: ignore


def extract_text(pdf_path: str) -> str:

    try:
        document = fitz.open(pdf_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text
    except Exception as e:
        print("Failed to extract text",e)
        raise
