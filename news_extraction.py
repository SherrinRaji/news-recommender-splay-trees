# Using newspaper3k package
from distutils.file_util import write_file
from tracemalloc import stop
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import newspaper
from newspaper import Article
import pandas as pd
import numpy as np
# for similarity measure
from sklearn.metrics.pairwise import cosine_similarity
# to preprocess tweets
import nltk
import string
import re
from rake_nltk import Rake
import utility
nltk.download('omw-1.4')
nltk.download('words')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')



def article_extraction():
    cnn_paper = newspaper.build(
        'https://www.cnn.com/', language='en', memoize_articles=False)  # CNN paper
    WP_paper = newspaper.build(
        'https://www.washingtonpost.com', language='en', memoize_articles=False)  # WP paper
    NYT_paper = newspaper.build(
        'https://www.nytimes.com', language='en', memoize_articles=False)  # NYT paper

    df_text = pd.DataFrame(columns=['Link', 'text'])
    for news in [cnn_paper, WP_paper, NYT_paper]:
        for i in range(len(news.articles)):
            link = news.articles[i].url
            try:

                news.articles[i].download()
                news.articles[i].parse()
                news.articles[i].nlp()
                news.articles[i].text
                temp = {'Link': link,
                        'text': news.articles[i].text}
                df_text = df_text.append(temp, ignore_index=True)
                if(i>50):
                    break
            except:
                pass
    return df_text


def get_keywords(df_text: pd.DataFrame):

    for index, row in df_text.iterrows():
        print("For index: {}\n".format(index))
        article = re.sub("[^a-zA-Z]", " ", str(row['text']))
        article = article.lower()  # converting to lowercase letters
        r = Rake()
        r.extract_keywords_from_text(article)
        cont = r.get_ranked_phrases()
        if(cont != []):
            row['text'] = cont[0]
            # utility.file_write("data/splay_info.txt","{}|{}\n".format(index,cont[0]))
    df_text = df_text.sort_values(by = "text")
    df_text['text'].replace('', np.nan, inplace=True)
    df_text = df_text.dropna().drop_duplicates(subset="text").reset_index(drop=True)
    print(df_text.head())
    return df_text

        
def driver():
    df_text = article_extraction()
    df = get_keywords(df_text)
    utility.df_to_file("data/lookup_info.txt","data/splay_info.txt",df)


if __name__ == "__main__":
    driver()
