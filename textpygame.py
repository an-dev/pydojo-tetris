import sys

class Bitmap:
    def __init__(self, text):
        self._text = text

    def get_width(self):
        return len(self._text)
    
    def get_height(self):
        return len(self._text)

    def __str__(self):
        return self._text

class Font:
    def render(self, text, whatever, color):
        return Bitmap(text)
    

class FontModule:
    def init(self):
        pass

    def SysFont(self, font, size, bold=False):
        return Font()

class Window:
    def fill(self, rect):
        pass
       
    def blit(self, text, pos):
        print(text)

class Display:
    def set_mode(self, size):
        return Window()

    def set_caption(self, caption):
        pass

    def update(self):
        pass

    def quit(self):
        sys.exit()

class Event:
	def __init__(self, type, key):
		self.type = type
		self.key = key

QUIT = "quit"
KEYDOWN = "key"

K_LEFT = "left"
K_RIGHT = "right"
K_DOWN = "down"
K_SPACE = "space"
K_UP = "up"

last_key = ""

class EventModule:
	def get(self):
            global last_key
            while True:
                print("\n> ", end="")
                sys.stdout.flush()
                line = sys.stdin.readline()
                key = line.strip()
                if key == "":
                    key = last_key
                else:
                    last_key = key
                if key == QUIT:
                    return [Event(QUIT, "")]
                else:
                    return [Event(KEYDOWN, key)]

class Clock:
    def __init__(self):
        self._time = 0

    def get_rawtime(self):
        self._time += 270
        return self._time 

    def tick(self):
        pass

class TimeModule:
    def Clock(self):
        return Clock()

class DrawModule:
    def __init__(self):
        self._x = 0
        self._y = 0
        self._lowest = None
        self._colors = {(0, 0, 0): '.'}

    def rect(self, win, col, rect, ab):
        if self._lowest is None:
            self._lowest = rect[0]
        if rect[0] == self._lowest:
            print()

        if col not in self._colors:
            self._colors[col] = str(len(self._colors))

        char = self._colors[col]
        print(char, end="")
        pass

    def line(self, win, col, ab, cd):
        pass

font = FontModule()

display = Display()

event = EventModule()

time = TimeModule()

draw = DrawModule()

def quit():
	sys.exit()
