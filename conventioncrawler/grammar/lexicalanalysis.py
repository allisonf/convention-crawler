# The Lexical Analysis package is for
# tokenizing a convention file according to the grammar

import conventioncrawler.grammar.conventiongrammar as cg


def tokenize(filename, app_name):

    file_string = _openAndRead(filename)

    if (app_name):
        parser = cg.ConventionGrammar.parser({'app_name': app_name})
    else:
        parser = cg.ConventionGrammar.parser()

    tokenized_file = parser.parse_string(file_string)

    return tokenized_file


def _openAndRead(filename):

    file = open(filename)
    file_string = file.read()
    file.close()

    return file_string
