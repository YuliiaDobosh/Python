class Color:
    COLORS = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',

        'reset': '\033[0m'
    }

    @classmethod
    def colored(cls, text, color_name):
        color = cls.COLORS.get(color_name, "")
        if color:
            return color + text + cls.COLORS['reset']
        else:
            return text