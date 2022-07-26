import re
import spacy

class identityExtractor:
    english_nlp = spacy.load("en_core_web_lg")
    
    # extract name from a piece of text
    def extract_name(self, text):
        text_parsed = self.english_nlp(text)
        print("text parsed: " + str(text_parsed))

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
        return name

    # extract phone number from text
    def extract_phone_numbers(self,text):
        #the pattern of phone number 
        center_with_country_code = "\s+\+?(?:\d{1})?\(\d{3}\) ?\d{3}\-\d{4}\s+" #e.g. " (213)693-4567 "
        start_with_country_code = "^\+?(?:\d{1})?\(\d{3}\) ?\d{3}\-\d{4}\s+" #e.g. " (213)693-4567 "
        end_with_country_code = "\s+\+?(?:\d{1})?\(\d{3}\) ?\d{3}\-\d{4}\$" #e.g. " (213)693-4567 "
        only_number = "\s*\d{10}\s*" #e.g. " 2136934567"
         
        # '\+\d{1}\s*\d{3})?\d{3}\-?\d{3,4}'
        phone_numbers = re.findall(f'{center_with_country_code}|{start_with_country_code}|{end_with_country_code}|{only_number}',text)
        # phone_numbers = re.findall(f'{pattern1} | {pattern2}',text)

        for i in range(len(phone_numbers)):
            phone_numbers[i] = phone_numbers[i].strip()

        return phone_numbers

if __name__ == "__main__":
    ie = identityExtractor()
    phone_numbers = ie.extract_phone_numbers("My name is (213)693-4567 and 2136934567 +12136934567 and +1(213)618-8342 and +3(097)877-4388")
    if phone_numbers:
        for phone_number in phone_numbers:
            print(phone_number)


