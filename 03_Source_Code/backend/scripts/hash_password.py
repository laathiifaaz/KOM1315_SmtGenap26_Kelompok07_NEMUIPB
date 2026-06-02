from passlib.context import CryptContext

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

password = "password"  # pastikan ini string biasa
hashed = pwd.hash(password)

print(hashed)