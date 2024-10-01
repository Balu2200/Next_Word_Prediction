import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the model
model = load_model('next_word_lstm.h5')

# Load the tokenizer
import pickle
with open('tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)



def predict_next_word(model, tokenizer, text, max_sequence_len):
  token_list = tokenizer.texts_to_sequences([text])[0]
  token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
  predicted_probs = model.predict(token_list, verbose=0) 
  predicted_index = np.argmax(predicted_probs)
  predicted_word = tokenizer.index_word[predicted_index]
  return predicted_word

st.title('Next Word Prediction')
input_text = st.text_input('Enter your text')
if st.button('Predict'):
  max_sequence_len = model.input_shape[1]+1
  predicted_word = predict_next_word(model, tokenizer, input_text, max_sequence_len)
  st.write(f'The predicted word is: {predicted_word}')

