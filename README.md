## Next Word Prediction 

#### This Project aims to develop a deep learning model for predicting the nextword in a given sequence of words.The model is built using  LSTM networks, which are well suited for sequence prediction tasks. The project includes these following steps:

####  1.Data collection: 
###### We use text of Shakespeares "Hamlet" as our dataset.This rich,complex text provides a good challenge for our model.

#### 2. Data Preprocessing: 
###### The text is tokenized,converted into sequence, and padded to ensure uniform input length.The Sequence and then split into training and testing tests.

#### 3. Model Building : 
###### An LSTM model is constructed with an embedding layer,two LSTM Layers, and a dense output layer with a softmax activation function to predict the probability of the nextword.

#### 4.Model Training: 
###### The model is trained using prepared sequences, with early stopping implemened to prevent overfitting.Early stopping  monitors the validation loss and stops training when loss stops improving.

#### 5.MOdel Evaluation: 
###### The model is evaluated using an set of example sentences to test its ability to predict the nextword accuratedly

#### 6.Deployment: 
###### A Streamlit web application is deveploped to allow users to input a sequence of words and get the predicted next word in real time