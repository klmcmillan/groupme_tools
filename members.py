import json
from collections import Counter, defaultdict
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def get_users(transcript):
    """
    Sorts through GroupMe transcript and returns a dictionary where the keys are
    user ids and the values are lists of names used for each user id.
    """
    users = defaultdict(list)

    for message in transcript:
        id = message[u'user_id']
        name = message[u'name']

        users[id].append(name)

    return users


def filter_users(transcript, users):
    """
    Filters dictionary of user ids and names and returns lists of user ids for
    real users and exiled users (i.e. bots). For each user id, exiled users are
    identified using the following tests:
    (1) if 'GroupMe' is present in the most common name associated with the user
        id -- indicates that user id is associated with a system response
    (2) if none of the system messages contain a combination of the word 'added'
        and any of the names associated with a user id -- implies that the user
        id is a bot because bots cannot be explicitly added as members of the
        group or add other memebers to the group.
    """
    real_ids = []
    exiled_ids = []

    for key in users:
        if 'GroupMe' in Counter(users[key]).most_common(1)[0][0].split():
            exiled_ids.append(key)
        else:
            id_found = False
            for message in transcript:
                if message[u'text'] is not None:
                    if message[u'system'] and 'added' in message[u'text'] and any(name in message[u'text'] for name in users[key] if name == name.rstrip()):
                        real_ids.append(key)
                        id_found = True
                        break
            if not id_found:
                exiled_ids.append(key)

    return real_ids, exiled_ids


def print_users(users, real_ids, exiled_ids, n):
    """
    Prints out formatted list of real and exiled users ids as well a list of the
    n most common names associated with each user id. Use n = 1 to return the
    most common name for each user id.
    """
    exiled_ids_len = [len(id) for id in exiled_ids]
    max_exiled_id_len = max(exiled_ids_len)
    pad_width = max(max_exiled_id_len, len('UserID')) + 5

    print '\n===EXILED USERS===\n'
    print '{:<{}s}'.format('UserID', pad_width) + 'Name(s)'
    for id in exiled_ids:
        print '{:<{}s}'.format(id, pad_width) + ', '.join([name for name, _ in Counter(users[id]).most_common(n)])

    real_ids_len = [len(id) for id in real_ids]
    max_real_id_len = max(real_ids_len)
    pad_width = max(max_real_id_len, len('UserID')) + 5

    print '\n===REAL USERS===\n'
    print '{:<{}s}'.format('UserID', pad_width) + 'Name(s)'
    for id in real_ids:
        print '{:<{}s}'.format(id, pad_width) + ', '.join([name for name, _ in Counter(users[id]).most_common(n)])


def main():
    """
    User-specified parameters:
    (1) transcriptName: name of JSON GroupMe transcript to read

    Returns:
    Reads GroupMe transcript, executes functions to load and filter user ids and
    prints (to screen) real and exiled user ids as well as name(s) associated
    with each user id.
    """
    transcriptName = 'transcript-name.json'

    transcriptFile = open(transcriptName)
    transcript = json.load(transcriptFile)
    transcriptFile.close()

    users = get_users(transcript)
    real_ids, exiled_ids = filter_users(transcript, users)
    print_users(users, real_ids, exiled_ids, 1)


if __name__ == '__main__':
    main()
    sys.exit(0)
