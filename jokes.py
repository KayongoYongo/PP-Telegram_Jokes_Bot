import requests

def get_jokes(category: str, type: str) -> dict:
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
    url = f"https://v2.jokeapi.dev/joke/{category}{blacklist}&type={type}"

    # The response
    response = requests.get(url)

    return response.json()