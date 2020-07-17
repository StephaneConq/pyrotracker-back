import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth

# Use a service account
cred = credentials.Certificate('credentials/firebase-service-account.json')
firebase_admin.initialize_app(cred)


class FirestoreIO:

    def __init__(self):
        self.db = firestore.client()

    def insert(self, collection, data):
        self.db.collection(collection).add(data)

    def delete(self, collection, id):
        self.db.collection(collection).document(id).delete()

    def list_users(self):
        users = []
        page = auth.list_users()
        while page:
            for user in page.users:
                users.append({
                    "uid": user.uid,
                    "displayName": user.display_name,
                    "email": user.email,
                    "photoURL": user.photo_url,
                })
            page = page.get_next_page()

        return users
