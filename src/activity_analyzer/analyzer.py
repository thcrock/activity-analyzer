import requests
from collections import Counter, defaultdict
from typing import List, Dict
import logging
logging.basicConfig(level=logging.INFO)


def retrieve_events_from_github(user: str):
    """Retrieve up to 100 events for a user from the Github API"""
    url = f"https://api.github.com/users/{user}/events?per_page=100"
    response = requests.get(url)
    json_response = response.json()
    return json_response


def partition_events_by_repo(events: List) -> Dict[str, List]:
    """Split the given events by the full repo name.

    Any events without a repo name will not be present in the output.
    """
    events_by_repo = defaultdict(list)
    for event in events:
        if "repo" in event and "name" in event["repo"]:
            events_by_repo[event["repo"]["name"]].append(event)
        else:
            logging.info("Event id %s did not include repository information, skipping", event["id"])
    return events_by_repo  

def most_used_event_types(events: List) -> List[str]:
    """Return the three most used event types from the list of events"""
    counter = Counter()
    for event in events:
        if "type" not in event:
            logging.info("Event id %s did not include a type. Skipping", event["id"])
        else:
            counter[event["type"]] += 1
    return [row[0] for row in counter.most_common(3)]


def is_repo_owned_by_user(repo: str, user: str) -> bool:
    """Infer whether or not the given repo is owned by the user"""
    repo_owner, _ = repo.split("/")
    if repo_owner == user:
        return True
    else:
        return False


def analyze(user: str):
    """Display up to three most common event types for each repository from the user's public Github events.

    Any repositories that the user owns are flagged with (OWNER)
    """
    try:
        json_response = retrieve_events_from_github(user)
    except requests.exceptions.RequestException:
        print("Problem retrieving user events from Github. Exception shown below.")
        raise
    if not json_response:
        print(user, 'has not been active in any public repositories recently')
        return

    events_by_repo = partition_events_by_repo(json_response)
    print("Most common activity types per repository for user", user)
    for repo, events in events_by_repo.items():
        report_string = repo
        if is_repo_owned_by_user(repo, user):
            report_string += " (OWNER)"

        common_events = most_used_event_types(events)
        report_string += ": " + str(common_events)
        print(report_string)
    
