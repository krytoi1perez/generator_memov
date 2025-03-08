from PIL import Image,ImageDraw,ImageFont

print("Генератор мемов запущен!")

top_text = input("Введите верхний текст:")
bottom_text = input("Введите нижний текст:")

print(top_text,bottom_text)

print("Список картинок:")
print("1. Кот в ресторане")
print("2. Кот в очках")
n = ''
image_number = int(input("Введите номер картинки:"))
if image_number == 1:
    n = "Кот в ресторане.png"
elif image_number == 2:
    n= "Кот в очках.png"
else:
    print("Неверный номер картинки")

Image = Image.open(n)

draw = ImageDraw.Draw(Image)

font = ImageFont.truetype('arial.ttf',size = 70)

draw.text((0, 0),top_text,font = font, fill ='black')
draw.text((0,100),bottom_text,font = font, fill ='black')

Image.save("new_meme.jpg")