def tagged(from_input):
    def wrapper(inp):
        return f"<title>{from_input(inp)}</title>"

    return wrapper
