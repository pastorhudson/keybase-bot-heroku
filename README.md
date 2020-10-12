# keybase-bot-heroku
This is a simple starter bot for launching a keybase bot on Heroku or Dokku

### Setup:

### Get a Bot Token

As your keybase user run:

```
$ keybase bot token create > /tmp/bot-token
```

You'll get back a base64 token, like: `6C37sjCBgMNf06Z6oTgixIxHJpja8G-Qp`. This is your *bot token* that allows you to sign up bots.

### Signup the Bot

You can signup for your bot in a new "bot home dir" using your bot token, and by specifying the username of the bot.
Here we use *standalone* mode which means the service and the client run in the same process, and then both exit
at the same time. It won't actually write any credentials to that directory, but we give it a non-standard home directory
in this example so we don't pick up your real user.

```
$ keybase --standalone --home=/tmp/bot bot signup -u <botname> -t $(cat /tmp/bot-token) > paper-key
```

This will output a paper key to standard output.
It is a paper key, and not standard device keys.

### Setup Bot Home Directory and Device IMPORTANT
You can make a directory that can be used to execute commands as the bot user.
This is needed for things like adding an avatar image.

- Make a Directory to keep your paper-key and bothome directory
`mkdire ~/Documents/mybot`
- Copy paper-key to your mybot directory
`cp paper-key ~/Documents/mybot/`
- Change to that directory
`cd ~/Documents/mybot`
- Copy paper-key to your clipboard
- Login With the paper-key and add a device. This will make the new bothome 
directory reusable for managing your bot moving forward
`keybase -home=./bothome login`
Select 1 for paper key
Paste your paper-key in the popup box.
Set a name for your current device like "dev-bothome-folder" 

### Set Bot Permissions
```
keybase chat edit-bot-member -u <botname> -r bot <team>
```

### Set Bot Avatar Image
Note: You have to have completed teh Setup Bot Home Directory Step First
```
keybase -home=~/mybot/bothome account upload-avatar <image-file>
```

## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/pastorhudson/keybase-bot-heroku/tree/master)

### Startup the Bot for local DEV

Next, start the service, logged in as the bot on startup:

```
$ keybase --home=/tmp/bot service --oneshot-username <botname> < paper-key
```

## Caveats

Only 5 bot signups per user are currently allowed, but we can consider relaxing that.
