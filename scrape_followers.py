from github_user import GithubUser

def scrape_all_followers():
    # code here
    return []
def scrape_curr_page():
    return 0
def get_most_followed(num):
    all_followers = scrape_all_followers()
    all_followers.sort(key=lambda user: user.followers, reverse=True)
    return all_followers[:num]