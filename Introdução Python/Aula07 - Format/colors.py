# Colors
# colored text and background

reset = '\033[0m'
bold = '\033[01m'
disable = '\033[02m'
underline = '\033[04m'
reverse = '\033[07m'
strikethrough = '\033[09m'
invisible = '\033[08m'

# foreground options
black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
orange = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
lightgrey = '\033[37m'
darkgrey = '\033[90m'
lightred = '\033[91m'
lightgreen = '\033[92m'
yellow = '\033[93m'
lightblue = '\033[94m'
pink = '\033[95m'
lightcyan = '\033[96m'

# background options
black_ = '\033[40m'
red_ = '\033[41m'
green_ = '\033[42m'
orange_ = '\033[43m'
blue_ = '\033[44m'
purple_ = '\033[45m'
cyan_ = '\033[46m'
lightgrey_ = '\033[47m'

# testes
for i in range(0, 108, 1):
    print("\033[{}m\033[{}m  {}".format(i, i, f"{i} - raquel"))
