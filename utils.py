def remove_newlines(text):
    return ' '.join(text.split())

def create_message(role, content):
    return {
        "role": role,
        "content": remove_newlines(content)
    }

def system_message(content):
    return create_message("system", content)

def user_message(content):
    return create_message("user", content)