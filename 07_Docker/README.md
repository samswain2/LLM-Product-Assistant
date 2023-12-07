## Folder Structure
Below is the folder structure of this project:

```
├── Dockerfile
├── README.md
├── requirements.txt
```

### File Descriptions

#### `Dockerfile`
The Dockerfile is used to build a Docker image for running a Flask-based chatbot application. Key aspects include:
- **Base Image**: Uses Python 3.10.7.
- **Working Directory**: Sets `/chatBot` as the working directory inside the container.
- **File Copying**: Copies the application files (`app.py`, `static`, `templates`, `.env`) and `requirements.txt` into the working directory.
- **Dependencies**: Installs Python packages specified in `requirements.txt`.
- **Environment Variables**: Sets Flask-specific environment variables (`FLASK_APP` and `FLASK_RUN_HOST`).
- **Command**: Executes `flask run` to start the Flask application.

#### `requirements.txt`
This is a standard text file listing all the Python package dependencies required for the Flask chatbot application. The Dockerfile uses this file to install the necessary packages inside the Docker container.