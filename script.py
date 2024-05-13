import nltk
from nltk.corpus import stopwords
from collections import Counter

nltk.download('stopwords')
nltk.download('punkt')

def r_text_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def rem_stopwords_from_text(text):
    st_words = set(stopwords.words('english'))
    words = nltk.word_tokenize(text)
    filter_words = [word for word in words if word.lower() not in st_words]
    return ' '.join(filter_words)

def c_letter_frequency(text):
    text = text.replace(" ", "")  
    letter_frequency = Counter(text)
    return letter_frequency

def d_letter_frequency(letter_frequency):
    for letter, frequency in letter_frequency.items():
        print(f"The letter '{letter}' appears {frequency} times.")

file_path = "/assignment4/random_paragraphs.txt"

text_content = r_text_file(file_path)

filter_text_content = rem_stopwords_from_text(text_content)

letter_frequency_result = c_letter_frequency(filter_text_content)

d_letter_frequency(letter_frequency_result)

original_letter_count = sum(1 for char in text_content if char.isalpha())
filter_letter_count = sum(1 for char in filter_text_content if char.isalpha())

t_words_before_filter = len(nltk.word_tokenize(text_content))

t_words_after_filter = len(nltk.word_tokenize(filter_text_content))

print(f"Number of Words after filtering: {t_words_after_filter}")
print(f"Number of Characters before filtering: {original_letter_count:,}")
print(f"Number of Words before filtering: {t_words_before_filter}")
print(f"Number of Characters after filtering: {filter_letter_count:,}")