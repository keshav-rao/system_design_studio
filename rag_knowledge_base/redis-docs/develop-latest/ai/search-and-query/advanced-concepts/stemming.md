# Stemming

```json metadata
{
  "schema_version": 2,
  "title": "Stemming",
  "description": "Stemming support",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"how-it-works","title":"How it works?"},{"id":"supported-languages","title":"Supported languages"},{"id":"chinese-support","title":"Chinese support"},{"id":"using-custom-dictionaries","title":"Using custom dictionaries"}]}

,
  "codeExamples": []
}
```


RediSearch supports stemming - that is adding the base form of a word to the index. This allows the query for "`hiring`" to also return results for "`hire`" and "`hired`", for example.

The current stemming support is based on the Snowball stemmer library, which supports most European languages, as well as Arabic and other. See the "[Supported languages](#supported-languages)" section below. We hope to include more languages soon (if you need a specific language support, please open an issue).

For further details see the [Snowball Stemmer website](https://snowballstem.org/).


## How it works?

Stemming maps different forms of the same word to a common root - "stem" - for example, the English stemmer maps *studied* ,*studies* and *study* to *studi* . So a searching for *studied* would also find documents which only have the other forms.


In order to define which language the Stemmer should apply when building the index, you need to specify the `LANGUAGE` parameter for the entire index or for the specific field. For more details check the [FT.CREATE](https://redis.io/docs/latest/commands/ft.create) syntax.

**Create a index with language definition**

Create a index for words in German "`wort:`" with a single `TEXT` field "`wort`"


redis> FT.CREATE idx:german ON HASH PREFIX 1 "wort:" LANGUAGE GERMAN SCHEMA wort TEXT


**Adding words**

Adding some words with same stem in German, all variations of the word `stück` ( `piece` in english): `stück stücke stuck stucke` => `stuck`


redis> HSET wort:1 wort stück
(integer) 1
redis> HSET wort:2 wort stücke
(integer) 1
redis> HSET wort:3 wort stuck
(integer) 1
redis> HSET wort:4 wort stucke
(integer) 1


**Searching for a common stem**

Search for "stuck" (german for "piece"). As of v2.10, it's only necessary to specify the `LANGUAGE` argument when it wasn't specified to create the index being used to search.
Note the results for words that contains "`ü`" are encoded in UTF-8.


redis> FT.SEARCH idx:german '@wort:(stuck)' German
1) (integer) 4
2) "wort:3"
3) 1) "wort"
   2) "stuck"
4) "wort:4"
5) 1) "wort"
   2) "stucke"
6) "wort:1"
7) 1) "wort"
   2) "st\xc3\xbcck"
8) "wort:2"
9) 1) "wort"
   2) "st\xc3\xbccke"


## Supported languages

The following languages are supported and can be passed to the engine when indexing or querying using lowercase:

* `arabic`
* `armenian`
* `basque`
* `catalan`
* `chinese` (see below)
* `danish`
* `dutch`
* `english`
* `finnish`
* `french`
* `german`
* `greek`
* `hindi`
* `hungarian`
* `indonesian`
* `irish`
* `italian`
* `lithuanian`
* `malay`
* `nepali`
* `norwegian`
* `portuguese`
* `romanian`
* `russian`
* `serbian`
* `spanish`
* `swedish`
* `tagalog`
* `tamil`
* `turkish`
* `yiddish`

## Chinese support

Indexing a Chinese document is different than indexing a document in most other languages because of how tokens are extracted. While most languages can have their tokens distinguished by separation characters and whitespace, this is not common in Chinese.

Chinese tokenization is done by scanning the input text and checking every character or sequence of characters against a dictionary of predefined terms and determining the most likely match based on the surrounding terms and characters.

Redis Open Source makes use of the [Friso](https://github.com/lionsoul2014/friso) chinese tokenization library for this purpose. This is largely transparent to the user and often no additional configuration is required.

## Using custom dictionaries

If you wish to use a custom dictionary, you can do so at the module level when loading the module. The `FRISOINI` setting can point to the location of a `friso.ini` file which contains the relevant settings and paths to the dictionary files.

Note that there is no default `friso.ini` file location. RedisSearch comes with its own `friso.ini` and dictionary files that are compiled into the module binary at build-time.

