# JSONata Playground

A simple, clean, and responsive web-based playground for evaluating [JSONata](https://jsonata.org/) expressions against JSON data in real-time.

This application provides a side-by-side view for your JSON input and your JSONata expression, with the result displayed in a separate panel below the expression. It's a handy tool for developing, testing, and debugging JSONata queries.

## Features

-   **Live Evaluation**: The JSONata expression is evaluated automatically as you type.
-   **Syntax Highlighting**: CodeMirror is used for pleasant syntax highlighting for both JSON and the JSONata expression.
-   **JSON Formatting**: A "Format JSON" button to quickly prettify your JSON input.
-   **Resizable Layout**: Drag the dividers to resize the panels to your liking.
-   **Error Handling**: Displays clear error messages for invalid JSON or JSONata expressions.
-   **State Persistence**: Your last JSON input and expression are saved to your browser's local storage, so you can pick up where you left off.
-   **Autocomplete**: Suggests JSONata functions as you type in the expression editor (press `Ctrl-Space` to trigger).

## Tech Stack

-   **Backend**: Python with [Flask](https://flask.palletsprojects.com/)
-   **JSONata Engine**: [jsonata-python](https://pypi.org/project/jsonata-python/)
-   **Frontend**: Vanilla JavaScript, HTML, and CSS
-   **Editor**: [CodeMirror](https://codemirror.net/)

## Setup and Installation

Follow these steps to run the application locally.

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd jsonata-playground
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python app.py
    ```

5.  **Open your browser:**
    Navigate to `http://127.0.0.1:5000` to start using the playground.

## How to Use

1.  **JSON Input**: Enter or paste your JSON data into the left-hand panel. You can click the **Format JSON** button to prettify it.
2.  **JSONata Expression**: Write your JSONata query in the top-right panel.
3.  **Result**: The output of the expression will appear automatically in the bottom-right panel. A status badge will indicate if the evaluation was successful (`OK`) or resulted in an error (`Error`).

The layout is fully resizable. You can drag the vertical and horizontal dividers to adjust the size of the panels to best suit your needs.