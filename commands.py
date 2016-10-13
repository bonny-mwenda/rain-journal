"""

This example uses docopt with the built in cmd module to demonstrate an

interactive command application.



Usage:



	journal create (<journal name>)...



	journal (<journal name>) newentry (<subtitle> <entry>)



	journal (<journal name>) view -a



	journal (<journal name>) view -l



	journal --h | --help

		

	journal exit



Options:



	--h --help Show this screen

	create creates new journal

	newentry create new entry in journal

	view -a to output list of all entries in journal

	view -l to output the latest journal entry 

	exit exits the journal app back to starts

	

"""


import sys

import cmd

from docopt import docopt, DocoptExit

from create import Journal

# import lst


def docopt_cmd(func):
    """

    This decorator is used to simplify the try/except block and pass the result

    of the docopt parsing to the called action.

    """

    def fn(self, arg):

        try:

            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:

            # The DocoptExit is thrown when the args do not match.

            # We print a message to the user and the usage block.

            print('Invalid Command!')

            print(e)

            return

        except SystemExit:

            # The SystemExit exception prints the usage for --help

            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__

    fn.__doc__ = func.__doc__

    fn.__dict__.update(func.__dict__)

    return fn


class command(cmd.Cmd):

    intro = 'Welcome to my interactive program! (type help for a list of commands.)'

    prompt = '(my_program) '

    file = None

    @docopt_cmd
    def do_create(sel, args):
        """journal create (<journal name>)"""

        Journal.create_journal(args)

        print args

    def do_newentry(self, args):
        """ journal (<journal name>) newentry (<subtitle> <entry>) """

        Journal.create_entry(args)

        print args

    def do_exit(self, args):
        """ journal exit """
