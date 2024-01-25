from functions import add_contact, contact_detail, delete_contact, list_contacts, list_favorites, toggle_star, update_contact

contacts = []

while True:
  print(" \n📒 AGENDA\n")
  print(" 1. Adicionar um contato")
  print(" 2. Visualizar a lista de contatos cadastrados")
  print(" 3. Editar um contato")
  print(" 4. Marcar/desmarcar um contato como favorito")
  print(" 5. Ver uma lista de contatos favoritos")
  print(" 6. Apagar um contato")
  print(" 7. Detalhar um contato")
  print(" 8. Sair")

  option = input("\n Digite a opção desejada: ")

  if option == "1":
    name = input("\n Nome: ")
    phone = input(" Telefone: ")
    email = input(" Email: ")
    add_contact(contacts, name, phone, email)
  elif option == "2":
    list_contacts(contacts)
  elif option == "3":
    list_contacts(contacts)
    indice = input("\n Contato a ser atualizado: ")
    print(" Dados para atualização:")
    name = input(" Nome: ")
    email = input(" Email: ")
    phone = input(" Telefone (somente números): ")
    update_contact(contacts, indice, name, phone, email)
  elif option == "4":
    list_contacts(contacts)
    indice = input("\n Escolha o contato: ")
    toggle_star(contacts, indice)
  elif option == "5":
    list_favorites(contacts)
  elif option == "6":
    list_contacts(contacts)
    indice = input("\n Escolha o contato a ser removido: ")
    delete_contact(contacts, indice)
  elif option == "7":
    list_contacts(contacts)
    indice = input("\n Escolha o contato: ")
    contact_detail(contacts, indice)
  elif option == "8":
    print("\n ✨Agenda encerrada!✨\n")
    break


