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
    url = "https://v2.jokeapi.dev/joke/" + category
    response = requests.get(url)

    return response.json()