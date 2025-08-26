# Flask Blog Application

A simple, lightweight blog application built with Flask that demonstrates core web development skills including CRUD operations, template rendering, and file-based data storage.

## Features

- **Create** new blog posts with author, title, and content
- **Read** and display all blog posts on the main page
- **Update** existing blog posts with inline editing
- **Delete** unwanted blog posts
- Clean, responsive HTML interface
- JSON-based data persistence

## Technologies Used

- **Backend:** Python 3.x, Flask
- **Frontend:** HTML5, CSS3, Jinja2 templating
- **Data Storage:** JSON file-based storage
- **Styling:** Custom CSS

## Installation & Setup

1. **Install dependencies:**
   ```bash
   pip install flask
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Open your browser and visit:**
   ```
   http://localhost:5000
   ```

## Usage

### View Blog Posts
Navigate to the home page to see all published blog posts with their authors, titles, and content.

### Add a New Post
- Click the "Add a new blog posts here" link on the main page
- Fill out the form with author name, title, and content
- Submit to publish your post

### Edit an Existing Post
- Click the "edit" link next to any blog post
- Modify the fields as needed
- Submit to save changes

### Delete a Post
- Click the "delete" link next to any blog post
- The post will be permanently removed

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Display all blog posts |
| GET | `/add` | Show new post form |
| POST | `/add` | Create new blog post |
| GET | `/edit/<id>` | Show edit form for specific post |
| POST | `/edit/<id>` | Update specific blog post |
| GET | `/delete/<id>` | Delete specific blog post |

## Code Features Demonstrated

### Backend Skills
- **Flask Framework:** Route handling, request processing, template rendering
- **File I/O Operations:** JSON reading/writing with proper encoding
- **Data Manipulation:** CRUD operations on structured data
- **Error Handling:** 404 responses for missing resources
- **Function Documentation:** Comprehensive docstrings following Python standards

### Frontend Skills
- **Template Inheritance:** Jinja2 templating with dynamic content
- **Form Handling:** HTML forms with validation and proper encoding
- **Semantic HTML:** Proper use of HTML5 elements and attributes

### General Programming Practices
- **Code Organization:** Clean separation of concerns
- **Function Modularity:** Reusable helper functions
- **Data Persistence:** JSON-based storage with proper formatting
- **Input Validation:** Required fields and data type checking

## Development Notes

This project uses JSON file storage for simplicity and portability. For production applications, consider migrating to:
- SQLite for single-user applications
- PostgreSQL or MySQL for multi-user applications
- Implementing CSRF protection
- Adding input sanitization and validation

## Contributing

This is a portfolio project showcasing development skills. Feel free to explore the code!

---

**Created by** Konrad Tesch