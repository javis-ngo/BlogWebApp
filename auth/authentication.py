import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyDWkspNd1a_1z0ccGBlTBHNVuV6DdAaZVY",
  'authDomain': "my-project-a382e.firebaseapp.com",
  'projectId': "my-project-a382e",
  'storageBucket': "my-project-a382e.firebasestorage.app",
  'messagingSenderId': "105146903618",
  'appId': "1:105146903618:web:dd066063c90235468fd1db",
  'measurementId': "G-8GT6EPTH8C",
  'databaseURL': ""
}

def test_firebase():
  firebase = pyrebase.initialize_app(firebaseConfig)
  auth = firebase.auth()
  email = 'test@gmail.com'
  password = '123456'
  user = auth.create_user_with_email_and_password(email, password)
  print(user)


if __name__ == "__main__":
    test_firebase()