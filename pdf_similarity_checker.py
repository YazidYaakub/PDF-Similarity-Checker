from tqdm import tqdm
from pathlib import Path
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def compare_texts(text1, text2):
    vectorizer = TfidfVectorizer(stop_words='english')
    vectorized_text = vectorizer.fit_transform([text1, text2])
    similarity_score = cosine_similarity(vectorized_text)[0, 1]
    return similarity_score

directory = Path('')

pdf_data = []

for file_path in tqdm(list(directory.glob('**/*.pdf')), desc="Processing PDFs"):
    pdf_reader = PdfReader(file_path)
    pdf_text = ''.join(page.extract_text() for page in pdf_reader.pages if page.extract_text())
    if pdf_text:
        pdf_data.append((file_path.name, str(file_path), pdf_text))

data = []
for i, (filename1, path1, text1) in tqdm(enumerate(pdf_data), desc="Calculating Similarity", total=len(pdf_data)):
    for j, (filename2, path2, text2) in enumerate(pdf_data[i+1:], start=i+1):
        similarity_score = compare_texts(text1, text2)
        if abs(similarity_score - 1.0) < 1e-6:
            data.append({'PDF 1': filename1, 'PDF 2': filename2, 'Similarity Score': similarity_score, 'Path 1': path1, 'Path 2': path2})

data = pd.DataFrame(data)

data.to_csv('', index=False)
