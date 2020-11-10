def save_data(obj, id, mode):
    f = open("./reviews/reviews_" + id + ".txt", mode, encoding="utf-8")
    f.write(str(obj))
    f.close()