import re 
import uuid
from datetime import datetime

_HOST_URL = "https://short.ly/"

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
    
    ret: str = _HOST_URL + uuid.uuid4().hex[:length]
    return ret

def get_timestamp() -> str:
    """
    Get the current timestamp in a readable format.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_short_url(hash_path: str) -> str:
    """
    Extract the short URL part from the full URL.

    :param hash_path: Hash of the short url
    """
    return _HOST_URL + hash_path