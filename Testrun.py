
print('Bollean logic')
print('Bollean logic')

print(2 == 2 and 3==3)
print(2 == 2 and 3==4)
print(2 == 2 or 3==4)
print(2 == 2 or 3==3)
print(not 2 == 2 )
print(not 2 != 2 )

# Fetching Jokes From Internet
# Fetching Jokes From Internet




from urllib import request
import json
# Fetching Jokes From Internet
# Fetching Jokes From Internet
url = "https://official-joke-api.appspot.com/random_joke"

r = request.urlopen(url)
# print(r)
print(r.getcode())
# print(r.read())
data = r.read()
jsonData = json.loads(data)

#print(jsonData)


class Joke:

    def __init__(self, setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline

    def __str__(self) -> str:
        return f"setup {self.setup} punchline {self.punchline}"


jokes = []

for j in jsonData:
    setup = j["setup"]
    punchline = j["punchline"]
    joke = Joke(setup, punchline)
    jokes.append(joke)

print(f"Got {len(jokes)} jokes")

for joke in jokes:
    print(joke)
