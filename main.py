from scrape_followers import get_most_followed
github_username = "Joe-Huber"
github_followers_link = f"https://github.com/{github_username}?tab=followers"

if __name__ == "__main__":
    most_followed = get_most_followed(github_followers_link, 3)
    for user in most_followed:
        print(user)