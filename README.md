# Accent Guesser

Prompts user to record themselves reading a passage, then uses a neural network
to guess the accent of the speaker. The passage (as well as the data the network
is trained on) was taken from kaggle. Recordings and correct answers (taken from
feedback) are stored to improve the network.

The classifier is accessed through a flask webapp. Backend work was done with the 
Panotti audio classifier using tensorflow. 

Website with more information [here.](https://jonahspicher.github.io/AccentGuesser/)

## Authors:

Jillian MacGregor

Jonah Spicher

Ashley Swanson

(With significant contributions from a github repo by drscotthawley at https://github.com/drscotthawley/panotti for audio classification)

## Required packages:
Librosa-

To install:

    $pip install librosa

tensorflow-

To install:

    $pip3 install tensorflow

Flask-

To install:

    $pip install Flask

Keras-

To install:

    $pip install keras
    
Pickle-

To install:

    $pip install pickle




## Usage:
To use the app to guess accents, navigate to the Front_End folder and run web_app.py in python3. The webapp has instructions from there. The home page will direct you to a record page, on which you can record your voice. You will need to download this recording. Then, you will need to upload this recording. We are really sorry, this was the only way we could get the prediction function to read the audio file. Hit submit to run the class prediction code, and the guess should pop up on the next page.

After that, you will be asked to give the correct answer, regardless of whether or not the guess was correct. This allows your recording to be added to the training data. If you would rather this not happen, simply do not provide a correct answer.
