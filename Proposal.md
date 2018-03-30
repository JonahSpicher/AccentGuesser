Software Design Final Project Proposal

**Idea:**

    Using a kaggle dataset containing about 2000 different recordings of
    different international accents in the English language, we plan to create
    software which can recognize the accent of recorded speech using machine
    learning. The dataset has each speaker reading the same passage, so at
    minimum it would detect the accent of someone new reading that same passage,
    and ideally, it could detect an accent for any arbitrary speech. An
    exciting but probably difficult stretch goal is to also create an algorithm
    or neural network that generates speech which sounds like a given accent,
    or distorts speech to change the accent.



**Learning Goals:**

Ashley - During this project, I would really like to focus on learning how to structure a large scale project, as organization becomes more and more important as scale increases and I have never coded a project this large from scratch before. I would also like to work on learning to integrate code written separately, as I have mostly used the para programming approach up until this point. I am also excited about learning about machine learning algorithms.

Jillian - For this particular project, I hope to gain a better understanding of
          the interdisciplinary applications of machine learning and neural
          networks, as well as applying it to an area of interest for me. Through
          this, I hope to get better at working through conceptualizing and
          developing a framework and final project while improving my teaming
          abilities.

Jonah - Learn about neural networks & machine learning, become more proficient
        at git stuff, make more presentable code


**Implementation Plan:**

We got our data here:

https://www.kaggle.com/rtatman/speech-accent-archive/version/2

    At this point, we are not sure exactly how the project will be structured.
    The plan is to have two neural networks, one of which is trained on our
    kaggle dataset to recognize accents, and one of which is trained against
    the first one, trying to trick it into believing the soundbyte it creates
    is speech of the correct accent. Accent distortion could possibly even be
    done with an evolutionary algorithm, but again, that is a ways down the
    line. We need to do a lot of research into machine learning and neural
    networks in order to determine how feasible this is and how to do it.


**Project Schedule:**

**3/29** - Project Proposal Submission

**3/29-4/3** - Familiarization with possible libraries and project frameworks to
come up with a comprehensive architectural plan for the project to present for
the AR; pivot time if needed

**4/3-4/16** - Use collaboration plan to develop and implement code to have a
solid basis by the first three weeks of the project; last week and a half to
debug and improve

**4/17** - Focus on website development and implementation

**4/24** - Code progress and Website Draft due

**5/1** - Final Website

**5/7** - Demo Poster Completed

**5/8** - Demo Session; poster printed before noon; code submitted



**Collaboration Plan:**

    As of right now, we are still figuring out preferences for the final
    project, but we all have a good level of comfort with pair programming.
    From an implementation standpoint, it seems that the initial research and
    development stages of the project will require a bit more individual
    programming. This will be aided by differing schedules, which will
    hopefully result in fewer merge conflicts, and as the project begins to
    culminate, pair programming will be more evident in our implementation as
    we debug and improve our code.

**Risks:**

    This might be much harder than we think it will be, especially the stretch
    goals. We really have very little concept of how hard even the initial part
    will be; it might be very simple, or it might be almost too challenging all
    by itself. Our main concern is definitely feasibility.

**Additional Course Content:**

-Learning more about implementing different libraries and finding appropriate
ones; parsing through documentation; scipy, numpy, etc.

-Delve more in-depth into some of the toolboxes, especially machine learning and
evolutionary algorithms; possibly the web apps one in order to provide clarity
for the website.
