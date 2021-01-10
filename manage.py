from app import create_app
from app.settings import HOST, PORT, DEBUG_STATUS
from flask_script import Server, Manager
from flask_migrate import  MigrateCommand

# Pass the create_app to script Manager 
manager = Manager(create_app)

manager.add_command('db', MigrateCommand)

# Configure the server
server = Server(host=HOST, port=PORT, use_debugger=DEBUG_STATUS)
manager.add_command("runserver", server)

# Then run the manager
if __name__ == "__main__":
    manager.run()


# app = create_app()

# # Run the Server
# if __name__ == '__main__':
#     app.run(debug=DEBUG_STATUS, port=PORT)