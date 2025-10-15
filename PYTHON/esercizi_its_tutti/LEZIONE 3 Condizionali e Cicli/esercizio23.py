'''6-3. Glossary: A Python dictionary can be used to model an actual dictionary. 
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
• Print each word and its meaning as neatly formatted output. 
You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. 
Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.'''

glossary = {
    'variable': 'A named storage location in memory that holds a value.',
    'loop': 'A control flow statement that allows code to be executed repeatedly.',
    'function': 'A block of organized, reusable code that performs a specific task.',
    'list': 'An ordered collection of items.',
    'dictionary': 'A collection of key-value pairs.',
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n  {meaning}\n")