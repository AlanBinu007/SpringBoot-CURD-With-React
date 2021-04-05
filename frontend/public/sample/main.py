import os

## Number of days you want to make commits
for i in range(10):
    d = str(i) + ' day ago'
    ## Open a text file and modify it
    with open('bot.txt', 'a') as file:
        file.write(d+'\n')
    ## Add bot.txt to staging area
    os.system('git add bot.txt')
    ## Commit it
    os.system('git commit --date="' + d + '" -m "initial commit"')

## push the commit to github
os.system('git push -u origin master -f')