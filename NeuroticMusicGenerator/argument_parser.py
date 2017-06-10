from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, \
    ArgumentTypeError


# function to arg parse check type to avoid using choose
def randomise_percent_type(x):
    x = int(x)
    if 0 <= x <= 100:
        return x
    raise ArgumentTypeError("Randomise percent must be between 0 and "
                            "100(includes)")


# function to arg parse check type to avoid using choose
def fun_repeats_type(x):
    x = int(x)
    if 1 <= x <= 100:
        return x
    raise ArgumentTypeError("Functions repeats must be between 1 and "
                            "100(includes)")


# class to contains a parse arguments
class ProgramArguments:
    def __init__(self):
        self.file_name = ""  # output file name or path
        self.rand_percent = 0
        self.list_fun = ['sin,cos']
        self.fun_repeats = 2  # how many times repeat everything
        self.speed = 180

    def parse(self):
        from random import randint
        par = ArgumentParser(
            description='Midi music generator.',
            formatter_class=ArgumentDefaultsHelpFormatter,
            epilog='Available functions: sin cos tan sqrt'
                   'or your own function, declaration syntax eq. \"3 * x + 2\". '
                   'if you want more functions at the same time specify arguments '
                   'like that: sin,cos,\"3*x+2\" - it makes them play at the same '
                   'time. Only one variable x, do not use space, your function '
                   'have to be enable to eval in python interpreter. ')
        par.add_argument('-o', '--outfile', nargs='?', type=str,
                         default=str(randint(1, 200000000)) + ".mid",
                         help="output file name or path", dest="filename")
        par.add_argument('-r', '--randomise_percent',
                         type=randomise_percent_type, default=0,
                         help="percent of random notes [0,100]",
                         dest="randomise_percent")
        par.add_argument('-f', '--math_fun', nargs='*', type=str,
                         default=['sin,cos'],
                         help="math function to generate music, eg. -f sin,cos"
                              ",\"x\" cos,3*x sin,\"x + 2\" ", dest="math_fun")
        par.add_argument('-c', '--fun_repeats', type=fun_repeats_type,
                         default=2,
                         help="number of cycles that every function will be "
                              "repeat [1,100]", dest="fun_repeats")
        par.add_argument('-s', '--speed', type=int,
                         default=180,
                         help="speed of music eg. 60 - slow, 480 - fast",
                         dest="speed")
        # par.print_help()
        args = par.parse_args()

        from sys import exit
        try:
            with open(args.filename, 'wb') as f:
                f.close()
                self.file_name = args.filename
                if str.find(self.file_name, ".mid") == -1:
                    self.file_name += ".mid"
                elif str.find(self.file_name, ".mid") + 4 < len(
                        self.file_name):
                    print("The file extension is wrong!")
                    exit(2)
        except IOError:
            print("Could not read or create file: " + str(args.filename))
            exit(2)

        self.rand_percent = args.randomise_percent
        self.list_fun = args.math_fun
        self.fun_repeats = args.fun_repeats
        self.speed = args.speed

    def get_file_name(self):
        return self.file_name

    def get_rand_percent(self):
        return self.rand_percent

    def get_fun_list(self):
        return self.list_fun

    def get_fun_repeats(self):
        return self.fun_repeats

    def get_speed(self):
        return self.speed
