from datetime import datetime
from scrape_followers import get_most_followed
from main import github_followers_link

if __name__ == "__main__":
    most_followed = get_most_followed(github_followers_link, 5)  # Get top 5

    with open("README.md", "r") as f:
        readme_content = f.read()

    # Create the markdown table
    table = "| Profile | Name | Followers |\n|---|---|---|\n"
    for user in most_followed:
        table += f"| <img src='{user.profile_image_link}' width='30' height='30'> | [{user.name}]({user.link}) | {user.followers} |\n"

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

    # Update the "Last updated" timestamp
    last_updated_placeholder_start = "<!-- LAST_UPDATED_START -->"
    last_updated_placeholder_end = "<!-- LAST_UPDATED_END -->"
    
    start_index = readme_content.find(last_updated_placeholder_start)
    end_index = readme_content.find(last_updated_placeholder_end)
    
    if start_index != -1 and end_index != -1:
        now_utc = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        readme_content = (
            readme_content[:start_index + len(last_updated_placeholder_start)] +
            f"\n*Last updated: {now_utc} UTC*\n" +
            readme_content[end_index:]
        )

    with open("README.md", "w") as f:
        f.write(readme_content)
