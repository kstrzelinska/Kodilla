shopping_list = {
    'piekarnia': ['chleb', 'pączek', 'bułki'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}

print("Lista zakupów")
for i, j in shopping_list.items():
    # Capitalize the store name and each item in the list
    capitalized_items = [item.capitalize() for item in j]
    print(f"Idę do {i.capitalize()} i kupuję tam: {', '.join(capitalized_items)}")
    
#test
print("hello")

#zad2
for liczba in range (0,101):
  if liczba%5 == 0:
    print(liczba)  
    print(liczba**3)


