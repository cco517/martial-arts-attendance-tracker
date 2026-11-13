from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager() 

login_manager.login_view = 'auth.login' #Tells python where to send logged out users
                                        #when they hit a @login_required tag
                                        
login_manager.login_message_category = 'info' 