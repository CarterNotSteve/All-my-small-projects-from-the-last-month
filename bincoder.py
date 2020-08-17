from PIL import Image

eod = input("Encode or Decode?\n: ")
image = Image.new('RGB', (8,1), 'white')
pixels = image.load()

if eod.capitalize() == "Encode":
  char = input("input a character to encode to binary.\n: ")
  char = list(char)
  char = char[0]
  charnum = ord(char)
  charnum = bin(charnum)
  charnum = list(charnum)
  charnum.remove("0")
  charnum.remove("b")
  charnum = "".join(charnum)
  if len(charnum) < 8:
    for i in range(8-len(charnum)):
      charnum = list(charnum)
      charnum.append(0)
      charnum = "".join(str(charnum))
  if charnum[0] == 1:
    pixels[0,0] = 'black'

  if charnum[1] == 1:
    pixels[1,0] = 'black'

  if charnum[2] == 1:
    pixels[2,0] = 'black'

  if charnum[3] == 1:
    pixels[3,0] = 'black'

  if charnum[4] == 1:
    pixels[4,0] = 'black'

  if charnum[5] == 1:
    pixels[5,0] = 'black'

  if charnum[6] == 1:
    pixels[6,0] = 'black'

  if charnum[7] == 1:
    pixels[7,0] = 'black'

image.show()