import os
from posixpath import dirname
import webbrowser

from dotenv import load_dotenv
from badge_generator import BadgeGenerator
from generate_svg import generate_svg

load_dotenv(os.path.abspath(
    os.path.join(dirname(__file__), os.pardir, '.env')))
instance = BadgeGenerator()

url, is_download_needed = instance.init()
webbrowser.open(url, new=2)

if is_download_needed:
    generate_svg(url)
