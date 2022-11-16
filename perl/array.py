def array():
    name = ["hari", "bala", "sugan"]
    age = ["24", "34", "45"]
    mapped = zip(name, age)
    print(set(mapped))


if __name__ == '__main__':
    array()
