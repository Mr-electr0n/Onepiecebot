import discord
from discord.ext import commands
from discord.ui import View, Button
import asyncio

class Island(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.pages = [
            discord.Embed(
                title="Create your own island",
                description="Please fill in the following details to create your own island for the game",
                color=discord.Color.green()
            ),
            discord.Embed(
                title="Port",
                description="Do you want a port on your island?",
                color=discord.Color.green()
            ),
            discord.Embed(title="Market", description="Do you want a market on your island?", color=discord.Color.green()),
            discord.Embed(title="Town", description="Do you want a town on your island?", color=discord.Color.green()),
            discord.Embed(title="Fort", description="Do you want a fort on your island?", color=discord.Color.green()),
            discord.Embed(title="Theme", description="Choose what kind of atmosphere and style you want your island to have", color=discord.Color.green()),
            discord.Embed(title="Inhabitants", description="Describe what kind of people and creatures live on your island", color=discord.Color.green()),
            discord.Embed(title="Events", description="Describe what kind of events and quests happen on your island", color=discord.Color.green())
        ]

    @commands.command()
    async def island(self, ctx):
        class IslandMenuView(View):
            def __init__(self, pages):
                super().__init__()
                self.current_page = 0
                self.pages = pages

            async def show_page(self):
                embed = self.pages[self.current_page]
                await self.message.edit(content=None, embed=embed)

            @discord.ui.button(label="Back", style=discord.ButtonStyle.primary)
            async def previous_page(self, button: discord.ui.Button, interaction: discord.Interaction):
                self.current_page -= 1
                if self.current_page < 0:
                    self.current_page = len(self.pages) - 1
                await self.show_page()

            @discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
            async def next_page(self, button: discord.ui.Button, interaction: discord.Interaction):
                self.current_page += 1
                if self.current_page >= len(self.pages):
                    self.current_page = 0
                await self.show_page()

            @discord.ui.button(label="Yes", style=discord.ButtonStyle.primary)
            async def port_yes(self, button: discord.ui.Button, interaction: discord.Interaction):
                await interaction.response.edit_message(content="You selected 'Yes' for port.", embed=None, view=None)

            @discord.ui.button(label="No", style=discord.ButtonStyle.primary)
            async def port_no(self, button: discord.ui.Button, interaction: discord.Interaction):
                await interaction.response.edit_message(content="You selected 'No' for port.", embed=None, view=None)

        view = IslandMenuView(self.pages) # Create an instance of the IslandMenuView
        embed = self.pages[0]

        # Send the initial embed message to the channel with the interactive menu
        message = await ctx.send(embed=embed, view=view)
        view.message = message

    # Add more commands related to the island here
    @commands.command()
    async def testisland(self, ctx):
        embed = discord.Embed(
            title="Create your own island",
            description="Please fill in the following details to create your own island for the game",
            color=discord.Color.green()
        )

        # Add fields to the embed object
        embed.add_field(name="Name", value="Enter the name of your island", inline=False)
        embed.add_field(name="Type", value="Choose from desert, forest, snow, mountain, sky, underwater, etc.", inline=False)
        embed.add_field(name="Size", value="Choose a number from 1 to 10, where 1 is the smallest and 10 is the largest", inline=False)
        embed.add_field(name="Port", value="Do you want a port on your island? If yes, how big (1 to 5) and on what location (north, south, east, west, etc.)?", inline=False)
        embed.add_field(name="Market", value="Do you want a market on your island? If yes, how big (1 to 5) and on what location (north, south, east, west, etc.)?", inline=False)
        embed.add_field(name="Town", value="Do you want a town on your island? If yes, how big (1 to 5) and on what location (north, south, east, west, etc.)?", inline=False)
        embed.add_field(name="Fort", value="Do you want a fort on your island? If yes, how big (1 to 5) and on what location (north, south, east, west, etc.)?", inline=False)
        embed.add_field(name="Theme", value="Choose what kind of atmosphere and style you want your island to have, such as pirate, marine, ancient, modern, fantasy, etc.", inline=False)
        embed.add_field(name="Inhabitants", value="Describe what kind of people and creatures live on your island, such as humans, animals, monsters, etc.", inline=False)
        embed.add_field(name="Events", value="Describe what kind of events and quests happen on your island, such as battles, puzzles, mysteries, festivals, etc.", inline=False)

        # Send the initial embed message to the channel
        message = await ctx.send(embed=embed)

        # Wait for user input
        def check(m):
            return m.channel == ctx.channel and m.author == ctx.author

        try:
            user_input = await self.bot.wait_for("message", check=check, timeout=60)  # Adjust the timeout if needed
        except asyncio.TimeoutError:
            await ctx.send("You took too long to respond.")
            return

        # Process the user input
        await ctx.send(f"You entered: {user_input.content}")


async def setup(bot):
    await bot.add_cog(Island(bot))

    
        # Add more commands related to the island here
    
    