from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton



api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())


menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Расчитать'),KeyboardButton(text='Информация')],
    [KeyboardButton(text='Купить')]

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
@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in range(1,5):
        await message.answer(f'Название: Product{i} | Описание: описание {i} | Цена: {i*100}')
        with open(f'Product{i}.jpg', 'rb') as photo:
            await message.answer_photo(photo)
    await message.answer('Выберите продукт для покупки:', reply_markup=inline_products)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы приобрели продукт")



class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
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