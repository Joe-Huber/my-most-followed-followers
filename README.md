# Most Followed Followers GitHub Action

This GitHub Action scrapes your most followed followers and displays them in a dynamic list on your profile's `README.md`.

## Usage

To use this action in your own repository, follow these steps:

1.  **Update your `README.md`:**

    Add the following placeholders to your `README.md` file. This is where the dynamic list of followers will be inserted.

    ```markdown
    <!-- FOLLOWERS_LIST_START -->
### [My Most Famous Followers](https://github.com/Joe-Huber/my-most-followed-followers)
| Profile | Name | Followers |
|---|---|---|
| <img src='https://avatars.githubusercontent.com/u/44704454?v=4' width='30' height='30'> | [AwesomeCoder412412](https://github.com/AwesomeCoder412412) | 9 |
| <img src='https://avatars.githubusercontent.com/u/202472355?v=4' width='30' height='30'> | [macnmath](https://github.com/macnmath) | 2 |
| <img src='https://avatars.githubusercontent.com/u/148095806?v=4' width='30' height='30'> | [KadenXu5001](https://github.com/KadenXu5001) | 1 |

*Last updated: 2025-11-20 20:28:22 UTC*
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
        steps:
          - name: Check out repository
            uses: actions/checkout@v3

          - name: Update README with most followed followers
            uses: Joe-Huber/my-most-followed-followers@v1 # Replace with your repo if you forked
            with:
              GITHUB_USER_NAME: ${{ github.repository_owner }}
              MAX_FOLLOWER_COUNT: 10 # Optional: specify the number of followers to show
    ```

    This workflow will run daily, but you can also trigger it manually from the "Actions" tab in your repository.

## How It Works

This action uses a Docker container to run a Python script that:
- Scrapes your followers using Selenium.
- Finds your most followed followers.
- Updates your `README.md` with a dynamically generated table.

---
<!-- FOLLOWERS_LIST_START -->
<!-- FOLLOWERS_LIST_END -->
Psst, if you follow me you can show up on here! ^-^
