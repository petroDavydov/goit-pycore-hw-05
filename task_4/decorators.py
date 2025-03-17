def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Invalid input. Use: name phone"
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid input. Please provide necessary arguments."
    return inner
