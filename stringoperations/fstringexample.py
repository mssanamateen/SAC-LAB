name = "Alice"
pi = 3.14159265

print(f"Name: {name:10}")      # width 10 → "Alice     "
print(f"Pi: {pi:.2f}")         # precision 2 → "3.14"
print(f"Pi: {pi:8.3f}")        # width 8, precision 3 → "   3.142"
print(f"Sum: {10+20}")         # expressions allowed → "30"
