# ATM App
This is a simple ATM application built using Kivy and KivyMD. The app simulates basic ATM functionalities like inserting a card, entering a PIN, checking balance, withdrawing cash, depositing cash, and viewing transaction history.

## Features
- Insert Card: Start the ATM interaction.
- Enter PIN: Validate the user with a PIN.
- Check Balance: View the current balance.
- Withdraw Cash: Withdraw a specified amount of cash.
- Deposit Cash: Deposit a specified amount of cash.
- View Transaction History: View a list of past transactions.

## Screens
1. **Start Screen**: Initial screen where the user can insert their card.
2. **Welcome Screen**: Screen to enter the PIN.
3. **Transaction Screen**: Menu for different transaction options.
4. **Balance Screen**: Display the current balance.
5. **Withdraw Screen**: Screen to enter the amount to withdraw.
6. **Deposit Screen**: Screen to enter the amount to deposit.
7. **History Screen**: Display the transaction history.

## How to Run

1. **Install dependencies**:
   - Install Kivy and KivyMD if not already installed:
     ```bash
     pip install kivy kivymd
     ```

2. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/atm-app.git
   cd atm-app
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

## Code Overview
- `main.py`: The main file that contains the app logic and screen management.
- `kv`: The Kivy language string that defines the UI layout.

### Key Methods
- **insert_card**: Moves to the welcome screen to enter the PIN.
- **update_pin_input**: Updates the PIN input field with the entered value.
- **clear_pin_input**: Clears the PIN input field.
- **enter_pin**: Validates the entered PIN and navigates to the transaction screen if the PIN is correct.
- **go_to_balance**: Displays the current balance.
- **go_to_withdraw**: Navigates to the withdraw screen.
- **go_to_deposit**: Navigates to the deposit screen.
- **go_to_history**: Displays the transaction history.
- **withdraw_cash**: Withdraws the entered amount if the balance is sufficient.
- **deposit_cash**: Deposits the entered amount.
- **go_back_to_transaction**: Navigates back to the transaction screen.
- **exit_to_welcome**: Exits to the welcome screen.
- **exit_app**: Exits the application.

## Customization
- **Logo**: Replace `atm_logo.png` with your own image in the `StartScreen` section of the KV string.
- **PIN**: Change the hardcoded PIN in the `enter_pin` method if necessary.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
Special thanks to the open-source community and everyone who provided support and guidance during the development of this project.

## Contact
If you have any questions, feel free to reach out:
- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/sivapriya-b-3b2a72294/)
- Github: [Github Profile](https://github.com/SIVAPRIYA-3065)
