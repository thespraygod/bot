from discord.ext import commands
client = commands.Bot(command_prefix="!")
token = "NzYyMzQ5NDU5MTExMDE4NTQ4.X3n3Qg.SuGY85g0KtgTq-qJos8XFIGnH6Q"


@client.event
async def on_message(message):
    if message.content.startswith("!news"):
        news = "https://edition.cnn.com/2020/10/03/us/california-wildfires-saturday/index.html"
        date = "October 3,2020"
        await message.channel.send(news)
        await message.channel.send(f"```Last updated:{date}```")
    elif message.content.startswith("!stats"):
        carbon_val = 417.16
        temperature = 2
        percentage = 12.85
        mass = 427
        length_val = 3.3
        source_link = "https://climate.nasa.gov"
        date = "May, 2020"
        await message.channel.send(f"```{carbon_val} particles per million``````Global temperature increased by: {temperature}°C``````Arctic ice decreasement percentage:{percentage}%``````Ice sheet decreasement by {mass} gigatones``````Sea level increased by {length_val} milimeters```\n")
        await message.channel.send("```-----------------------------------```")
        await message.channel.send(f"```Last updated:{date}```")
        await message.channel.send(f"```Updated from: {source_link}```")


client.run(token)
