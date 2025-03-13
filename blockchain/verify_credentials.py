# blockchain/verify_credentials.py

from aptos_sdk.client import RestClient
from aptos_sdk.account import Account
from aptos_sdk.transaction import EntryFunction
from aptos_sdk.types import TxnBuilderTypes
import json

# Setup the Aptos client and network
node_url = "https://fullnode.devnet.aptoslabs.com"
client = RestClient(node_url)

def verify_credentials(student_id, student_name, student_grade):
    """
    Verify student credentials from the Aptos blockchain.

    Args:
        student_id (str): The student’s ID.
        student_name (str): The student’s name.
        student_grade (str): The student's grade.
    """
    # Query for credentials stored in the blockchain
    payload = EntryFunction.natural(
        "0x1::credential_storage",
        "get_credentials",
        [student_id]
    )
    
    txn_result = client.submit_transaction(payload)
    
    # Wait for the result of the transaction
    txn_result.wait_for_confirmation()
    
    # Parse the returned credentials
    stored_credentials = txn_result.result  # This assumes the result is in the form of a JSON object

    if stored_credentials.get("student_name") == student_name and stored_credentials.get("student_grade") == student_grade:
        print("Credentials verified successfully!")
    else:
        print("Credentials mismatch!")

# Example usage
verify_credentials("12345", "John Doe", "A")
