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
    start_placeholder = "<!-- FOLLOWERS_LIST_START -->"
    end_placeholder = "<!-- FOLLOWERS_LIST_END -->"
    
    start_index = readme_content.find(start_placeholder)
    end_index = readme_content.find(end_placeholder)

    if start_index != -1 and end_index != -1:
        new_readme = (
            readme_content[:start_index + len(start_placeholder)] +
            "\n" + table + "\n" +
            readme_content[end_index:]
        )
        with open("README.md", "w") as f:
            f.write(new_readme)
    else:
        print("Placeholders not found in README.md")
