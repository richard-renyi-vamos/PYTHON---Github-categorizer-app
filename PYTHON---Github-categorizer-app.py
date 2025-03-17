import requests

# GitHub API base URL
GITHUB_API_URL = "https://api.github.com"

# Optional: GitHub API Token (to increase rate limit)
GITHUB_API_TOKEN = "your_github_token_here"  # Replace with your token if needed
HEADERS = {"Authorization": f"token {GITHUB_API_TOKEN}"} if GITHUB_API_TOKEN else {}

def get_github_repositories(username):
    """
    Get a list of repositories for a GitHub user.
    :param username: GitHub username to search for
    :return: List of repositories
    """
    url = f"{GITHUB_API_URL}/users/{username}/repos"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        return response.json()  # List of repositories in JSON format
    else:
        print(f"Failed to fetch data for {username}. Status code: {response.status_code}")
        return []

def categorize_repositories(repos):
    """
    Categorize repositories based on language and topics.
    :param repos: List of repositories
    :return: Categorized repositories
    """
    categories = {"Python": [], "JavaScript": [], "Ruby": [], "Java": [], "Other": []}
    
    for repo in repos:
        name = repo.get("name")
        description = repo.get("description", "No description available")
        language = repo.get("language", "Other")
        topics = repo.get("topics", [])
        
        # Categorize based on language
        if language in categories:
            categories[language].append({"name": name, "description": description, "topics": topics})
        else:
            categories["Other"].append({"name": name, "description": description, "topics": topics})
    
    return categories

def display_categories(categories):
    """
    Display the categorized repositories.
    :param categories: Categorized repositories
    """
    for category, repos in categories.items():
        print(f"\nCategory: {category}")
        if repos:
            for repo in repos:
                print(f"  - {repo['name']}: {repo['description']}")
                if repo['topics']:
                    print(f"    Topics: {', '.join(repo['topics'])}")
                print("\n")
        else:
            print("  No repositories found in this category.")

def main():
    username = input("Enter GitHub username: ")
    repos = get_github_repositories(username)
    
    if repos:
        categories = categorize_repositories(repos)
        display_categories(categories)

if __name__ == "__main__":
    main()
