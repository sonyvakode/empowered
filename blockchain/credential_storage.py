# blockchain/credential_storage.py

from aptos_sdk.client import RestClient
from aptos_sdk.account import Account
from aptos_sdk.transaction import EntryFunction
from aptos_sdk.types import TxnBuilderTypes
from aptos_sdk.bcs import Serializer
import json

# Setup the Aptos client and network
node_url = "https://fullnode.devnet.aptoslabs.com"
client = RestClient(node_url)

# Define your account
private_key = "YOUR_PRIVATE_KEY"
account = Account.from_private_key(private_key)

def store_credentials(student_id, student_name, student_grade):
    """
    Store student credentials on the Aptos blockchain.

    Args:
        student_id (str): The student’s ID.
        student_name (str): The student’s name.
        student_grade (str): The student's grade.
    """
    # Create an EntryFunction for the transaction
    payload = EntryFunction.natural(
        "0x1::credential_storage",
        "store_credentials",
        [student_id, student_name, student_grade],
    )

    # Build and sign the transaction
    txn = client.generate_transaction(account.address, payload)
    signed_txn = client.sign_transaction(account, txn)

    # Submit the transaction
    txn_result = client.submit_transaction(signed_txn)
    txn_result.wait_for_confirmation()

    print(f"Transaction {txn_result.txn_id} successfully submitted!")
    
# Example usage
store_credentials("12345", "John Doe", "A")
