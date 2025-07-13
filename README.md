# Telegram Gift Auto-Buyer  
**Python 3.12.3 | Telethon**  

⚠ **WARNING** ⚠  
Before proceeding:  
- Ensure you have read the instructions below.  
- Running `main.py` without a relevant `dark_list.txt` may result in **loss of Stars**.  

---

## **Installation**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/LNucky/Telegram_Gift_Auto_Buyer.git
   ```  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Copy `.env.example` to `.env`:  
   ```bash
   cp .env.example .env
   ```  
4. Fill `.env` with your credentials.  
5. Run `create_dark_list.py`:  
   ```bash
   python create_dark_list.py
   ```  
6. Log in to your Telegram account when prompted. This generates a `session.session` file.  
7. Verify that `dark_list.txt` in the directory. Now it mustcontains up-to-date data. If so, setup is complete!  

---

## **Usage**  
1. Ensure `dark_list.txt` contains up-to-date data. If not, rerun `create_dark_list.py`.  
2. Start the auto-buyer:  
   ```bash
   python main.py
   ```  
   The script will now monitor Telegram for new gifts and purchase them instantly.  

---

## **Contacts**  
Telegram: [@JOHMER](https://t.me/JOHMER)  