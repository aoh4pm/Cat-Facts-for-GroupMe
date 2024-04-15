 # Cat Facts for GroupMe
    #### Description:
    You know how sometimes you wish your friends knew more about cats?
    This is a program that allows you to automatically send random cat facts to your friends using GroupMe.
    
    Requirements:
    - GroupMe Account
    - GroupMe Access Token:
        - Create application at: https://dev.groupme.com/applications
        - Access token will be provided for user's GroupMe account
    - Friends that use GroupMe

    Cat facts are taken from the Cat Facts API
    - Base URL: https://catfact.ninja/#/
  
    Messages are sent through the GroupMe API
    - Base URL: https://api.groupme.com/v3
    - Documentation: https://dev.groupme.com/

#### Setup Steps
Gather your cat fact by passing the base URL to the Cat Facts API
```commandline
    from cat_facts import Cats

    cat_fact = Cats("https://catfact.ninja").get_random_fact()

```

Before you can send your cat fact, you will need the ID of the group you want to send your fact to.

```commandline
    from groupme import GroupMe
    
    access_token = 'YOUR-ACCESS-TOKEN-HERE'
    gm = GroupMe(access_token)
    
    # This will print out the user's groups and group IDs
    gm.get_groups_info()
```

Then you can send your cat fact using the send_group_cat_fact function
```commandline
    # Function takes the GroupMe class, user's desired group, and the cat fact as parameters
    send_group_cat_fact(gm, cat_group_id, cat_fact)
```

Upcoming:
- Send cat facts as a direct message

#### Files contained:
- main.py
  - Imports Cats and GroupMe classes
  - send_group_cat_fact() will send the user's cat fact after the user provides group ID and access-token
- cat_facts.py
  - Class that contains method for obtaining a cat fact from Cat Facts API 
- groupme.py
  - Class that contains methods for interacting with the GroupMe API
  - get_groups_info() will print the user's GroupMe groups and group ID's
  - send_group_message() will send a message to the user's selected group
  - Additional methods for interacting with GroupMe API
    - images() will allow user to upload images to GroupMe API to send in messages or update group Avatars
    - get_messages() will allow user to retrieve messages from their selected group
    - add_member_to_group() will allow user to add additional members to a selected group 
- tests.py
  - Contains tests to verify Cat Facts and GroupMe API responses
  - test_cat_facts() will verify a 200 response from Cat Facts API
  - test_groups_info() will verify a 200 response and URL format when obtaining user's group list from GroupMe API
  - test_group() will verify a 200 response and URL format when user selects an individual group from GroupMe API
  - test_send_message() will verify a 201 response and send a test message for the user's selected group from GroupMe API
