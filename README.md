# git-create-project

Creates both a project locally in your machine and a repository on github

## Depencencies

**[MechanicalSoup](https://github.com/MechanicalSoup/MechanicalSoup)** - required for the script to work

**pass** - used to get encrypted password. The password can be hardcoded, but it is not recommended.

## Usage

```git-create-project <name-of-the-project>```

The script will create the project folder inside ~/MyProjects, git init inside it, log into yout github account, add a repository with the same name, add the remote origin, create a simple README.md file and push it to the repository.
