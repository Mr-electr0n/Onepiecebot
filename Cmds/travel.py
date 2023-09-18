import discord
from discord.ext import commands
import asyncio
from database import collection_name 
import requests
from io import BytesIO

class Travel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.available_servers = {}  # Dictionary to store server options and IDs

    @commands.command()
    async def travel(self, ctx):
        # Check if the user has the required role in the current server
        await ctx.send(f"Hello {ctx.author}")

        # Create an embed message
        embed = discord.Embed(
            title="Server Map",
            description="Here's the map of the server:",
            color=discord.Color.blue()
        )

        # Fetch the image from the URL using requests
        image_url = "https://i.ibb.co/HCCB9kB/image-with-colored-lines.png"
        image_response = requests.get(image_url)

        # Check if the image was fetched successfully
        if image_response.status_code == 200:
            # Convert the image response content to bytes
            image_bytes = BytesIO(image_response.content)

            # Add the image to the embed
            embed.set_image(url=image_url)

            # Create a view class with buttons
            class ButtonView(discord.ui.View):
                def __init__(self):
                    super().__init__()

                @discord.ui.button(label="1", style=discord.ButtonStyle.primary)
                async def button_1(self, button, interaction):
                    await interaction.response.edit_message(content="You clicked button 1", embed=embed)

                @discord.ui.button(label="2", style=discord.ButtonStyle.primary)
                async def button_2(self, button, interaction):
                    await interaction.response.edit_message(content="You clicked button 2", embed=embed)

                @discord.ui.button(label="3", style=discord.ButtonStyle.primary)
                async def button_3(self, button, interaction):
                    await interaction.response.edit_message(content="You clicked button 3", embed=embed)

                @discord.ui.button(label="4", style=discord.ButtonStyle.primary)
                async def button_4(self, button, interaction):
                    await interaction.response.edit_message(content="You clicked button 4", embed=embed)

            # Create a view object
            view = ButtonView()

            # Send the embed with the view
            await ctx.send(embed=embed, view=view)
        else:
            await ctx.send("Failed to fetch the image.")


async def setup(bot):
    await bot.add_cog(Travel(bot))


















# I'm glad you want to use MongoDB GridFS to store and retrieve images for your discord bot. MongoDB GridFS is a specification for storing and retrieving files that exceed the BSON-document size limit of 16 MB. GridFS divides a file into chunks and stores each chunk as a separate document. You can use the PyMongo library to access GridFS from your python application. Here are some details and a sample code for using GridFS with python:

# - To use GridFS, you need to import the PyMongo and GridFS modules, and create a MongoClient object to connect to your MongoDB Atlas cluster. You also need to create a GridFS object with the database name that you want to use for storing your files. For example:

# ```python
# from pymongo import MongoClient
# import gridfs

# # Replace the connection string with your own
# client = MongoClient("mongodb+srv://<username>:<password>@<cluster-url>/test?retryWrites=true&w=majority")
# db = client.gridfs_example # The database name
# fs = gridfs.GridFS(db) # The GridFS object
# ```

# - To upload an image to GridFS, you can use the `put()` method of the GridFS object. This method takes a file-like object (an object with a `read()` method) or a bytes object as an argument, and returns the `_id` of the file document. You can also pass additional keyword arguments to store metadata along with the file. For example:

# ```python
# # Upload an image from a local file
# with open("image.jpg", "rb") as f:
#     image_id = fs.put(f, filename="image.jpg", content_type="image/jpeg")

# # Upload an image from a bytes object
# image_data = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01\x00\x00\x00..."
# image_id = fs.put(image_data, filename="image.png", content_type="image/png")
# ```

# - To retrieve an image from GridFS, you can use the `get()` method of the GridFS object. This method takes the `_id` of the file document as an argument, and returns a file-like object that you can read from. You can also access the metadata of the file by using dot notation on the file-like object. For example:

# ```python
# # Retrieve an image by its _id
# image_file = fs.get(image_id)
# image_data = image_file.read()
# print(image_file.filename)
# print(image_file.content_type)

# # Retrieve an image by its filename
# image_file = fs.find_one({"filename": "image.jpg"})
# image_data = image_file.read()
# print(image_file._id)
# print(image_file.content_type)
# ```

# - To delete an image from GridFS, you can use the `delete()` method of the GridFS object. This method takes the `_id` of the file document as an argument, and removes the file and its chunks from the database. For example:

# ```python
# # Delete an image by its _id
# fs.delete(image_id)
# ```

# You can find more information and examples about using GridFS with python in this web article: [GridFS Example - PyMongo 4.4.1 documentation](^1^).

# I hope this helps you with your project. If you have any other questions, feel free to ask me. I'm always happy to chat with you. 😊

# Source: Conversation with Bing, 8/18/2023
# (1) GridFS Example - PyMongo 4.4.1 documentation - Read the Docs. https://pymongo.readthedocs.io/en/stable/examples/gridfs.html.
# (2) GridFS Example — PyMongo 3.4.0 documentation. https://api.mongodb.com/python/3.4.0/examples/gridfs.html.
# (3) GridFS Example — PyMongo v1.8 documentation. https://api.mongodb.com/python/1.8/examples/gridfs.html.














        # required_role = "Traveler"  # Replace "Traveler" with the name of the required role
        # if not any(role.name == required_role for role in ctx.author.roles):
        #     await ctx.send(f"You need the {required_role} role to use this command.")
        #     return
 
        # # Fetch the available servers from the server_info collection in MongoDB
        # self.available_servers = {}  # Reset the dictionary
        # for idx, server_info in enumerate(collection_name.find(), 1):
        #     # print(f"server_info: {server_info}")
        #     if str(server_info["_id"]) != str(ctx.guild.id):
        #         self.available_servers[str(idx)] = server_info

        # # Prepare the embed with the list of available servers
        # embed = discord.Embed(title="Available Servers", description="", color=discord.Color.green())

        # # Add an image to the embed (replace 'image_url_here' with the actual URL of the image)
        # # file = discord.File("E:\\ONEPIECEBOT\\IMAGES\\resized_rotated_image.png", filename="image.png")
        # # uploaded_file = await ctx.channel.send(file=file)
        # image_url = 'https://cdn.discordapp.com/attachments/1130106361573810306/1137358271221604373/image.png'
        # embed.set_image(url=image_url)

        # for idx, server_info in self.available_servers.items():
        #     if isinstance(server_info, dict) and 'guild_name' in server_info:
        #         embed.description += f"{idx}. {server_info['guild_name']}\n"
        #     else:
        #         embed.description += f"{idx}. Unknown Guild\n"

        # # Send the embed to the user with the available server list
        # message = await ctx.send(embed=embed)

        # # Add reactions to the message for each server option
        # for idx in range(1, len(self.available_servers) + 1):
        #     await message.add_reaction(f"{idx}\N{COMBINING ENCLOSING KEYCAP}")

        # # Wait for the user's reaction (server selection)
        # def check(reaction, user):
        #     return user == ctx.author and str(reaction.emoji) in [f"{idx}\N{COMBINING ENCLOSING KEYCAP}" for idx in self.available_servers.keys()]

        # try:
        #     reaction, _ = await self.bot.wait_for("reaction_add", check=check, timeout=60)

        #     # Get the selected index from the reaction
        #     selected_idx = reaction.emoji[0]

        #     # Check if the selected index is in the available server keys
        #     if selected_idx in self.available_servers:
        #         selected_server = self.available_servers[selected_idx]
        #         guild = self.bot.get_guild(selected_server['_id'])
        #         if guild:
        #             invite = await guild.text_channels[0].create_invite()  # Create an invite link
        #             await ctx.author.send(f"You have joined {guild.name}! Here is the invite link: {invite.url}")
        #         else:
        #             await ctx.send("Failed to join the selected server.")
        #     else:
        #         await ctx.send("Invalid selection. Please try again.")
        # except asyncio.TimeoutError:
        #     await ctx.send("Reaction timeout. Please try again.")
