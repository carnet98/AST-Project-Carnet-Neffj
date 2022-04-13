#!/usr/bin/env python3

# take code. transform to compile ready. keep track of DCEMarkers
# PRECONDITION: The markers are numbered continuously
def precompute(candidate_code):
    print("PRECOMPUTE FOR COMPILATION")
    counter = 0
    x = candidate_code.find("void DCEMarker{}_(void);".format(counter))
    gdb_commands = ""
    # interate through all markers
    while(not x == -1):
        candidate_code = candidate_code.replace("void DCEMarker{}_(void);".format(counter), "void DCEMarker{}_(void){{}}".format(counter))
        gdb_commands = gdb_commands + "break DCEMarker{}_\n".format(counter)
        # next iteration
        counter += 1
        x = candidate_code.find("void DCEMarker{}_(void);".format(counter))
    
    new_candidate = open('tmp/candidate.c', 'w+')
    new_candidate.write(candidate_code)
    new_candidate.close()
    command_file = open('tmp/command_file.txt', 'w+')
    command_file.write(gdb_commands)
    command_file.close()



def run():
    print("RUN THE DC INSERTER")






# enter program from generator.py
def entrance(candidate_code):
    # store program in tmp/
    program_txt = open('tmp/candidate.txt', 'w+')
    program_txt.write(candidate_code)
    program_txt.close()
    run()

# enter program standalone
def main():
    text_file = open("tmp/candidate.txt", "r")
    candidate_code = text_file.read()
    text_file.close()
    precompute(candidate_code)
    run()

if __name__ == "__main__":
    main()

    





