# import tensorflow as tf
#from tensorflow.keras.preprocessing.text import Tokenizer
#from tensorflow.keras.preprocessing.sequence import pad_sequences
import json
import numpy as np


with open('duranz/interview.json') as file:
    data = json.load(file)


training_sentences = []
training_labels = []
labels = []
responses = []


for intent in data['intents']:
    for pattern in intent['patterns']:
        training_sentences.append(pattern)
        training_labels.append(intent['tag'])
    responses.append(intent['responses'])
    
    if intent['tag'] not in labels:
        labels.append(intent['tag'])


vocab_size = 10000
embedding_dim = 16
max_len = 20
trunc_type = 'post'
oov_token = "<OOV>"

#tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token) # adding out of vocabulary token
#tokenizer.fit_on_texts(training_sentences)


from sklearn.preprocessing import LabelEncoder


enc = LabelEncoder()
enc.fit(training_labels)
training_labels = enc.transform(training_labels)


# new_model = tf.keras.models.load_model("duranz/z_bot")


word_index = {'<OOV>': 1,
 'you': 2,
 'what': 3,
 'your': 4,
 'are': 5,
 'how': 6,
 'is': 7,
 'old': 8,
 'do': 9,
 'good': 10,
 'day': 11,
 'whats': 12,
 'see': 13,
 'i': 14,
 'kunal': 15,
 'age': 16,
 'name': 17,
 'should': 18,
 'yourself': 19,
 'who': 20,
 'language': 21,
 'know': 22,
 'can': 23,
 'we': 24,
 'hi': 25,
 'anyone': 26,
 'there': 27,
 'hello': 28,
 'up': 29,
 'cya': 30,
 'later': 31,
 'goodbye': 32,
 'am': 33,
 'leaving': 34,
 'have': 35,
 'a': 36,
 'bye': 37,
 'call': 38,
 'tell': 39,
 'me': 40,
 'about': 41,
 'hobbies': 42,
 'skills': 43,
 'help': 44,
 'us': 45,
 'programming': 46,
 'why': 47,
 'hire': 48,
 'past': 49,
 'experience': 50,
 'earlier': 51,
 'projects': 52,
 'completed': 53,
 'github': 54,
 'profile': 55,
 'contact': 56,
 'number': 57,
 'were': 58,
 'find': 59,
 'to': 60,
 'reach': 61,
 'on': 62,
 'social': 63,
 'media': 64,
 'goals': 65,
 'dreams': 66,
 'and': 67,
 'ambition': 68,
 'where': 69,
 'in': 70,
 '5': 71,
 'years': 72,
 'passions': 73}
 
 
def total_preprocessing(string, maxlen):
    import numpy as np
    from nltk import word_tokenize
    
    
    def text_to_sequences(string):
        string = string.lower()
        string = word_tokenize(string)
        result = [word_index.get(i, 1) for i in string]
        return result
    def padding_sequence(maxlen):
        token = text_to_sequences(string)
        pad =  np.pad(token,(20-len(token),0), 'constant')#np.zeros((1,max_len), dtype='int32')
        return pad #np.append(pad, text_to_sequences(string))
    
    return list(padding_sequence(maxlen))  #.reshape(1,20)

# def check(string):
#     result = new_model.predict(total_preprocessing(string, max_len))
#     category = enc.inverse_transform([np.argmax(result)])
#     for i in data['intents']:
#         if i['tag']==category:
#             return np.random.choice(i['responses'])










