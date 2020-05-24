from apiapp.models import users
import bcrypt


def authenticate(username,password):
    user = users.query.filter_by(username=username).first()
    print(user.username,user.password)
    password = password.encode('utf-8')
    if bcrypt.checkpw(password, user.password) and user:
        return user 
    else:
        return "User not Found or Incorrect"

def identity(payload):
    user_id = payload['identity']
    return users.find_by_id(user_id)
