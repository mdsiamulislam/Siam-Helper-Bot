# Siam Helper Bot

Siam Helper Bot is a custom Telegram bot that allows users to add, remove, and manage text filters. The bot responds to specific keywords and provides predefined responses. Additionally, users can interact with the bot via clickable buttons to view filters and responses.

## Features

- Add custom filters with a keyword and response.
- Remove existing filters.
- List all available filters with clickable buttons.
- Handles group messages and responds based on filters.
- Simple command structure for easy interaction.

## Commands

- `/start` - Starts the bot and welcomes the user.
- `/help` - Shows a list of available commands.
- `/add_filter <key> <response>` - Adds a new filter. `<key>` is the keyword to trigger the response, and `<response>` is the message to reply with.
- `/remove_filter <key>` - Removes a filter by its keyword.
- `/list_filters` - Lists all filters with clickable buttons to show the responses.

## Installation and Setup

1. Clone the repository or download the code:

   ```bash
   git clone https://github.com/mdsiamulislam/siam_helper_bot.git
   cd siam_helper_bot
   ```

2. Install the required dependencies:

   ```bash
   pip install python-telegram-bot
   ```

3. Replace the `TOKEN` variable with your own bot's token in the code:

   ```python
   TOKEN: Final = 'YOUR_BOT_TOKEN'
   ```

4. Run the bot:

   ```bash
   python bot.py
   ```

## Usage

Once the bot is running, you can interact with it via Telegram using the commands mentioned above.

### Example

- Add a new filter:
  ```
  /add_filter hello Hi there! How can I help you?
  ```
- Remove a filter:
  ```
  /remove_filter hello
  ```
- List filters and click on any filter to see the response:
  ```
  /list_filters
  ```

## Contributing

Feel free to fork the repository, make your changes, and submit a pull request. Contributions are welcome!
