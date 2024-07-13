# src/widget.py

from masks import mask_card, mask_account


def mask_account_card(info: str) -> str:
    if info.startswith("Счет"):
        return f"Счет {mask_account(info.split()[1])}"
    else:
        card_type, card_number = info.rsplit(' ', 1)
        return f"{card_type} {mask_card(card_number)}"
