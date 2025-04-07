import db

def click(user_id):
    user = db.get_user(user_id)
    if user:
        money = user[1] + user[2]  # money + speed
        db.update_user(user_id, money, user[2], user[3], user[4])
        return money

def upgrade_speed(user_id):
    user = db.get_user(user_id)
    if user and user[1] >= 20:
        money = user[1] - 20
        speed = user[2] + 1
        db.update_user(user_id, money, speed, user[3], user[4])
        return True
    return False

def hire_assistant(user_id):
    user = db.get_user(user_id)
    if user and user[1] >= user[4]:
        money = user[1] - user[4]
        assistants = user[3] + 1
        cost = user[4] + 5
        db.update_user(user_id, money, user[2], assistants, cost)
        return True
    return False
