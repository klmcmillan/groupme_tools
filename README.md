# groupme_tools

This repository provides scripts to analyze the various forms of data created in GroupMe chats (e.g. text, image). Usage instructions and descriptions of the various files are provided below.

Before you can use any of these files, you need to create a transcript of your GroupMe chat(s). GroupMe provides a nice [API](https://dev.groupme.com/docs/v3) for reading the chat data as JSON data. You can either write your own script to scrape the GroupMe data out use code that already exists out there. I've been using [code by Chris Dzombak](https://github.com/cdzombak/groupme-tools) to scrape my GroupMe chats. Please note that his code was writing for GroupMe API v2 while the API is currently in v3.

## members.py
