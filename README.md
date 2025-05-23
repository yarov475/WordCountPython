# Kivy Translator and Word Frequency Analyzer

This application provides a graphical user interface (GUI) for translating text and analyzing word frequency.

## How to Run

1.  **Install Dependencies:**
    Make sure you have Python installed. Then, install the necessary libraries using pip:
    ```bash
    pip install kivy nltk eng_to_ipa googletrans
    ```
    You may also need to download NLTK data. Run python and type:
    ```python
    import nltk
    nltk.download('wordnet')
    nltk.download('omw-1.4') # Open Multilingual Wordnet
    ```

2.  **Run the Application:**
    Navigate to the `scripts/kivy/` directory in your terminal and run:
    ```bash
    python main.py
    ```

## GUI Overview

The application window is divided into two main sections:

*   **Left Text Area (Input):** Paste or type the text you want to analyze and translate here.
*   **Right Text Area (Output):** This area displays:
    *   The most frequent words from the input text.
    *   Their IPA (International Phonetic Alphabet) transcriptions.
    *   Their translations into Russian.
*   **Translate Button:** Click this button to process the input text and display the results in the output area.
*   **Download CSV Button:** Click this button to save the content of the output area (the list of words, transcriptions, and translations) into a CSV file. The CSV file will be named with the timestamp of when it was created (e.g., `YYYY-MM-DD HH:MM:SS.ffffff.csv`).

## Features

*   **Text Processing:**
    *   The input text is converted to lowercase.
    *   Punctuation (except apostrophes and hyphens within words) is removed.
    *   Common English words (stopwords) are filtered out. The list of stopwords is maintained in `txt/stopwords.txt`.
*   **Word Frequency:**
    *   The application counts the occurrences of each word in the processed text.
    *   It displays the top 10 most frequent words.
*   **Translation:**
    *   Each of the top words is translated into Russian using the `googletrans` library.
*   **IPA Transcription:**
    *   The `eng_to_ipa` library is used to generate IPA transcriptions for the original English words.
*   **Stopword List Update:**
    *   Successfully processed and translated words (specifically, their lemmatized forms) are automatically added to the `txt/stopwords.txt` file. This helps to avoid re-processing or re-translating them in future uses, potentially refining the analysis over time.
*   **CSV Export:**
    *   The results (original word, IPA, translation) can be exported to a CSV file for later review or use.

## Dependencies

*   Kivy (`kivy`): For the graphical user interface.
*   NLTK (`nltk`): For natural language processing tasks, specifically lemmatization.
*   eng-to-ipa (`eng_to_ipa`): For generating IPA transcriptions.
*   Googletrans (`googletrans`): For translating text.
