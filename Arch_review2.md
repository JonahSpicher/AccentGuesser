Ashley Swanson, Jillian MacGregor, Jonah Spicher
Software Design
Spring 2018

# Architectural Review \#2 Reflection

##Feedback and Decisions:

During the course of our architectural review, we posed the following questions to our peers in order to gain feedback on certain portions of our project:

   - Based on the CNN developed from the audio processor code on Github, should we try to find something different/build our own, or stick with it and try to make it work?
   - The dataset problem: how do we continue there?  Any insightful suggestions?

Based off the responses we received, we have decided to stick with the CNN that we found on the repository for the audio processor, and it proved to be a fruitful task. After being able to resolve the matrix dimension errors, we can now begin feeding more data to the neural net, and hopefully put it on the supercomputer and be able to test it on that in a little while. Although the task of resolving the matrix dimensions seems to depend on how the data is preprocessed, it seems to work fine for the original dataset on one computer, so we have decided to stick with one set of preprocessed data, rather than doing it on separate computers. Using the supercomputer will hopefully resolve this problem as well. In addition to this, we mostly resolved the dataset problem with the CNN resolution. We are continuing to research more datasets and hopefully will be able to add them in to strengthen the neural net even more. 
Although it was not a focus in the architectural review, it is important to note that the GUI is progressing nicely, and we will likely have a nice front-end product for the user to be able to interface with.

## Review Process Reflection:

Although we didn’t have many questions or updates on certain aspects of the code, we believe that the architectural review was helpful in allowing us to share our struggles with our peers and have them give suggestions on various aspects of our project. We got some great recommendations for data sources, and will probably be looking more into that, and received encouragement to stick with the CNN that we had spent time on - which proved to be a good idea. For improvements, we feel that having a bit more interfacing with the actual work we were doing could have been more informative and helpful, and with a little more preparation our reviews could go even better.
