from telegram_notifier import send_message
from surebet_finder import find_surebets
from config import get_config

def main():
    config = get_config()
    surebets = find_surebets(config)
    for match in surebets:
        send_message(match)

if __name__ == "__main__":
    main()
