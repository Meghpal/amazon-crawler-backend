def save_data(obj, id, mode):
    f = open("./reviews/reviews_" + id + ".txt", mode, encoding="utf-8")
    f.write("\n".join(map(lambda x: repr(x)[1:-1], obj)))
    f.close()