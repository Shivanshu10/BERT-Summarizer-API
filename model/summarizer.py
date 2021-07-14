from summarizer import Summarizer

def summarize(text):
    model = Summarizer()
    return model(text)