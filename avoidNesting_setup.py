################ TO DO ###################
# - create database-spawn

# setup.py file belonging to PyPassV

# version-control and matching
PyPassV_version = 0.1

# import libs
import os, bcrypt, getpass

# import sqlcipher api using pysqlcipher3
from pysqlcipher3 import dbapi2 as sqlite


def check_existence(file):
    for i in file:
        if not os.path.exists(i):
            raise FileNotFoundError(i)
        else:
            continue
    return True


def create_user_files(user_name, user_password):

    def create_database_table(user_password):
        conn = sqlite.connect("database.db")
        c = conn.cursor()
        c.execute(f"PRAGMA key='{user_password}'")
        c.execute('CREATE TABLE passwords (service, username, password, note)')
        conn.commit()
        c.close()

    def create_key(user_name, user_password):
        user_name = str(user_name)
        user_password = user_password.encode('UTF-8')
        my_salt = bcrypt.gensalt()
        hashed_user_password = bcrypt.hashpw(user_password, my_salt)
        hashed_user_password = hashed_user_password.decode()
        with open(f"{user_name}_key", 'w') as f:
            f.write(user_name)
            f.close
        with open(f"{user_name}_key", 'a') as f:
            f.seek(len(user_name))
            f.write(' | ' + hashed_user_password)
            f.close

    create_database_table(user_password)
    create_key(user_name, user_password)


def main():

    check_existence(['func.py', 'graphics.py', 'main.py'])

    import graphics, func

    func.clear_shell()

    graphics.show_logo()
    print(f"{' ' * 14}First time setup{' ' * 14}\n{'-' * 44}") # logo bottom-text

    def input_error_choice():
        choice = input(f"Invalid input.\nEither; the input exceeds {50} characters,or a character wasn't recognized.\nPress [ENTER] to continue.")
        func.input_sanetizer(choice)
        func.wipe_line(5)

    valid_user_name = False

    while not valid_user_name:
        user_name = input("Create a username\n~> ")
        if func.input_sanetizer(user_name):
            valid_user_name = True
            func.wipe_line(2)

        else:
            input_error_choice()
            continue

    valid_user_password = False

    while not valid_user_password:
        user_password = getpass.getpass("Create a password [input hidden]\n~> ")
        if func.input_sanetizer(user_password):
            func.wipe_line(2)
            user_password_check = getpass.getpass("Type that again [input hidden]\n~> ")
            if func.input_sanetizer(user_password_check):
                if user_password_check == user_password:

                    valid_user_password = True
                    
                    create_user_files(user_name, user_password)
                else:
                    choice = input("The passwords does not match, press [ENTER] to try again.")
                    func.input_sanetizer(choice)
                    func.wipe_line(3)
                    continue
            else:
                input_error_choice()
                continue
        else:
            input_error_choice()
            continue

if __name__ == '__main__':
    main()