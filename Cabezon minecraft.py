import json
import requests
import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import io
import time
import os
import urllib.request

bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help

@bot.command()
async def Skin(ctx, *, SkinMinecraft):
   
    response = requests.get(f"https://jose89fcb.es/minecraft/3D/skin/CabezonMinecraft/p/skins/skin.php?cabezon={SkinMinecraft}")
    imagen = response.json()['CabezonMinecraft']

    url_imagen = f"{imagen}"
    
    nombre_local_imagen = f"Skin-{SkinMinecraft}.png"
    
    
    imagen = requests.get(url_imagen).content


    
   
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)


    skin = imagen
    # cargo la imagen desde la memoria
    img1 = Image.open(io.BytesIO(requests.get(url_imagen).content)).convert("RGBA")

   



    

    
    
   
    


    
    
 

    
    

    with io.BytesIO() as image_binary:
       

        img1.save(image_binary, 'PNG')
        
       
         
        image_binary.seek(0)
        
       
  
        embed = discord.Embed(title=f"{SkinMinecraft}", description=f"{SkinMinecraft}", color=discord.Colour.random()) 
        
       
   

        embed.set_image(url=f"attachment://Skin-{SkinMinecraft}.png")
        await ctx.send(embed=embed, file=discord.File(fp=image_binary, filename=f"Skin-{SkinMinecraft}.png"))
        os.remove(f"Skin-{SkinMinecraft}.png")
       
   


        

   



@bot.event
async def on_ready():
    print("BOT listo!")
    
bot.run('') #OBTEN UN TOKEN EN: https://discord.com/developers/application