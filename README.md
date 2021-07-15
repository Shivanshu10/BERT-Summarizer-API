# BERT-Summarizer-API
This API will summarize the given text and provide the summary as response

## Depolyment
```
git clone https://github.com/Shivanshu10/BERT-Summarizer-API.git
cd BERT-SUmmarizer-API
pip install -r requirements.txt
cd src
gunicorn --bind 0.0.0.0:80 wsgi:app
```
