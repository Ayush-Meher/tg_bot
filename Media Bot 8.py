from telethon import TelegramClient, events
import json
import asyncio

api_id = 29505484
api_hash = "3c19e77988e864ca800b127f582c3f21"
phone_number = "+6282196104451"
filename = "C:\\Users\\ayush\\ayush backup\\Ayush Backup\\Programs\\Program\\Telegram Bot\\Media Message Bot (Spanish)\\replied_users_mike.json"
video_path = "C:\\Users\\ayush\\ayush backup\\Ayush Backup\\Programs\\Program\\Telegram Bot\\Media Message Bot (Spanish)\\Vid.mp4"

client = TelegramClient("session_mike", api_id, api_hash)

group_ids = (1001660783909, 1001685280773, 1001521452479, 1001199203323, 1001605910397)

message = (
    "Hola\n\n"
    "¿Te gustaría potenciar tu perfil de Instagram?\n\n"
    "Puedo ayudarte a aumentar los Me gusta de los seguidores, etc.\n\n"
    r"Nuestros servicios son 100% seguros y genuinos."
    "\n\nLos seguidores de Instagram comienzan desde solo 3 dólares por 1000 seguidores\n\n "
    "Si está interesado, envíeme un mensaje.\n\n"
    "Nota: Se aceptan pagos a través de PayPal, tarjeta de crédito/débito y criptomonedas.\n\n"
    "Que tenga un buen día"
)

try:
    with open(filename, "r") as file:
        replied_users_id = json.load(file)
except FileNotFoundError:
    replied_users_id = []

@client.on(events.NewMessage(chats=group_ids))
async def handle_new_message(event):
    user_id = event.message.sender_id
    user_name = event.message.sender.first_name
    if user_id not in replied_users_id:
        try: 
            await event.respond(video_path, caption=message)
        except:
            await event.message.reply(message)
        print(f"Sent message to {user_name} ({user_id}) in group {event.chat_id}")
        replied_users_id.append(user_id)

        with open(filename, "w") as file:
            json.dump(replied_users_id, file)
        
        #Delay
        await asyncio.sleep(120)

if __name__ == "__main__":
    client.start(phone_number)
    client.run_until_disconnected()
