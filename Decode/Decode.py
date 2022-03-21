import logging
from discord.ext import commands


logging.basicConfig(level=logging.INFO)

"""Strings Conversion"""


async def string_to_ascii(strings: list):
    """A list vo strings get char vise converted to there ascii code"""
    result = ""
    for char in " ".join(strings):
        result += str(ord(char)) + " "
    return result


async def ascii_to_string(integers: list):
    """A list of integer values get converted to the char"""
    if not await check_for_integer(integers):
        return "Only Integers are allowed !"
    result = ""
    for integer in integers:
        result += chr(int(integer))
    return result


async def string_to_binary(strings: list):
    """A list of strings get char vise converted to there ascii code, which get's converted to a binary string"""
    result = ""
    for char in " ".join(strings):
        result += f"{ord(char):08b} "
    return result


async def binary_to_string(integers: list):
    """A list of binary strings get's converted to there ascii code value which get's converted to the char"""
    if not await check_for_integer(integers):
        return "Only Integers are allowed !"
    result = ""
    for integer in integers:
        result += chr(int(integer, base=2))
    return result


async def string_to_hex(strings: list):
    """A list of strings get char vise converted to there ascii code, which get's converted to a hex string"""
    result = ""
    for char in " ".join(strings):
        result += f"{hex(ord(char))} "[2:]
    return result


async def hex_to_string(integers: list):
    """A list of hex strings get's converted to there ascii code value which get's converted to the char"""
    result = ""
    for integer in integers:
        result += chr(int(integer, base=16))
    return result


async def string_to_oct(strings: list):
    """A list of strings get char vise converted to there ascii code, which get's converted to a oct string"""
    result = ""
    for char in " ".join(strings):
        result += f"{oct(ord(char))} "[2:]
    return result


async def oct_to_string(integers: list):
    """A list of oct strings get's converted to there ascii code value which get's converted to the char"""
    result = ""
    for integer in integers:
        result += chr(int(integer, base=8))
    return result


"""Integer Conversion"""


async def integer_to_binary(integers: list):
    if not await check_for_integer(integers):
        return "Only Integers are allowed !"
    result = ""
    for integer in integers:
        result += f"{int(integer):08b} "
    return result


async def binary_to_integer(integers: list):
    if not await check_for_integer(integers):
        return "Only Integers are allowed !"
    result = ""
    for integer in integers:
        result += str(int(integer, base=2)) + " "
    return result


async def integer_to_hex(integers: list):
    if not await check_for_integer(integers):
        return "Only Integers are allowed !"
    result = ""
    for integer in integers:
        result += f"{hex(int(integer))} "[2:]
    return result


async def hex_to_integer(integers: list):
    result = ""
    for integer in integers:
        result += str(int(integer, base=16)) + " "
    return result


async def integer_to_oct(integers: list):
    if not await check_for_integer(integers):
        return "Only Integers are allowed !"
    result = ""
    for integer in integers:
        result += f"{oct(int(integer))} "[2:]
    return result


async def oct_to_integer(integers: list):
    if not await check_for_integer(integers):
        return "Only Integers are allowed !"
    result = ""
    for integer in integers:
        result += str(int(integer, base=8)) + " "
    return result


async def check_for_integer(integer: list):
    for x in integer:
        try:
            int(x)
        except Exception as e:
            print(str(e))
            return False
    return True


class Convert(commands.Cog):

    @commands.command(description="""Converts Strings and Numbers:\n
    sa = String  -> ASCII\n
    as = ASCII   -> String\n
    sb = String  -> Binary\n
    bs = Binary  -> String\n
    sh = String  -> Hex\n
    hs = Hex     -> String\n
    so = String  -> Oct\n
    os = Oct     -> String\n
    ib = Integer -> Binary\n
    bi = Binary  -> Integer\n
    ih = Integer -> Hex\n
    hi = Hex     -> Integer\n
    io = Integer -> Oct\n
    oi = Oct     -> Integer""", pass_context=True, name="convert", aliases=['c'])
    async def convert(self, context: commands.Context, conversion_type: str, *values):
        """Converts the input string to ascii, binary, hex, oct"""
        if len(values) == 0:
            await context.message.channel.send("nothing to convert")
            return
        if conversion_type == 'sa':
            result = await string_to_ascii(values)
            logging.info(f"string to ascii: {values}")
            await context.message.channel.send(result)
        elif conversion_type == 'as':
            result = await ascii_to_string(values)
            logging.info(f"ascii to string: {values}")
            await context.message.channel.send(result)
        elif conversion_type == 'sb':
            result = await string_to_binary(values)
            logging.info(f"string to binary: {values}")
            await context.message.channel.send(result)
        elif conversion_type == 'bs':
            result = await binary_to_string(values)
            logging.info(f"binary to string: {values}")
            await context.message.channel.send(result)
        elif conversion_type == 'sh':
            result = await string_to_hex(values)
            logging.info(f"string to hex: {values}")
            await context.message.channel.send(result)
        elif conversion_type == 'hs':
            result = await hex_to_string(values)
            logging.info(f"hex to string: {values}")
            await context.message.channel.send(result)
        elif conversion_type == 'so':
            result = await string_to_oct(values)
            logging.info(f"string to oct: {values}")
            await context.message.channel.send(result)
        elif conversion_type == 'os':
            result = await oct_to_string(values)
            logging.info(f"oct to string: {values}")
            await context.message.channel.send(result)
        elif conversion_type == 'ib':
            result = await integer_to_binary(values)
            logging.info(f"integer to binary: {values}")
            await context.message.channel.send(result)
        elif conversion_type == 'bi':
            result = await binary_to_integer(values)
            logging.info(f"binary to integer: {values}")
            await context.message.channel.send(result)
        elif conversion_type == 'ih':
            result = await integer_to_hex(values)
            logging.info(f"integer to hex: {values}")
            await context.message.channel.send(result)
        elif conversion_type == 'hi':
            result = await hex_to_integer(values)
            logging.info(f"hex to integer: {values}")
            await context.message.channel.send(result)
        elif conversion_type == 'io':
            result = await integer_to_oct(values)
            logging.info(f"integer to oct: {values}")
            await context.message.channel.send(result)
        elif conversion_type == 'oi':
            result = await oct_to_integer(values)
            logging.info(f"oct to integer: {values}")
            await context.message.channel.send(result)


def setup(client):
    client.add_cog(Convert(client))
