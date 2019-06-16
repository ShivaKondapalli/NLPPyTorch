# Natural Language processing

## Introduction 

The best way to learn is by doing. Here is an implementation of various NLP tasks in *Pytorch*. 

## **1. RNN Classification: RNNClassification.py**

Created and Compared a*plain vanilla* reccurent neural network to a *Gated Recurrent Unit* on classyfying
the nationality of Individuals based on their names. 

Created a *Confusion Matrix* to compare the two models. The Gated Recurrent unit does much better since the diagonal entries are brighter.

This is expected as GRu netwokrs remember hidden state information which allows them to withhold important data.

## Prerequistes 

```
numpy - pip install numpy if using pip or conda install numpy 
Pytorch - Visit https://pytorch.org/ and choose installation based on your machine's specific configuration.
matplotlib - pip install matplotlib or conda install matplotlib
```
## Data

The data for this project is hosted at [Name to Nationality](https://download.pytorch.org/tutorial/data.zip).
Create a folder called **data** in your *current working directory*. 
Extract the *data.zip* file into that folder. 

## GPU vs CPU:

The code was written to run on a cpu. So don't worry if you don't have a Gpu. 
Notice how the diagonal entries for the GRU network are brighter compare the plain vanilla RNN.
