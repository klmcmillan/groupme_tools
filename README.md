# groupme_tools

This repository provides scripts to analyze the various forms of data created in GroupMe chats (e.g. text, image). Usage instructions and descriptions of the various files are provided below.

Before you can use any of these files, you need to create a transcript of your GroupMe chat(s). GroupMe provides a nice [API](https://dev.groupme.com/docs/v3) for reading the chat data as JSON data. You can either write your own script to scrape the GroupMe data or use code that already exists out there. I've been using [code by Chris Dzombak](https://github.com/cdzombak/groupme-tools) to scrape my GroupMe chats. Please note that his code was writing for GroupMe API v2 while the API is currently in v3.

## members.py

In GroupMe chats, a user can be identified by their username or user ID. The username can be changed at any time, but the user ID is immutable. Therefore, if you want to isolate data created by a specified user, it's best to index the data by their user ID.

GroupMe also allows users to create bots to interact with the chats. Each bot within a chat has its own user ID. Sometimes bots have names that make them look like humans (or potentially names that are very close to those of non-bot users within the chat). If someone was interested in analyzing data from real users (i.e. humans) only, it would be important to seperate user IDs for humans and bots.

This file can be used to get all the user IDs in a user-specified GroupMe transcript. Using a set of rules, it will seperate the user IDs into real users and bots. In order to use this file, the following lines from the main() function need to be changed:

```python
transcriptName = 'transcript-name.json'
```

```transcriptName``` is the name of the GroupMe chat transcript to be analyzed.

After changes to the ```main()``` function are made, run the file, and a formatted list of real and bot users IDs as well as a list of the n most common names associated with each user ID will be printed to screen. Change the parameter ```n``` in the function ```print_users(users, real_ids, exiled_ids, n)``` in order to change the number of names associated with each user ID that are printed to screen.
