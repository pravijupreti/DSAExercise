s = input().lower()
counter = 0
for ch in s:
    if ch in ("a","e","i","o","u"):
        counter +=1
print(f"Number of vowels:{counter}")

cout = sum(1 for ch in s if ch in ("aeiou"))
print(f"{cout}")