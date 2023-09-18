# ohke so in this file we are first making a users profile 
import discord
from discord.ext import commands
from database import collection_name , reserved_collection_name ,connection_string , profile_data





class Setup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def Set(self, ctx):
        user = ctx.author
        user_info = {
            '_id': user.id,
            'user_name' : user.name,

        }
        
        profile_data.insert_one(user_info)
        

        await ctx.send('Your profile has been made')


    # Import discord and commands modules

# Define a command called island



async def setup(bot):
    await bot.add_cog(Setup(bot))