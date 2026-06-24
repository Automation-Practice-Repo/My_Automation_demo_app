import os
from app import create_app
from dotenv import load_dotenv

load_dotenv()

app = create_app(os.environ.get('FLASK_ENV', 'development'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(debug=True, host='0.0.0.0', port=port)
