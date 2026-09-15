```markdown
> ⚠️ This repository is archived.
> It is no longer actively maintained. The code is provided as-is for reference and learning purposes.
```
# TextUtils - A Modern Text Analyzer & Utility <sub>([🌐 Live Demo](https://textutils-5dz1.onrender.com))</sub>

> A lightning-fast, client-side text utility tool built with Django & vanilla JavaScript. No page reloads, just instant results.

![TextUtils Banner](https://github.com/Dhiraj73Ray/TextUtils/blob/main/SS/Screenshot.png?raw=true) <!-- Replace with a real screenshot! -->

## 🚀 Features

- **Core Transformations:** Case conversion (UPPER, lower, Title, Sentence), remove punctuation/numbers, reverse text/lines, sort lines (A-Z, Z-A, by length), and more.
- **Advanced Utilities:** Find & Replace, Extract Emails/URLs, Base64 Encode/Decode, URL Encode/Decode, and JSON Formatting.
- **Modern UX:** Split-screen layout, dark mode toggle, file upload/download (.txt), and live character/word/line statistics.
- **Instant Processing:** All operations run client-side in real-time. The server is only used to serve the initial page.

## 🛠️ Tech Stack

- **Backend:** Python 3.x, Django 4.2+
- **Frontend:** HTML5, Bootstrap 5.3, Vanilla JavaScript (ES6)
- **Deployment:** Render

## 🏁 Getting Started (Local Development)

Follow these steps to get the project running on your machine.

### Prerequisites
- Python 3.8+
- pip

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YourUsername/textutils.git
    cd textutils
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    # Windows:
    env\Scripts\activate
    # macOS/Linux:
    source env/bin/activate
    ```


3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:

    ```bash
    python manage.py migrate
    ```

5. Start the development server:

    ```bash
    python manage.py runserver
    ```

6. **Open your browser and go to http://127.0.0.1:8000.**

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

📄 License
Distributed under the MIT License. See LICENSE for more information.


Project Link: https://github.com/Dhiraj73Ray/TextUtils
