# system module
import os

#path dir
cur_dir = os.path.dirname(__file__)
tmp_dir = cur_dir

from src.utils.sentence_similarity import tokenDealer
from src.T5_Generator.output import Generate_Paraphrase

#create a result directory
try:
    os.makedirs(tmp_dir+'/result')
except:
    pass

if __name__ == "__main__":
    #create our output file in /result dir
    output = open("result\\next.txt","w")

    td = tokenDealer()
    target = open("message.txt",'r').read()
    print(f"target text is {target}")

    #generate the Paraphrases Sentences by T5
    Generate_Paraphrase = Generate_Paraphrase()
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
    
    #rank the similarity of sentence in descending order (the top is the sentence that have the most similar meaning with the original text)
    for similarity_meaning, words_absolute_similarity, paraphrases_text in sorted(similarities)[::-1]:
        output.write(f"Words Overlapping: {words_absolute_similarity} | Sentence Meaning: {similarity_meaning} | Extracted: {paraphrases_text} \n")
    output.close()