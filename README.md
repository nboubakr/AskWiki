AskWiki
=======
AskWiki is a python package for querying WikiPedia in any language from your python application.

## Usage

Import the package to your project:

```python
import AskWiki

# Instantiate a new object and ask it
obj = AskWiki('en')  # Add wikipedia language as param or leave it for english
print obj.ask('API') # To ask wikipedia for an article
```

This package was inspired from [AskWiki - Ruby Gem](https://github.com/blazeeboy/askwiki)
