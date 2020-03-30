field_name | type | description
-- | -- | --
github_repo_url | string | the repo's direct link on GitHub
repo_description | string | the repo's description provided by the owner of the repo, see more here: https://help.github.com/en/github/getting-started-with-github/create-a-repo
topics | string | topics are labels that can be added to repos for classification, see more here: https://help.github.com/en/github/administering-a-repository/classifying-your-repository-with-topics
owner_repo_name | string | the owner and repo name parsed from the URL
owner_name | string | the login name of the user or org that owns the repo
owner_type | string | repos may be owned by individual or organization accounts, this filed indicates what the owner is, see more here: https://help.github.com/en/github/getting-started-with-github/types-of-github-accounts
organization_bio | string | organizations/users may choose to personalize themselves with a description/bio, if that is provided, it's included. See more: https://help.github.com/en/github/setting-up-and-managing-your-github-profile/about-your-organizations-profile and https://help.github.com/en/github/setting-up-and-managing-your-github-profile/personalizing-your-profile#adding-a-bio-to-your-profile
repo_created_day | date | the date that the repo was created on GitHub
primary_language_name | string | the primary detected language of the files within the repo based on linguist, see more here: https://help.github.com/en/github/creating-cloning-and-archiving-repositories/about-repository-languages
license_name | string | if a user has licensed their public repository, the license's lower case SPDX ID is provided, see more here: https://choosealicense.com/
is_github_pages | boolean | this boolean indicates whether the owner of the repo has created a GitHub pages site, see more here: https://help.github.com/en/github/working-with-github-pages
has_readme | boolean | this boolean indicates if the repo has a README.md file detected in its root
has_wiki | boolean | this boolean indicates if the repo has a wiki, see more here: https://help.github.com/en/github/building-a-strong-community/about-wikis
has_merged_prs | boolean | this boolean indicates if the repo has pull requests that have been merged into one or more repo branches
has_issues | boolean | this boolean indicates if the repo has created issues
has_contributor_guide | boolean | this boolean indicates if the repo has a contributor guide, see more here: https://help.github.com/en/github/building-a-strong-community/setting-guidelines-for-repository-contributors
has_code_of_conduct | boolean | this boolean indicates if the repo has a code of conduct, see more here: https://help.github.com/en/github/building-a-strong-community/adding-a-code-of-conduct-to-your-project
count_of_public_forks | integer | this count indicates the number of times the repo has been forked, see more here: https://help.github.com/en/github/getting-started-with-github/fork-a-repo
count_of_stars | integer | this count indicates the number of times the repo has been starred by other users, see more here: https://help.github.com/en/github/getting-started-with-github/saving-repositories-with-stars
count_of_watchers | integer | this count indicates the number of times the repo has been watched by other users that wish to receive notifications about it, see more here: https://help.github.com/en/github/receiving-notifications-about-activity-on-github/watching-and-unwatching-repositories
count_distinct_contributors | integer | this count includes the number of unique users that have contributed to the repo in some way (by committing, opening an issue, opening a pull request, reviewing a pull request or making a comment on an issue, commit, pull request, etc), see more about contributions and the contribution graph here: https://help.github.com/en/github/setting-up-and-managing-your-github-profile/viewing-contributions-on-your-profile
count_contributions | integer | this count is the sum total of the following counts (commits, commit_comments,  created_issues, pull_requests_created, pull_requests_reviewed and comments_on_issues_and_pull_requests)
count_commits | integer | this count is the sum total of all commits made across all branches on the repo, see more here: https://help.github.com/en/github/committing-changes-to-your-project
count_commit_comments | integer | this count is the number of comments made on commits to the repo, see more here: https://developer.github.com/v3/guides/working-with-comments/
count_created_issues | integer | this count is the number issues created on the repository, see more here: https://help.github.com/en/github/managing-your-work-on-github/creating-an-issue
count_pull_requests_created | integer | this count is the number of pull requests made against the repo, see more here: https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests
count_pull_requests_reviews | integer | this count is the number of pull requests made against the repo, see more here: https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-request-reviews
count_comments_on_issues_and_pull_requests | integer | this count is the sum total number of all issue and pull request related comments made, for pull requests, see more here: https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/commenting-on-a-pull-request
