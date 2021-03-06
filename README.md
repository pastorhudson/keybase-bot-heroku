# keybase-bot-heroku
This is a simple starter bot for launching a keybase bot on Heroku or Dokku

### Setup:

### 1 Get a Bot Token

As your keybase user run:

```
$ keybase bot token create > /tmp/bot-token
```

You'll get back a base64 token, like: `6C37sjCBgMNf06Z6oTgixIxHJpja8G-Qp`. This is your *bot token* that allows you to sign up bots.

### 2 Signup the Bot

Here we use *standalone* mode which means the service and the client run in the same process, and then both exit
at the same time. It won't actually write any credentials to that directory, but we give it a non-standard home directory
in this example so we don't pick up your real user.

```
$ keybase --standalone --home=/tmp/bot bot signup -u <botname> -t $(cat /tmp/bot-token) > paper-key
```

This will output a paper key to standard output.
It is a paper key, and not standard device keys.

### 3 Setup Bot Home Directory and Device IMPORTANT

Keybase runs as your logged in user so if you want to run commands as your bot you need a directory setup fornyour bot's keybase profile. Once we setup this directory you can run keybase commands as your bot with `keybase -home=<directory>`

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
Paste your paper-key we generated in Step 2 in the popup box.
Set a name for your current device like "dev-bothome-folder" 

### 4 Set Bot Permissions

This tells keybase who can use your bot.
```
keybase chat edit-bot-member -u <botname> -r bot <team>
```

### 5 Set Bot Avatar Image
Note: You have to have completed Step 3 for this to work.
```
keybase -home=~/mybot/bothome account upload-avatar <image-file>
```

## 6 Deploy To Heroku
You will need 2 things to deploy
- Your Paper Key
- Your Bot Name
- Optional: Bot Alias

If you have these ready then click the button below!

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/pastorhudson/keybase-bot-heroku/tree/main)

## 7 Try Your Bot
Use the `!update` command to cause the bot to update the alias, and advertize the commands.
These are the included commands to get you started:
- `!test` Responds "I'm ALIVE!"
- `!joke` Tells a joke from pyjoke
- `!help` Prints out the commands it can do
- `!update` Updates the commands advertised for the bot. 
This is very important! If you add a bot to a team and select "Restricted Bot" 
then the bot has to advertise it's bot commands so keybase knows which messages to encrypt with the bot's keys.

### Startup the Bot for local DEV

You need to run the Keybase service locally if you want to run bot.py

```
$ keybase --home=/tmp/bot service --oneshot-username <botname> < paper-key
```
Install Requirements
`pip install -r requirements.txt`

You'll also need to setup the same environment variables we need for Heroku or bot.py will fail.

Run the bot:
`python3 bot.py`

## Caveats

Only 5 bot signups per user are currently allowed, but we can consider relaxing that.
