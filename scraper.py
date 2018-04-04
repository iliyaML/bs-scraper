import requests
from bs4 import BeautifulSoup

# Source page
url = 'http://www.bbc.com/'

# Format source code
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")

# Container output
output = ""

# Get all links in home page
for link in soup.findAll('a'):
    output = output + link.get('href') + "\n"

# Write output into file
text_file = open("bbc-links.txt", "w")
text_file.write(output)
text_file.close()