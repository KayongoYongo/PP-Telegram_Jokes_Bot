import requests

def get_jokes(category: str) -> dict:
    """
    Description:
        This function fetches Jokes based on their provided category

    Args:
        category: The category of the joke in string form

    Return:
        A dictionary representation of the function
    """
    # Parameters to blacklist
    blacklist = "?blacklistFlags=nsfw,racist,sexist,explicit"

    # The base url
    url = "https://v2.jokeapi.dev/joke/" + category + blacklist

    # Need to fix the API url to accept a specific category

    # The response
    response = requests.get(url)

    return response.json()