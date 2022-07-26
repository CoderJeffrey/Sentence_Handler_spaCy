import spacy
from lib2to3.pgen2 import token
from torch import double

# 2 ways to import relative packages
# import os
# import sys
# from .. T5_Generator.demo import Generate_Paraphrase
# #path dir
# cur_dir = os.path.dirname(__file__)
# tmp_dir = cur_dir
# target_dir = os.path.join(cur_dir, "..", "Paraphrase-Generator")
# sys.path.append(target_dir)
# #self-defined module
# import demo

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