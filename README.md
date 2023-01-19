# ⭐ THIS REPO HAS BEEN DEPRECATED ⭐
The development is still undergoing at
[Yor the discord bot](https://github.com/LynBean/Yor)

# Chat GPT in Discord!

Chat GPT is an artificial intelligence chatbot that can do, well, pretty much everything. It can code, it can write articles, it can solve most of your questions.

Today, this technology is now present in Discord thanks to my efforts!

## Features

All the features are only used by one command:

`/chat`

![introduction](https://user-images.githubusercontent.com/80762068/208718991-103ae23b-db69-4bd4-b7f4-bd44769bd455.gif)

![image](https://user-images.githubusercontent.com/80762068/208718928-48a01208-19f8-4f67-ae8e-e22c412c3b1f.gif)


### List of OPTIONAL parameters

* Ephemeral - The bot will send the message as a ephemeral message. Which means that the message only visible to the user who sent the command.

![ephemeral](https://user-images.githubusercontent.com/80762068/208716712-b11dd57b-5375-4579-95f1-0a1228e73bfc.gif)

* Engine - ID of the model to use.

* Frequency Penalty - Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.

* Max tokens - The maximum number of tokens to generate in the completion.
The token count of your prompt plus max_tokens cannot exceed the model's context length. Most models have a context length of 2048 tokens (except for the newest models, which support 4096).

* Presence Penalty - Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.

* Temperature - What sampling temperature to use. Higher values means the model will take more risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones with a well-defined answer. We generally recommend altering this or top_p but not both.

* Top P - An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend altering this or temperature but not both.

![parameter](https://user-images.githubusercontent.com/80762068/208720842-73be789b-27ef-4817-90d8-caa00fc410d3.gif)

## Installation
Before installation, make sure that you have Python >= 3.8 installed.

### Method 1:
```bash
# Download the repo, unzip it, and cd into the directory
$ python -m pip install -r requirements.txt

# Run the command under same directory as the source directory to execute the script
$ python .\main.py
```

### Method 2:
```bash
# It is recommended to use Administrator terminal to execute the following command to avoid any errors occur.
$ python -m pip install 'git+https://github.com/LynBean/chatgpt-in-discord@main'

# After installation completed, please restart your terminal. Then, open the termianl again and execute the following command.
$ chatgpt-in-discord.exe
```

## Getting Discord Bot Token
1. Goto this website https://discord.com/developers/applications.
2. Create an new application.
3. Go into the application section, under bot tab, create a bot.
4. Turn on MESSAGE CONTENT INTENT.

![image](https://user-images.githubusercontent.com/57824016/208707269-bb068b87-4918-4c48-aaab-e3decc1011e9.png)

5. Finally, copy the CLIENT SECRET and save it for later use.

![image](https://user-images.githubusercontent.com/57824016/208707883-978ef7a2-a21e-4637-9f8c-e43394198118.png)

## Getting OpenAI API Key
1. Goto this website https://beta.openai.com/account/api-keys.
2. Create a key and save it for later use.

![image](https://user-images.githubusercontent.com/57824016/208708354-50fc0cce-38ae-4682-b7d1-21049405cb6e.png)
