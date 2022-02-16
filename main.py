import sys
def check_rgb(rgb, og):
    if not len(rgb) == 3:
        print(f"Invalid Colour: {og}")
        sys.exit(0)
    try:
        if 0 <= int(rgb[0]) <= 255 and 0 <= int(rgb[1]) <= 255 and 0 <= int(rgb[2]) <= 255:
            return True
        else:
            print(f"Invalid Colour: {og}")
            sys.exit(0)
    except ValueError:
        print(f"Invalid Colour: {og}")
        sys.exit(0)
def gradient(startrgb,endrgb,text):
        changer = int((int(endrgb[0]) - int(startrgb[0]))/len(text))
        changeg = int((int(endrgb[1]) - int(startrgb[1]))/len(text))
        changeb = int((int(endrgb[2]) - int(startrgb[2]))/len(text))
        r = int(startrgb[0])
        g = int(startrgb[1])
        b = int(startrgb[2])
        for letter in text:
            if letter == '\n':pass
            with open('output.tfx', 'a', encoding='utf8') as f:
                f.write(f"\x1b[40;38;2;{r};{g};{b}m{letter}\033[0m")
            r+=changer 
            g+=changeg 
            b+=changeb
def main():
    if sys.argv[1].lower() == "verti" or sys.argv[1].lower() == "verticle":
        try:
            colour1 = sys.argv[2]
            startcolour = tuple(colour1.split(','))
            check_rgb(startcolour, colour1)
        except IndexError:
            print("Invalid Args!\nfade.py vert/hori r,g,b1 r,g,b2 text_art.file")
            sys.exit(0)
        try:
            colour2 = sys.argv[3]
            endcolour = tuple(colour2.split(','))
            check_rgb(endcolour, colour2)
        except IndexError:
            print("Invalid Args!\nfade.py vert/hori r,g,b1 r,g,b2 text_art.file")
            sys.exit(0)
        try:
            banner = open(sys.argv[4], "r", encoding="utf8").read()
            output_lines = banner.split("\n")
            r = int(startcolour[0])
            g = int(startcolour[1])
            b = int(startcolour[2])
            for x in output_lines:
                changer = int((int(endcolour[0]) - int(startcolour[0]))/len(output_lines))
                changeg = int((int(endcolour[1]) - int(startcolour[1]))/len(output_lines))
                changeb = int((int(endcolour[2]) - int(startcolour[2]))/len(output_lines))
                rgb_code = f"\x1b[40;38;2;{r};{g};{b}m"
                r+=changer  
                g+=changeg 
                b+=changeb
                with open('output.tfx', 'a', encoding='utf8') as f:
                    f.write(f"{rgb_code}{x}\n")
            with open('output.tfx', 'a', encoding='utf8') as f:
                    f.write(f"\033[0m")
            print("Written to output.tfx")
        except IndexError:
            print("Invalid Args!\nfade.py vert/hori r,g,b1 r,g,b2 text_art.file")
            sys.exit(0)
    elif sys.argv[1].lower() == "hori" or sys.argv[1].lower().lower() == "horizontal":
        try:
            colour1 = sys.argv[2]
            startcolour = tuple(colour1.split(','))
            check_rgb(startcolour, colour1)
        except IndexError:
            print("Invalid Args!\nfade.py vert/hori r,g,b1 r,g,b2 text_art.file")
            sys.exit(0)
        try:
            colour2 = sys.argv[3]
            endcolour = tuple(colour2.split(','))
            check_rgb(endcolour, colour2)
        except IndexError:
            print("Invalid Args!\nfade.py vert/hori r,g,b1 r,g,b2 text_art.file")
            sys.exit(0)
        try:
            with open(sys.argv[4], 'r', encoding='utf8') as f:
                for x in f.readlines():
                    gradient(startcolour, endcolour, x)
                with open('output.tfx', 'a', encoding='utf8') as f:
                    f.write(f"\n\033[0m")
                print("Written to output.tfx")
        except IndexError:
            print("Invalid Args!\nfade.py vert/hori r,g,b1 r,g,b2 text_art.file")
            sys.exit(0)
with open('output.tfx', 'w') as f:
    f.write("")
main()