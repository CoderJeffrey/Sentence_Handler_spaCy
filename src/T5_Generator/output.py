import torch
import torchvision
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class Generate_Paraphrase:
    def generate(self, target):
        tokenizer = AutoTokenizer.from_pretrained("Vamsi/T5_Paraphrase_Paws")  
        model = AutoModelForSeq2SeqLM.from_pretrained("Vamsi/T5_Paraphrase_Paws")

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        #fetch the target phrase from extract_name module
        sentence = target

        text =  "paraphrase: " + sentence + " </s>"

        encoding = tokenizer.encode_plus(text,pad_to_max_length=True, return_tensors="pt")

        input_ids, attention_masks = encoding["input_ids"].to(device), encoding["attention_mask"].to(device)

        outputs = model.generate(
            input_ids=input_ids, attention_mask=attention_masks,
            max_length=256,
            do_sample=True,
            top_k=200,
            top_p=0.95,
            early_stopping=True,
            num_return_sequences=10
        )

        result = set()
        for output in outputs:
            line = tokenizer.decode(output, skip_special_tokens=True,clean_up_tokenization_spaces=True)
            result.add(line)
        return list(result)

# if __name__=="__main__":
#     Generator = Generate_Paraphrase()
#     Generator.generate("My name is Jeffrey Liu")