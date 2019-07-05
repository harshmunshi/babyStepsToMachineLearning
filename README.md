# babyStepsToMachineLearning

# Introduction
This repo would be a great start for someone who wants to use deep learning for computer vision. I'm a learner myself and hence open to all the suggestions that you might have. In this module we would be training a very simple Cats and Dogs classifier using tensorflow, save the model and the weights and use a finally use a function to test the accuracy.

# Requirements
1. Tensorflow (https://www.tensorflow.org/versions/r0.10/get_started/os_setup)
2. Python
3. Numpy

# Download the Dataset
You can download the data from https://www.kaggle.com/c/dogs-vs-cats/data . Follow the instructions and register yourself.

# Getting started
```
<br /> $ git clone https://github.com/harshmunshi/babyStepsToMachineLearning
<br /> $ cd babyStepsToMachineLearning
<br /> $ mkdir data
<br />$ cd data && mkdir training && mkdir validation
<br />$ cd training && mkdir cats && mkdir dogs
<br />$ cd ..
<br />$ cd validation && mkdir cats && mkdir dogs
```
From the dataset you have downloaded, 
1. put the cat pictures index 0-999 in data/train/cats
2. put the cat pictures index 1000-1400 in data/validation/cats
3. put the dogs pictures index 0-999 in data/train/dogs
4. put the dog pictures index 1000-1400 in data/validation/dogs

Now Run the following command(s)

<br />$ python harshNet.py
<br />$ python save_asjson.py
<br />$ python guess.py <path_to_image>

# Credits

https://gist.github.com/fchollet/0830affa1f7f19fd47b06d4cf89ed44d
