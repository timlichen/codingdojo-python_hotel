def iterate_dictionary(students):
    for val in students:
        my_Str = ""
        for k, v in val.items():
            my_Str += f"{k} - {v}"
        print(my_Str)

things = [{1:"a"}, {2:"b"}]

iterate_dictionary(things)
