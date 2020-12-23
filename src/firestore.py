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

    def update(self, collection, id, payload):
        doc = self.db.collection(collection).document(id)
        doc.update(payload)

    def list(self, collection):
        docs = self.db.collection(collection).stream()
        doc_list = []
        for doc in docs:
            doc_dict = doc.to_dict()
            doc_dict['id'] = doc.id
            doc_list.append(doc_dict)
        return doc_list

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
