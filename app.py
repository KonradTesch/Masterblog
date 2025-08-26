from flask import Flask, render_template
import json

app = Flask(__name__)

def get_json_blog_posts():
    with open('blog_posts.json', 'r', encoding='utf-8') as json_file:
        posts_data = json.load(json_file)

    return posts_data
@app.route('/')
def index():
    posts_data = get_json_blog_posts()
    return render_template('index.html', posts=posts_data)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
