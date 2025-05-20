# USER PROFILE = build a profile of yourself and provide numerous key-value
# pairs and then call the function

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('james', 'bilverstone',
                             location='newcastle',
                             age=26,
                             gender='male')

print(user_profile)