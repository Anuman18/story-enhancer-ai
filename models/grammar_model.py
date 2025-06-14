from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class GrammarCorrector:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("vennify/t5-base-grammar-correction")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("vennify/t5-base-grammar-correction")

    def correct(self, text):
        input_text = "grammar: " + text
        inputs = self.tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
        outputs = self.model.generate(inputs, max_length=512, num_beams=4, early_stopping=True)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
