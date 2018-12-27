class Colors:
    OK = '\x1b[7;32;40m'
    WARNING = '\x1b[7;33;40m'
    FAIL = '\x1b[7;31;40m'
    LOG = '\x1b[7;34;40m'
    END = '\x1b[0m'

    @staticmethod
    def print_format_table():
        for style in range(8):
            for fg in range(30, 38):
                s1 = ''
                for bg in range(40, 48):
                    fmt = ';'.join([str(style), str(fg), str(bg)])
                    s1 += '\x1b[%sm %s \x1b[0m' % (fmt, fmt)
                print(s1)
            print('\n')

    @staticmethod
    def success(text, prev="test"):
        print(prev + ": " + Colors.OK + text + Colors.END)

    @staticmethod
    def warning(text, prev="test"):
        print(prev + ": " + Colors.WARNING + text + Colors.END)

    @staticmethod
    def fail(text, prev="test"):
        print(prev + ": " + Colors.FAIL + text + Colors.END)

    @staticmethod
    def log(text, prev="test"):
        print(prev + ": " + Colors.LOG + text + Colors.END)


class Test:
    @staticmethod
    def is_sorted(array):
        s = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                s = False
        if s:
            Colors.success("PASS", "IS_SORTED")
        else:
            Colors.fail("FAIL", "IS_SORTED")
