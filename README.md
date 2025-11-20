# Most Followed Followers GitHub Action

This GitHub Action scrapes your most followed followers and displays them in a dynamic list on your profile's `README.md`.

<!-- FOLLOWERS_LIST_START -->
<!-- FOLLOWERS_LIST_END -->
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
        steps:
          - name: Check out repository
            uses: actions/checkout@v3

          - name: Update README with most followed followers
            uses: Joe-Huber/my-most-followed-followers@main # Or use a specific version like @v1
            with:
              GITHUB_USER_NAME: ${{ github.repository_owner }}
              MAX_FOLLOWER_COUNT: 10 # Optional: specify the number of followers to show
          
          - name: Commit and push changes
            run: |
              git config --global user.name 'github-actions[bot]'
              git config --global user.email 'github-actions[bot]@users.noreply.github.com'
              git add README.md
              git commit -m "Automated README update" || exit 0
              git push
    ```

    This workflow will run daily, but you can also trigger it manually from the "Actions" tab in your repository.

## How It Works

This action uses a Docker container to run a Python script that:
- Scrapes your followers using Selenium.
- Finds your most followed followers.
- Updates your `README.md` with a dynamically generated table.

---

#### Legal Note
Scraping is allowed in GitHub's TOS: https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies
    ```
        You may use information from our Service for the following reasons, regardless of whether the information was scraped, collected through our API, or obtained otherwise
    ```
