from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import time

# Dictionary to keep track of user claims
user_claims = {}

# Define the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome! Use /claim to claim your coin daily, weekly, or monthly.')

# Define the /claim command
def claim(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    current_time = time.time()  # Get current time in seconds

    if user_id not in user_claims:
        user_claims[user_id] = {'daily': 0, 'weekly': 0, 'monthly': 0}

    # Check claim type
    if not context.args or len(context.args) != 1:
        update.message.reply_text('Please specify the claim type: daily, weekly, or monthly.')
        return

    claim_type = context.args[0].lower()

    if claim_type == 'daily':
        last_claim_time = user_claims[user_id]['daily']
        if current_time - last_claim_time >= 86400:  # 86400 seconds in a day
            user_claims[user_id]['daily'] = current_time
            update.message.reply_text('You have successfully claimed your daily coin!')
        else:
            update.message.reply_text('You can only claim daily coins once every 24 hours.')

    elif claim_type == 'weekly':
        last_claim_time = user_claims[user_id]['weekly']
        if current_time - last_claim_time >= 604800:  # 604800 seconds in a week
            user_claims[user_id]['weekly'] = current_time
            update.message.reply_text('You have successfully claimed your weekly coin!')
        else:
            update.message.reply_text('You can only claim weekly coins once every 7 days.')

    elif claim_type == 'monthly':
        last_claim_time = user_claims[user_id]['monthly']
        if current_time - last_claim_time >= 2592000:  # 2592000 seconds in a month
            user_claims[user_id]['monthly'] = current_time
            update.message.reply_text('You have successfully claimed your monthly coin!')
        else:
            update.message.reply_text('You can only claim monthly coins once every 30 days.')
    else:
        update.message.reply_text('Invalid claim type. Use daily, weekly, or monthly.')

def main():
    # Replace 'YOUR_TOKEN' with your bot's API token
    updater = Updater("YOUR_TOKEN")

    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("claim", claim))

    # Start the bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
