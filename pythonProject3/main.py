def q1():
    from PIL import Image

    pic = "gvozd.jpg"
    with Image.open(pic) as img:
        img.load()
    img.show()
    w, h = img.size
    f = img.format
    m = img.mode

    print("ширина: ", w)
    print("высота:  ", h)
    print("формат: ", f)
    print("цвет модель:", m)

def q2():
    from PIL import Image
    file = "gvozd.jpg"
    with Image.open(file) as img:
            img.load()

    new_img = img.resize((img.width // 3, img.height // 3))
    new_img.save("newgvozd.jpg")

    c1_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    c1_img.save("top.jpg")
    c2_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    c2_img.save("netop.jpg")

    new_img.show()
    c1_img.show()
    c2_img.show()

q2()