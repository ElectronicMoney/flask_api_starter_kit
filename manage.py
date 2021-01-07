from app import create_app
from app.settings import PORT, DEBUG_STATUS

app = create_app()

# Run the Server
if __name__ == '__main__':
    app.run(debug=DEBUG_STATUS, port=PORT)