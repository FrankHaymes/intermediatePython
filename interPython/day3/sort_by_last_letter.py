
store = []


def sort_by_last_letter(string):
    """
    Task define a function that takes a string
    as input parameter.
        Defines a local function that returns the last letter of the string
        Your main function return a sorted list
    :param string:  A list of strings
    :return: sorted list base on last letter
    """

    # A local function
    def last_letter(s):
        return s[-1]
    store.append(last_letter)
    print(last_letter)
    # Hint: use the local function as lambda to
    # the sorted built-in function
    return sorted(string, key=last_letter)


def logger(msg):
    def log_message():
        print("Log: ", msg)
    return log_message


def html_tag(tag):
    """
    Creates a htm tag base on input
    :param tag:  Tag
    :return: a callable function
    """
    def wrap_text(msg):
        print("<{0}>{1}</{0}>".format(tag, msg))

    return wrap_text



def main():
    names =["Hugo", "maria", "peter", "el Chapo", "mario"]
    print(sort_by_last_letter(names))
    print(sort_by_last_letter(names))
    print(sort_by_last_letter(names))





if __name__ == '__main__':
    main()
    exit(0)