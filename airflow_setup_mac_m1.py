# mac useradd command
# if this doesn't work, just go to 'preference' (reference: https://support.apple.com/ko-kr/HT201548)
# you can also set your password there!

sudo dscl . -create /home_directory_name/username

# mac user login command in terminal (not gui)
login

# if you are trying to get to the docker image of airflow, run the command 'cd' and move on to the home_directory
