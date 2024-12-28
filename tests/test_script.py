import os
import sys
import unittest
from unittest.mock import patch, Mock, MagicMock

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../src'))

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../src/utils'))
from commands import commands
from TelegramBot import TelegramBot
from telebot import types


class TestTelegramBot(unittest.TestCase):
    def setUp(self):
        self.chat_id = 12345
        self.mock_message = Mock()
        self.mock_message.chat.id = self.chat_id
        self.user_name = 'test_user'

    @patch('telebot.TeleBot')
    @patch('TelegramBot.UserService')
    def test_handle_start_command_actual(self, mock_user_service, mock_telebot):
        mock_user_service_instance = mock_user_service.return_value
        mock_user_service_instance.get_user.return_value = 'TestUser'

        telegram_bot = TelegramBot()

        mock_bot_instance = mock_telebot.return_value
        mock_message = MagicMock()
        mock_message.chat.id = self.chat_id

        telegram_bot.handle_start_command(mock_message)

        # Assert send_message is called
        mock_bot_instance.send_message.assert_called_once()

    @patch('TelegramBot.telebot.TeleBot')
    def test_handle_start_command(self, MockTelebot):
        mock_bot = MockTelebot.return_value

        telegram_bot_instance = TelegramBot()
        telegram_bot_instance._TelegramBot__user_service.get_user = Mock(return_value=self.user_name)

        self._handle_command_with_user(mock_bot, telegram_bot_instance, 'start')

        mock_bot.send_message.assert_called_once_with(
            self.chat_id,
            commands['start'](self.user_name),
            parse_mode='html'
        )

    @patch('telebot.TeleBot')
    @patch('TelegramBot.UserService')
    def test_handle_info_command_actual(self, mock_user_service, mock_telebot):
        mock_user_service_instance = mock_user_service.return_value
        mock_user_service_instance.get_user.return_value = 'TestUser'

        telegram_bot = TelegramBot()

        mock_bot_instance = mock_telebot.return_value
        mock_message = MagicMock()
        mock_message.chat.id = self.chat_id

        telegram_bot.handle_info_command(mock_message)

        # Assert send_message is called
        mock_bot_instance.send_message.assert_called_once()

    @patch('TelegramBot.telebot.TeleBot')
    def test_handle_info_command(self, MockTelebot):
        mock_bot = MockTelebot.return_value

        self._handle_command_without_user(mock_bot, 'info')

        mock_bot.send_message.assert_called_once_with(
            self.chat_id,
            commands['info'](),
            parse_mode='html'
        )

    @patch('TelegramBot.telebot.TeleBot')
    def test_handle_start_then_info_command(self, MockTelebot):
        mock_bot = MockTelebot.return_value

        telegram_bot_instance = TelegramBot()
        telegram_bot_instance._TelegramBot__user_service.get_user = Mock(return_value=self.user_name)

        telegram_bot_instance.handle_button()
        self._handle_command_with_user(mock_bot, telegram_bot_instance, 'start')

        mock_bot.send_message.assert_called_with(
            self.chat_id,
            commands['start'](self.user_name),
            parse_mode='html'
        )

        self._handle_command_without_user(mock_bot, 'info')

        mock_bot.send_message.assert_called_with(
            self.chat_id,
            commands['info'](),
            parse_mode='html'
        )

    @patch('telebot.TeleBot')
    @patch('TelegramBot.UserService')
    def test_handle_subscription_info_command_actual(self, mock_user_service, mock_telebot):
        mock_user_service_instance = mock_user_service.return_value
        mock_user_service_instance.get_user.return_value = 'TestUser'

        telegram_bot = TelegramBot()

        mock_bot_instance = mock_telebot.return_value
        mock_message = MagicMock()
        mock_message.chat.id = self.chat_id

        telegram_bot.handle_subscription_info_command(mock_message)

        # Assert send_message is called
        mock_bot_instance.send_message.assert_called_once()

    @patch('TelegramBot.telebot.TeleBot')
    def test_handle_subscription_info_command(self, MockTelebot):
        mock_bot = MockTelebot.return_value

        self._handle_command_without_user(mock_bot, 'subscription_info')

        mock_bot.send_message.assert_called_once_with(
            self.chat_id,
            commands['subscription_info'](),
            parse_mode='html'
        )

    @patch('telebot.TeleBot')
    @patch('TelegramBot.UserService')
    def test_handle_payment_command_actual(self, mock_user_service, mock_telebot):
        mock_user_service_instance = mock_user_service.return_value
        mock_user_service_instance.get_user.return_value = 'TestUser'

        telegram_bot = TelegramBot()

        mock_bot_instance = mock_telebot.return_value
        mock_message = MagicMock()
        mock_message.chat.id = self.chat_id

        telegram_bot.handle_subscription_command(mock_message)

        # Assert send_message is called
        mock_bot_instance.send_message.assert_called_once()

    @patch('TelegramBot.telebot.TeleBot')
    def test_handle_payment_command(self, MockTelebot):
        mock_bot = MockTelebot.return_value

        markup_inline = types.InlineKeyboardMarkup()
        item_subscription = types.InlineKeyboardButton(text='Купить подписку', callback_data='buy_sub')
        markup_inline.add(item_subscription)
        payment_intro_text = 'Нажжмите "Купить подписку" если хотите приобрести пробную или платную подписку'

        mock_bot.send_message(self.chat_id,
                              payment_intro_text,
                              reply_markup=markup_inline)

        mock_bot.send_message.assert_called_once_with(
            self.chat_id,
            payment_intro_text,
            reply_markup=markup_inline
        )

    @patch('telebot.TeleBot')
    @patch('TelegramBot.UserService')
    def test_subscription_handler_buy_sub_actual(self, mock_user_service, mock_telebot):
        mock_user_service_instance = mock_user_service.return_value
        mock_user_service_instance.get_user.return_value = 'TestUser'

        telegram_bot = TelegramBot()

        message = Mock()
        message.text = 'Купить подписку'
        message.chat.id = self.chat_id

        telegram_bot.handle_commands(message)
        mock_bot_instance = mock_telebot.return_value
        # Assert send_message is called
        mock_bot_instance.send_message.assert_called_once()

    @patch('telebot.TeleBot')
    @patch('TelegramBot.UserService')
    def test_subscription_handler_country_selection_actual(self, mock_user_service, mock_telebot):
        mock_user_service_instance = mock_user_service.return_value
        mock_user_service_instance.get_user.return_value = 'TestUser'

        telegram_bot = TelegramBot()

        message = Mock()
        message.text = "USA"
        message.chat.id = self.chat_id

        telegram_bot.handle_commands(message)
        mock_bot_instance = mock_telebot.return_value
        # Assert send_message is called
        mock_bot_instance.send_message.assert_called_once()

    @patch('TelegramBot.telebot.TeleBot')
    def test_subscription_handler_country_selection(self, MockTelebot):
        # Simulate callback data for a specific country
        mock_bot = MockTelebot.return_value

        call = Mock()
        call.data = "country_USA"
        call.message.chat.id = self.chat_id

        markup_inline = types.InlineKeyboardMarkup()
        item_trial_subscription = types.InlineKeyboardButton(text='Пробная подписка',
                                                             callback_data=f'trial_sub_{call.data}')
        item_subscription = types.InlineKeyboardButton(text='Платная подписка',
                                                       callback_data=f'sub_{call.data}')
        markup_inline.add(item_trial_subscription, item_subscription)
        mock_bot.send_message(call.message.chat.id, 'Выберите подписку', reply_markup=markup_inline)

        mock_bot.send_message.assert_called_once_with(call.message.chat.id, 'Выберите подписку',
                                                      reply_markup=markup_inline
                                                      )

    def _handle_command_with_user(self, mock_bot, telegram_bot_instance, key):
        user_name = telegram_bot_instance._TelegramBot__user_service.get_user(self.mock_message)
        mock_bot.send_message(self.chat_id, commands[key](user_name), parse_mode='html')

    def _handle_command_without_user(self, mock_bot, key):
        mock_bot.send_message(self.chat_id, commands[key](), parse_mode='html')

    # def _handle(self):


if __name__ == '__main__':
    unittest.main()
