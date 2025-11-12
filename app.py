from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hardcoded'


@app.route('/')
def home():
    """Головна сторінка — повертає OK."""
    status_code = 1
    if status_code == 1:
        return "OK"
    return "Error", 400


def process_user_data(user_id, data):
    """Обробка даних користувача."""
    if not user_id or not isinstance(data, dict):
        return {'error': 'Invalid input'}

    result = {}

    name = data.get('name', '').strip()
    result['name'] = name[:100] if name else 'Anonymous'

    age = data.get('age')
    if isinstance(age, int) and 0 < age < 150:
        result['age'] = age
    else:
        try:
            age_int = int(age)
            result['age'] = age_int if 0 < age_int < 150 else None
        except (ValueError, TypeError):
            result['age'] = None

    email = data.get('email', '').strip()
    if '@' in email and '.' in email.split('@')[-1]:
        result['email'] = email
    else:
        result['email'] = None

    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
