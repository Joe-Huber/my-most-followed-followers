from datetime import datetime, timezone
from .scrape_followers import get_most_followed, close_driver
from .main import github_followers_link

if __name__ == "__main__":
    try:
        # Scrape most followed users
        most_followed = get_most_followed(github_followers_link, 5)  # Get top 5

        with open("README.md", "r") as f:
            readme_content = f.read()

        # Create the markdown table and add the timestamp
        now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        title = "### [My Most Famous Followers](https://github.com/Joe-Huber/my-most-followed-followers)\n"
        table = f"{title}| Profile | Name | Followers |\n|---|---|---|\n"
        for user in most_followed:
            table += f"| <img src='{user.profile_image_link}' width='30' height='30'> | [{user.name}]({user.link}) | {user.followers} |\n"
        table += f"\n*Last updated: {now_utc} UTC*"

        # Use placeholders to insert the table
        followers_start_placeholder = "<!-- FOLLOWERS_LIST_START -->"
        followers_end_placeholder = "<!-- FOLLOWERS_LIST_END -->"
        
        start_index = readme_content.find(followers_start_placeholder)
        end_index = readme_content.find(followers_end_placeholder)

        if start_index != -1 and end_index != -1:
            readme_content = (
                readme_content[:start_index + len(followers_start_placeholder)] +
                "\n" + table + "\n" +
                readme_content[end_index:]
            )

        with open("README.md", "w") as f:
            f.write(readme_content)
            
    finally:
        close_driver()
