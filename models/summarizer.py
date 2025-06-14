from transformers import pipeline

class StorySummarizer:
    def __init__(self):
        self.summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

    def summarize(self, text):
        return self.summarizer(text, max_length=120, min_length=30, do_sample=False)[0]['summary_text']
