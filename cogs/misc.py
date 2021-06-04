from discord.ext import commands
import discord

import tools


class Misc(commands.Cog):
    """Random commands for the bot"""

    def __init__(self, bot):
        self.bot = bot
        self.database = bot.database

    @commands.command(name='invite', aliases=["getinvite", "botinvite"],
                      usage="invite", description="Invite the bot to your own server")
    @tools.has_perm()
    async def invite(self, ctx):
        await ctx.send(
            "You can invite me here: https://discord.com/oauth2/authorize?client_id=809122042573357106&permissions=8&scope=bot%20applications.commands")

    @commands.command(name="credit", description="Get the names of the people who developed the bot", usage="credit")
    async def credit(self, ctx):
        embed = discord.Embed(colour=0x36a39f, title="The list of contributors",
                              description="FluxedScript\nPatPatFred\nBlaze\nMark")
        embed.set_footer(text="Ploxy | Contributor list")
        await ctx.send(embed=embed)

    @commands.command(name="repo", description="Get the bot's repository", usage="repo")
    async def credit(self, ctx):
        await ctx.send("You can find me here: https://github.com/PloxHost-LLC/community-bot")

    @commands.command(name="permcheck", description="Check if the bot has permissions needed", usage="permcheck")
    async def permcheck(self, ctx):
        bot_user: discord.Member
        bot_user = ctx.guild.me
        permissions = bot_user.guild_permissions

        def check_perm(perm):
            for bot_perm in permissions:
                if perm == bot_perm[0] and bot_perm[1]:
                    return "✅"
            return "❌"

        embed = discord.Embed(colour=0x36a39f, title="Permissions check",
                              description="Ensure all of these have ✅ unless you know what you are doing.")
        embed.add_field(name=f"Administrator {check_perm('administrator')}",
                        value="If enabled, the rest of permissions don't matter. Allows the bot to function without needing to check this command.")
        embed.add_field(name=f"Manage Channels {check_perm('manage_channels')}",
                        value="Create, Delete, Edit channels. Helpful for a ticket system and muting members.")
        embed.add_field(name=f"Manage Roles {check_perm('manage_roles')}",
                        value="Create, Delete, Edit, Give/Remove roles. Needed for mute system as well as reaction roles.")
        embed.add_field(name=f"Manage Emojis {check_perm('manage_emojis')}",
                        value="Optional. Has no real use. Create, edit, delete emojis.")
        embed.add_field(name=f"View server insights {check_perm('view_guild_insights')}",
                        value="Optional. View statistics collected by Discord.")
        embed.add_field(name=f"Manage Nicknames {check_perm('manage_nicknames')}",
                        value="Nickname members in your server, helpful for the web panel management system as well as profanity monitoring.")
        embed.add_field(name=f"View audit log {check_perm('view_audit_log')}",
                        value="View logs collected by Discord. Helpful for own logs as well as leave messages.")
        embed.add_field(name=f"Manage webhooks {check_perm('manage_webhooks')}",
                        value="Create, Delete webhooks. Helpful for logs.")
        embed.add_field(name=f"Manage Server {check_perm('manage_guild')}", value="Change guild settings, helpful for the web panel.")
        embed.add_field(name=f"Create Invite {check_perm('create_instant_invite')}", value="Create an invite to your server, helpful for the invite management.")
        embed.add_field(name=f"Kick Members {check_perm('kick_members')}", value="Kick people. Needed for the moderation")
        embed.add_field(name=f"Ban members {check_perm('ban_members')}", value="Ban people. Needed for moderation")
        embed.add_field(name=f"Read messages {check_perm('read_messages')}", value="Respond to commands")
        embed.add_field(name=f"Send messages {check_perm('send_messages')}", value="Send messages as a response")
        embed.add_field(name=f"Embed links {check_perm('embed_links')}", value="Allow the use of cool embeds.")
        embed.add_field(name=f"Attach files {check_perm('attach_files')}", value="Allow the use of many features such as images and log files")
        embed.add_field(name=f"Add reactions {check_perm('add_reactions')}", value="Allow adding/removing reactions")
        embed.add_field(name=f"Use external emojis {check_perm('external_emojis')}", value="Use my custom emoji's for the commands. Won't work if disabled!")
        embed.add_field(name=f"Manage messages {check_perm('manage_messages')}", value="Chat moderation. Needed for most features.")
        embed.add_field(name=f"Read message history {check_perm('read_message_history')}", value="Read channel history, moderation.")
        embed.add_field(name=f"Connect {check_perm('connect')}", value="Connect to a voice channel")
        embed.add_field(name=f"Speak {check_perm('speak')}", value="Speak in a voice channel")
        embed.set_footer(text="Ploxy | Permissions Check")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Misc(bot))
