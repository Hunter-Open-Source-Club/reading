# Computing Reading Group of CUNY Hunter College

## About

![Tree](assets/icons/tree.ico) Let's learn stuff together :)

## Suggest

Have something you want to read? Open an  <a href="https://github.com/Hunter-Open-Source-Club/reading/issues/new?title=Reading%20Suggestion:%20[title]&body=Title:%0AAuthor%20(optional):%0AURL%20(optional):%0A%0AWhy%20do%20you%20want%20to%20read%20this%3F%20(super%20optional):">issue</a> here.

## Usage

The reading list is contained in `readings.js` -- it is generated and manipulated by a set of Python programs in `assets/`, 
and inserted into the webpage by `scripts.js`.

As of right now there's no mechanism set up to automatically update the reading list with the contents of new suggestions, 
but it's possible to set up a GitHub Action to do so (which is why we have the following programs written to manipulate the reading list).

### `insert-reading.py`
```sh
usage: insert-reading.py [-h] [-a AUTHOR] [-u URL] [-c CATEGORY] title

positional arguments:
  title

optional arguments:
  -h, --help            show this help message and exit
  -a AUTHOR, --author AUTHOR
  -u URL, --url URL
  -c CATEGORY, --category CATEGORY
  
$ python3 insert-reading.py "Socialism: Utopian and Scientific" -a "Frederick Engels" -u "https://www.marxists.org/archive/marx/works/1880/soc-utop/index.htm" -c "Philosophy"
```

### `change-category.py`
```sh
usage: change-category.py [-h] [-a AUTHOR] -c CATEGORY title

positional arguments:
  title

optional arguments:
  -h, --help            show this help message and exit
  -a AUTHOR, --author AUTHOR
  -c CATEGORY, --category CATEGORY
                        category to move the reading into
                        
$ python3 change-category.py "Socialism: Utopian and Scientific" -c "Cool Stuff"
# trick to delete a reading (empty category)
$ python3 change-category.py "Socialism: Utopian and Scientific" -c ""
```

### `clear-readings.py`
```sh
Usage: python3 clear-readings.py
Clears all entries from reading list.
```
