from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

def get_json_blog_posts():
    """
    Load and return all blog posts from the JSON file
    :return: List of blog post dictionaries
    """
    with open('blog_posts.json', 'r', encoding='utf-8') as json_file:
        posts_data = json.load(json_file)

    return posts_data


def get_json_blog_post(post_id):
    """
    Retrieve a specific blog post by its ID
    :param post_id: The unique identifier of the blog post
    :return: Blog post dictionary if found, None otherwise
    """
    posts_data = get_json_blog_posts()

    for post in posts_data:
        if post['id'] == post_id:
            return post

    return None


def update_json_blog_posts(posts_data):
    """
    Save the updated blog posts data to the JSON file
    :param posts_data: List of blog post dictionaries to save
    :return: None
    """
    with open('blog_posts.json', 'w', encoding='utf-8') as json_file:
        json.dump(posts_data, json_file)


def add_json_blog_posts(author, title, content):
    """
    Add a new blog post to the JSON file
    :param author: Name of the blog post author
    :param title: Title of the blog post
    :param content: Content/body of the blog post
    :return: None
    """
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
    """
    Delete a blog post from the JSON file by its ID
    :param index_to_delete: ID of the blog post to delete
    :return: None
    """
    current_data = get_json_blog_posts()

    for post in current_data:
        if post['id'] == index_to_delete:
            current_data.remove(post)

            update_json_blog_posts(current_data)


def edit_json_blog_posts(index_to_edit, author, title, content):
    """
    Edit an existing blog post in the JSON file
    :param index_to_edit: ID of the blog post to edit
    :param author: Updated author name
    :param title: Updated title
    :param content: Updated content
    :return: None
    """
    current_data = get_json_blog_posts()

    for post in current_data:
        if post['id'] == index_to_edit:
            post['author'] = author
            post['title'] = title
            post['content'] = content

            update_json_blog_posts(current_data)


@app.route('/')
def index():
    """
    Render the main page displaying all blog posts
    :return: Rendered HTML template with blog posts
    """
    posts_data = get_json_blog_posts()
    return render_template('index.html', posts=posts_data)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Handle adding new blog posts - display form on GET, process submission on POST
    :return: Rendered add form template on GET, redirect to index on successful POST
    """
    if request.method == 'POST':
        author = request.form['author']
        title = request.form['title']
        content = request.form['content']

        add_json_blog_posts(author, title, content)
        return redirect(url_for("index"))

    return render_template('add.html')


@app.route('/delete/<int:post_index>')
def delete(post_index):
    """
    Delete a blog post and redirect to the main page
    :param post_index: ID of the blog post to delete
    :return: Redirect to the main page
    """
    delete_json_blog_posts(post_index)
    return redirect(url_for("index"))


@app.route('/edit/<int:post_index>', methods=['GET', 'POST'])
def edit(post_index):
    """
    Handle editing blog posts - display prefilled form on GET, process updates on POST
    :param post_index: ID of the blog post to edit
    :return: Rendered edit form on GET, redirect to index on successful POST, 404 if post not found
    """
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