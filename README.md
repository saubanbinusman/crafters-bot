We are going to break things down into following steps

1. Read a pdf and parse text
2. Separate our paragraphs
3. Filter/recommend paragraphs that may contain value for us

## Additional Features
1. Read book from google drive
2. Automatically post on group
3. Take input on topics to filter on

## Workflow
1. Run [Parsr|https://github.com/axa-group/Parsr] locally (the README is easy to follow).
2. Convert PDF to JSON using Parsr's UI on localhost. Turn off all the modules except the following:
    - header-footer-detection
    - words-to-line-new
    - reading-order-detection
    - lines-to-paragraph
    - hierarchy-detection
3. Wait.
4. Download the JSON from the Document Viewer tab.
5. Supply it to the script and get the output file.