import sys
import array


from past.builtins import raw_input


def standard_sys():
    """Here we have the next part of the main example"""
    stdin_fileneno = sys.stdin

    # Here we use the main loop as we can note
    for line in stdin_fileneno:
        if 'exit' == line.strip():
            print('Found exit. Terminate the program')
        else:
            print('Message from sys.stdin: ---> {}<---'.format(line))


# Here we have a simple output with the next part


def simple_input(sample_input):
    stdout_fileno = sys.stdout
    for ip in sample_input:
        stdout_fileno.write(ip + '\n')


def print_the_exit_as_c(some_str):
    some_str = input(some_str) # Here we call as the input
    some_str = raw_input(some_str)
    print("The input is the next",  some_str)

