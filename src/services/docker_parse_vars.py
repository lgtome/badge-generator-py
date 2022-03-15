import os


def docker_parse_variables():
    try:
        name = os.environ['name'].strip('"\'')
        logo = os.environ['logo'].strip('"\'')
        bgColor = os.environ['bgColor'].strip('"\'')
        logoColor = os.environ['logoColor'].strip('"\'')
        return [name, logo, bgColor, logoColor]
    except:
        print('Bad env vars')


arr = ["'✨I'm there!✨'", "'spotify'", "'green'", "'black'"]
