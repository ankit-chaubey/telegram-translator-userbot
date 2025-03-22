from telethon import TelegramClient, events
from googletrans import Translator

api_id = "YOUR_API_ID"
api_hash = "YOUR_API_HASH"

client = TelegramClient("session", api_id, api_hash)
translator = Translator()

@client.on(events.NewMessage(pattern=r'\.t-([a-z]{2,5}) (.+)', outgoing=True))
async def autodetect_and_translate(event):
    target_lang = event.pattern_match.group(1)
    text = event.pattern_match.group(2)
    translated = await translator.translate(text, src='auto', dest=target_lang)
    await event.edit(f"{translated.text}")

@client.on(events.NewMessage(pattern=r'\.t-([a-z]{2,5}):([a-z]{2,5}) (.+)', outgoing=True))
async def translate_with_source(event):
    source_lang = event.pattern_match.group(1)
    target_lang = event.pattern_match.group(2)
    text = event.pattern_match.group(3)

    full_text = '\n'.join(event.raw_text.splitlines()[1:])

    translated = await translator.translate(full_text, src=source_lang, dest=target_lang)
    await event.edit(f"{translated.text}")

client.start()
client.run_until_disconnected()
