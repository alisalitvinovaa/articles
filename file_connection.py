import json

def get_articles():
    with open('articles.json', 'r', encoding='utf-8') as f:
        q=json.load(f)
    return q
def zapis(name, text):
    with open('articles.json', 'r', encoding='utf-8') as f:
        q=json.load(f)
    q[name]=text
    with open('articles.json', 'w', encoding='utf-8') as f:
        json.dump(q, f, ensure_ascii=False)
def delete_article(name):
    with open('articles.json', 'r', encoding='utf-8') as f:
        q = json.load(f)
    del q[name]
    with open('articles.json', 'w', encoding='utf-8') as f:
        json.dump(q, f, ensure_ascii=False)
