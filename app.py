from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

def get_json_blog_posts():
    with open('blog_posts.json', 'r', encoding='utf-8') as json_file:
        posts_data = json.load(json_file)

    return posts_data


def get_json_blog_post(post_id):
    posts_data = get_json_blog_posts()

    for post in posts_data:
        if post['id'] == post_id:
            return post

    return None


def update_json_blog_posts(posts_data):
    with open('blog_posts.json', 'w', encoding='utf-8') as json_file:
        json.dump(posts_data, json_file)


def add_json_blog_posts(author, title, content):
    current_data = get_json_blog_posts()
    next_id = current_data[-1]['id'] + 1
    new_post = {
        "id" : next_id,
        "author" : author,
        "title" : title,
        "content" : content
    }
    current_data.append(new_post)

    update_json_blog_posts(current_data)

def delete_json_blog_posts(index_to_delete):
    current_data = get_json_blog_posts()

    for post in current_data:
        if post['id'] == index_to_delete:
            current_data.remove(post)

            update_json_blog_posts(current_data)


def edit_json_blog_posts(index_to_edit, author, title, content):
    current_data = get_json_blog_posts()

    for post in current_data:
        if post['id'] == index_to_edit:
            post['author'] = author
            post['title'] = title
            post['content'] = content

            update_json_blog_posts(current_data)


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

        add_json_blog_posts(author, title, content)
        return redirect(url_for("index"))

    return render_template('add.html')


@app.route('/delete/<int:post_index>')
def delete(post_index):
    delete_json_blog_posts(post_index)
    return redirect(url_for("index"))


@app.route('/edit/<int:post_index>', methods=['GET', 'POST'])
def edit(post_index):
    if request.method == 'POST':
        author = request.form['author']
        title = request.form['title']
        content = request.form['content']

        edit_json_blog_posts(post_index, author, title, content)
        return redirect(url_for("index"))

    post = get_json_blog_post(post_index)
    if post is None:
        # Post not found
        return "Post not found", 404
    return render_template('edit.html', post=post)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

