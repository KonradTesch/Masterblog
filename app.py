from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

def get_json_blog_posts():
    with open('blog_posts.json', 'r', encoding='utf-8') as json_file:
        posts_data = json.load(json_file)

    return posts_data

def update_json_blog_posts(author, title, content):
    current_data = get_json_blog_posts()
    next_id = current_data[-1]['id'] + 1
    new_post = {
        "id" : next_id,
        "author" : author,
        "title" : title,
        "content" : content
    }
    current_data.append(new_post)
    with open('blog_posts.json', 'w', encoding='utf-8') as json_file:
        json.dump(current_data, json_file)


@app.route('/')
def index():
    posts_data = get_json_blog_posts()
    return render_template('index.html', posts=posts_data)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        author = request.form['author']
        title = request.form['title']
        content = request.form['content']

        update_json_blog_posts(author, title, content)
        return redirect(url_for("index"))

    return render_template('add.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
