import json
import subprocess
import sys
import os

def upload_book(file_path):
    # Upload the book
    subprocess.run(['gh', 'release', 'upload', 'v1.1', file_path], check=True)

    # Get the download URL of the uploaded book
    result = subprocess.run(
        ['gh', 'release', 'view', 'v1.1', '--json', 'assets', '--jq', '.assets | sort_by(.createdAt | fromdateiso8601) | .[-1] | .url'],
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout.strip()

def add_book_to_json(subject, title, url, json_file):
    with open(json_file, 'r+') as f:
        data = json.load(f)
        if subject not in data:
            confirm = input(f"Subject '{subject}' not found. Do you want to add it? (yes/no): ")
            if confirm.lower() != 'yes':
                print("Aborting.")
                sys.exit(1)
            data[subject] = []
        # Check if the book is already in the JSON
        if not any(book['url'] == url for book in data[subject]):
            data[subject].append({'title': title, 'url': url})
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()

def regenerate_html():
    subprocess.run(['python', 'generate_books_html.py'], check=True)

def git_commit_and_push():
    subprocess.run(['git', 'add', 'books.json', 'books_content.html', 'books_secret.enc.js'], check=True)
    subprocess.run(['git', 'commit', '-m', 'Add new book'], check=True)
    subprocess.run(['git', 'push'], check=True)

def encrypt_html():
    file_path = "encrypt_books.js"

    try:
        result = subprocess.run(
            ["node", file_path],
            capture_output=True,
            text=True,
            check=True
        )

        print("Node.js script output:")
        print(result.stdout)

        if result.stderr:
            print("Node.js script errors:")
            print(result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"Error running Node.js script: {e}")
        print(f"Stderr: {e.stderr}")
    except FileNotFoundError:
        print("Error: 'node' command not found. Make sure Node.js is installed and in your system's PATH.")

if __name__ == "__main__":
    # do everything
    if True:
        if len(sys.argv) != 3:
            print("Usage: python add_book.py <subject> <file_path>")
            exit()

        subject = sys.argv[1]
        file_path = sys.argv[2]
        title = os.path.basename(file_path).replace('.', ' ').replace(' pdf', '')

        if not os.path.isfile(file_path):
            print(f"File not found: {file_path}")
            sys.exit(1)

        url = upload_book(file_path)
        add_book_to_json(subject, title, url, 'books.json')
        regenerate_html()
        encrypt_html()
        git_commit_and_push()

    # just create the content
    else:
        regenerate_html()
        encrypt_html()
