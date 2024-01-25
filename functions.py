def add_contact(contacts, name, phone, email):
  try:
    info = {
      "name": name,
      "phone": int(phone),
      "email": email,
      "favorite": False
    }
    
    contacts.append(info)
    print("\n Contato adicionado com sucesso!\n")
  except ValueError as e:
    print(f"Error: {e}")
  return

def list_contacts(contacts):
  if len(contacts) == 0:
    return print("\n Agenda vazia!!!")
  for indice, value in enumerate(contacts, start=1):
    star = "⭐" if value["favorite"] else "  "
    print(f" {star} {indice}. {value["name"]}")
  return

def update_contact(contacts, indice, name=None, email=None, phone=None):
  i = int(indice) - 1
  if i < 0 or i > len(contacts):
    return "Índice inválido!"
  if name:
    contacts[i]["name"] = name
  if email:
    contacts[i]["email"] = email
  if phone:
    contacts[i]["phone"] = int(phone)
  return print("\n Contato atualizado com sucesso!!!")

def toggle_star(contacts, indice):
  i = int(indice) - 1
  if i < 0 or i > len(contacts):
    return "Índice inválido!"
  if contacts[i]["favorite"]:
    contacts[i]["favorite"] = False
  else:
    contacts[i]["favorite"] = True
  return list_contacts(contacts)

def list_favorites(contacts):
  for i, v in enumerate(contacts, start=1):
    if v["favorite"]:
      print(f" {i}. {v["name"]}")
  return

def delete_contact(contacts, indice):
  i = int(indice) - 1
  if i < 0 or i > len(contacts):
    return print("\n Índice inválido.")
  del contacts[i]
  print("\n Contato removido com sucesso!!!\n")
  return list_contacts(contacts)

def contact_detail(contacts, indice):
  i = int(indice) - 1
  if i < 0 or i > len(contacts):
    return print("\n Índice inválido.")
  contact = contacts[i]
  print(f"\n Nome: {contact["name"]}")  
  print(f" Email: {contact["email"]}")  
  print(f" Telefone: {contact["phone"]}")
  return  