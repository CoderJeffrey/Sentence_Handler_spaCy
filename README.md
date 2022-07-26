## Overview 
A Module can be implemented to 
 1. extract name from a sentence
 2. extract phone number from a conversation (US only)
 3. Compare the similarity of two sentences based on their words matching and rank them based on their similarity in terms of meaning
    1. Utilize the Paraphrase Generator (T5) to generate a fixed number of similar sentences for testing purposes

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
### Prerequisites
#### spaCy 

- pip
- Conda (recommended - optional)
- spaCy   

For people aren't acquainted with conda, it is a package management and environment management system that allows you to have different environments based on your current project. 
An easy example will be: if you need spacy and Python (version 3.9) in this project for Project A, and you need transformers and Python (version 3.10) for project B, then you need two environments.

Pip is another package installer for Python.

#### T5 Paraphrase Generator

- Streamlit library
- Huggingface transformers library
- Pytorch
- Tensorflow 


### Installation 

In short, run setup.sh to install all needed packages.
```
$ sh setup.sh
```

And install pytorch from https://pytorch.org/
(e.g. System of Windows using Python + pip (in conda) and doesn't have CUDA in system can use the following script)
```
$ pip3 install torch torchvision torchaudio
```


For people interested in the details of the needed packages:
#### spaCy 
- pip
```
$ conda install pip
```
- spaCy

```
$ pip install -U pip setuptools wheel
$ pip install -U spacy
$ python -m spacy download en_core_web_lg (or can change to other dictionaries based on your needs)
```
    - or can change to other dictionaries based on your needs
        - sm: small (without vectors)
        - md: medium
        - lg: large


### T5 Paraphrase Generator


- Huggingface transformers library
```
$ pip install transformers
```

- Tensorflow
```
$ pip install --upgrade tensorflow
```

### General Usage
python demo.py (to display the results of the similarity index between a sentence and 10 of its paraphrased sentences)

#### Results
Results are in the ./result dir
