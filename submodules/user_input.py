from telegram import ParseMode
from submodules import classifier as cf
from telegram.ext.dispatcher import run_async
import os, threading

image_types_format_name = ["png", "jpg", "jpeg", "tiff"]

def start(update, context):
    """
    The function welcomes the user and prompts user to input dog images.
    Args:
        update: default telegram arg
        context: default telegram arg
    """
    update.message.reply_text("Hello there! Drop an image of a dog here to begin!")

@run_async
def get_document(update, context):
    """
    This function captures files sent as documents.
    Args:
        update: default telegram arg
        context: default telegram arg
    """
    input_type = update.message.document.mime_type[6:]
    if input_type in image_types_format_name:
        get_photo(update, context)
    else:
        update.message.reply_text("Unsupported file uploaded. Do /help to see supported file formats.")
    return None

@run_async
def get_sticker(update, context):
    """
    This function captures telegram stickers.
    Args:
        update: default telegram arg
        context: default telegram arg
    """
    input_type = "jpg"
    if update.message.sticker.is_animated:
        update.message.reply_text("Animated stickers are currently unsupported :(")
    else:
        get_photo(update, context)
    return None

@run_async
def get_photo(update, context):
    """
    This function takes and prepares the image input from the user before calling the output_breed function.
    Args:
        update: default telegram arg
        context: default telegram arg
    """
    executing_code = False
    def load_animation(update, message):
        """
        Function that provides loading animation during code execution.
        Args:
            update: default telegram arg
            context: default telegram arg
        """
        while executing_code:
            message.edit_text(text="<b>Processing file /</b>", parse_mode=ParseMode.HTML)
            message.edit_text(text="<b>Processing file -</b>", parse_mode=ParseMode.HTML)
            message.edit_text(text="<b>Processing file \\</b>", parse_mode=ParseMode.HTML)
            message.edit_text(text="<b>Processing file |</b>", parse_mode=ParseMode.HTML)
        message.edit_text(text="<b>Processing complete. Breed identified:</b>", parse_mode=ParseMode.HTML)
        return None

    chat_id = update.message.chat_id
    try:
        file_id = update.message.document.file_id
        input_type = update.message.document.mime_type[6:]
    except:
        try:
            file_id = update.message.photo[-1].file_id
            context.bot.send_message(chat_id=chat_id, text="You sent your image as a photo. If you run into issues, send your image as a file instead.")
        except:
            file_id = update.message.sticker.file_id
        input_type = "jpg"

    executing_code = True
    receiving_msg = context.bot.send_message(chat_id=chat_id, text="<b>Processing file |</b>", parse_mode=ParseMode.HTML)
    threading.Thread(target=load_animation, args=(update, receiving_msg)).start()
    newFile = context.bot.get_file(file_id, timeout=None)
    newFile.download('./input_media/{}.{}'.format(chat_id, input_type))
    output_breed(update, context, input_type)
    executing_code = False
    return None

def output_breed(update, context, input_type):
    """
    This function calls the classifier and sends the user the breed returned.
    Args:
        update: default telegram arg
        context: default telegram arg
        input_type: format of file sent by user
    """
    chat_id = update.message.chat_id
    try:
        breed = cf.classify_breed(chat_id, input_type)
        context.bot.send_message(chat_id=chat_id, text="<pre>{}</pre>".format(breed), parse_mode=ParseMode.HTML)
    # throw error on failure
    except:
        context.bot.send_message(chat_id=chat_id, text="<pre>An error has occurred, please contact an admin.</pre>", parse_mode=ParseMode.HTML)
    # remove all media files at the end
    finally:
        os.remove("./input_media/{}.{}".format(chat_id, input_type))
    return None

def show_help(update, context):
    """
    Function to show support image types to users.
    Args:
        update: default telegram arg
        context: default telegram arg
    """
    update.message.reply_text("""Here are the currently supported format types:\n
    <b>Images:</b><pre>
        - png
        - jpg
        - tiff
        - Telegram Stickers
    </pre>
Drop a dog image here to begin! Have ideas and suggestions for this mini project? Head over to the <a href="https://github.com/tjtanjin/woofbuddybot">Project Repository</a>!""", parse_mode=ParseMode.HTML, disable_web_page_preview=True)
    return None