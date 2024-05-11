def filter_tags(input_file, output_file, keywords):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    matching_lines = []
    remaining_lines = []
    for line in lines:
        if any(keyword in line for keyword in keywords):
            matching_lines.append(line)
        else:
            remaining_lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as file:
        for line in matching_lines:
            file.write(line)

    with open(input_file, 'w', encoding='utf-8') as file:
        for line in remaining_lines:
            file.write(line)

# Usage:
# filter_tags('tags_sample.txt', 'clothes.txt', ['clothes', 'shirt', 'pants', 'dress'])

def main():
    input_file = 'General'  # Replace with your input file path
    output_file = 'NSFW2'  # Replace with your output file path
    keywords = ['breasts']
 
    filter_tags(input_file, output_file, keywords)

if __name__ == "__main__":
    main()
