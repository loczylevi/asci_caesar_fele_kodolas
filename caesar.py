

#97 a
#122 z 

bekeres = input("Kérek egy szót: ").lower()

titkositott = ""

for betu in bekeres:
    if betu.isalpha() and betu.isascii():
            if ord(betu) == 122:
                 titkositott += chr(ord(betu)-25)
            else:
                titkositott += chr(ord(betu)+1)

print(f"Eredeti szó: {bekeres}\nTitkositott szó: {titkositott}")

tyityok = [chr(ord(betu)+1) for betu in bekeres if betu.isalpha() and betu.isascii()]

for x in tyityok:
    print(x,end="")

print()

#________________________________________________
print("visszafejtés")

vissza = [chr(ord(betu)-1) for betu in titkositott if betu.isalpha() and betu.isascii()]

for y in vissza:
    print(y,end="")

print()

visszafejtes = ""

for betu in titkositott:
    if betu.isalpha() and betu.isascii():
            if ord(betu) == 97:
                 visszafejtes += chr(ord(betu)+25)
            else:
                visszafejtes += chr(ord(betu)-1)

print(f"Caesar féle kodolás: {visszafejtes}")
