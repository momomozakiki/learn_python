def concatenate_string():
    def merge_string(string1, string2):
        return string1 + string2

    return merge_string


def func():
    # return the reference of merge_string func
    conc_obj = concatenate_string()
    print(conc_obj)  # prints the reference

    # executes the reference
    print(conc_obj('Hello, ', 'George'))


func()

print(range(1,7))

