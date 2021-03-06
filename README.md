# Natural Language processing

## Introduction 

The best way to learn is by doing. Here is an implementation of various NLP tasks in *Pytorch*. 

## 1. RNN Classification: Classyfying names to nationality- RNNClassification.py

Created and Compared a*plain vanilla* reccurent neural network to a *Gated Recurrent Unit* on classyfying
the nationality of Individuals based on their names. 

Created a *Confusion Matrix* to compare the two models. The Gated Recurrent unit does much better since the diagonal entries are brighter.

This is expected as GRu netwokrs remember hidden state information which allows them to withhold important data.

## Prerequistes 

```
numpy - pip install numpy if using pip or conda install numpy 
matplotlib - pip install matplotlib or conda install matplotlib
```
## Get Pytorch

Pytorch - Visit <https://pytorch.org/> and choose installation based on your machine's specific configuration.

## Data

The data for this project is hosted at [Name to Nationality](https://download.pytorch.org/tutorial/data.zip).
Create a folder called **data** in your *current working directory*. 
Extract the *data.zip* file into that folder. 

## GPU vs CPU:

The code was written to run on a cpu. So don't worry if you don't have a Gpu. 
Notice how the diagonal entries for the GRU network are brighter compare the plain vanilla RNN.

## 2. LSTM Classification: Classyfying names to gender - LSTMClassification.py

Wrote a web_scraper *web_scraper.py* to pull names of boys and girls from the web. Used *requests* and *beautifulsoup4* to achieve this.
Used a *Long short term memory network* to perform the classification. *LSTM* models are really powerful for storing lon term dependencies in natural language. 

## Prerequisites 

```
requests - pip install requests or conda install requests.
beautifulsoup4- pip install beautifulsoup4 or conda install beautifulsoup4
```
The other libraries are as previsouly mentioned in task 1. 

## Data

The *data* folder contains 'Girls.txt' and 'Boys.txt' files along with the names data for the previous project. Download this folder, extract to current working directory. 

A *Confusion matrix* is plotted to gauge the performance of our deep classifier.

## 3. Text Generation with LSTM: Generating movie scripts with LSTM.py - Generate_Text.py:

*Langauge modelling* is one the canonical applications of LSTM models. With gates that regulate the flow of information. These models 
can remember words that have occured a long time ago to predict the next word. Sampling from this distribution gives us new words. 

Developed a *character level* language model, trainig it on *Apocalypse Now*, to generate new words from the probability distribution 
found the model upon training. 

## Preqrequsites

```
PyPDF2 - pip install PyPDF2
```
The *PdfFileReader* class reads in pdf content. Extracted the data into a txt file. Cleaned it up and fed into the model. 

## Data

The *Apocalypse_Now.pdf* data is present in the *data* folder. Download and extract to current working directory.


