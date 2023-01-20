# main.py file belonging to PyPassV

# version-control and matching
main_PyPassV_version = 0.1

# import libs
import time, glob, bcrypt, getpass

# import sqlcipher api using pysqlcipher3
from pysqlcipher3 import dbapi2 as sqlite

# import locals
import func


def login():

    password_valid = False

    tries = 1

    user_key = glob.glob("*_key")
    user_key = str(user_key[0])

    while not password_valid:
        login_password_input = getpass.getpass("Enter password [input hidden]\n~> ")
        login_password_input = login_password_input.encode('UTF-8')
        with open(user_key, 'r') as key_file:
            line = key_file.readline()
            line = line.split("| ")
            key_string = str(line[1])
            key_string = key_string.encode("UTF-8")
            key_file.close()
            if bcrypt.checkpw(login_password_input, key_string):
                password_valid = True
                #func.wipe_line(14)
            else:
                if tries == 3:
                    print("\n3 wrong inputs, exiting...")
                    exit()
                tries += 1
                print("\nWrong, try again.")
                time.sleep(1)
                func.wipe_line(4)
                continue


def command_controller(input):

    func.input_sanetizer(input)

    if input.lower() == 'h' or input.lower() == 'help' or input.lower() == '--help':

        display_commands = r'''
        h       --help              - display this prompt

        q       --quit              - quit the program, at any time

        v       --view [OPTION]     - view all entries,
                                    or the credentials for a specific entry

        n       --new               - make a new entry to the database

        r       --remove [OPTION]   - remove an entry from the database

        nuke    --nuke              - encrypt and disposal of the entire database,
                                    inluding the user
        '''

        print(display_commands)


def main():

    login()


if __name__ == '__main__':
    main()