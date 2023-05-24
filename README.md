
# PDF Text Similarity Checker

This Python script compares the similarity of text extracted from multiple PDF files. It preprocesses the text using natural language processing (NLP) techniques, such as stop word removal and lemmatization. It then calculates the cosine similarity between the preprocessed texts to determine their similarity.

## Dependencies

The script requires the following dependencies:

- tqdm: A library for creating progress bars during the processing of PDF files.
- pathlib: A module for working with file and directory paths.
- PyPDF2: A library for extracting text from PDF files.
- scikit-learn: A machine learning library used for text vectorization and cosine similarity calculation.
- pandas: A library for data manipulation and analysis.
- nltk: The Natural Language Toolkit, used for downloading stopwords.
- spacy: An open-source library for advanced NLP tasks.

Make sure to install these dependencies before running the script.

## Preprocessing

The script uses NLTK and spaCy libraries for text preprocessing. It downloads the stopwords corpus from NLTK and loads the spaCy English language model (`en_core_web_sm`).

The `preprocess_text(text)` function preprocesses the text by removing stopwords and lemmatizing the remaining words using spaCy. It returns the preprocessed text as a string.

## Text Comparison

The `compare_texts(text1, text2)` function compares the similarity between two preprocessed texts. It uses scikit-learn's `CountVectorizer` to transform the texts into vectors and then calculates the cosine similarity between the vectors. The similarity score is returned.

## File Processing

The script processes PDF files located in a specific directory specified by the `directory` variable. It extracts the text from each PDF file using the PyPDF2 library and preprocesses the text using the `preprocess_text()` function. The preprocessed text and the corresponding filenames are stored in separate lists.

## Similarity Calculation

The script compares the similarity of the preprocessed texts from each pair of PDF files. It loops through the lists of preprocessed texts and calculates the similarity score using the `compare_texts()` function. If the similarity score is close to 1.0 (within a small threshold), the pair is considered highly similar.

## Similarity Score

The similarity score represents the degree of similarity between two preprocessed texts. It is calculated using cosine similarity, which is a metric commonly used to measure the similarity between two vectors.

Cosine similarity ranges from 0 to 1, where 0 indicates no similarity and 1 indicates perfect similarity. In the context of this script, the similarity score represents the similarity between the extracted texts from two PDF files. A higher similarity score indicates a greater resemblance in the content of the PDF files.

The script considers a similarity score close to 1.0 as an indication of high similarity. It uses a threshold value of 1e-6 to determine if the score is practically equal to 1.0, accounting for potential floating-point precision differences. If the absolute difference between the similarity score and 1.0 is less than the threshold, the pair of PDF files is considered highly similar.

The similarity score provides a quantitative measure of how closely related the contents of two PDF files are after preprocessing. This information can be valuable in various applications such as plagiarism detection, document clustering, or content analysis.

## Output

The script creates a pandas DataFrame called `data` to store the pairs of PDF filenames, their similarity scores, and the path of the directory. For each highly similar pair, a new DataFrame is created and concatenated with the existing `data` DataFrame. Finally, the `data` DataFrame is saved as a CSV file named "pdf_content_similarity_check.csv" in the specified output directory.

Ensure that you have the necessary permissions and provide a valid directory path for the output file.

Make sure to adjust the directory path and other relevant variables according to your specific requirements before running the script.
