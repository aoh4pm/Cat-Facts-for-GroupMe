import json
from cat_facts import Cats
from groupme import GroupMe


def main():
    # Cat Facts API
    cat_fact = Cats("https://catfact.ninja").get_random_fact()

    # GroupMe API
    access_token = 'YOUR-ACCESS-TOKEN-HERE'
    group_id = 'YOUR GROUP ID HERE'

    # Send message to group
    gm = GroupMe(access_token)
    gm.get_groups_info()
    send_group_cat_fact(gm, group_id, cat_fact)


def send_group_cat_fact(gm, cat_group_id, cat_fact):
    cat_group_message = gm.send_group_message(cat_group_id, cat_fact)


if __name__ == "__main__":
    main()
