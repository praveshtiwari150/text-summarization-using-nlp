import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

def summarizer(rawDoc):
    # Filtering out stop words Examples of stop "the", "a", "an", "and", and so on.
    stopwords = list(STOP_WORDS)
    # print(stopwords)

    nlp = spacy.load('en_core_web_sm')
    doc = nlp(rawDoc)

    # print(doc)


    freq_word = {}

    for word in doc:
        
        if word.text.lower() not in stopwords and  word.text.lower() not in punctuation:
            if word.text not in freq_word.keys():
                freq_word[word.text] = 1
                
            else:
                freq_word[word.text] += 1
                
    # print(freq_word)

    # maximum frequency
    max_freq = max(freq_word.values())
    # print(max_freq)

    # Normalized frequency

    for word in freq_word.keys():
        freq_word[word] = freq_word[word]/max_freq
        
    # print(freq_word)

    # creating sentence tokens
    tokens_sent = [sent for sent in doc.sents]
    # print(tokens_sent)

    sentence_scores = {}

    for sent in tokens_sent:
        for word in sent:
            if word.text in freq_word.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = freq_word[word.text]
                    
                else:
                    sentence_scores[sent] += freq_word[word.text]

    # summary

    select_len = int(len(tokens_sent) * 0.3)
    # print(select_len)
    summary = nlargest(select_len, sentence_scores, key = sentence_scores.get)
    # print(summary)

    total_summ = [word.text for word in summary]
    summary = ' '.join(total_summ)
    # print(summary)
    
    return summary, doc, len(rawDoc.split(' ')), len(summary.split(' '))