import os
from datetime import datetime
from src.scrape_followers import get_most_followed, close_driver

def run_action():
    # Get inputs from the workflow file, which are passed as environment variables
    user_name = os.environ["INPUT_GITHUB_USER_NAME"]
    max_followers = int(os.environ.get("INPUT_MAX_FOLLOWER_COUNT", 5))
    
    followers_link = f"https://github.com/{user_name}?tab=followers"
    
    try:
        # Scrape the data
        most_followed = get_most_followed(followers_link, max_followers)

        # The user's repository is checked out at this path in the container
        readme_path = "/github/workspace/README.md"
        with open(readme_path, "r") as f:
            readme_content = f.read()

        # --- Create the markdown content ---
        now_utc = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        
        # 1. The title
        title = f"### [My Most Famous Followers](https://github.com/Joe-Huber/my-most-followed-followers)"
        
        # 2. The table header
        table_header = "| Profile | Name | Followers |\n|---|---|---|"
        
        # 3. The table rows
        table_rows = []
        for user in most_followed:
            table_rows.append(f"| <img src='{user.profile_image_link}' width='30' height='30'> | [{user.name}]({user.link}) | {user.followers} |")
        
        # 4. The timestamp
        timestamp = f"\n\n*Last updated: {now_utc} UTC*" # Add a blank line before the timestamp

        # 5. Combine all parts with correct spacing for markdown
        # A blank line is needed between the title and the table for correct rendering
        full_content = f"\n{title}\n\n{table_header}\n" + "\n".join(table_rows) + timestamp

        # --- Replace the placeholder in the README ---
        start_placeholder = "<!-- FOLLOWERS_LIST_START -->"
        end_placeholder = "<!-- FOLLOWERS_LIST_END -->"
        start_index = readme_content.find(start_placeholder)
        end_index = readme_content.find(end_placeholder)

        if start_index != -1 and end_index != -1:
            new_readme = (
                readme_content[:start_index + len(start_placeholder)] +
                "\n" + full_content + "\n" +
                readme_content[end_index:]
            )
            with open(readme_path, "w") as f:
                f.write(new_readme)
        else:
            print("Placeholders not found in README.md. Skipping update.")

    finally:
        # Clean up the Selenium driver
        close_driver()

if __name__ == "__main__":
    run_action()
