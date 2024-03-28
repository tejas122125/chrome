import requests 
from bs4 import BeautifulSoup
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_text_splitters import CharacterTextSplitter



def get_all_links (url):
    link_collection = []

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
    # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all anchor tags (links) in the parsed HTML
        links = soup.find_all('a')

        # Extract the href attribute (URL) from each link
        for link in links:
            href = link.get('href')
            if href:
                link_collection.append(href)
                print(href)
    else:
        print("Failed to fetch the webpage. Status code:", response.status_code)

def data_loader(urls):
    for url in urls :
        loader = UnstructuredURLLoader(urls=url)



        
def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

        

def main():
    get_all_links("https://python.langchain.com/docs/modules/chains")

if __name__ == '__main__':
    
    main()    