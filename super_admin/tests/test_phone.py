from phonenumber_field.phonenumber import to_python

# Sustituye con el número que te está dando problemas
phone = to_python("+584141234567") 

print(f"¿Es válido?: {phone.is_valid()}")

if not phone.is_valid():
    # Esto te dirá qué formato esperaba la librería
    from phonenumbers import is_possible_number
    print(f"¿Es siquiera posible?: {phone.is_possible()}")