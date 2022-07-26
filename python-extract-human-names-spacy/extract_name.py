import spacy
from lib2to3.pgen2 import token
from torch import double

# system module
import os
import sys

#path dir
cur_dir = os.path.dirname(__file__)
tmp_dir = cur_dir
target_dir = os.path.join(cur_dir, "..", "Paraphrase-Generator")
sys.path.append(target_dir)

#self-defined module
import demo

class tokenDealer:
    nlp = spacy.load("en_core_web_lg")

    def preprocess(self, target_text):
        #remove leading and trailing spaces 
        target_text = target_text.strip()
        # target_text_nlp = nlp()
        #other preprocessing needed
        return target_text

    def similar_compare(self, target_text, paraphrase_text):
        target_text_nlp, paraphrase_text_nlp = self.nlp(target_text), self.nlp(paraphrase_text)
        target_text_nlp_processed = self.nlp(' '.join([str(t_text) for t_text in target_text_nlp if not t_text.is_stop]))
        paraphrase_text_nlp_processed = self.nlp(' '.join([str(t_text) for t_text in paraphrase_text_nlp if not t_text.is_stop]))

        tmp = []
        count = 0
        l_target_text = target_text.split()
        l_paraphrase_text = paraphrase_text.split()
        for word in l_paraphrase_text:
            if word in l_target_text:
                count+=1
                tmp.append(word)
        
        words_absolute_similarity = (count*2) / (len(l_target_text) + len(l_paraphrase_text))
        # target_text_nlp = self.nlp(' '.join([str(t_text) for t_text in target_text if t_text.pos_ in ['NOUN','PRONOUN']])
        
        similarity_meaning = target_text_nlp_processed.similarity(paraphrase_text_nlp_processed)
        similarity_meaning = round(similarity_meaning,2)
        words_absolute_similarity = round(words_absolute_similarity, 2)
        return similarity_meaning, words_absolute_similarity


    def extract(self, text):
        english_nlp = spacy.load("en_core_web_sm")
        text_parsed = english_nlp(text)
        print("text parsed: " + str(text_parsed))

        #ents means the named entities of the text
        name = set()

        #number of the person appeared in a single piece of text
        name_count = 0
        for entity in text_parsed.ents:
            print(entity)
            entry = str(entity.lemma_).lower()
            text.replace(str(entity).lower(),"")
            print("entity is: " + str(entity))
            print(str(entity.text) + " is of type: " + str(entity.label_))

            #extract Name
            if str(entity.label_) == "PERSON":
                name.add(entity.text.lower())
        print(name)

if __name__== '__main__':

    #create a result directory
    try:
        os.makedirs(tmp_dir+'/result')
    except:
        pass
    
    #create our output file in /result dir
    output = open("result\\next.txt","w")

    td = tokenDealer()
    target = open("message.txt",'r').read()

    #generate the Paraphrases Sentences by T5
    Generate_Paraphrase = demo.Generate_Paraphrase()
    paraphrases = Generate_Paraphrase.generate(target)

    #preprocess our target text
    output.write("Original Text: " + str(target) + "\n")
    target_text = td.preprocess(target)

    similarities = []
    for i in range(len(paraphrases)):
        # preprocess the input text
        paraphrases_text = td.preprocess(paraphrases[i])

        #find out its similarity with our target text
        similarity_meaning, words_absolute_similarity = td.similar_compare(target_text, paraphrases_text)
        similarities.append([similarity_meaning, words_absolute_similarity, paraphrases_text])

    for similarity_meaning, words_absolute_similarity, paraphrases_text in sorted(similarities)[::-1]:
        output.write(f"Words Overlapping: {words_absolute_similarity} | Sentence Meaning: {similarity_meaning} | Extracted: {paraphrases_text} \n")
    output.close()