import discord
from discord.ext import commands
from map import  design_map,local_location
from database import collection_name , reserved_collection_name ,connection_string ,reserved_collection_name
from extra_function import add_parts_to_island as island




class start(commands.Cog):
    @commands.command()
    async def Start(self, ctx):
        await ctx.send('I am working fine')


    
    @commands.command()
    async def mapdata(self,ctx):
        island(server_id=ctx.guild.id)
        await ctx.send('Inserted successfully')        






    @commands.command()
    async def delete(self,ctx): 
        collection_name.delete_one({'_id':ctx.guild.id})



    @commands.command()
    async def test(self, ctx):
        ''' In this at moment we are trying to import  the server details and store it in mongo db collection '''

        # await ctx.send(server_boundries)
        # await ctx.send(latest_server_dict)


        # # Extract server coordinates
        # server_coordinates = {key: value for key, value in latest_server_dict.items() if "coordinate" in key}

        # # Construct the server_boundaries dictionary
        # server_boundaries = {
        #     key: value for key, value in latest_server_dict.items() if "bound" in key
        # }

        # Construct the server_info dictionary
        server_info = {
            "_id": ctx.guild.id,
            "guild_id": ctx.guild.id,
            "guild_name": ctx.guild.name,
            "guild_pfp": str(ctx.guild.icon.url) if ctx.guild.icon else None,
            "owner_id": ctx.guild.owner_id,
            # Add other fields if needed
        }

        # await ctx.send(server_info)

        # # Update or insert server information in the database
        collection_name.insert_one(server_info)
        
        
        await ctx.send('Inserted successfully')







    @commands.command()
    async def mapt(self , ctx):
        design_map(server_id=ctx.guild.id)
        # with open('E:\\ONEPIECEBOT\\IMAGES\\image_with_colored_lines.png', 'rb') as file:
        #     await ctx.send(file=discord.File(file, 'merged_image.png'))
    
    @commands.command()
    async def local_location(self,ctx,setts):
        local_location(int(setts))
        await ctx.send(f"{setts} local location added")


async def setup(bot):
    await bot.add_cog(start(bot))