import requests
from bs4 import BeautifulSoup

def extract_content(blog_link):
    response = requests.get(blog_link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # TODO: extracting the data from the blog (right now only tested with wordpress biology blog)
        main_content = soup.find('div', class_='entry-content')

        if main_content:
            # extract the text from the blog
            paragraphs = main_content.find_all(['p', 'ul'])
            content = '\n\n'.join(para.get_text(strip=True) for para in paragraphs)
            return content
        else:
            return "Main content area not found."
    else:
        return "Failed to fetch the blog content."
    
if __name__ == "__main__":
    blog_link = input()
    content = extract_content(blog_link)
    print(content)