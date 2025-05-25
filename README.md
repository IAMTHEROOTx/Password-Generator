# Password Generator

---

## 🔐 Description

**Password Generator** is a simple Python tool that creates **strong**, **random**, and **unique** passwords using a customizable character set. It is designed to be lightweight, fast, and easy to use.

---

## 🧰 Features

- Random password generation
- Customizable length
- Uses a secure mix of:
  - Lowercase letters
  - Digits
  - Special characters

---

## ⚙️ Requirements

- Python 3.x  
- [`art`](https://pypi.org/project/art/) module (for ASCII art banner)

Install required module using:

```bash
pip install art
```

---

## 💡 Usage

Run the script:

```bash
python password_generator.py
```

You will be prompted to enter the desired password length:

```text
Choose how many characters your password should have:
```

The tool will then generate and display your password, along with its length:

```text
Generated password is:
<your_password_here>

Your password is 16 characters long.
```

---

## 📄 Example Output

```text
This program generates unique and strong passwords

Choose how many characters your password should have:
> 16

Generated password is:

g^2=+8x#;y&<0a/

Your password is 16 characters long.
```

---

## 🧠 How It Works

- Uses Python's `random` module to generate characters
- Uses the `art` module to display ASCII banners
- Generates passwords from a custom character set:
  ```
  abcdefghijklmnopqrstuwxyz1234567890()=^:/-#~&^@=+*!;<>.
  ```

---

## 📁 File Structure

```text
password_generator.py     # Main script
```

---

## 📝 License

This project is open-source and free to use, modify, and distribute.

---

Enjoy creating secure passwords! 🔐  
