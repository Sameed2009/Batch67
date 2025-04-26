def star_border(func):
    def wrapper(message):
        border = "*" * (len(message) + 10)
        return f"{border}\n*** {func(message)} ***\n{border}"
    return wrapper

def emoji_wrap(func):
    def wrapper(message):
        return f"🎉 {func(message)} 🎉"
    return wrapper
