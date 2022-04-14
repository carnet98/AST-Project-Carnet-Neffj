#!/usr/bin/env python3

import os



# take code. transform to compile ready. keep track of DCEMarkers
# PRECONDITION: The markers are numbered continuously
def precompute(candidate_code):
    print("PRECOMPUTE FOR COMPILATION")
    counter = 0
    x = candidate_code.find("void DCEMarker{}_(void);".format(counter))
    gdb_commands = ""
    # interate through all markers
    while(not x == -1):
        # complete DCEMarker to a explicit function definition
        candidate_code = candidate_code.replace("void DCEMarker{}_(void);".format(counter), "void DCEMarker{}_(void){{}}".format(counter))
        # add the marker as breakpoint
        gdb_commands = gdb_commands + "break DCEMarker{}_\n".format(counter)
        # next iteration
        counter += 1
        x = candidate_code.find("void DCEMarker{}_(void);".format(counter))
    
    # store candidate as .c file to compile
    new_candidate = open('tmp/candidate.c', 'w+')
    new_candidate.write(candidate_code)
    new_candidate.close()
    # complete gdb_commands to automatically run and log the program.
    gdb_commands = gdb_commands + "set logging file gdb_log.txt\nset logging on\nr\nwhile 1\ns\ninfo locals\ncontinue\nend"

    # store gdb_commands as .txt file to run in a gdb session
    command_file = open('tmp/command_file.txt', 'w+')
    command_file.write(gdb_commands)
    command_file.close()


def run_gdb():
    print("COMPILE AND EXECUTE GDB AND GET LOCAL VARIABLE INFO")
    os.system("./gdb_script.sh")


def eval_log():
    print("START: EVALUTATE LOG FILE")
    curr_break = ""
    var_vals = {}
    with open("tmp/gdb_log.txt", "r") as log_file:
        # iterate through each line in the log file
        for line in log_file:
            stripped_line = line.strip()
            # split lines into list of tokens
            tokens = stripped_line.split()

            # catch breakpoint and update the current active marker
            if (len(tokens) > 0 and tokens[0] == "Breakpoint"):
                curr_break = tokens[2]
                if not (curr_break in var_vals):
                    var_vals[curr_break] = {}

            # catch variable values
            if(len(tokens) > 0 and tokens[1] == "="):
                var = tokens[0]
                val = tokens[2]
                # add new variable to dictionary
                if not (var in var_vals[curr_break]):
                    var_vals[curr_break][var] = []
                # bring value to int format
                val = int(val, 0)
                if not (val in var_vals[curr_break][var]):
                    var_vals[curr_break][var].append(val)
                
    print(var_vals)
    print("END: EVALUATED LOG FILE")
    
    


# enter program from generator.py
def entrance(candidate_code):
    # store program in tmp/
    program_txt = open('tmp/candidate.txt', 'w+')
    program_txt.write(candidate_code)
    program_txt.close()
    precompute(candidate_code)
    run_gdb()
    eval_log()

# enter program standalone
def main():
    text_file = open("tmp/candidate.txt", "r")
    candidate_code = text_file.read()
    text_file.close()
    precompute(candidate_code)
    run_gdb()
    eval_log()

if __name__ == "__main__":
    main()


