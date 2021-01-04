<p align="center">
  <img src="https://i.imgur.com/UkEq2V4.jpg" />
  <h1 align="center">Woof Buddy</h1>
</p>

## Table of Contents
* [Introduction](#introduction)
* [Features](#features)
* [Technologies](#technologies)
* [Setup](#setup)
* [Team](#team)
* [Contributing](#contributing)
* [Others](#others)

### Introduction
Woof buddy bot is a simple telegram bot that takes in an image of a dog as input and identifies its breed for output to the user. Note that this repository contains work pertaining only to the telegram bot for users to interact with. Work for the first iteration of the trained model was completed back in 2019 but was never uploaded nor made public. Further improvements/refinements are being carried out on the model this start of 2021 and the code for those will be available in a separate repository below:
```
https://github.com/tjtanjin/project_woof_model
```
Currently, a live version based on the old model is already available at the bot below:
```
https://t.me/woofbuddybot
```

### Features
Woof buddy bot was created to put to use an initial trained model for dog breed classification done back in 2019. The model first went live on the website below whose design was never fully completed (but is planned to be continued):
```
https://project-woof.herokuapp.com
```
It currently only supports images/telegram stickers as input and owing to a limited dataset, the accuracy sees significant areas for improvements. In lieu of that, a future release of this bot would see an option for users to verify the results returned by the model and should a dog be wrongly classified, prompt the user to advice on the correct breed of the dog. With the permission of the user, this image would be added to our dataset which would mean eventual potential growth!

### Technologies
Technologies used by Woof buddy bot are as below:
##### Done with:

<p align="center">
  <img height="150" width="150" src="https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png"/>
</p>
<p align="center">
Python
</p>

##### Deployed on:
<p align="center">
  <img height="150" width="150" src="https://i.dlpng.com/static/png/404295_thumb.png" />
</p>
<p align="center">
Digital Ocean
</p>

##### Project Repository
```
https://github.com/tjtanjin/woofbuddybot
```

### Setup
The following section will guide you through setting up your own woof buddy bot (telegram account required).
* First, head over to [BotFather](#https://t.me/BotFather) and create your own telegram bot with the /newbot command. After choosing an appropriate name and telegram handle for your bot, note down the bot token provided to you.
* Next, cd to the directory of where you wish to store the project and clone this repository. An example is provided below:
```
$ cd home/user/exampleuser/projects/
$ git clone https://github.com/tjtanjin/woofbuddybot.git
```
* Following which, create a token.json file under the config folder and save the token you received from [BotFather](#https://t.me/BotFather) as a value to the key "token" as shown below:
```
{"token": "your bot token here"}
```
Next, owing to the file size limit on github, you will have to create a models folder at the base of the project then manually download the [model](https://drive.google.com/file/d/1c37hpQVtazDhF73EgiuI89jD34XJvPmm/view?usp=sharing) and place it within this new folder.
* Finally, from the base directory of the project, execute the following command and the terminal should print "running..." if everything has been setup correctly!
```
$ python3 main.py
```

### Team
* [Tan Jin](https://github.com/tjtanjin)
* [Tan Ying Qi](https://github.com/yingqi98)

### Contributing
If you have code to contribute to the project, open a pull request and describe clearly the changes and what they are intended to do (enhancement, bug fixes etc). Alternatively, you may simply raise bugs or suggestions by opening an issue.

### Others
For any questions regarding the implementation of the project, please drop an email to: cjtanjin@gmail.com.
