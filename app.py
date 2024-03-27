from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_geek():
  return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
    <div class="container">
        <h1>Perfil de Usuario</h1>
        <style>
                body {
              font-family: Arial, sans-serif;
              margin: 0;
              padding: 0;
              background-color: #f0f0f0;
          }
          .container {
              max-width: 800px;
              margin: 20px auto;
              background-color: #fff;
              padding: 20px;
              border-radius: 8px;
              box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
          }
          h1 {
              text-align: center;
              margin-bottom: 20px;
          }
          .profile {
              display: flex;
              align-items: center;
              justify-content: center;
              flex-direction: column;
          }
          .profile img {
              width: 150px;
              height: 150px;
              border-radius: 50%;
              margin-bottom: 10px;
          }
          .profile h2 {
              margin-bottom: 5px;
          }
          .profile p {
              color: #666;
          }
        </style>
        <div class="profile">
            <img src="https://cdn.kibrispdr.org/data/862/user-icon-png-transparent-11.png" alt="Avatar">
            <h2>Lennyn Bendezu</h2>
            <p>Correo electrónico: i2227613@continental.edu.pe</p>
            <p>Teléfono: 123456789</p>
            <p>Fecha de Nacimiento: 01/01/1900</p>
            <p>Ubicación: Huancayo, Perú</p>
        </div>
    </div>
    </body>
    </html>
    '''


if __name__ == "__main__":
  app.run(debug=True)

