# Simple Python Web Server

A lightweight Python web server built as a group project using concepts from "500 Lines or Less: A Simple Web Server".

The goal of this project is to learn how web servers work internally by building one from scratch using Python 3.

## Features

This project implements:

- ✔ Basic HTTP request handling.
- ✔ Serving static HTML files.
- ✔ Directory listing.
- ✔ Custom 404 error handling.
- ✔ Simple Python CGI execution (optional but included).
- ✔ Clean modular architecture using "case handlers".

## Project Structure

```
simple-web-server/
│
├── server.py                     # Main server file
│
├── handlers/                     # Case handler classes
│   ├── base_case.py
│   ├── case_no_file.py
│   ├── case_existing_file.py
│   ├── case_directory.py
│   ├── case_cgi.py
│
├── www/                          # Public web root (static files)
│   ├── index.html
│   ├── ... other HTML files
│   └── time.py                   # Example CGI script
│
├── README.md                     # Project description
└── CONTRIBUTING.md               # Contribution workflow
```

## Python Version

This project uses:

- **Python 3.x**

The original tutorial uses Python 2, so we have to update all code to be Python 3–compatible.

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd simple-web-server
```

### 2. Run the server

```bash
python3 server.py
```

### 3. Open in your browser

Go to:

```
http://localhost:8080
```

You should see your `index.html` file load.

## How It Works (Short Explanation)

The server uses a rule-based (case) system:

- If the path is a file → serve file
- If the path is a directory with `index.html` → serve index
- If the path is a directory without index → show a listing
- If the file doesn't exist → return 404
- If the file is a `.py` → execute as CGI script

Each behavior lives inside its own handler class in the `handlers/` folder.

This keeps the code clean, readable, and easy to extend.

## Testing (Optional for Later)

You can test your server by placing extra files inside the `www/` folder:

- Add `about.html`
- Add folders like `/pages/index.html`
- Try requesting invalid URLs to test the 404 page

## Team Members

- **Project Lead:** Emmanuel Kiplimo
- **Backend Developer:** Faith Bonareri
- **Backend Developer:** Daniel Mwago

## Contribution Guide

For details on contributing, branching, and pull requests, see:

➡ [CONTRIBUTING.md](CONTRIBUTING.md)

(Everything you need is in there.)

## Screenshots

You can add screenshots later, for example:

- Web server running in terminal
- Index page loading in the browser
- Directory listing page

Just upload the images to GitHub and reference them here.

## Project Goal

This project is intended for learning:

- How HTTP works
- How web servers route requests
- Python file I/O
- Basic networking concepts
- Software engineering collaboration
- Git/GitHub workflows

It is not meant to replace production web servers, but to help us understand the fundamentals behind them.

---

## Happy Coding!

If you've reached this part you're awesome.

Now run the server, break it, fix it, and learn from it.
