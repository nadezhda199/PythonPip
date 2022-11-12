import logging
from math import sqrt
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
from comply import compl_1, compl_2

logging.basicConfig(filename='my_log', filemode='a', encoding='utf-8',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO
                    )
logger = logging.getLogger(__name__)

operation_keybord = [["Сложение", "Вычитание", "Умножение"],
                     ["Деление", "Возведение в степень", "Корень квадратный числа"],
                     ["Главное меню"]]

operation_keybord_main = "Сложение|Вычитание|Умножение|Деление|Возведение в степень|Корень квадратный числа|Главное меню"

MAINMENU, CHOOSING, OPERCHOISE, OPERCHOISE_COMPL, CATCHREPLY, CATCHREPLY2, CATCHREPLY3, CATCHREPLY4, DIVISION, \
CATCHREPLY5, CATCHREPLY6, CATCHREPLY7, MULTIPLY, SUM_COMPL, SUBTRACTION_COMPL, DEGREE_COMPL, SQRT_COMPL, DIVISION_COMPL, \
INT_DIV_COMPL, DIV_COMPL, MULTIPLY_COMPL = range(21)


def start(update, _):
    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Здравствуйте, вас приветсвует телеграм-калькулятор. Для продолжения нажмите любую клавишу')

    return MAINMENU


def mainmenu(update, _):
    user = update.message.from_user
    logger.info("Пользователь %s начал работу с калькулятором.", user.first_name)
    # Список кнопок для ответа
    reply_keyboard = [['Рациональные', 'Комплексные', 'Выход']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, True)
    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Выберите с какими числами вы хотите работать',
        reply_markup=markup_key, )

    return CHOOSING  # выбор вида чисел


def choosing(update, _):
    user = update.message.from_user
    num_choiсe = update.message.text
    if num_choiсe == 'Рациональные':
        markup_key = ReplyKeyboardMarkup(operation_keybord, one_time_keyboard=True)
        update.message.reply_text('Какое действие вы хотите выполнить?', reply_markup=markup_key, )
        logger.info("Пользователь %s выбрал рациональные числа.", user.first_name)
        return OPERCHOISE  # меню выбора оператора
    elif num_choiсe == 'Комплексные':
        markup_key = ReplyKeyboardMarkup(operation_keybord, one_time_keyboard=True)
        update.message.reply_text('Какое действие вы хотите выполнить?', reply_markup=markup_key, )
        logger.info("Пользователь %s выбрал комплексные числа.", user.first_name)
        return OPERCHOISE_COMPL  # меню выбора оператора
    elif num_choiсe == 'Выход':
        logger.info("Пользователь %s вышел", user.first_name)
        update.message.reply_text(
            'Спасибо, что посетили нас',
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END
    else:
        pass


def oper_choice(update, _):
    oper = update.message.text
    if oper == "Сложение":
        update.message.reply_text('Введите два числа через пробел')
        return CATCHREPLY  # сложение рациональных чисел
    elif oper == "Вычитание":
        update.message.reply_text('Введите два числа через пробел')
        return CATCHREPLY2  # вычитание рациональных чисел
    elif oper == "Возведение в степень":
        update.message.reply_text('Введите два числа через пробел')
        return CATCHREPLY3  # возведение в степень рациональных чисел
    elif oper == "Деление":
        reply_keyboard = [['Остаток', 'Целочисленное', 'Обычное', 'Главное меню']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, True)
        update.message.reply_text('Выберите тип деления', reply_markup=markup_key)
        return DIVISION  # выбор вида деления
    elif oper == "Корень квадратный числа":
        update.message.reply_text('Введите число')
        return CATCHREPLY4  # вычисляет квадратный корень числа
    elif oper == "Умножение":
        update.message.reply_text('Введите два числа через пробел')
        return MULTIPLY  # вычисляет квадратный корень числа
    elif oper == "Главное меню":
        update.message.reply_text(
            'возвращение в главное меню',
        )
        return MAINMENU
    else:
        pass


def oper_choice_compl(update, _):
    oper = update.message.text
    if oper == "Сложение":
        update.message.reply_text('Введите действительную часть и мнимую часть двух чисел через пробелы')
        return SUM_COMPL  # сложение комплексных чисел
    elif oper == "Вычитание":
        update.message.reply_text('Введите действительную часть и мнимую часть двух чисел через пробелы')
        return SUBTRACTION_COMPL  # вычитание комплексных чисел
    elif oper == "Возведение в степень":
        update.message.reply_text('Введите действительную часть и мнимую часть двух чисел через пробелы')
        return DEGREE_COMPL  # возведение в степень комплексных чисел
    elif oper == "Деление":
        reply_keyboard = [['Целочисленное', 'Обычное', 'Главное меню']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, True)
        update.message.reply_text('Выберите тип деления', reply_markup=markup_key)
        return DIVISION_COMPL  # выбор вида деления
    elif oper == "Корень квадратный числа":
        update.message.reply_text('Введите действительную часть и мнимую часть чисела через пробелы')
        return SQRT_COMPL  # вычисляет квадратный корень комплексного числа
    elif oper == "Умножение":
        update.message.reply_text('Введите действительную часть и мнимую часть двух чисел через пробелы')
        return MULTIPLY_COMPL  # умножение комплексных чисел
    elif oper == "Главное меню":
        update.message.reply_text(
            'возвращение в главное меню',
        )
        return MAINMENU
    else:
        pass


def division_ch(update, _):
    # user = update.message.from_user
    msg = update.message.text
    if msg == 'Остаток':
        update.message.reply_text('Введите два числа через пробел')
        return CATCHREPLY5
    elif msg == 'Целочисленное':
        update.message.reply_text('Введите два числа через пробел')
        return CATCHREPLY6
    elif msg == 'Обычное':
        update.message.reply_text('Введите два числа через пробел')
        return CATCHREPLY7
    elif msg == "Главное меню":
        update.message.reply_text('возвращение в главное меню')
        return MAINMENU
    else:
        update.message.reply_text('Попобуйте еще раз выбрать')
        return DIVISION


def div_choice_compl(update, _):
    msg = update.message.text
    if msg == 'Целочисленное':
        update.message.reply_text('Введите действительную часть и мнимую часть двух чисел через пробелы')
        return INT_DIV_COMPL
    elif msg == 'Обычное':
        update.message.reply_text('Введите действительную часть и мнимую часть двух чисел через пробелы')
        return DIV_COMPL
    elif msg == "Главное меню":
        update.message.reply_text('возвращение в главное меню')
        return MAINMENU
    else:
        update.message.reply_text('Попобуйте еще раз выбрать')
        return DIVISION_COMPL


def sum_oper(update, _):
    user = update.message.from_user
    msg = update.message.text
    print(msg)
    items = msg.split()  # /sum 123 534543
    try:
        x = float(items[0])
        y = float(items[1])
        update.message.reply_text(f'{x}+{y} = {x + y}')
        logger.info("Пример пользователя %s: %s + %s = %s ", user.first_name, x, y, x + y)
        return OPERCHOISE  # меню выбора оператора
    except:
        update.message.reply_text('Вы ввели неправильно, введите еще раз')
        return CATCHREPLY


def sum_oper_compl(update, _):
    user = update.message.from_user
    msg = update.message.text
    print(msg)
    items = msg.split()  # /sum 123 534543
    try:
        x = compl_1(items)
        y = compl_2(items)
        update.message.reply_text(f'{x}+{y} = {x + y}')
        logger.info("Пример пользователя %s: %s + %s = %s ", user.first_name, x, y, x + y)
        return OPERCHOISE_COMPL  # меню выбора оператора
    except:
        update.message.reply_text('Вы ввели неправильно, введите еще раз')
        return SUM_COMPL


def subtraction_oper(update, _):
    user = update.message.from_user
    msg = update.message.text
    print(msg)
    items = msg.split()
    try:
        x = float(items[0])
        y = float(items[1])
        update.message.reply_text(f'{x}-{y} = {x - y}')
        logger.info("Пример пользователя %s: %s - %s = %s ", user.first_name, x, y, x - y)
        return OPERCHOISE  # меню выбора оператора
    except:
        update.message.reply_text('Вы ввели неправильно, попробуйте еще раз')
        return CATCHREPLY2


def subtraction_oper_compl(update, _):
    user = update.message.from_user
    msg = update.message.text
    print(msg)
    items = msg.split()
    try:
        x = compl_1(items)
        y = compl_2(items)
        update.message.reply_text(f'{x}-{y} = {x - y}')
        logger.info("Пример пользователя %s: %s - %s = %s ", user.first_name, x, y, x - y)
        return OPERCHOISE_COMPL  # меню выбора оператора
    except:
        update.message.reply_text('Вы ввели неправильно, попробуйте еще раз')
        return SUBTRACTION_COMPL


def power_oper(update, _):
    user = update.message.from_user
    msg = update.message.text
    print(msg)
    items = msg.split()
    try:
        x = float(items[0])
        y = float(items[1])
        update.message.reply_text(f'{x}**{y} = {x ** y}')
        logger.info("Пример пользователя %s: %s ** %s = %s ", user.first_name, x, y, x ** y)
        return OPERCHOISE  # меню выбора оператора
    except:
        update.message.reply_text('Вы ввели неправильно, введите еще раз')
        return CATCHREPLY3


def degree_oper_compl(update, _):
    user = update.message.from_user
    msg = update.message.text
    print(msg)
    items = msg.split()
    try:
        x = compl_1(items)
        y = compl_2(items)
        update.message.reply_text(f'{x}**{y} = {x ** y}')
        logger.info("Пример пользователя %s: %s ** %s = %s ", user.first_name, x, y, x ** y)
        return OPERCHOISE_COMPL  # меню выбора оператора
    except:
        update.message.reply_text('Вы ввели неправильно, введите еще раз')
        return DEGREE_COMPL


def sqrt_oper(update, _):
    # user = update.message.from_user
    msg = update.message.text
    items = msg
    try:
        x = float(items)
        update.message.reply_text(f'√{x}= {round(sqrt(x), 2)}')
        return OPERCHOISE  # меню выбора оператора
    except:
        update.message.reply_text('Вы ввели неправильно, введите еще раз')
        return CATCHREPLY4


def sqrt_oper_compl(update, _):
    # user = update.message.from_user
    msg = update.message.text
    items = msg.split()
    try:
        x = compl_1(items)
        update.message.reply_text(f'√{x}= {round(sqrt(x), 2)}')
        return OPERCHOISE_COMPL  # меню выбора оператора
    except:
        update.message.reply_text('Вы ввели неправильно, введите еще раз')
        return SQRT_COMPL


def div_rem(update, _):
    msg = update.message.text
    items = msg.split()
    try:
        x = float(items[0])
        y = float(items[1])
        if y == 0:
            update.message.reply_text('На ноль делить нельзя! Попробуйте еще раз')
            logger.info("Ошибка. Деление на 0", update.message.from_user.first_name, x, y, x % y)
            return CATCHREPLY5
        else:
            update.message.reply_text(f'{x}%{y} = {x % y}')
            logger.info("Пример пользователя %s: %s % %s = %s ", update.message.from_user.first_name, x, y, x % y)
            return DIVISION
    except:
        update.message.reply_text('Ошибка ввода')
        logger.error('Ошибка ввода',
                     ext_info=True)  # вот тут я применил метод error модуля logging и здесь я остановился с включением логов
        return CATCHREPLY5


def division_int(update, _):
    user = update.message.from_user
    msg = update.message.text
    items = msg.split()
    try:
        x = float(items[0])
        y = float(items[1])
        if y != 0:
            update.message.reply_text(f'{x}//{y} = {x // y}')
            return DIVISION
        else:
            update.message.reply_text('На ноль делить нельзя! Попробуйте еще раз')
            return CATCHREPLY6
    except:
        update.message.reply_text('Вы ввели неправильно, введите еще раз')
        return CATCHREPLY6


def div_int_compl(update, _):
    # user = update.message.from_user
    msg = update.message.text
    items = msg.split()
    try:
        x = compl_1(items)
        y = compl_2(items)
        if y != 0:
            update.message.reply_text(f'{x}//{y} = {x // y}')
            return DIVISION_COMPL
        else:
            update.message.reply_text('На ноль делить нельзя! Попробуйте еще раз')
            return INT_DIV_COMPL
    except:
        update.message.reply_text('Вы ввели неправильно, введите еще раз')
        return INT_DIV_COMPL


def division(update, _):
    # user = update.message.from_user
    msg = update.message.text
    items = msg.split()
    try:
        x = float(items[0])
        y = float(items[1])
        if y != 0:
            update.message.reply_text(f'{x}/{y} = {round((x / y), 2)}')
            return DIVISION
        else:
            update.message.reply_text('На ноль делить нельзя! Попробуйте еще раз')
            return CATCHREPLY7
    except:
        update.message.reply_text('Вы ввели неправильно, введите еще раз')
        return CATCHREPLY7


def div_compl(update, _):
    # user = update.message.from_user
    msg = update.message.text
    items = msg.split()
    try:
        x = compl_1(items)
        y = compl_2(items)
        if items[2] != 0 or items[3] != 0:
            update.message.reply_text(f'{x}/{y} = {round((x / y), 2)}')
            return DIVISION_COMPL
        else:
            update.message.reply_text('На ноль делить нельзя! Попробуйте еще раз')
            return DIV_COMPL
    except:
        update.message.reply_text('Вы ввели неправильно, введите еще раз')
        return DIV_COMPL


def multiply(update, _):
    msg = update.message.text
    print(msg)
    items = msg.split()
    try:
        x = float(items[0])
        y = float(items[1])
        update.message.reply_text(f'{x}*{y} = {x * y}')
        logger.info("Пример пользователя %s: %s * %s = %s ", update.message.from_user.first_name, x, y, x ** y)
        return OPERCHOISE  # меню выбора оператора
    except:
        update.message.reply_text('Вы ввели неправильно, введите еще раз')
        return MULTIPLY


def multiply_compl(update, _):
    msg = update.message.text
    items = msg.split()
    try:
        x = compl_1(items)
        y = compl_2(items)
        update.message.reply_text(f'{x}*{y} = {x * y}')
        logger.info("Пример пользователя %s: %s * %s = %s ", update.message.from_user.first_name, x, y, x ** y)
        return OPERCHOISE_COMPL  # меню выбора оператора
    except:
        update.message.reply_text('Вы ввели неправильно, введите еще раз')
        return MULTIPLY_COMPL


def cancel(update, _):
    user = update.message.from_user
    logger.info("User %s finished work with calculator.", user.first_name)
    update.message.reply_text(
        'Спасибо, что посетили нас',
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater("TOKEN")
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler`
    conv_handler = ConversationHandler(  # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            MAINMENU: [MessageHandler(Filters.text & ~Filters.command, mainmenu)],
            CHOOSING: [MessageHandler(Filters.regex('^(Рациональные|Комплексные|Выход)$'), choosing)],
            OPERCHOISE: [MessageHandler(Filters.regex(f'^{operation_keybord_main}$'), oper_choice)],
            OPERCHOISE_COMPL: [MessageHandler(Filters.regex(f'^{operation_keybord_main}$'), oper_choice_compl)],
            DIVISION: [MessageHandler(Filters.regex('^(Остаток|Целочисленное|Обычное|Главное меню)$'), division_ch)],
            DIVISION_COMPL: [MessageHandler(Filters.regex('^(Целочисленное|Обычное|Главное меню)$'), div_choice_compl)],
            CATCHREPLY: [MessageHandler(Filters.text & ~Filters.command, sum_oper)],
            SUM_COMPL: [MessageHandler(Filters.text & ~Filters.command, sum_oper_compl)],
            CATCHREPLY2: [MessageHandler(Filters.text & ~Filters.command, subtraction_oper)],
            SUBTRACTION_COMPL: [MessageHandler(Filters.text & ~Filters.command, subtraction_oper_compl)],
            CATCHREPLY3: [MessageHandler(Filters.text & ~Filters.command, power_oper)],
            DEGREE_COMPL: [MessageHandler(Filters.text & ~Filters.command, degree_oper_compl)],
            CATCHREPLY4: [MessageHandler(Filters.text & ~Filters.command, sqrt_oper)],
            SQRT_COMPL: [MessageHandler(Filters.text & ~Filters.command, sqrt_oper_compl)],
            CATCHREPLY5: [MessageHandler(Filters.text & ~Filters.command, div_rem)],
            CATCHREPLY6: [MessageHandler(Filters.text & ~Filters.command, division_int)],
            INT_DIV_COMPL: [MessageHandler(Filters.text & ~Filters.command, div_int_compl)],
            CATCHREPLY7: [MessageHandler(Filters.text & ~Filters.command, division)],
            DIV_COMPL: [MessageHandler(Filters.text & ~Filters.command, div_compl)],
            MULTIPLY: [MessageHandler(Filters.text & ~Filters.command, multiply)],
            MULTIPLY_COMPL: [MessageHandler(Filters.text & ~Filters.command, multiply_compl)],
        },
        fallbacks=[CommandHandler('cancel', cancel)])  # точка выхода из разговора

    dispatcher.add_handler(conv_handler)  # Добавляем обработчик разговоров `conv_handler`

    # Запуск бота
    updater.start_polling()
    updater.idle()
