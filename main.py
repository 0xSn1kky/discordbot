import discord
import time
from discord.ext import commands
import settings as cfg
import random as rand 

# Все настройки в settings.py
# Автор данного кода: 0xSn1kky
# Выдача кода за свой запрещено
# Разрешено использовать код только в собственных целях
# Если вы хотите выложить данный код то yкажите автора: 0xSn1kky
print("Автор кода: 0xSn1kky\n")

# Устанавливаем префикс
client = commands.Bot( command_prefix = cfg.prefix)

# Создаем текст в консоль когда бот зайдет в онлайн
@client.event
async def on_ready ():
    print("Бот Запущен!")
    print(f"""<Настройки (settings.py)>
    ¦Токен: {cfg.token}
    ¦ Префикс: {cfg.prefix}""") 
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f'{cfg.botname}, {cfg.prefix}помощь'))
   
# Команда bot
@client.command(pass_context=True)
async def bot (ctx):
    # В name пременную name будет указан юзернейм участника
    name = ctx.message.author
    # Сощдаем ответ .mention нужно чтобы участник был отмечен ботом
    await ctx.send(f"Привет {name.mention} Я здесь ✅")

@client.command(pass_context=True)
# Принимаем 2 параметра (кроме ctx) чтобы получить юзернеймы/имена
async def ship (ctx, p1, p2):
    await ctx.send(f"Совместимость {p1} и  {p2} ♥️")
    await ctx.send("Узнаю совместиммость подождите...")
    # Создаем паузу
    time.sleep(2)
    # Рандом от 1 до 100
    shipr = rand.randint(1, 100)
    await ctx.send(f"Совместимость равна {shipr}%")
        
@client.command(pass_context=True)
#Создаем чтобы команда была только длч администраторов
@commands.has_permissions(administrator = True)
async def clear (ctx, number = 100):
    # Отчищаем
    await ctx.channel.purge(limit = number)
    await ctx.channel.send(f"Было удалено: {number} сообщений")
    time.sleep(1)
    await ctx.channel.purge(limit=1)
  
# Я устал писать коментарии дальше.Мне лень учите python крч
@client.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def stop (ctx, code):
    try:
        if code == cfg.cdo:
            name = ctx.message.author
            await ctx.channel.purge(limit=1)
            await ctx.send("Бот был остановлен")
            exit(0)
    except:
        print(f"Бот был остановлен пользователем {name}")
        time.sleep(100)
        exit(0)

@client.command(pass_context=True)
async def random (ctx):
    randm = rand.randint(1, 5000)
    emb = discord.Embed(title="Рандом 💭", colour=discord.Color.blue(), description=f"Выпало число: {randm}")
    await ctx.send(embed=emb)
 
@client.command(pass_context=True)
async def duel(ctx, user):
    r = rand.SystemRandom().choice(["Вы выйграли ", "Вы проиграли"])
    await ctx.send(f"Дуэль с пользователем {user} началась...")
    await ctx.send("https://media.tenor.com/images/dd6318bbaebd9eb0a83893f6cb666fa2/tenor.gif")
    time.sleep(2)
    await ctx.send(f"🔥 Результаты дуэли: {r}")

@client.command(pass_context=True)
async def кнб (ctx, knb):
    await ctx.send(f"Вы выбрали: {knb}")
    knbb = rand.SystemRandom().choice(["Камень", "Ножницы", "Бумага"])
    await ctx.send(f"Бот выбрал: {knbb}")

@client.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def kick (ctx, member: discord.Member, *, reason = None):
    await member.kick(reason=reason)
    await ctx.channel.purge(limit=1)
    await ctx.send(f"Сейчас был кикнут пользователь: {member.mention} за нарушение правил! ⛔")
    print(f"Был кикнут {member}")
    
@client.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def ban (ctx, member: discord.Member, *, reason = "Без причины"):
    await member.ban (reason = reason)
    await ctx.channel.purge(limit=1)
    await ctx.send(f"Сейчас был забанен пользователь: {member.mention} \n Причина: {reason} ⛔")
    print(f"Был забанен пользователь {member} по причине {reason}")
  
  
@client.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def pardon (ctx, *, member):
    banned_users = await ctx.guild.bans()
    for banned in banned_users:
        user = ban_entry.user
        await ctx.guild.unban(user)
        await ctx.channel.purge(limit=1)
        await ctx.send(f"Сейчас был разбанен пользователь: {user.mention} 😁")
        print(f"Был разбанен пользователь {user}")

@client.command(pass_context=True)
async def invite(ctx):
    name = ctx.message.author
    await ctx.send(f"{name.mention} Я отправил тебе ссылку для приглашения бота в лс")
    time.sleep(0.9)
    await ctx.channel.purge(limit=2)
    await ctx.author.send(f"{name.mention} Вот ссылка 🔗 чтобы пригласить данного бота на сервер: {cfg.invitelink}")
 
# Я хз будет ли работать этот код (я его не тестил)   
@client.command(pass_text=True)
@commands.has_permissions(administrator = True)
async def banlist(ctx):
    bans = await ctx.guild.bans()
    for bans in banlist:
        await ctx.send(f"Все баны: {banlist}")




@client.command(pass_context=True)
async def cube(ctx, numv):
    num = int(numv)
    if num > 6:
        await ctx.send("Вы выбрали число больше 6 😔")
    else:
        cube = rand.randint(1, 6)
        await ctx.send(f"Вы выбрали число: {num}")
        await ctx.send("Кидаем кубик 🎲 ")
        time.sleep(3)
        await ctx.send(f"Выпало число: {cube} 🎲")
        if cube == num:
            await ctx.send("Вы выйграли 🎲✅")
        else:
            await ctx.send("Вы проиграли ❌🎲")
    
    
@client.command(pass_context=True)
async def помощь (ctx):
    p = cfg.prefix
    emb = discord.Embed(title="💭 Список команд 💭", colour=discord.Color.blue(), description=f"{p}bot - Узнать находиться ли бот в онлайне\n {p}ship - Зашиперить😍 \n {p}clear - отчистить чат (если не указать сколько сообщений хотите отчистить то отчистится 100)\n {p}stop - остановить бота (нужен специальный код) \n {p}random - рандомное число от 1 до 5000 \n {p}duel - Дуэль с пользователями \n {p}кнб - Камень, Ножницы, Бумага \n {p}kick - Кикнуть пользователя \n {p}ban - Забанить пользователя \ {p} pardon - разбанить пользователя \n {p}invite - добавть ботс на свой сервер \n {p}cube (число от 1 до 6) - Кинуть кубик 🎲 ")
    await ctx.send(embed=emb)

@client.command(pass_context=True)
async def codeauthor(ctx):
    await ctx.author.send("Создатель данного кода: 0xSn1kky")

client.run(cfg.token)