import json
import subprocess

def get_release_assets(version):
    result = subprocess.run(
        ['gh', 'release', 'view', version, '--json', 'assets', '--jq', '.assets[].url'],
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout.strip().split('\n')

def load_books_json(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)

def find_new_books(json_file, versions):
    data = load_books_json(json_file)
    existing_urls = {book['url'] for books in data.values() for book in books}

    new_books = []
    for version in versions:
        assets = get_release_assets(version)
        for url in assets:
            if url not in existing_urls:
                new_books.append(url)

    return new_books

def add_book_to_json(subject, title, url, json_file):
    with open(json_file, 'r+') as f:
        data = json.load(f)
        if subject not in data:
            confirm = input(f"Subject '{subject}' not found. Do you want to add it? (yes/no): ")
            if confirm.lower() != 'yes':
                print("Aborting.")
                return
            data[subject] = []
        # Check if the book is already in the JSON
        if not any(book['url'] == url for book in data[subject]):
            data[subject].append({'title': title, 'url': url})
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()

if __name__ == "__main__":
    json_file = 'books.json'
    versions = ['v1.1', 'v1.0']
    new_books = find_new_books(json_file, versions)

    if new_books:
        print("New books found:")
        for book in new_books:
            print(book)
            subject = input(f"Enter the subject for {book}: ")
            title = book.split('/')[-1].replace('.', ' ').replace(' pdf', '')
            add_book_to_json(subject, title, book, json_file)
    else:
        print("No new books found.")
