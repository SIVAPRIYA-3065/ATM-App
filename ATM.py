from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivymd.app import MDApp

KV = '''
ScreenManager:
    StartScreen:
    WelcomeScreen:
    TransactionScreen:
    BalanceScreen:
    WithdrawScreen:
    DepositScreen:
    HistoryScreen:

<StartScreen>:
    name: 'start'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'atm_logo.png'  # Path to your image file
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDRaisedButton:
            text: "Insert Card"
            pos_hint: {"center_x": 0.5}
            on_release: app.insert_card()

<WelcomeScreen>:
    name: 'welcome'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        MDLabel:
            text: "Welcome to ATM"
            halign: 'center'
            font_style: 'H4'
        MDTextField:
            id: pin_input
            hint_text: "Enter PIN"
            password: True
            mode: "rectangle"
            multiline: False
        MDGridLayout:
            cols: 3
            rows: 4
            spacing: dp(10)
            MDRaisedButton:
                text: "1"
                on_release: app.update_pin_input('1')
            MDRaisedButton:
                text: "2"
                on_release: app.update_pin_input('2')
            MDRaisedButton:
                text: "3"
                on_release: app.update_pin_input('3')
            MDRaisedButton:
                text: "4"
                on_release: app.update_pin_input('4')
            MDRaisedButton:
                text: "5"
                on_release: app.update_pin_input('5')
            MDRaisedButton:
                text: "6"
                on_release: app.update_pin_input('6')
            MDRaisedButton:
                text: "7"
                on_release: app.update_pin_input('7')
            MDRaisedButton:
                text: "8"
                on_release: app.update_pin_input('8')
            MDRaisedButton:
                text: "9"
                on_release: app.update_pin_input('9')
            MDRaisedButton:
                text: "Clear"
                on_release: app.clear_pin_input()
            MDRaisedButton:
                text: "0"
                on_release: app.update_pin_input('0')
            MDRaisedButton:
                text: "Enter"
                on_release: app.enter_pin()
        MDBoxLayout:
            orientation: 'horizontal'
            spacing: dp(10)
            MDRaisedButton:
                text: "Exit"
                on_release: app.exit_app()
            MDLabel:
                id: message
                text: ""
                halign: 'center'

<TransactionScreen>:
    name: 'transaction'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        MDLabel:
            text: "Transaction Options"
            halign: 'center'
            font_style: 'H4'
        MDRaisedButton:
            text: "Check Balance"
            on_release: app.go_to_balance()
        MDRaisedButton:
            text: "Withdraw Cash"
            on_release: app.go_to_withdraw()
        MDRaisedButton:
            text: "Deposit Cash"
            on_release: app.go_to_deposit()
        MDRaisedButton:
            text: "Transaction History"
            on_release: app.go_to_history()
        MDRaisedButton:
            text: "Exit"
            on_release: app.exit_to_welcome()
        MDRaisedButton:
            text: "Close App"
            on_release: app.exit_app()

<BalanceScreen>:
    name: 'balance'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        MDLabel:
            id: balance_label
            text: ""
            halign: 'center'
            font_style: 'H4'
        MDRaisedButton:
            text: "Back"
            on_release: app.go_back_to_transaction()

<WithdrawScreen>:
    name: 'withdraw'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        MDTextField:
            id: withdraw_input
            hint_text: "Enter amount to withdraw"
            mode: "rectangle"
            multiline: False
        MDRaisedButton:
            text: "Withdraw"
            on_release: app.withdraw_cash()
        MDRaisedButton:
            text: "Back"
            on_release: app.go_back_to_transaction()
        MDLabel:
            id: message
            text: ""
            halign: 'center'

<DepositScreen>:
    name: 'deposit'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        MDTextField:
            id: deposit_input
            hint_text: "Enter amount to deposit"
            mode: "rectangle"
            multiline: False
        MDRaisedButton:
            text: "Deposit"
            on_release: app.deposit_cash()
        MDRaisedButton:
            text: "Back"
            on_release: app.go_back_to_transaction()
        MDLabel:
            id: message
            text: ""
            halign: 'center'

<HistoryScreen>:
    name: 'history'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        MDLabel:
            id: history_label
            text: ""
            halign: 'center'
            font_style: 'H4'
        MDRaisedButton:
            text: "Back"
            on_release: app.go_back_to_transaction()
'''

class StartScreen(Screen):
    pass

class WelcomeScreen(Screen):
    pass

class TransactionScreen(Screen):
    pass

class BalanceScreen(Screen):
    pass

class WithdrawScreen(Screen):
    pass

class DepositScreen(Screen):
    pass

class HistoryScreen(Screen):
    pass

class ATMApp(MDApp):
    def build(self):
        self.balance = 500000000
        self.transaction_history = []
        Window.bind(on_key_down=self._on_keyboard_down)
        return Builder.load_string(KV)

    def insert_card(self):
        self.root.current = 'welcome'

    def update_pin_input(self, value):
        current_text = self.root.get_screen('welcome').ids.pin_input.text
        self.root.get_screen('welcome').ids.pin_input.text = current_text + value

    def clear_pin_input(self):
        self.root.get_screen('welcome').ids.pin_input.text = ''

    def enter_pin(self):
        entered_pin = self.root.get_screen('welcome').ids.pin_input.text
        if entered_pin == "1234":
            self.root.get_screen('welcome').ids.message.text = "Access Granted"
            self.root.current = 'transaction'
        else:
            self.root.get_screen('welcome').ids.message.text = "Access Denied"
            self.clear_pin_input()

    def go_to_balance(self):
        self.root.get_screen('balance').ids.balance_label.text = f"Your balance is ${self.balance:.2f}"
        self.root.current = 'balance'

    def go_to_withdraw(self):
        self.root.current = 'withdraw'

    def go_to_deposit(self):
        self.root.current = 'deposit'

    def go_to_history(self):
        history = "\n".join(self.transaction_history)
        self.root.get_screen('history').ids.history_label.text = f"Transaction History:\n{history}"
        self.root.current = 'history'

    def withdraw_cash(self):
        amount = self.root.get_screen('withdraw').ids.withdraw_input.text
        try:
            amount = float(amount)
            if self.balance >= amount:
                self.balance -= amount
                self.transaction_history.append(f"Withdraw: ${amount:.2f}")
                self.root.get_screen('withdraw').ids.message.text = "Please collect your cash"
            else:
                self.root.get_screen('withdraw').ids.message.text = "Insufficient balance"
        except ValueError:
            self.root.get_screen('withdraw').ids.message.text = "Invalid amount"

    def deposit_cash(self):
        amount = self.root.get_screen('deposit').ids.deposit_input.text
        try:
            amount = float(amount)
            self.balance += amount
            self.transaction_history.append(f"Deposit: ${amount:.2f}")
            self.root.get_screen('deposit').ids.message.text = "Cash deposited successfully"
        except ValueError:
            self.root.get_screen('deposit').ids.message.text = "Invalid amount"

    def go_back_to_transaction(self):
        self.root.current = 'transaction'

    def exit_to_welcome(self):
        self.root.current = 'welcome'
        self.clear_pin_input()
        self.root.get_screen('welcome').ids.message.text = ""

    def exit_app(self):
        MDApp.get_running_app().stop()

    
    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 8:  # Backspace key
            self.clear_pin_input()

if __name__ == '__main__':
    ATMApp().run()