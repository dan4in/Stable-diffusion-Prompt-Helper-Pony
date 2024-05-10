from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def read_tags_from_file(filename):
    with open(filename, 'r') as file:
        return [tag.strip() for tag in file]

# Read tags from the text files
tags = read_tags_from_file('tags')
characters_tags = read_tags_from_file('tags_Characters')

def generate_words(num_words, pony_options, characters=False):
    if characters:
        selected_words = random.sample(characters_tags, min(num_words, len(characters_tags)))
    else:
        selected_words = random.sample(tags, min(num_words, len(tags)))
    
    result = ', '.join(selected_words)
    
    # Include score if selected
    if pony_options.get('Pony_score', False):
        result = 'score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, ' + result
    
    # Include selected rating options
    if pony_options.get('rating_safe', False):
        result += ', rating_safe'
    if pony_options.get('rating_explicit', False):
        result += ', rating_explicit'
    if pony_options.get('rating_questionable', False):
        result += ', rating_questionable'
    
    # Include selected source options
    for word, selected in pony_options.items():
        if word.startswith('source_') and selected:
            result += ', ' + word
    
    return result

@app.route('/generate-tags', methods=['POST'])
def generate_tags():
    num_words = int(request.form['num_words'])
    pony_options = {key: True if request.form.get(key) == 'on' else False for key in request.form.keys()}
    tags_result = generate_words(num_words, pony_options)
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
            characters_result = generate_words(1, pony_options, characters=True)
        else:
            result = generate_words(num_words, pony_options)
        
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
    characters_result = generate_words(1, pony_options, characters=True)  # Always generate one character tag
    return jsonify(characters_result=characters_result, num_words=num_words, form_values=request.form)

if __name__ == '__main__':
    app.run(debug=True)
