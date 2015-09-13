## Part-of-Speech (POS) Tagger for Turkish

### Build and Run
* [Python](https://www.python.org/) and [NLTK](http://www.nltk.org/) is necessary to build and run this project.
* The module is named as `pos_tagger` and for the given sentence `tag(sentence)` will return `(word, tag)` pairs.
* The system is trained with the development file provided in [CENG463 course](https://cow.ceng.metu.edu.tr/Courses/index.php?course=ceng463&semester=20121) it includes 5110 sentences.
* Example:

```
>>> from pos_tagger import tag
>>> tag('Bunu başından beri biliyordum zaten .')
[('Bunu', 'Pron'), ('başından', 'Noun_Abl'), ('beri', 'Postp'), ('biliyordum', 'Verb'), ('zaten', 'Adv'), ('.', 'Punc')]
```

### Implementation Idea

### Results

### Future Work
