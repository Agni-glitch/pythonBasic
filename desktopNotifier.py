import asyncio
import time
# import signal

# from desktop_notifier import DesktopNotifier
# notifier = DesktopNotifier()

# async def main():
#     await notifier.send(title="Hello world!", message="Sent from Python")

# asyncio.run(main())


from desktop_notifier import DesktopNotifier, Urgency, Button, ReplyField, DEFAULT_SOUND
async def main() -> None:
    while True:
        time.sleep(20)
        notifier = DesktopNotifier(
            app_name="Your AI",
            notification_limit=10,
        )
        await notifier.send(
            title="message from AI",
            message="ask me any thing?",
            urgency=Urgency.Critical,
            buttons=[
                Button(
                    title="Mark as read",
                    on_pressed=lambda: print("Marked as read"),
                )
            ],
            reply_field=ReplyField(
                on_replied=lambda text: print("Brutus replied:", text),
            ),
            on_clicked=lambda: print("Notification clicked"),
            on_dismissed=lambda: print("Notification dismissed"),
            sound=DEFAULT_SOUND,
        )
try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Program interrupted by user")