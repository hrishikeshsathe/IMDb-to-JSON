try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Easily get IMDb page information as a JSON file!',
    'author': 'Hrishikesh Sathe',
    'url': 'https://github.com/hrishikeshsathe/IMDb-to-JSON',
    'download_url': 'https://github.com/hrishikeshsathe/IMDb-to-JSON',
    'author_email': 'hrishikesh.sathe90@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],['requests'],['BeautifulSoup'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'imdb_to_json'
}

setup(**config)