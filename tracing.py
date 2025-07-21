

class Trace:
    def accept_tokens(self, tokens):
        raise NotImplementedError

    def accept(self, variable, value):
        raise NotImplementedError

    def accept_result(self, result):
        raise NotImplementedError


class TraceToFile(Trace):
    def __init__(self, filename):
        self.file = open(filename, 'w')

    def accept_tokens(self, tokens):
        self.file.write(f"{tokens}\n\n")

    def accept(self, variable, value):
        self.file.write(f"{variable}\n{value}\n\n")

    def accept_result(self, result):
        self.file.write(f"{result}\n")

    def close(self):
        if not self.file.closed:
            self.file.flush()
            self.file.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


class TraceToHTML(Trace):
    num_tokens = 0
    first = True

    def __init__(self, filename):
        self.file = open(filename, 'w')
        self.file.write("<table border='1'>\n")

    def write_list(self, list, markup=lambda x: x):
        self.file.write("<tr>\n")
        for val in list:
            self.file.write("<td style='padding: 10px;'>{}</td>\n".format(markup(val)))
        self.file.write("</tr>\n")

    def accept_tokens(self, tokens):
        if not self.first:
            self.file.write("</table><table border='1'>\n")

        self.write_list([""] + list(tokens))
        self.num_tokens = len(tokens)
        self.first = False

    def accept(self, variable, value):
        self.write_list([variable] + value)

    def accept_result(self, result):
        self.write_list(["Result"] + [""] * (self.num_tokens-1) + [result], markup=lambda x: f"<strong>{x}</strong>")

    def close(self):
        if not self.file.closed:
            self.file.write("</table>\n")
            self.file.flush()
            self.file.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()