import json
import requests
import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import io
import time


bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help

@bot.command()
async def Skin(ctx, *, SkinMinecraft):
    await ctx.message.delete()
    await ctx.send(f"Generando Skin {SkinMinecraft}...", delete_after=0)
    time.sleep(3)
   
   
    url = f"https://jose89fcb.es/minecraft/3D/skin/CabezonMinecraft/p/skins/CabezonMinecraft.php?usuario={SkinMinecraft}"
    imagen = Image.open(io.BytesIO(requests.get(url).content))
    r = requests.get(url)
    if  r.status_code ==200:
        imagen = Image.open(io.BytesIO(requests.get(url).content))
        with io.BytesIO() as imagen_binary:
            imagen.save(imagen_binary, 'PNG')
            imagen_binary.seek(0)
            embed=discord.Embed(title="Skin Minecraft", url="https://jose89fcb.es", description=f"Skin - {SkinMinecraft}")
    
            embed.set_image(url=f"attachment://Skin-{SkinMinecraft}.png")
            embed.set_footer(text="BOT Programado Por Jose89fcb")
            await ctx.send(embed=embed, file=discord.File(fp=imagen_binary, filename=f"Skin-{SkinMinecraft}.png"))
    else:
        await ctx.send(f":(")


@skin.error
async def skin_error(ctx, error):
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send("La skin no existe!")        


   



@bot.event
async def on_ready():
    print("BOT listo!")
    
bot.run('') 
