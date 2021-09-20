enhanced-discord.py
===================

.. image:: https://discord.com/api/guilds/514232441498763279/embed.png
   :target: https://discord.gg/TvqYBrGXEm
   :alt: Discord server invite
.. image:: https://img.shields.io/pypi/v/enhanced-dpy.svg
   :target: https://pypi.python.org/pypi/enhanced-dpy
   :alt: PyPI version info
.. image:: https://img.shields.io/pypi/pyversions/enhanced-dpy.svg
   :target: https://pypi.python.org/pypi/enhanced-dpy
   :alt: PyPI supported Python versions

A modern, maintained, easy to use, feature-rich, and async ready API wrapper for Discord written in Python.

The Future of enhanced-discord.py
--------------------------

Enhanced discord.py is a fork of Rapptz's discord.py, that went unmaintained (`gist <https://gist.github.com/Rapptz/4a2f62751b9600a31a0d3c78100287f1>`_)

It is currently maintained by (in alphabetical order)

- Chillymosh#8175
- Daggy#9889
- dank Had0cK#6081
- Dutchy#6127
- Eyesofcreeper#0001
- Gnome!#6669
- IAmTomahawkx#1000
- Jadon#2494

An overview of added features is available on the `custom features page <https://enhanced-dpy.readthedocs.io/en/latest/index.html#custom-features>`_.

Key Features
-------------

- Modern Pythonic API using ``async`` and ``await``.
- Proper rate limit handling.
- Optimised in both speed and memory.

Installing
----------

**Python 3.8 or higher is required**

To install the library without full voice support, you can just run the following command:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U enhanced-dpy

    # Windows
    py -3 -m pip install -U enhanced-dpy


To install the development version, do the following:

.. code:: sh

    $ git clone https://github.com/iDevision/enhanced-discord.py
    $ cd enhanced-discord.py
    $ python3 -m pip install -U .[voice]


Optional Packages
~~~~~~~~~~~~~~~~~~

* `PyNaCl <https://pypi.org/project/PyNaCl/>`__ (for voice support)

Please note that on Linux installing voice you must install the following packages via your favourite package manager (e.g. ``apt``, ``dnf``, etc) before running the above commands:

* libffi-dev (or ``libffi-devel`` on some systems)
* python-dev (e.g. ``python3.6-dev`` for Python 3.6)

Quick Example
--------------

.. code:: py

    import discord

    class MyClient(discord.Client):
        async def on_ready(self):
            print('Logged on as', self.user)

        async def on_message(self, message):
            # don't respond to ourselves
            if message.author == self.user:
                return

            if message.content == 'ping':
                await message.channel.send('pong')

    client = MyClient()
    client.run('token')

Bot Example
~~~~~~~~~~~~~

.. code:: py

    import discord
    from discord.ext import commands

    bot = commands.Bot(command_prefix='>')

    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')

    bot.run('token')

You can find more examples in the examples directory.

Links
------

- `Documentation <https://enhanced-dpy.readthedocs.io/en/latest/index.html>`_
- `Official Discord Server <https://discord.gg/TvqYBrGXEm>`_
- `Discord API <https://discord.gg/discord-api>`_
