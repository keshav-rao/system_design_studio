# Stop words

```json metadata
{
  "schema_version": 2,
  "title": "Stop words",
  "description": "Stop words support",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"default-stop-word-list","title":"Default stop word list"},{"id":"overriding-the-default-stop-word-list","title":"Overriding the default stop word list"},{"id":"disable-the-use-of-stop-words","title":"Disable the use of stop words"},{"id":"avoiding-stop-word-detection-in-search-queries","title":"Avoiding stop word detection in search queries"}]}

,
  "codeExamples": []
}
```


Redis Open Source has a default list of [stop words](https://en.wikipedia.org/wiki/Stop_words). These are words that are usually so common that they do not add much information to search, but take up a lot of space and CPU time in the index. 

When indexing, stop words are discarded and not indexed. When searching, they are also ignored and treated as if they were not sent to the query processor. This is done when parsing the query. 

At the moment, the default stop word list applies to all full-text indexes in all languages and can be overridden manually at index creation time. 

## Default stop word list

The following words are treated as stop words by default: 

```
 a,    is,    the,   an,   and,  are, as,  at,   be,   but,  by,   for,
 if,   in,    into,  it,   no,   not, of,  on,   or,   such, that, their,
 then, there, these, they, this, to,  was, will, with
```

## Overriding the default stop word list

Stop words for an index can be defined (or disabled completely) on index creation using the `STOPWORDS` argument with the [[`FT.CREATE`](https://redis.io/docs/latest/commands/ft.create) command.

The format is `STOPWORDS {number} {stopword} ...` where number is the number of stop words given. The `STOPWORDS` argument must come before the `SCHEMA` argument. For example:

```
FT.CREATE myIndex STOPWORDS 3 foo bar baz SCHEMA title TEXT body TEXT 
```

## Disable the use of stop words

Disabling stop words completely can be done by passing `STOPWORDS 0` to [`FT.CREATE`](https://redis.io/docs/latest/commands/ft.create).


## Avoiding stop word detection in search queries

In rare use cases, where queries are very long and are guaranteed by the client application not to contain stop words, it is possible to avoid checking for them when parsing the query. This saves some CPU time and is only worth it if the query has dozens or more terms in it. Using this without verifying that the query doesn't contain stop words might result in empty queries. 

