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
Pytorch - link the Pytorch website for machine specific installation
matplotlib - pip install matplotlib or conda install matplotlib
```
## Data

The data for this project is hosted at [Name to Nationality] (https://download.pytorch.org/tutorial/data.zip)
Extract the zip file into your current working directory. 

## GPU vs CPU:

The code was written to run on a cpu. So don't worry if you don't have a cpu. 
