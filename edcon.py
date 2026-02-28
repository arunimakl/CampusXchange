from flask import Flask, render_template, request, jsonify
import os
app = Flask(__name__)

# In-memory book store (seed data)
user_books = [
    {"id":1,"title":"Fluid Mechanics and Hydraulic Machines","author":"R.K. Bansal","subject":"Fluid Mechanics","dept":"Mechanical","topics":"fluid flow viscosity pressure turbine pump hydraulic","price":300,"condition":"Good","holder":"Sneha Joy","contact":"9876543210","emoji":"&#128230;"},
    {"id":2,"title":"Thermal Engineering","author":"R.S. Khurmi","subject":"Thermal Engineering","dept":"Mechanical","topics":"thermodynamics heat engine boiler steam turbine","price":250,"condition":"Used","holder":"Aswin Jacob","contact":"9812345678","emoji":"&#128293;"},
    {"id":3,"title":"Design Data Handbook","author":"K. Mahadevan & K. Balaveera Reddy","subject":"Machine Design","dept":"Mechanical","topics":"design data stress strain material properties tables","price":300,"condition":"Good as New","holder":"Abhinav Krishna","contact":"9988776655","emoji":"&#128215;"},
    {"id":4,"title":"Operations Management","author":"S. Paneerselvam","subject":"Operations Management","dept":"Management","topics":"production planning scheduling inventory supply chain","price":200,"condition":"Good","holder":"Akshaya Suresh","contact":"9123456789","emoji":"&#128200;"},
]
_next_id = 5


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/tutors')
def tutors():
    return render_template('tutors.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(user_books)

@app.route('/api/books', methods=['POST'])
def add_book():
    global _next_id
    data = request.get_json(force=True)

    required = ['title', 'author', 'subject', 'dept', 'price', 'condition', 'holder', 'contact']
    for f in required:
        if not data.get(f):
            return jsonify({'error': f'Missing field: {f}'}), 400

    dept_emoji = {
        'mechanical': '&#9881;&#65039;',
        'computer science': '&#128187;',
        'electrical': '&#9889;',
        'civil': '&#127959;&#65039;',
        'management': '&#128200;',
        'mathematics': '&#128208;',
        'physics': '&#128301;',
        'chemistry': '&#129514;',
        'arts': '&#127912;',
    }
    emoji = dept_emoji.get(data['dept'].strip().lower(), '&#128218;')

    book = {
        'id': _next_id,
        'title': data['title'].strip(),
        'author': data['author'].strip(),
        'subject': data['subject'].strip(),
        'dept': data['dept'].strip(),
        'topics': data.get('topics', '').strip(),
        'price': int(data['price']),
        'condition': data['condition'],
        'holder': data['holder'].strip(),
        'contact': data['contact'].strip(),
        'emoji': emoji,
    }
    user_books.append(book)
    _next_id += 1
    return jsonify(book), 201


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # Bind to 0.0.0.0 so external traffic can reach the app
    app.run(host='0.0.0.0', port=port, debug=True)
