

import glob

POS_FILES_PATTERN = 'positive_reviews/*.txt' 

NEG_FILES_PATTERN = 'negative_reviews/*.txt' 

# Load and parse positive reviews 
pos_files = glob.glob(POS_FILES_PATTERN)
pos_reviews = [] 
for file in pos_files: 
    with open(file, encoding='utf-8') as stream:
        content = stream.read() 
        words = content.lower().replace('<br />', ' ').split()
        pos_reviews.append(words) 

# Load and parse negative reviews
neg_files = glob.glob(NEG_FILES_PATTERN)
neg_reviews = []
for file in neg_files:
    with open(file, encoding='utf-8') as stream:
        content = stream.read()
        words = content.lower().replace('<br /n', ' ').split()
        neg_reviews.append(words)

# Get Sentence
sentence = input("Proszę podaj komentarz: ") # np. This is a wonderfull movie
words = sentence.lower().replace('<br /n', ' ').split()

# compute sentece sentiment
sentence_sentiment = 0 
for word in words:
    positive = 0 
    negative = 0
    for review in pos_reviews: 
        if word in review: 
            positive += 1 
    for review in neg_reviews:
        if word in review:
            negative += 1
    all_ = positive + negative 
    if all_ != 0: 
        word_sentiment = (positive - negative) / all_ 
    else:
        word_sentiment = 0.0
    
    print(word, word_sentiment)

    sentence_sentiment += word_sentiment
sentence_sentiment /= len(words)

# Raport
if sentence_sentiment > 0:
    label = 'positive'
else:
    label = 'negative'
print('--')
print("This sentence is", label, ', sentiment =', sentence_sentiment)
