import re 
import uuid
from datetime import datetime

def validate(url: str) -> bool:
    """
    Validate the given url.
    Currently supports HTTP(s) and FTP(s).

    :param url: URL to validate
    """

    pat = re.compile(r"^(http|ftp)s?:\/\/[^\s/$\.\?\#].[^\s]*$")
    if not re.fullmatch(pat, url):
        return False
    return True

def generate_short_url(length: int = 8) -> str:
    """
    Generate a random short URL string of given length.

    :param length: Length of the short URL string
    """
    
    return uuid.uuid4().hex[:length]

def get_timestamp() -> str:
    """
    Get the current timestamp in a readable format.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
