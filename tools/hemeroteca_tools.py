import os
import requests
from bs4 import BeautifulSoup
from typing import List
from pathlib import Path
from PyPDF2 import PdfReader


BASE_URL = "https://hemeroteca-pdf.bn.gov.br/093092/"


def list_pdfs(base_url: str = BASE_URL) -> List[str]:
    """List PDF files available at the given base URL."""
    response = requests.get(base_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    return [a['href'] for a in soup.find_all('a') if a['href'].lower().endswith('.pdf')]


def download_pdf(pdf_name: str, dest_dir: str = ".", base_url: str = BASE_URL) -> Path:
    """Download a PDF by name."""
    url = base_url.rstrip('/') + '/' + pdf_name
    response = requests.get(url)
    response.raise_for_status()
    dest_path = Path(dest_dir) / pdf_name
    dest_path.write_bytes(response.content)
    return dest_path


def read_pdf_text(pdf_path: Path) -> str:
    """Extract text from a local PDF file."""
    reader = PdfReader(str(pdf_path))
    text = []
    for page in reader.pages:
        text.append(page.extract_text() or "")
    return "\n".join(text)


__all__ = ["list_pdfs", "download_pdf", "read_pdf_text"]
