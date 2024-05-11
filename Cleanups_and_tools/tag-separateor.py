# Read tags from the text file
with open('tags_line.txt', 'r') as file:
    tags_line = file.read()

# Split the tags_line on commas to get a list of tags
tags = tags_line.split(', ')

# Write each tag to a new line in a text file
with open('tags.txt', 'w') as file:
    for tag in tags:
        file.write(tag.strip() + '\n')
