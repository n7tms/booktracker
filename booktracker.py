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

            return {
                "Title": book.get("title", "N/A"),
                "Subtitle": book.get("subtitle", "N/A"),
                "Authors": ", ".join(book.get("authors", ["Unknown Author"])),
                "Publisher": book.get("publisher", "N/A"),
                "Published Date": book.get("publishedDate", "N/A"),
                "Description": book.get("description", "No description available"),
                "Page Count": book.get("pageCount", "N/A"),
                "Categories": ", ".join(book.get("categories", ["N/A"])),
                "Average Rating": book.get("averageRating", "N/A"),
                "Ratings Count": book.get("ratingsCount", "N/A"),
                "Language": book.get("language", "N/A"),
                "ISBN-10": next((id["identifier"] for id in book.get("industryIdentifiers", []) if id["type"] == "ISBN_10"), "N/A"),
                "ISBN-13": next((id["identifier"] for id in book.get("industryIdentifiers", []) if id["type"] == "ISBN_13"), "N/A"),
                "Thumbnail": book.get("imageLinks", {}).get("thumbnail", "No image available"),
                "Preview Link": book.get("previewLink", "N/A"),
                "Info Link": book.get("infoLink", "N/A"),
            }
        else:
            return {"Error": "No book found for this ISBN"}
    else:
        return {"Error": f"API request failed with status code {response.status_code}"}

# Example usage
# isbn = "9780143126560"  # Example ISBN
isbn = "1913666522"
book_info = get_book_info(isbn)

for key, value in book_info.items():
    print(f"{key}: {value}")
