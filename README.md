# Most Followed Followers GitHub Action

[![Update README Status](https://github.com/Joe-Huber/my-most-followed-followers/actions/workflows/update_readme.yml/badge.svg)](https://github.com/Joe-Huber/my-most-followed-followers/actions/workflows/update_readme.yml)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/Joe-Huber/my-most-followed-followers)](https://github.com/Joe-Huber/my-most-followed-followers/releases)
[![GitHub Marketplace](https://img.shields.io/badge/GitHub%20Marketplace-Most%20Followed%20Followers-blue?logo=github)](https://github.com/marketplace/actions/most-followed-followers-action)
[![Top Language](https://img.shields.io/github/languages/top/Joe-Huber/my-most-followed-followers)](https://github.com/Joe-Huber/my-most-followed-followers)
[![Code Size](https://img.shields.io/github/languages/code-size/Joe-Huber/my-most-followed-followers)](https://github.com/Joe-Huber/my-most-followed-followers)
[![Last Commit](https://img.shields.io/github/last-commit/Joe-Huber/my-most-followed-followers)](https://github.com/Joe-Huber/my-most-followed-followers/commits/main)
[![Issues](https://img.shields.io/github/issues/Joe-Huber/my-most-followed-followers)](https://github.com/Joe-Huber/my-most-followed-followers/issues)
[![Forks](https://img.shields.io/github/forks/Joe-Huber/my-most-followed-followers)](https://github.com/Joe-Huber/my-most-followed-followers/network/members)
[![Stars](https://img.shields.io/github/stars/Joe-Huber/my-most-followed-followers)](https://github.com/Joe-Huber/my-most-followed-followers/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This GitHub Action scrapes your most followed followers and displays them in a dynamic list on your profile's `README.md`.

<!-- FOLLOWERS_LIST_START -->
### [My Most Famous Followers](https://github.com/Joe-Huber/my-most-followed-followers)
| Profile | Name | Followers |
|---|---|---|
| <img src='https://avatars.githubusercontent.com/u/44704454?v=4' width='30' height='30'> | [AwesomeCoder412412](https://github.com/AwesomeCoder412412) | 9 |
| <img src='https://avatars.githubusercontent.com/u/202472355?v=4' width='30' height='30'> | [macnmath](https://github.com/macnmath) | 2 |
| <img src='https://avatars.githubusercontent.com/u/148095806?v=4' width='30' height='30'> | [KadenXu5001](https://github.com/KadenXu5001) | 1 |

*Last updated: 2026-01-06 00:58:44 UTC*
<!-- FOLLOWERS_LIST_END -->
Psst, if you follow me you can end up on here! ^-^

## Usage

To use this action in your own repository, follow these steps:

1.  **Update your `README.md`:**

    Add the following placeholders to your `README.md` file. This is where the dynamic list of followers will be inserted.

    ```markdown
    <!-- FOLLOWERS_LIST_START -->
    <!-- FOLLOWERS_LIST_END -->
    ```

2.  **Create a GitHub Actions workflow:**

    Create a new file in your repository at `.github/workflows/update_readme.yml` with the following content:

    ```yaml
    name: Update README with Top Followers

    on:
      schedule:
        - cron: '0 0 * * *' # Runs daily at midnight
      workflow_dispatch:

    jobs:
      update-readme:
        runs-on: ubuntu-latest
        permissions:
          contents: write # Required to push changes back to the repository
        steps:
          - name: Check out repository
            uses: actions/checkout@v3

          - name: Update README with most followed followers
            uses: Joe-Huber/my-most-followed-followers@main
            with:
              GITHUB_USER_NAME: ${{ github.repository_owner }}
              MAX_FOLLOWER_COUNT: 10
          
          - name: Commit and push changes
            run: |
              git config --global user.name 'github-actions[bot]'
              git config --global user.email 'github-actions[bot]@users.noreply.github.com'
              git add README.md
              git commit -m "Automated README update" || exit 0
              git push
    ```

    This workflow will run daily, but you can also trigger it manually from the "Actions" tab in your repository.
## Inputs

The following inputs can be configured in your workflow file's `with` block:

| Input                | Description                                                | Default                        | Required |
| -------------------- | ---------------------------------------------------------- | ------------------------------ | -------- |
| `GITHUB_USER_NAME`   | Your GitHub username.                                      | `${{ github.repository_owner }}` | `true`   |
| `MAX_FOLLOWER_COUNT` | The number of top followers to display in the table.       | `5`                            | `false`  |

## How It Works

This action uses a Docker container to run a Python script that:
- Scrapes your followers using Selenium.
- Finds your most followed followers.
- Updates your `README.md` with a dynamically generated table.

---

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

#### Legal Note
Scraping is allowed under GitHub's Terms of Service for the purposes of this action. For more details, see the [GitHub Acceptable Use Policies](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies).
