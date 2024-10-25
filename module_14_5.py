from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
from crud_functions2 import *


api = "7326151357:AAEgc-QlG352kWASrQW_dvkbWj2jUgJHmho"
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())


menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Расчитать'),KeyboardButton(text='Информация')],
    [KeyboardButton(text='Купить'),KeyboardButton(text='Регистрация')]

], resize_keyboard=True)


inline_choise = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text='Рассчитать норму калорий',callback_data='сalories'),
        InlineKeyboardButton(text='Формулы расчета',callback_data='formulas')
    ]
]
)

inline_products = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text='Продукт 1',callback_data='product_buying'),
        InlineKeyboardButton(text='Продукт 2',callback_data='product_buying'),
        InlineKeyboardButton(text='Продукт 3',callback_data='product_buying'),
        InlineKeyboardButton(text='Продукт 4',callback_data='product_buying')
    ]
]
)
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balanse = State('1000')






@dp.message_handler(text='Регистрация')
async  def sing_up(message):
    await message.answer('Введите ваше имя:')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async  def set_username(message, state):
    if not is_included(message.text):
        await state.update_data(username=message.text)
        await message.answer("Введите ваш email:")
        await RegistrationState.email.set()
    else:
        await message.answer('Такое имя уже есть.Введите другое имя:')
        await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message,state):
    await state.update_data(email=message.text)
    await message.answer('Введите ваш возраст:')
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def  set_age(message,state):
    if 120 >= int(message.text) >= 0:
        await state.update_data(age=message.text)
        data =await state.get_data()
        add_user(data['username'],data['email'],data['age'])
        await message.answer('Регистрация успешна!')
        await state.finish()
    else:
        await message.answer("Введите корректный возраст!")
        await RegistrationState.age.set()








@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for  index,product in enumerate(get_all_products()):
        await message.answer(f'Название: {product[1]} | Описание: описание {product[2]} | Цена: {product[3]*100}')
        with open(f'Product{index+1}.jpg', 'rb') as photo:
            await message.answer_photo(photo)
    await message.answer('Выберите продукт для покупки:', reply_markup=inline_products)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы приобрели продукт")





@dp.message_handler(text='Расчитать')
async def main_menu(message):
    await message.answer('Выберите пункт:', reply_markup=inline_choise)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 x все(кг) + 6,25 х рост(см) - 5 х возраст(г) -161')



@dp.callback_query_handler(text='сalories')
async  def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message,state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message,state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight= message.text)
    data = await state.get_data()
    result = 10 * int(data['weight']) + 6.25 * int(data['growth'] )- 5 * int(data['age']) - 161
    await message.answer(f'Ваша норма колорий {result}')
    await state.finish()



@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! я бот помогающий твоему здоровью.',reply_markup = menu)
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_masssages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')
    print('Введите команду / start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)