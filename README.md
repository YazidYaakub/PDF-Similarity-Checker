## PDF Content Similarity Checker

The **PDF Content Similarity Checker** script compares the content similarity between multiple PDF files in a given directory. It extracts the text from each PDF file, applies text vectorization using the TF-IDF (Term Frequency-Inverse Document Frequency) algorithm, calculates the cosine similarity between pairs of texts, and saves the results to a CSV file.

### Dependencies

- `tqdm`: A library for creating progress bars in the command line.
- `pathlib`: A module for working with file paths and directories.
- `PyPDF2`: A library for reading and manipulating PDF files.
- `scikit-learn`: A machine learning library that includes the `TfidfVectorizer` and `cosine_similarity` classes.
- `pandas`: A data manipulation and analysis library.

### Functions

#### `compare_texts(text1, text2)`

Calculates the cosine similarity between two input texts using TF-IDF vectorization.

- **Input:**
  - `text1` (str): The first text to compare.
  - `text2` (str): The second text to compare.
- **Output:**
  - `similarity_score` (float): The cosine similarity score between the two texts.

### Main Procedure

1. Set the directory path where the PDF files are located.
2. Initialize an empty list, `pdf_data`, to store the extracted text, filename, and path for each PDF.
3. Iterate through each PDF file in the specified directory:
   - Create a `PdfReader` object to read the PDF file.
   - Extract the text from each page of the PDF and concatenate it into a single string.
   - If the extracted text is not empty, add the filename, path, and text to the `pdf_data` list.
4. Initialize an empty list, `data`, to store the similarity results.
5. Iterate through each pair of PDF texts in `pdf_data`:
   - Calculate the similarity score using the `compare_texts` function.
   - If the similarity score is close to 1.0, add the filenames, similarity score, and paths to the `data` list.
6. Create a pandas DataFrame from the `data` list.
7. Save the DataFrame to a CSV file named "pdf_content_similarity_check.csv".

### Usage

1. Install the required dependencies listed above.
2. Set the directory path where the PDF files are located in the `directory` variable.
3. Run the script.
4. The progress of processing PDFs and calculating similarity will be displayed in the command line.
5. Once completed, the results will be saved in the specified CSV file.

### Example

Suppose you have a directory named "PDFs" containing the following PDF files:
- "file1.pdf"
- "file2.pdf"
- "file3.pdf"

Running this script with the "PDFs" directory will perform the following steps:
1. Extract the text from each PDF file.
2. Calculate the similarity between pairs of texts.
3. Identify pairs of PDFs with a similarity score close to 1.0.
4. Save the results to a CSV file named "pdf_content_similarity_check.csv".

The resulting CSV file will include the following columns:
- "PDF 1": The filename of the first PDF in the pair.
- "PDF 2": The filename of the second PDF in the pair.
- "Similarity Score": The cosine similarity score between the texts of the two PDFs.
- "Path 1": The path of the first PDF file.
- "Path 2": The path of the second PDF file.

#### Explanation of How `cosine_similarity` Works to Compare Texts

**Vectorization:**

Before comparing texts, the text data needs to be transformed into numerical representations that can be processed mathematically. This process is called vectorization. The `TfidfVectorizer` class from the scikit-learn library is used to perform vectorization. It converts the text data into a matrix of TF-IDF (Term Frequency-Inverse Document Frequency) features.

TF-IDF stands for Term Frequency-Inverse Document Frequency. It is a numerical statistic that reflects the importance of a word in a document relative to a collection of documents. The vectorizer calculates the TF-IDF values for each word in the text and constructs a vector representation for each document.

**Cosine Similarity Calculation:**

Once the text data is transformed into vectors, the cosine similarity can be calculated between the vectors. Cosine similarity measures the cosine of the angle between two vectors, which indicates their similarity.

The formula for cosine similarity is:

![Cosine Similarity Formula](https://latex.codecogs.com/png.image?\dpi{150}&space;\bg_white&space;\large&space;\text{cosine\_similarity}&space;=&space;\frac{(A&space;\cdot&space;B)}{(||A||&space;\cdot&space;||B||)})

- `A` and `B` are the vectors being compared.
- `(A \cdot B)` denotes the dot product of vectors `A` and `B`, which is the sum of the element-wise products of the corresponding elements in the vectors.
- `||A||` and `||B||` represent the Euclidean norms (lengths) of vectors `A` and `B`, respectively.

The cosine similarity ranges between -1 and 1, where:
- 1 indicates that the vectors are identical (highest similarity).
- 0 indicates that the vectors are orthogonal (no similarity).
- -1 indicates that the vectors are diametrically opposed (highest dissimilarity).

**Interpreting Cosine Similarity:**

In the context of text comparison, a cosine similarity score close to 1 indicates that the two texts have similar content and are likely to be related. Conversely, a cosine similarity score close to 0 or -1 indicates dissimilar or unrelated texts.

The similarity score obtained from `cosine_similarity` is a quantitative measure of how similar the texts are.

**Application in the Code:**

In the provided code, the `compare_texts` function takes two input texts (representing the content of two PDF files) and performs the following steps:

1. Creates a `TfidfVectorizer` object with stop_words set to 'english'.
2. Uses the vectorizer to fit and transform the input texts, obtaining vector representations for each text.
3. Calculates the cosine similarity between the two vectors using the `cosine_similarity` function.
4. Returns the similarity score.

By using the cosine similarity metric, the code compares the textual content of PDF files and determines their similarity based on the angle between their vector representations. This allows for the identification of similar or closely related documents within a given set.

📝 **Note**: The cosine similarity calculation is a widely used method for comparing texts in natural language processing and information retrieval tasks.

**Note:**
- This script assumes that the necessary dependencies are installed and the PDF files in the specified directory are accessible and
