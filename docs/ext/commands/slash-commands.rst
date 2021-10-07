.. currentmodule:: discord

.. _ext_commands_slash_commands:

Slash Commands
==============

Slash Commands are currently supported in enhanced-discord.py using a system on top of ext.commands.

This system is very simple to use, and can be enabled via :attr:`.Bot.slash_commands` globally,
or only for specific commands via :attr:`.Command.slash_command`.

There is also the parameter ``slash_command_guilds`` which can be passed to either :class:`.Bot` or the command
decorator in order to only upload the commands as guild commands to these specific guild IDs, however this
should only be used for testing or small (<10 guilds) bots.

If you want to add option descriptions to your commands, you should use :class:`.Option`

For troubleshooting, see the :ref:`FAQ <ext_commands_slash_command_troubleshooting>`

.. admonition:: Slash Command Only

    For parts of the docs specific to slash commands, look for this box!
