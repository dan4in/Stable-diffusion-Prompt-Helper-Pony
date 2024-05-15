from flask import Flask, render_template, request, jsonify
import random
import datetime


app = Flask(__name__)

def read_tags_from_file(filename):
    with open(filename, 'r') as file:
        return [tag.strip() for tag in file]

# Read tags from the text files
tags = {
    'general': read_tags_from_file('General'),
    'characters': read_tags_from_file('Character'),
    'clothes': read_tags_from_file('clothes'),
    'accessory': read_tags_from_file('Accessory'),
    'copyright': read_tags_from_file('Copyright'),
    'artist': read_tags_from_file('Artist'),
    'nsfw': read_tags_from_file('NSFW'),
    'meta': read_tags_from_file('meta'),
    'hair': read_tags_from_file('hair'),
    'Age': read_tags_from_file('Age'),
}

def generate_words(num_words, pony_options, category):
    selected_words = random.sample(tags[category], min(num_words, len(tags[category])))
    
    # If "Undanbooru Tags" is selected, replace certain characters with a space in the tags
    if pony_options.get('undanbooru_tags', False):
        selected_words = [word.replace('_', ' ').replace('(', ' ').replace(')', ' ').replace('{', ' ').replace('}', ' ').replace('-', ' ').replace('!?', ' ').replace(';', ' ').replace('+', ' ').replace('=', ' ').replace('@', ' ').replace('^', ' ').replace('<', ' ').replace('>', ' ') for word in selected_words]
    
    result = ', '.join(selected_words)
    
    # Include score if selected
    if pony_options.get('Pony_score', False):
        # Define the two score strings
        score_string1 = 'score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up'
        score_string2 = 'score_10, score_9_up, score_8_up, score_7_up, score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up'
        
        # Use the current minute to decide which score string to use
        current_minute = datetime.datetime.now().minute
        selected_score_string = score_string1 if current_minute % 2 == 0 else score_string2
        
        result = selected_score_string + ', ' + result
    
    # Include selected rating options
    if pony_options.get('rating_safe', False):
        result += ', rating_safe'
    if pony_options.get('rating_explicit', False):
        result += ', rating_explicit'
    if pony_options.get('rating_questionable', False):
        result += ', rating_questionable'
    if pony_options.get('rating_realistic', False):
        result += ', score_hyper-realistic, realistic, ((Full Body:1.2))'
    
    # Include selected source options
    for word, selected in pony_options.items():
        if word.startswith('source_') and selected:
            result += ', ' + word
    
    return result

@app.route('/generate-tags/<category>', methods=['POST'])
def generate_tags(category):
    num_words = int(request.form['num_words'])
    pony_options = {key: True if request.form.get(key) == 'on' else False for key in request.form.keys()}
    tags_result = generate_words(num_words, pony_options, category)
    return jsonify(tags_result=tags_result)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    characters_result = ''
    form_values = {}
    
    if request.method == 'POST':
        num_words = int(request.form['num_words'])
        pony_options = {key: True if request.form.get(key) == 'on' else False for key in request.form.keys()}
        
        if 'num_words_characters' in request.form:
            characters_result = generate_words(1, pony_options, 'characters')
        else:
            result = generate_words(num_words, pony_options, 'general')
        
        form_values = request.form

    return render_template('index.html', result=result, characters_result=characters_result, form_values=form_values)
   
@app.route('/generate-random-values', methods=['GET'])
def generate_random_values():
    # Generate random values for cfg and steps
    cfg = random.randint(3, 12)
    steps = random.randint(20, 60)
    
    # Return the values as JSON
    return jsonify(cfg=cfg, steps=steps)

@app.route('/generate-characters', methods=['POST'])
def generate_characters():
    num_words = request.form.get('num_words', '1')  # Default to 1 if num_words is not provided
    pony_options = {key: True if request.form.get(key) == 'on' else False for key in request.form.keys()}
    characters_result = generate_words(1, pony_options, 'characters')  # Always generate one character tag
    return jsonify(characters_tags_result=characters_result, num_words=num_words, form_values=request.form)

@app.route('/generate-mixed-tags', methods=['POST'])
def generate_mixed_tags():
    pony_options = {key: True if request.form.get(key) == 'on' else False for key in request.form.keys()}
    mixed_tags_result = {category: generate_words(1, pony_options, category) for category in tags.keys()}
    
    # Remove category names and format the tags without {" and :
    cleaned_tags_result = {key: value.replace('"', '').replace(':', '') for key, value in mixed_tags_result.items()}
    
    return jsonify(mixed_tags_result=cleaned_tags_result)


    
if __name__ == '__main__':
    app.run(debug=True)
