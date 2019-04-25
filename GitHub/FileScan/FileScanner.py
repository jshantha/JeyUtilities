from github import Github

actk = ""
base_url = "https://api.github.com"
file_query = "org:jshantha extension:py"

def process_repos():
    scan_for_files()
    
def scan_for_files():
    print('Processing Repos')
    # using username and password
    # g = Github("", "")
    
    # or using an access token
    # g = Github(actk)

    # Github Enterprise with custom hostname
    g = Github(base_url=base_url, login_or_token=actk)
    
    # Then play with your Github objects:
    print('... All Repos')
    for repo in g.get_user().get_repos():
        print(repo.name)
        
    # Then play with your Github objects:
    print('... Python Repos')
    for repo in g.search_code(query=file_query):
        print(repo.repository.name)