from flask import Flask, request, jsonify
from flask_cors import CORS  # 引入 CORS
import json

app = Flask(__name__)
CORS(app)  # 啟用 CORS

# 讀取Josn檔,暫時的~有空就改成讀DB
def load_articles():
    with open('articles.json', 'r',encoding='utf-8') as f:
        return json.load(f)

# 儲存內文
def save_articles(articles):
    with open('articles.json', 'w') as f:
        json.dump(articles, f, indent=4)

# 取得所有文章
@app.route('/api/articles', methods=['GET'])
def get_articles():
    articles = load_articles()
    return jsonify(articles)

# 新增文章
@app.route('/api/articles', methods=['POST'])
def add_article():
    new_article = request.json
    articles = load_articles()
    articles.append(new_article)
    save_articles(articles)
    return jsonify(new_article), 201

if __name__ == '__main__':
    app.run(debug=True)