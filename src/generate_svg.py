import re
import requests
from helpers.generate_hash import generate_hash
from helpers.write_files import write_files
from constants import svg_regex


def generate_svg(url):
    try:
        url_request = requests.get(url).content.decode('utf-8')
        content = re.search(svg_regex, url_request).group()
        write_files(content, 'logo_{}.svg'.format(generate_hash()))
    except:
        print(':)')
