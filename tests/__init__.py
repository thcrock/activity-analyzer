from src.activity_analyzer.analyzer import most_used_event_types

def test_most_used_event_types_basic():
    events = [
        {'id': 1, 'type': 'PullRequest'},
        {'id': 2, 'type': 'PullRequest'},
        {'id': 3, 'type': 'PullRequest'},
        {'id': 4, 'type': 'PullRequest'},
        {'id': 5, 'type': 'CreateRepo'},
        {'id': 6, 'type': 'CreateRepo'},
        {'id': 7, 'type': 'CreateRepo'},
        {'id': 8, 'type': 'Comment'},
        {'id': 9, 'type': 'Comment'},
        {'id': 10, 'type': 'IssueOpen'},
    ]
    assert sorted(most_used_event_types(events)) == [
        'Comment', 'CreateRepo', 'PullRequest'
    ]

def test_most_used_event_types_some_types_missing():
    events = [
        {'id': 1, 'type': 'PullRequest'},
        {'id': 2, 'type': 'PullRequest'},
        {'id': 3, 'type': 'PullRequest'},
        {'id': 4, 'type': 'PullRequest'},
        {'id': 5},
        {'id': 6, 'type': 'CreateRepo'},
        {'id': 7, 'type': 'CreateRepo'},
        {'id': 8, 'type': 'Comment'},
        {'id': 9, 'type': 'Comment'},
        {'id': 10, 'type': 'IssueOpen'},
    ]
    assert sorted(most_used_event_types(events)) == [
        'Comment', 'CreateRepo', 'PullRequest'
    ]