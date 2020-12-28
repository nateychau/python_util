import json

#helper function to find nth occurance of a target character
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start


f = open("bookmarks_12_27_20.html", "r") # replace filename with appropriate name
out = open("db.json", 'w') #output file name can be changed as needed
db = {} #dictionary to hold what will become our json file
outer_key = None #flag save current outer folder name
inner_key = None #save current inner folder name

#read one line at a time
for line in f:
    whitespace = len(line) - len(line.lstrip()) #count of leading whitespace (to calculate indentation)
    if "/H3" in line: #this block handles outer/inner keys (folder names)
        start = find_nth(line, '>', 2)
        end = find_nth(line, '<', 3)
        if whitespace == 8:  
          outer_key = line[start+1:end].capitalize()
          inner_key = None
          db[outer_key] = {}
        if whitespace > 8:
          inner_key = line[start+1:end].capitalize()
          db[outer_key][inner_key] = {}
    else:
        link_start = find_nth(line, '"', 1)
        link_end = find_nth(line, '"', 2)
        if line[link_start+1] != "h": #line does not contain a link, so skip it
            continue
        else: #this block handles links and their titles
          link = line[link_start+1:link_end]
          name_start = find_nth(line, '>', 2)
          name_end = find_nth(line, '<', 3)
          name = line[name_start+1:name_end]
          if inner_key and whitespace == 16:
            db[outer_key][inner_key][name] = link
          elif outer_key and whitespace < 16:
            db[outer_key][name] = link

out.write(json.dumps(db)) #write to specified file
f.close()
out.close()
