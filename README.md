# Accent Guesser

Prompts user to record themselves reading a passage, then uses a neural network
to guess the accent of the speaker. The passage (as well as the data the network
is trained on) was taken from kaggle. Recordings and correct answers (taken from
feedback) are stored to improve the network.

**Authors:**

Jillian MacGregor

Jonah Spicher

Ashley Swanson

(Possibly with significant contributions from a github repo by drscotthawley at https://github.com/drscotthawley/audio-classifier-keras-cnn)

**Required packages:**

Librosa-

To install:

    $pip install librosa

tensorflow-

To install:

Follow instructions at https://www.tensorflow.org/install/

Flask-

To install:

    $pip install Flask

ffmpeg-

To install:

	$sudo add-apt-repository ppa:mc3man/trusty-media
	$sudo apt-get update  
	$sudo apt-get install ffmpeg
	$sudo apt-get install frei0r-plugins

Keras-

To install:

	$pip install keras


**Usage:**
As of right now, navigate to the front_end folder and run web_app.py in python
to see the most basic version of the website.

In the future, all interaction with the program should happen on this website,
which may or may not actually be a website.


**License:**
To be determined
