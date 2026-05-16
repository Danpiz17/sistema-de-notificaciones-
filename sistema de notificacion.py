from abc import ABC, abstractmethod

class Notificacion(ABC):

    @abstractmethod
    def enviar(self):
        pass


class EmailNotificacion(Notificacion):

    def __init__(self, destinatario, asunto, cuerpo):
        self.destinatario = destinatario
        self.asunto = asunto
        self.cuerpo = cuerpo

    def enviar(self):
        return f"""
===== EMAIL ENVIADO =====
Destinatario: {self.destinatario}
Asunto: {self.asunto}
Mensaje: {self.cuerpo}
"""


class SMSNotificacion(Notificacion):

    LIMITE = 160

    def __init__(self, numero, mensaje):
        self.numero = numero
        self.mensaje = mensaje

    def enviar(self):

        if len(self.mensaje) > self.LIMITE:
            return "Error: El SMS supera el límite de 160 caracteres."

        return f"""
===== SMS ENVIADO =====
Número: {self.numero}
Mensaje: {self.mensaje}
Caracteres usados: {len(self.mensaje)}
"""


# --------------------------
# MENÚ INTERACTIVO
# --------------------------

while True:

    print("\n=== SISTEMA DE NOTIFICACIONES ===")
    print("1. Enviar Email")
    print("2. Enviar SMS")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        destinatario = input("Correo destinatario: ")
        asunto = input("Asunto: ")
        cuerpo = input("Mensaje: ")

        email = EmailNotificacion(destinatario, asunto, cuerpo)

        print(email.enviar())

    elif opcion == "2":

        numero = input("Número de teléfono: ")
        mensaje = input("Mensaje SMS: ")

        sms = SMSNotificacion(numero, mensaje)

        print(sms.enviar())

    elif opcion == "3":

        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")
