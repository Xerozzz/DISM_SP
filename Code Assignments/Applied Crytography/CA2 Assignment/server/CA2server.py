import socket
import time
from datetime import datetime
from datetime import date
import calendar
import uuid
from time import gmtime, strftime
import csv
from Crypto.Cipher import AES
import random
from Cryptodome.Random import get_random_bytes
from Cryptodome.Signature import pkcs1_15
from Cryptodome.PublicKey import RSA
from Crypto.Signature import pss
import sys,traceback
from Cryptodome.Hash import SHA256
import pickle
import Crypto
from Crypto.Cipher import PKCS1_OAEP
import ast
secret_phrase = 'hi'

def check(menuEncoded):
    global secret_phrase
    privkey_bytes = open('Serverprivatekey.der' , 'rb').read()
    if len(privkey_bytes) == 0:
        return key_generator(secret_phrase,menuEncoded)
    else:
        return key_importer(secret_phrase,menuEncoded)
# Function to check whether a key is present or not
def key_generator(secret_phrase,menuEncoded):
    rsakey_pair=RSA.generate(2048)
    return key_exporter(secret_phrase,rsakey_pair,menuEncoded)
# Function to generate a key if there is none detected
def key_exporter(secret_phrase,rsakey_pair,menuEncoded):
    prikey_in_der=rsakey_pair.export_key(format="DER", passphrase=secret_phrase, pkcs=8,protection="scryptAndAES128-CBC")
    try:
        open("Serverprivatekey.der","wb").write(prikey_in_der)
        print("Export private key has been completed")
    except:
        print("Opps! failed to export the private key")
        sys.exit(-1)
    pubkey_in_pem=rsakey_pair.publickey().exportKey()
    try:
        open("Serverpublickey.pem","wb").write(pubkey_in_pem)
        print("Export public key has been completed")
    except:
        print("Opps! failed to export the public key")
        sys.exit(-1)
    return key_importer(secret_phrase,menuEncoded)
# Function to export the key to a file
def key_importer(secret_phrase,menuEncoded):
    prikey_bytes=open("Serverprivatekey.der","rb").read()
    restored_keypair=RSA.import_key(prikey_bytes,passphrase=secret_phrase)
    pubkey_bytes=open("Serverpublickey.pem","r").read()
    restored_pubkey=RSA.import_key(pubkey_bytes)
    return signer(restored_keypair , restored_pubkey , menuEncoded)
# Function to import a key in case needed
def signer(privateKey , publicKey ,menuEncoded):
    data = menuEncoded
    hashedMessage = SHA256.new(data)
    signature = pss.new(privateKey).sign(hashedMessage)
    return signature
# Function to sign data with the server's private key
def verifier(menuToVerify , con):
    signature = menuToVerify.pop() # Removing the last item as it is the signature that was appended
    menuBytes = (menuToVerify.pop()).decode()
    key = RSA.import_key(open('Clientpublickey.pem').read())
    hashedMessage = SHA256.new(menuBytes.encode())
    verifier = pss.new(key)
    try:
        verifier.verify(hashedMessage , signature) # Verifing the signature by recreating it 
        with open('ServerSignatureAuthenticator.txt' , 'w') as f:
            f.write(f'Signature is authentic.\nFrom Server at {dateToday}')
        return True
    except(ValueError , TypeError):
        sys.exit()
# Function to verify signature
def RSA_decrypter(items):
    global secret_phrase
    encrypted_aeskey=items[0]
    private_key_der = open('Serverprivatekey.der', 'rb').read()
    RSA_privatekey = RSA.import_key(private_key_der, passphrase=secret_phrase)
    decryptor = PKCS1_OAEP.new(RSA_privatekey)
    decrypted_aeskey = decryptor.decrypt(encrypted_aeskey)
    return decrypted_aeskey
# Function to Decrypt RSA from client
def cateringOptions(con):
    previewDay = con.recv(255)
    print(previewDay)
    Day = (previewDay.decode()).capitalize()
    with open(f'{Day}.txt') as preview:
        menuExtracted = preview.read()# Before menu is sent , hashed with sha256 and encrypted with the client secret key.(to create a digital signature)
        menuEncoded = menuExtracted.encode()
        con.sendall(menuEncoded)
        print("Menu has been successfully sent over to the client")
# Preorder Function
def menuPrep(con):
    print("connected")
    while True:
        buf = con.recv(255)
        choice = buf.decode()
        if choice == '1':
            with open(f'{dateToday}.txt') as file:
                menuExtracted = file.read()
                signature = check((menuExtracted).encode()) #Input RSA signing code here
                menuList = menuExtracted.split(sep=',') # Before menu is sent , hashed with sha256 and encrypted with the client secret key.(to create a digital signature)
                menuList.append(signature) # Appending the signature as the last item of the list
                con.sendall(pickle.dumps(menuList)) # encoding before sending
                print("Menu has been successfully sent over to the client")
                break
        elif choice == '2':
            return cateringOptions(con)
        elif choice == '3':#Admin login fucntion
            return adminLogin(con)
        elif choice == '4':
            return adminAdd(con)
        elif choice == '5':
            return adminRemove(con)
        else:
            buf = pickle.loads(con.recv(2048))
            print("logging file")
            return fileLogging(con , buf)
# Main function that splits and formats the menu
def encrypting(msg , hash_key):
    BLOCK_SIZE = 16
    PAD = '{'# If the last block is incomplete, padding required
    padding = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PAD
    Cipher = AES.new(hash_key , AES.MODE_ECB)
    result = Cipher.encrypt(padding(msg).encode('utf-8'))
    return result
# Function for AES encryption
def fileLogging(con, fileContents):
    global my_id,timeNow,datetime
    AES_key = "WmZq4t7w!z%C*F-J".encode()    #AES Key
    count = 1
    items = con.recv(255).decode()
    price = RSA_decrypter(fileContents)
    fileContents[0] = price
    if verifier(fileContents , con) == True:
        print("reached here")
        priceEncrypt = encrypting(items,AES_key)
        with open('logfile.txt' , 'a') as f:
            f.write(f'\n\n{str(dateToday)}\n=====Client session:{str(my_id)}=====\nClient made a payment of ${priceEncrypt} at {timeNow}')
            clientItems = items.split(sep='\n')
            clientItems.remove(clientItems[-1])
            for food in clientItems:
                # Code to encrypt starts here... here is the AES code
                encrypted_food = encrypting(food,AES_key)
                f.write(f'\n{count}: {encrypted_food}')# This is the part where we store the items in the file
                count = count+1
            f.write('\n=============================================================')
    ack = 'ack' 
    ackL = []
    signature = check(ack.encode())
    ackL.append(ack)
    ackL.append(signature)
    con.sendall(pickle.dumps(ackL))
# Function that logs the file with information from the client
def adminLogin(con):
    credentials = con.recv(255)
    combinedCredentials = credentials.decode()
    print(combinedCredentials)
    credentialsUser = combinedCredentials.split(sep=',')
    with open('admin.txt' , 'r') as file:
        file_reader = csv.reader(file)
        username = credentialsUser[0]
        password = credentialsUser[1]
        user_find(file_reader,username,password,con)
# Function that allows the admin to login 
def user_find(file,username,password,con):
    for row in file:
        if row[0] == username:
            print('Username found', username)
            user_found = [row[0],row[1]]
            pass_check(user_found,password,con)
            break
        else:
            msgToSendBack = 'no'
            encodedMsgToSendBack = msgToSendBack.encode()
            con.send(encodedMsgToSendBack)
# Function that searchs for admin user name in files
def pass_check(user_found,password,con):
    if user_found[1]==password:
        print('Password found')
        msgToSendBack = 'yes'
        encodedMsgToSendBack = msgToSendBack.encode()
        con.send(encodedMsgToSendBack)
        return adminRights(con)
    else:
        print("password incorrect")
        msgToSendBack = 'no'
        encodedMsgToSendBack = msgToSendBack.encode()
        con.send(encodedMsgToSendBack)
# Function that searchs for passwords in files
def adminRights(con):
    adminChoice = con.recv(255)
    decodedChoice = adminChoice.decode()
    if decodedChoice == '1':
        return adminAdd(con)
    elif decodedChoice == '2':
        print('reached here')
        return adminRemove(con)

def adminAdd(con):#Before menu is updated, it has to be encrytped with AES to match the top
    updatedMenu = con.recv(2048)
    decodedMenu = updatedMenu.decode()
    preUpdate = list(decodedMenu)
    preUpdate.pop()
    decodedMenu = ''.join(preUpdate)
    with open(f'{dateToday}.txt' , 'w') as file:
        file.write(decodedMenu)
    print('Menu has been updated')

def adminRemove(con):#Before menu is updated, it has ot be encrytped with AES to match the top
    updatedMenu = con.recv(2048)
    decodedMenu = updatedMenu.decode()
    preUpdate = list(decodedMenu)
    preUpdate.pop()
    decodedMenu = ''.join(preUpdate)
    with open(f'{dateToday}.txt' , 'w') as file:
        file.write(decodedMenu)
    print('Menu has been updated')

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('0.0.0.0', 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections
while True:
    timeNow = strftime("%H:%M:%S", gmtime())
    my_id = uuid.uuid1() #UUID should be encrypted with AES before it is stored as a ahcker might be able to replicate it .
    my_date = date.today()
    dateToday =calendar.day_name[my_date.weekday()]
    print('\n',f'\n{dateToday}')
    print("waiting a new call at accept()")
    connection, address = serversocket.accept()
    if menuPrep(connection) == 'file':
        None
print("Server stops")