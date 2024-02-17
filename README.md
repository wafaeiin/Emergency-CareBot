CareBot is a dedicated and intelligent chatbot tailored for addressing medical inquiries, designed to aid users in accessing information related to their health and overall well-being.

Chatbot UI

Overview
This bot has been trained on a carefully curated dataset containing intents, which represent common queries or statements users might make in the context of healthcare. Leveraging natural language processing (NLP) techniques, the bot comprehends user queries and provides relevant responses.

Installation
To utilize the bot, ensure you have the following dependencies installed:

Python 3.6+
NLTK
Keras
NumPy
Streamlit
You can install the necessary packages using pip. Here's a sample command:

sh
Copy code
pip install -r requirements.txt
Training
CareBot undergoes training using a dataset of intents stored in the intents.json file. The training script is located in training.py.

The training script carries out the following tasks:

Tokenizes each word in the patterns.
Incorporates the documents into the corpus.
Adds the classes to the classes list.
Lemmatizes and filters the words.
Creates the bag of words.
Constructs and trains the neural network model.
Saves both the model and training history.
Execute the training script using the following command:

sh
Copy code
python training.py
Usage
To launch the bot, execute the following command:

sh
Copy code
python interface.py
streamlit run interface.py
The bot will open in your browser. You can input a question or statement into the text box and click "Rerun" to receive a response.