#
# Book Tracker
#
# booktracker.py

# 

import requests

def get_book_info(isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if "items" in data:
            book = data["items"][0]["volumeInfo"]
            title = book.get("title", "N/A")
            authors = ", ".join(book.get("authors", ["Unknown Author"]))
            published_date = book.get("publishedDate", "N/A")
            description = book.get("description", "No description available")
            page_count = book.get("pageCount", "N/A")
            categories = ", ".join(book.get("categories", ["N/A"]))
            thumbnail = book.get("imageLinks", {}).get("thumbnail", "No image available")

            return {
                "Title": title,
                "Authors": authors,
                "Published Date": published_date,
                "Description": description,
                "Page Count": page_count,
                "Categories": categories,
                "Thumbnail": thumbnail,
            }
        else:
            return {"Error": "No book found for this ISBN"}
    else:
        return {"Error": f"API request failed with status code {response.status_code}"}

# Example usage
isbn = "9780143126560"  # Example ISBN
book_info = get_book_info(isbn)

for key, value in book_info.items():
    print(f"{key}: {value}")
