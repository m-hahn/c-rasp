

class Trace:
    def accept_tokens(self, tokens):
        raise NotImplementedError

    def accept(self, variable, value):
        raise NotImplementedError

    def accept_result(self, result):
        raise NotImplementedError



######## Write trace to a plain text file ##############

class TraceToFile(Trace):
    def __init__(self, filename):
        self.file = open(filename, 'w')
        self.first = True

    def accept_tokens(self, tokens):
        if not self.first:
            self.file.write("\n----------------------\n\n")

        self.file.write(f"{tokens}\n\n")
        self.first = False

    def accept(self, variable, value):
        self.file.write(f"{variable}\n{value}\n\n")

    def accept_result(self, result):
        self.file.write(f"Result: {result}\n")

    def close(self):
        if not self.file.closed:
            self.file.flush()
            self.file.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()





######## Write trace to an HTML file containing a table ##############

html_header = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>C-RASP trace</title>
  <style>
    table {
      border-collapse: collapse;
      border: 1px solid black;
      margin-bottom:50px;
    }

    th {
      padding: 12px;
      background-color: #eeeeee;
      font-weight: bold;
      border: 1px solid black;
      text-align: left;
    }
    
    td {
      padding: 12px;
      border: 1px solid black;
    }
    
    .final {
        background-color: #eeeeee;
        font-weight: bold;
    }
  </style>
</head>
<body>
<table>
'''

class TraceToHTML(Trace):
    num_tokens = 0
    first = True

    def __init__(self, filename):
        self.file = open(filename, 'w')
        self.file.write(html_header)

    def write_list(self, list, markup=lambda x: x, element="td", elclass=None):
        self.file.write("<tr>\n")
        str_elclass = f" class='{elclass}'" if elclass else ""
        for val in list:
            self.file.write(f"<{element}{str_elclass}>{markup(val)}</{element}>\n")
        self.file.write("</tr>\n")

    def accept_tokens(self, tokens):
        if not self.first:
            self.file.write("</table><table>\n")

        self.write_list([""] + list(tokens), element="th")
        self.num_tokens = len(tokens)
        self.first = False

    def accept(self, variable, value):
        self.write_list([variable] + value)

    def accept_result(self, result):
        self.write_list(["Result"] + [""]*(self.num_tokens-1) + [result], elclass="final")

    def close(self):
        if not self.file.closed:
            self.file.write("</table></body></html>\n")
            self.file.flush()
            self.file.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()