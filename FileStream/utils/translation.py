from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from FileStream.config import Telegram

class LANG(object):

    START_TEXT = """
<b>👋🏻 Hello, </b>{}\n\nI can provide stream links for Telegram files without the necessity of waiting for the download to complete.
With the ability to store files.\n\nI will also work on channels and groups."""

    HELP_TEXT = """
<b>⁉️ How To Use:</b>

• Just send me any document or media, and I will provide the streamable link with those options:
- Download link
- Watch link
- Shareable link
• You can also revoke the file if you want
• I can also store files. Just use /files to get the files you have sent to me

<b>💭 In Channel/Chat</b>
• Just add me to channel/chat,
that's it, I will add the file link in the message ad button

<b>⚠️ Note:</b> 🔞 Contents strictly prohibited</b>

🐞 Report Bugs At Support. <a href='https://telegram.me/anocy'>Owner</a>"""

    ABOUT_TEXT = """
<b>🤖 Bot Name :</b>{}\n
<b>- Version :</b> {}
<b>- Last Updated :</b> 31-January-2024
<b>- Developer:</b> <a href='https://telegram.me/Anocy'>Anocy</a>\n
"""

    STREAM_TEXT = """
<b>Your Link Generated !</b>\n
<b>📂 File Name :</b> <b>{}</b>\n
<b>📦 File Size :</b> <code>{}</code>\n
<b>📥 Download :</b> <code>{}</code>\n
<b>🖥 Watch :</b> <code>{}</code>\n
<b>🔗 Stream :</b> <code>{}</code>\n"""

    STREAM_TEXT_X = """
<b>Your Link Generated !</b>\n
<b>📂 File Name :</b> <b>{}</b>\n
<b>📦 File Size :</b> <code>{}</code>\n
<b>📥 Download :</b> <code>{}</code>\n
<b>🔗 Stream :</b> <code>{}</code>\n"""


    BAN_TEXT = "__Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ.__\n\n**[Cᴏɴᴛᴀᴄᴛ Dᴇᴠᴇʟᴏᴘᴇʀ](tg://user?id={}) Tʜᴇʏ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**"


class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⚙️ Help', callback_data='help'),
            InlineKeyboardButton('🤖 About', callback_data='about')
        ],
            [InlineKeyboardButton("📣 Updates Channel", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⚡️ Home', callback_data='home'),
            InlineKeyboardButton('🤖 About', callback_data='about'),
        ],
            [InlineKeyboardButton("📣 Updates Channel", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⚡️ Home', callback_data='home'),
            InlineKeyboardButton('⚙️ Help', callback_data='help'),
        ],
            [InlineKeyboardButton("📣 Updates Channel", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
