# Function to read tag samples from a text file
def read_tag_samples_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

# Read tag samples from the text file
tags_data = read_tag_samples_from_file('tags_samples.txt')

# Function to clean tags and extract counts
def clean_tags(tags_data):
    cleaned_tags = []
    for tag in tags_data:
        cleaned_tag = tag.split()[1]  # Remove "?" at the beginning
        cleaned_tags.append(cleaned_tag)
    return cleaned_tags

# Clean tags
cleaned_tags = clean_tags(tags_data)

# Function to group tags by count
def group_tags(tags):
    grouped_tags = {}
    for tag in tags:
        count_category = f"{len(tag.split()) - 1} COUNT"
        if count_category not in grouped_tags:
            grouped_tags[count_category] = []
        grouped_tags[count_category].append(tag)
    return grouped_tags

# Group tags by count
grouped_tags = group_tags(cleaned_tags)

# Write grouped tags to a text file
with open('grouped_tags.txt', 'w') as file:
    for count_category, tags in grouped_tags.items():
        file.write(count_category + '\n')
        file.write(', '.join(tags) + '\n')
