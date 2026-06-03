# Text Normalization

## What is text normalization?

**Text normalization** is the process of preprocessing text into a standardized form before tokenization. The goal is to reduce the vocabulary (the number of distinct tokens) to make training easier.

## HTML/URL/mention removal

Strip HTML tags, URLs, and social media handles (e.g. `@user`) from text. This is especially common when working with web-scraped or social media data.

**Example:** `"Check out @OpenAI at https://openai.com <b>now</b>"` $\to$ `"Check out at now"`

## Expanding contractions

Expand contractions to their full forms.

**Example:** `"I can't believe they're here"` $\to$ `"I cannot believe they are here"`

## Lowercasing

Convert all characters to lowercase.

**Example:** `"The"` $\to$ `"the"`

## Punctuation removal

Remove all punctuation characters.

**Example:** `"how are you doing?"` $\to$ `"how are you doing"`

## Trimming whitespace

Collapse consecutive whitespace characters into a single space.

**Example:** `"hi.  how are you doing?"` $\to$ `"hi. how are you doing?"`

## Stripping accent marks

Remove accent marks from characters.

**Example:** `"Señorita"` $\to$ `"Senorita"`

## Spelling correction

Correct misspelled words to their intended forms. This is especially important for user-generated text such as social media posts, search queries, and reviews.

**Example:** `"definately the bigest improvment"` $\to$ `"definitely the biggest improvement"`

## Stop word removal

Remove high-frequency, low-information words (e.g. "the", "is", "at", "of") that carry little semantic meaning. Most NLP libraries ship with a predefined stop word list.

**Example:** `"the cat is on the mat"` $\to$ `"cat mat"`

## Stemming

Remove word suffixes by matching tokens against a predefined list of common suffixes. The most widely used algorithms are the Porter stemmer and its successor, the Snowball stemmer.

**Example:** `"there is nothing either good or bad but thinking makes it so"` $\to$ `"there is noth either good or bad think make it so"`

Note that the algorithm mistakenly strips the "ing" from "nothing".

## Lemmatization

While stemming only removes suffixes, lemmatization more broadly reduces inflected forms of a word to its dictionary base form, or **lemma**. Because lemmatization aims to produce valid dictionary entries, it requires more robust morphological analysis than stemming. Part-of-speech tagging is a crucial step in lemmatization.

**Example:** `"There is nothing either good or bad but thinking makes it so"` $\to$ `"There be nothing either good or bad but think make it so"`
