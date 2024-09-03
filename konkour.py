import os
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, Update,
                      InlineKeyboardButton, InlineKeyboardMarkup)
from telegram.ext import (Application, CallbackQueryHandler, CommandHandler,
                          ContextTypes, ConversationHandler, MessageHandler, filters, Updater)
from dotenv import load_dotenv
import logging
import science_functions
import humanities_functions
import math_functions

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def replace_fa_with_en(text):
    en = "0123456789"
    fa = "۰۱۲۳۴۵۶۷۸۹"
    translation = str.maketrans(fa, en)
    return text.translate(translation)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    try:
        # x = await update.get_bot().getChatMember('@deltakonkurr', update.message.from_user.id)
        # y = await update.get_bot().getChatMember('-1001513566018', update.message.from_user.id)
        y = await update.get_bot().getChatMember('@delta_reshte', update.message.from_user.id)
    except Exception as e:
        print(e)
        await update.message.reply_text("مشکلی در پردازش ربات به وجود آمده است. لطفا بعدا دوباره تلاش کنید")
        return ConversationHandler.END
    
    if y.status == 'left':
        #channel link 
        keyboard = [
            [InlineKeyboardButton("عضویت در کانال مشاوره کنکور دلتا", url="https://t.me/deltakonkurr")],
            [InlineKeyboardButton("عضویت در کانال انتخاب رشته تیم دلتا", url="https://t.me/delta_reshte")],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('<b>لطفا در کانال های زیر عضو شوید و ربات را دوباره استارت کنید:</b>', parse_mode='HTML', reply_markup=reply_markup)
        return 8


    reply_keyboard = [['ریاضی', 'تجربی', 'انسانی']]

    await update.message.reply_text(
        'لطفا رشته مورد نظر خود را انتخاب کنید:',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True),
    )
    return 4


# 4
async def reshte_type(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    reshte_type_input = update.message.text

    if reshte_type_input not in ['ریاضی', 'تجربی', 'انسانی']:
        await update.message.reply_text('رشته شما به درستی ثبت نشده است. لطفا برای انتخاب رشته خود مجددا تلاش نمایید.')
        return 4
    
    context.user_data['reshte_type'] = reshte_type_input
    logger.info('reshte %s: %s', user.first_name, reshte_type_input)

    f = open("log.txt", "a")
    f.write("username: {}, user id: {}, full_name: {}, reshte: {}\n".format(
        user.username, user.id, user.full_name, reshte_type_input
    ))
    f.close()


    reply_keyboard = [['منطقه 1', 'منطقه 2', 'منطقه 3'], ['بازگشت به عقب']]

    await update.message.reply_text(
        'لطفا منطقه خود را انتخاب کنید:',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True),
    )
    return 5

# 5
async def region_type(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    region_type_input = update.message.text

    if region_type_input == 'بازگشت به عقب':
        return await start(update, context)

    if region_type_input not in ['منطقه 1', 'منطقه 2', 'منطقه 3']:
        await update.message.reply_text('منطقه شما به درستی ثبت نشده است. لطفا برای ثبت منطقه خود دوباره تلاش نمایید.')
        return 5
    
    context.user_data['region_type'] = region_type_input
    logger.info('region %s: %s', user.first_name, region_type_input)

    await update.message.reply_text(
        '<b>چطور میتونم کمکت کنم؟</b>',
        parse_mode='HTML',
        reply_markup=ReplyKeyboardRemove(),
    )

    # Define inline buttons for option selection
    keyboard = [
        [InlineKeyboardButton('تخمین تراز کنکور براساس درصد', callback_data='تخمین تراز کنکور براساس درصد')],
        [InlineKeyboardButton('تخمین تراز سوابق براساس معدل', callback_data='تخمین تراز سوابق براساس معدل')],
        [InlineKeyboardButton('تخمین رتبه کنکور براساس تراز کل', callback_data='تخمین رتبه کنکور براساس تراز کل')],
        [InlineKeyboardButton('تخمین رشته براساس رتبه کنکور', callback_data='تخمین رشته براساس رتبه کنکور')],
        [InlineKeyboardButton('بازگشت به عقب', callback_data='بازگشت به عقب')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('<b>لطفا انتخاب کنید:</b>', parse_mode='HTML', reply_markup=reply_markup)


async def specific_opt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    context.user_data['specific_option'] = query.data

    if query.data == 'بازگشت به عقب':
        await query.edit_message_text(
            text=f'رشته انتخابی: {context.user_data["reshte_type"]}',
            parse_mode='HTML',
        )
        reply_keyboard = [['منطقه 1', 'منطقه 2', 'منطقه 3'], ['بازگشت به عقب']]

        await query.message.chat.send_message(
            'لطفا منطقه خود را انتخاب کنید:',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True),
        )
        return 5

    # 0
    elif query.data == 'تخمین تراز سوابق براساس معدل':
        await query.edit_message_text(
            text=f'<b>لطفا معدل خود را وارد کنید:‌</b> \n مثال:\n18.5',
            parse_mode='HTML'
        )
        return 0
    
    # 1
    elif query.data == 'تخمین تراز کنکور براساس درصد':
        resh_type = context.user_data['reshte_type']
        
        if resh_type == 'تجربی':
            await query.edit_message_text(
                text='لطفا درصد دروس زیر را در هر سطر وارد کنید.\n\nریاضی\nشیمی\nزیست شناسی\nزمین شناسی\nفیزیک\n\
                    مثال: \n18\n17\n19\n18\n17',
            )
        
        elif resh_type == 'ریاضی':
            await query.edit_message_text(
                text='لطفا درصد دروس زیر را در هر سطر وارد کنید.\nریاضی\nفیزیک\nشیمی\n\
                    مثال: \n18\n17\n19',
            )
        
        elif resh_type == 'انسانی':
            await query.edit_message_text(
                text='لطفا درصد دروس زیر را در هر سطر وارد کنید:\nفنون\nریاضی\nروانشناسی\nاقتصاد\nعربی\nفلسفه و منطق\nتاریخ و جغرافیا\nجامعه شناسی\
                    مثال: \n18\n17\n19\n18\n17\n18\n19\n78',
            )
        
        else:
            await query.edit_message_text(
                text='رشته شما به درستی وارد نشده است. لطفا ربات را دوباره استارت کنید.'
            )
            return ConversationHandler.END
        
        return 1
    
    # 2
    elif query.data == 'تخمین رتبه کنکور براساس تراز کل':
        await query.edit_message_text(
            text=f'<b>لطفا معدل خود را وارد کنید:‌</b> \n مثال:\n18.5',
            parse_mode='HTML'
        )

        return 6
    
    # 3
    elif query.data == 'تخمین رشته براساس رتبه کنکور':
        await query.edit_message_text(
            text='لطفا رتبه کنکور خود را وارد کنید:\nمثال:\n100000',
        )
        return 3

# 0
async def get_grade(update, context):
    user_input = update.message.text
    try:
        float(user_input)

        if context.user_data['reshte_type'] == 'تجربی':
            taraz = science_functions.grade_taraz_func(user_input)

        elif context.user_data['reshte_type'] == 'انسانی':
            taraz = humanities_functions.grade_taraz_func(user_input)

        elif context.user_data['reshte_type'] == 'ریاضی':
            taraz = math_functions.grade_taraz_func(user_input)
            
        context.user_data['taraz_moadel'] = taraz
        response = f"تراز شما بین {taraz - 300} تا {taraz + 300} است."
        await update.message.reply_text(response)
        await update.message.reply_text("برای شروع مجدد  /start  کنید.", reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    except:
        await update.message.reply_text("لطفا معدل خود را به درستی وارد کنید")
        return 0

# 1
async def get_grade_of_lessons(update, context):
    user_input = update.message.text
    user_input = user_input.split("\n")

    try:
        user_input = [int(grade) for grade in user_input]
    except:
        await update.message.reply_text("لطفا درصد دروس خود را به درستی وارد کنید.")
        return 1
    
    if context.user_data['reshte_type'] == 'تجربی':
        if len(user_input) != 5:
            await update.message.reply_text("لطفا درصد همه دروس را وارد کنید")
            return 1
        
        total_taraz = int(science_functions.percent_taraz(user_input))
    
    elif context.user_data['reshte_type'] == 'ریاضی':
        if len(user_input) != 3:
            await update.message.reply_text("لطفا درصد همه دروس را وارد کنید")
            return 1

        total_taraz = int(math_functions.percent_taraz(user_input))

    elif context.user_data['reshte_type'] == 'انسانی':
        if len(user_input) != 8:
            await update.message.reply_text("لطفا درصد همه دروس را وارد کنید")
            return 1
        
        total_taraz = int(humanities_functions.percent_taraz(user_input))
    
    try:
        context.user_data['taraz_konkor'] = total_taraz
        await update.message.reply_text(f"تراز شما بین {total_taraz - 300} تا {total_taraz + 300} است.")
        await update.message.reply_text("برای شروع مجدد  /start  کنید.", reply_markup=ReplyKeyboardRemove())
    except:
        await update.message.reply_text("مشکلی در ارسال داده ها به وجود آمده است. لطفا بعدا تلاش کنید.")

    return ConversationHandler.END

# 6
async def get_grade_sec_2(update, context):
    user_input = update.message.text
    try:
        float(user_input)

        if context.user_data['reshte_type'] == 'تجربی':
            taraz = science_functions.grade_taraz_func(user_input)

        elif context.user_data['reshte_type'] == 'انسانی':
            taraz = humanities_functions.grade_taraz_func(user_input)

        elif context.user_data['reshte_type'] == 'ریاضی':
            taraz = math_functions.grade_taraz_func(user_input)
            
        context.user_data['taraz_moadel'] = taraz

        resh_type = context.user_data['reshte_type']
        
        if resh_type == 'تجربی':
            await update.message.reply_text(
                text='لطفا درصد دروس زیر را در هر سطر وارد کنید.\n\nریاضی\nشیمی\nزیست شناسی\nزمین شناسی\nفیزیک\n\
                    مثال: \n56\n45\n19\n56\n45',
            )
        
        elif resh_type == 'ریاضی':
            await update.message.reply_text(
                text='لطفا درصد دروس زیر را در هر سطر وارد کنید.\nریاضی\nفیزیک\nشیمی\n\
                    مثال: \n56\n45\n19',
            )
        
        elif resh_type == 'انسانی':
            await update.message.reply_text(
                text='لطفا درصد دروس زیر را در هر سطر وارد کنید:\nفنون\nریاضی\nروانشناسی\nاقتصاد\nعربی\nفلسفه و منطق\nتاریخ و جغرافیا\nجامعه شناسی\
                    مثال: \n56\n45\n19\n56\n45\n56\n19\n78',
            )
        
        else:
            await update.message.reply_text(
                text='رشته شما به درستی وارد نشده است. لطفا ربات را دوباره استارت کنید.'
            )
            return ConversationHandler.END

        return 2
    except:
        await update.message.reply_text("لطفا معدل خود را به درستی وارد کنید")
        return 6

# 2
async def get_taraz(update, context):
    user_input = update.message.text
    user_input = user_input.split("\n")

    try:
        user_input = [int(grade) for grade in user_input]
    except:
        await update.message.reply_text("لطفا درصد دروس خود را به درستی وارد کنید.")
        return 6
    
    if context.user_data['reshte_type'] == 'تجربی':
        if len(user_input) != 5:
            await update.message.reply_text("لطفا درصد همه دروس را وارد کنید")
            return 2
        
        total_taraz = int(science_functions.percent_taraz(user_input))
    
    elif context.user_data['reshte_type'] == 'ریاضی':
        if len(user_input) != 3:
            await update.message.reply_text("لطفا درصد همه دروس را وارد کنید")
            return 2

        total_taraz = int(math_functions.percent_taraz(user_input))

    elif context.user_data['reshte_type'] == 'انسانی':
        if len(user_input) != 8:
            await update.message.reply_text("لطفا درصد همه دروس را وارد کنید")
            return 2
        
        total_taraz = int(humanities_functions.percent_taraz(user_input))
    
    try:
        context.user_data['taraz_konkor'] = total_taraz
    except:
        await update.message.reply_text("مشکلی در ارسال داده ها به وجود آمده است. لطفا بعدا تلاش کنید.")

    try:
        if context.user_data['region_type'] == "منطقه 1":
            mantaghe = "1"
        elif context.user_data['region_type'] == "منطقه 2":
            mantaghe = "2"
        elif context.user_data['region_type'] == "منطقه 3":
            mantaghe = "3"

        try:
            t_kol = (int(context.user_data['taraz_konkor']) + int(context.user_data['taraz_moadel'])) / 2
        except:
            await update.message.reply_text("تراز معدل یا تراز کنکور شما به درستی ثبت نشده است")
            return ConversationHandler.END

        if context.user_data['reshte_type'] == "تجربی":
            res = science_functions.taraz_kol_func(t_kol, mantaghe)

        elif context.user_data['reshte_type'] == 'انسانی':
            res = humanities_functions.taraz_kol_func(t_kol, mantaghe)
        
        elif context.user_data['reshte_type'] == 'ریاضی':
            res = math_functions.taraz_kol_func(t_kol, mantaghe)

        await update.message.reply_text(res)  

        await update.message.reply_text("برای شروع مجدد  /start  کنید.", reply_markup=ReplyKeyboardRemove())

        return ConversationHandler.END

    except:
        return ConversationHandler.END

# 3
async def get_result(update, context):
    try:
        user_input = update.message.text

        if context.user_data['region_type'] == "منطقه 1":
            mantaghe = "1"
        elif context.user_data['region_type'] == "منطقه 2":
            mantaghe = "2"
        elif context.user_data['region_type'] == "منطقه 3":
            mantaghe = "3"
        
        if context.user_data['reshte_type'] == 'تجربی':
            res = science_functions.get_konkor_grade(user_input, mantaghe)
        
        elif context.user_data['reshte_type'] == 'انسانی':
            res = humanities_functions.get_konkor_grade(user_input, mantaghe)
        
        elif context.user_data['reshte_type'] == 'ریاضی':
            res = math_functions.get_konkor_grade(user_input, mantaghe)

        for i in range(0, len(res), 4000):
            message_chunk = res[i:i+4000]
            await update.message.reply_text(message_chunk)
        
        await update.message.reply_text("برای شروع مجدد  /start  کنید.", reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    except Exception as e:
        print(e)
        await update.message.reply_text("لطفا دوباره تلاش کنید")
        return 3


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text('برای شروع مجدد  /start  کنید.', reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    application = Application.builder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            0: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_grade)],
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_grade_of_lessons)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_taraz)],
            3: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_result)],
            4: [MessageHandler(filters.TEXT & ~filters.COMMAND, reshte_type)],
            5: [MessageHandler(filters.TEXT & ~filters.COMMAND, region_type), CallbackQueryHandler(specific_opt)],
            6: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_grade_sec_2)],
        },
        fallbacks=[CommandHandler('cancel', cancel), CommandHandler('start', start)],
    )

    application.add_handler(conv_handler)

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('cancel', cancel))


    application.run_polling()


if __name__ == '__main__':
    main()
