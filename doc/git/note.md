# References

https://git-scm.com/docs/
https://devhints.io/git-branch

# Configs and Prints

git config --global pager.branch false
git config --global pager.stash false

git count-objects -v
git log <--author=name>
git log --grep="Something in the message"
git log -S "Check for commit that adds this line"
git log --since=2.months.ago --until=1.day.ago --author=andy -S "something" --all-match
git log --pretty='%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%ar) %C(bold blue)<%an>%Creset' --all
git blame file_path
git branch | grep "*branch_name*" | xargs <git command, eg: git branch -D>

# Squash

git merge --squash branch_name

# Reset the last 2 commits, then force update remote history
 
git reset --soft HEAD~2
git reset --hard HEAD~2
git push --force origin branch_name

git reset --soft HEAD~5 && git commit -m "fix answers link crash"
git reset --soft HEAD~4 && git commit -m "update and rename existing checkmarx sh to gen_osa_zip sh"
git reset --soft HEAD~11 && git commit -m "impl rect radio button"

git reset --soft HEAD~6 && git commit -m "add SpendTrackerSelectAccountFragment"

# Reset file

git reset HEAD file_path

# Abandon local changes, and reset to <remote> branch

git reset --hard <origin/>branch_name

# Stash

git stash save "My stash message"
git stash save "My another stash message"
git stash list
git stash apply stash@{0}
git stash drop stash@{0}

# To ignore watching/tracking a particular directory/file run this:

git update-index --assume-unchanged <file>

# To get undo/show dir's/files that are set to assume-unchanged run this:

git update-index --no-assume-unchanged <file>

# To get a list of dir's/files that are assume-unchanged run this:

git ls-files -v|grep '^h'

# git ls-files -v
- untracked files start with (lower) h

# Remove the file from the repository, but keep it on the filesystem
git rm <file> --cached

# Rename
As long as you're just renaming a file, and not a folder, you can just use git mv:
git mv -f yOuRfIlEnAmE yourfilename
git mv -f IFwbHubRepository.kt IFwbHubRepository.kt

# Tag
git tag -a release/22.05.0 -m "Production 22.05.0 (4001948)"
git push origin release/22.05.0