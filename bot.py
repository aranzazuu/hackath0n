import discord
from model import get_class
from discord.ext import commands
import random as r

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="Bienvenido a la alpha de ECOSORT",
        description=("Recuerda que esta no va a ser la apariencia final del proyecto, todo va a cambiar para bien y mejorar. "
                     "Ahora con esto claro, esto es lo que tiene el bot por ahora:\n\n"
                     "**1.** Distinción entre latas y cartón con el comando `$check` y colocar tu foto o imagen.\n"
                     "**2.** Artículos de reciclaje con el comando `$recyclinginfo`.\n"
                     "**3.** maneras de ayudar con el comando `$como_puedo_ayudar`.\n"
                     "**4.** Datos curiosos sobre reciclar con el comando `$funfacts`."),
        color=discord.Color.green()
    )
    
    await ctx.send(embed=embed)

articulos_de_reciclaje = ("https://www.ecolatras.es/blog/reciclaje", "https://www.nationalgeographicla.com/medio-ambiente/2023/05/que-beneficios-nos-trae-el-reciclaje-5-datos-que-necesitas-saber", "https://espanol.epa.gov/espanol/el-reciclaje")

@bot.command()
async def recyclinginfo(ctx):
    await ctx.send(f"hola que tal? aqui te dejo un articulo interesante sobre el reciclaje! {r.choice(articulos_de_reciclaje)}")

datos_curiosos_reciclaje = (
    "El reciclaje de una lata de aluminio puede ahorrar suficiente energía para hacer funcionar un televisor durante 3 horas.",
    "El vidrio es 100 por ciento reciclable y puede ser reciclado infinitamente sin perder calidad o pureza.",
    "El reciclaje de una tonelada de papel puede salvar 17 árboles y 26,500 litros de agua.",
    "El reciclaje de plástico puede ahorrar hasta dos tercios de la energía necesaria para producir plástico nuevo.",
    "Reciclar una tonelada de aluminio puede ahorrar hasta 14,000 kilovatios hora de energía.",
    "El 90 por ciento del papel reciclado se utiliza para fabricar nuevos productos de papel.",
    "El reciclaje de una sola botella de vidrio puede ahorrar suficiente energía para iluminar una bombilla de 100 vatios durante 4 horas.",
    "Los neumáticos reciclados pueden ser utilizados para hacer asfalto para carreteras.",
    "Reciclar una tonelada de acero ahorra 1,100 kg de mineral de hierro y 630 kg de carbón.",
    "El plástico reciclado puede convertirse en ropa, muebles de jardín e incluso en nuevas botellas de plástico.",
    "El aluminio reciclado se puede transformar en latas, láminas de aluminio y piezas para aviones.",
    "El reciclaje de papel reduce la contaminación del agua en un 35% y la del aire en un 74%.",
    "El reciclaje de una tonelada de vidrio ahorra más de una tonelada de recursos naturales.",
    "Cada tonelada de papel reciclado ahorra el equivalente a 4,000 kilovatios hora de electricidad.",
    "El reciclaje de metales ahorra hasta un 95 por ciento de la energía necesaria para producir nuevos metales.",
    "Los productos electrónicos reciclados pueden recuperar metales preciosos como oro, plata y platino.",
    "El reciclaje de una tonelada de plástico ahorra hasta 7,200 kilovatios hora de electricidad.",
    "Los contenedores de vidrio reciclado se pueden reutilizar para almacenar alimentos y bebidas sin pérdida de calidad.",
    "Reciclar una tonelada de cartón puede ahorrar más de 200 litros de petróleo.",
    "El reciclaje ayuda a reducir la cantidad de desechos en los vertederos, lo que a su vez reduce la emisión de gases de efecto invernadero."
)

recycling_tips = (
    "Separar los residuos en orgánicos e inorgánicos.",
    "Utilizar productos reutilizables en lugar de desechables.",
    "Reciclar papel, vidrio, plástico y metal.",
    "Evitar el uso de plásticos de un solo uso.",
    "Reducir el consumo de energía apagando luces y electrodomésticos.",
    "Comprar productos con menos embalaje.",
    "Reutilizar recipientes de vidrio y plástico.",
    "Donar ropa y objetos en lugar de tirarlos.",
    "Usar bolsas de tela en lugar de bolsas plásticas.",
    "Instalar bombillas de bajo consumo energético.",
    "Utilizar el transporte público o compartir coche.",
    "Compostar los residuos orgánicos.",
    "Participar en programas de reciclaje comunitarios.",
    "Evitar imprimir documentos innecesarios.",
    "Comprar productos locales y de temporada.",
    "Utilizar botellas reutilizables para el agua.",
    "Recoger basura en áreas públicas.",
    "Plantar árboles y plantas en el hogar.",
    "Reducir el uso de productos químicos en la limpieza.",
    "Difundir información sobre prácticas de reciclaje y sostenibilidad."
)

@bot.command()
async def funfacts(ctx):
    await ctx.send(f"Sabias que...  {r.choice(datos_curiosos_reciclaje)}")

@bot.command()
async def como_puedo_ayudar(ctx):
    await ctx.send(f"puedes ayudar: {r.choice(recycling_tips)}")


@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{file_name}")
            await ctx.send(f"Imagen guardada en ./{file_url}")
            try:
                clase = get_class(model_path = "keras_model.h5", labels_path = "labels.txt", image_path = f"./{file_name}"  )
                if clase[0] == "carton":
                    await ctx.send("Es carton, este tipo de basura va en los botes de color blanco")
                elif clase[0] == "latas":
                    await ctx.send("Son latas, este tipo de basura va en los botes de color blanco")
            except:
                await ctx.send("No se pudo identificar la imagen")
    else:
        await ctx.send("No subiste una imagen :(")

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("token")