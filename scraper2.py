import requests
from bs4 import BeautifulSoup
import math

# Source page
url = 'https://news.ycombinator.com/'

# Format source code
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")

# Container output
output = ""
avgOfEachArticle = []

# Counter
i = 0
for link in soup.findAll('a', {'class': 'storylink'}):
    # Update count number
    i += 1

    # Get the title
    title = link.string
    
    # Split the title into an array of words
    words = title.split()

    # Append length of each word into an array
    lengthOfEachWord = []
    letter_count = { lengthOfEachWord.append(len(w)) for w in words }

    # Calculate average
    average = math.ceil(sum(lengthOfEachWord) / len(lengthOfEachWord))
    avgOfEachArticle.append(average)

    # Format output
    output += "Article {}\n".format(str(i))
    output += "\tTitle: {}\n".format(title)
    output += "\tWord Lengths: {}\n".format(', '.join(str(x) for x in lengthOfEachWord))
    output += "\tAverage Word Length: {}\n\n".format(str(average))

# Calculate the total average
totalAverage = math.ceil(sum(avgOfEachArticle) / len(avgOfEachArticle))

output += "Outcome: Base on these {} articles,".format(str(i))
output += "the average length of a word in Hacker News article title is {} letters.".format(str(totalAverage))

# Output
print(output)