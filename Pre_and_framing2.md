**Background and Context:**
As before, we are working on a neural network which should classify recorded speech based on the speaker’s accent. We have started working with tensorflow, and we found an audio classifier on github that promises to do a lot of the detail work for us. The front end, based on flask, is progressing nicely.

We have run into some problems. Our database is classified somewhat badly; the label “English” is used for anyone from anywhere in the US, UK Australia, or New Zealand. Obviously, those represent very different accents, even within each country, that we would really prefer to differentiate between. There are similar problems with Spanish and Arabic. We did find another dataset which is slightly more specific about different “English” accents, however it still does not get any more specific than “United States.”

Additionally, the audio classifier we found on github has proven difficult to work with. It seems to have been written for an outdated version of keras, which has caused several problems, and there are places where the dimensions of matrices don’t line up properly. This has required significant debugging, and in some cases trimming the data, which is far from ideal. We still do not have this audio classifier working.

**Key Questions:**
    - Given the state of the classifier we found, is the amount of work using it will save us worth the process of making it work, or would we be better off finding something else/making our own?
    - Any insightful suggestions for our dataset problem?

**Agenda:**
    - Re-explain background of project and possible pivot points
    - Notation of progress
    - Information on research and progress so far
    - Ask main questions that are also provided on the feedback form to generate discussion 

**Feedback Form Link:** https://goo.gl/forms/4We1rFr7J1ouvMI43
