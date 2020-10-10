# Chapter 11: Secure Electronic Transaction (SET)

Created: Feb 13, 2020 11:17 PM
Updated: Apr 6, 2020 7:56 PM

**Secure Electronic Transactions (SET):**

Details:

- Open encryption and security specification to protect Internet CC transactions
- Developed in 1996 by Mastercard and Visa
- Not a payment system, rather a set of security protocols and formats
    - Secure communications among parties
    - Trust from use of X.509v3 certificates
    - Privacy by restricted info to those who need it

Components:

[Chapter%2011%20Secure%20Electronic%20Transaction%20(SET)%20d1b8df00c2034c53972533e4551c3b69/untitled](Chapter%2011%20Secure%20Electronic%20Transaction%20(SET)%20d1b8df00c2034c53972533e4551c3b69/untitled)

Transaction:

- 1. Customer opens account
- 2. Customer receives a certificate
- 3. Merchants have their own certificates
- 4. Customer places an order
- 5. Merchant is verified
- 6. Order and payment are sent
- 7. Merchant requests payment authorization
- 8. Merchant confirms order
- 9. Merchant provides goods or service
- 10. Merchant requests payment

**Dual Signature:**

Details:

- Purpose of dual signatures is to link two messages that are intended for two different recipients by the same sender
- Customer creates dual messages
    - Order information (OI) for merchant
    - Payment Information (PI) for bank
- Neither party needs details of other but must know they are linked
- Use a dual signature for this

How it works:

- When customer wants to send OI to the merchant and the PI to the bank, the two items must be linked in a way that can be used to resolve disputes if necessary
- It prevents merchant from fabricating the OI and claims that the the original OI
- Linkage prevents it and link is needed so that customer can prove that payment is intended for this order
- Customer takes the hash using SHA-1 of PI and hash of OI, concatenates them, and hashes the results
- Finally, the customer encrypts the final hash with his or her private signature key, creating the dual signature
- The merchant does not need to know customer's CC number, and the bank does not need to know details of customer's order

**SET Purchase Request:**

Exchange of Messages:

- 1. Initiate Request - Get certificates
- 2. Initiate Response - Signed response
- 3. Purchase Request - of OI and PI
- 4. Purchase Response - ACK order

Purchase Request - Merchant:

- Verifies cardholder certificates using CA sigs
- Verifies dual signature using customer's public signature key to ensure order has not been tampered with in transit & that it was signed using cardholder's private signature key
- Processes order and forwards the payment information to the payment gateway for authorization
- Sends a purchase response to cardholder

**Payment Gateway Authorization:**

- Verifies all certificates and decrypts digital envelope of authorization book to obtain symmetric key & then decrypts authorization block
- Verifies merchant's signature on authorization block
- Decrypts digital envelope of payment block to obtain symmetric key & then decrypts payment block
- Verifies dual signature on payment block
- Verifies that transaction ID received from merchant matches that in PI received from customer
- Requests & receives an authorization from issuer
- Sends authorization response back to merchant

**Payment Capture:**

- Merchant sends payment gateway a payment capture reqeust
- Gateway checks request then causes funds to be transferred to merchants accounts
- Notifies merchant using capture response