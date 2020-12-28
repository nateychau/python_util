# Personal Python Utilities 


## Save Bookmarks to JSON (bookmark_html_to_json.py)
1. Navigate to the chrome bookmarks manager
  - Triple dots in top right corner
  - Bookmarks -> Bookmark manager
2. Click on the triple dots at the top right (in the blue header)
3. Click 'Export Bookmarks'. Save the HTML file in the same folder as bookmark_html_to_json.py. 
4. Navigate to the directory containing the script and new HTML file. 
5. Replace the read filename with the name of your HTML file. 
6. Replace the output filename with your desired name (end with .json).
7. In the terminal, run "python3 bookmark_html_to_json.py".
8. The JSON file will be written to the same directory. Best viewed with a JSON formatter - I suggest Prettier. 


Notes: 
- Currently only supports Google Chrome
- Some bugs caused by empty folders and folders nested more than 2 levels