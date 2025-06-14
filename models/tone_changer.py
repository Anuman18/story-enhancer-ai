from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class ToneChanger:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("prithivida/parrot_paraphraser_on_T5")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("prithivida/parrot_paraphraser_on_T5")

    def change_tone(self, text, tone='formal'):
        if tone == 'formal':
            prompt = f"paraphrase: {text} tone:formal"
        else:
            prompt = f"paraphrase: {text} tone:informal"

        inputs = self.tokenizer.encode(prompt, return_tensors="pt", max_length=512, truncation=True)
        outputs = self.model.generate(inputs, max_length=128, num_beams=5, num_return_sequences=1, temperature=1.5)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
