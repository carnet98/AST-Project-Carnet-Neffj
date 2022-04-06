#!/usr/bin/env python3

def run():
    print("RUN THE DC INSERTER")






# enter program from generator.py
def entrance(candidate_code):
    # store program in tmp/
    program = open('tmp/candidate.c', 'w+')
    program.write(candidate_code)
    program.close()
    run()

# enter program standalone
def main():
    run()

if __name__ == "__main__":
    main()

    





