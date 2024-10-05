import time

SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"
CLEAR = '\033[2H'

def draw_line(offset=0, lengh=1, color=222):
    line = ' ' * lengh
    print(f"{'  ' * offset}{SET_COLOR}{color}m{line}{END}")


def draw_romb():
    size = 15
    center = size // 2
    offset = size // 2


    step = 1
    lenght = 1


    #print(size,center,offset)

    colors = [222,157]

    while True:
        for color in colors:
            for line in range(size):
                draw_line(offset,lenght,color)

                if line < center:
                    offset -= step
                    lenght += step*4
                else:
                    offset += step
                    lenght -= step*4
            print(f"\x1b[{size+2}A")
            print(f"\x1b[{offset}D")

            lenght = 1
            offset = size // 2

            time.sleep(0.2)
if __name__ == "__main__":
    draw_romb()
                

"""for i in range(20):
    draw_line(lengh=20, color=10, offset=i)
    print(f"{CLEAR}")
    time.sleep(0.5)"""