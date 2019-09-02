from Pyfhel import Pyfhel, PyPtxt, PyCtxt

from commons.encryption.homomorphic_encryption import HomomorphicEncryption


class PheEncryption(HomomorphicEncryption):

    def __init__(self):
        self.HE = Pyfhel()
        self.HE.contextGen(p=65537)
        self.HE.keyGen()

    def encrypt_collection(self, public_key, collection):
        if any([type(i) == PyCtxt for i in collection]):
            return collection
        else:
            return [public_key.encrypt(i) for i in collection]

    def decrypt_collection(self, private_key, collection):
        return [private_key.decrypt(i) for i in collection]

    def decrypt_value(self, private_key, value):
        return private_key.decrypt(value)

    def get_deserialized_public_key(self, public_key):
        self.HE.savepublicKey("public_key")
        arch = open("publik_key", 'r')
        return HE.p(n=int(public_key))

    def get_encrypted_number(self, pub_key, value):
        ciphertext, exponent = value["ciphertext"], value["exponent"]
        return HE.EncryptedNumber(pub_key, int(ciphertext), int(exponent))

    def get_serialized_encrypted_number(self, value):
        return dict(ciphertext=str(value.ciphertext()), exponent=value.exponent)

    def generate_key_pair(self, key_length):
        return paillier.generate_paillier_keypair(n_length=key_length)
