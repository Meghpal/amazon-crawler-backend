def save_data(obj):
    f = open("reviews.txt", "a")
    f.write(str(obj))
    f.close()