def S2N_littendian(s):
    tot = 0
    esp = 0
    for c in s:
        tot = tot + 256**esp * ord(c)
        esp += 1
    return tot

def S2Ne_littlendian(s):
    tot = 0
    for c in s[::-1]:
        tot = (tot << 8) | ord(c)
    return tot


def hex_converter(num_hex: str) -> int | None:
    num_hex = num_hex.replace(":", "")
    num_hex = num_hex.replace("\n", "")
    try:
        return int(num_hex, 16)
    except ValueError:
        print("Input non valido")
        return None
    
    
def message_conversion(message:str):
    new_message = int.from_bytes(message.encode(),byteorder="big")
    return new_message

def int_to_string(message:int)->str:
    new_message = message.to_bytes((message.bit_length() + 7) // 8, byteorder='big').decode()
    return new_message






def cypher_rsa(message:int, p_exponent:int, modulus:int)->int:
    rsa_cypher= pow(message,p_exponent,modulus)
    return rsa_cypher


def decypher_rsa(int_message:int, priv_exponent:int, modulus:int):
    rsa_decypher=pow(int_message,priv_exponent,modulus)
    return rsa_decypher

    


modulus = "00:d3:c6:42:8c:fb:01:33:08:b1:ca:30:ff:74:73:a5:a8:35:3f:de:eb:82:c6:ee:a7:5d:b3:19:73:4e:13:08:6f:23:97:4b:1d:4f:36:7b:ef:d2:02:0b:fa:02:3a:0e:9d:c6:7c:78:d5:64:d0:e2:9e:18:58:a1:4b:f3:f2:c2:b9:94:9d:c9:7f:4e:c1:c5:4f:dd:30:ae:4f:60:c5:c1:e1:b8:43:96:47:d7:6c:1c:be:1f:b3:cc:9c:6c:00:21:8f:ae:7e:2d:e8:31:2f:04:2b:97:88:e4:71:4d:a3:eb:90:75:a3:31:ce:d4:c5:3d:02:ce:8d:ba:25:08:6c:85:38:92:1c:f4:92:9d:7b:63:c6:5a:36:68:f8:b3:76:d7:73:71:d2:ac:33:81:69:6e:09:74:68:6b:72:fe:93:51:b8:ca:ce:98:ac:c2:43:ee:6b:68:ce:c0:66:5b:eb:7e:e4:32:f3:ae:cc:b7:7a:59:9f:44:40:73:4e:24:b1:f2:2e:a1:58:2b:d0:f0:5b:ec:34:49:6c:ad:15:d9:1f:21:93:5c:46:5c:2d:79:75:45:33:72:98:29:12:20:4e:1d:0d:d6:ec:e8:51:f0:f8:c4:70:ab:66:0b:08:36:d6:c8:aa:95:63:ba:05:fd:86:e6:4c:a1:3a:ba:15:e2:cf:75:63"

privateExponent = "23:4b:b5:c2:29:d5:88:81:72:f7:08:2a:93:68:9b:9c:08:df:fa:7c:95:cb:d2:71:3a:48:84:3d:e2:58:81:67:db:43:e1:da:37:de:69:fd:4d:ab:01:ff:00:5f:02:6f:a1:14:be:ce:3b:78:25:c5:04:0e:c5:8c:a8:a8:75:c9:98:c4:f6:ea:8d:20:4b:8d:4f:88:1d:0d:3a:cb:a0:50:49:60:99:0b:f9:3c:af:75:05:48:a2:1a:12:00:05:97:f2:6a:5c:fc:08:32:80:b1:ee:96:d0:bd:8c:f0:a7:42:be:45:dd:a2:78:cb:8a:2b:22:6c:f4:5b:81:67:6b:89:20:01:82:92:89:e3:fe:ae:e7:32:f9:98:bb:7f:4f:2c:db:19:2f:50:f0:46:23:a5:42:91:88:8a:5d:a9:7d:74:c9:9c:a5:10:13:91:be:0b:30:11:98:96:52:30:f9:ce:ed:ef:02:40:51:50:09:09:b5:f8:30:b0:51:82:27:ef:2e:3e:8c:52:95:46:5a:65:6a:80:2a:a7:8a:7d:f2:3f:2b:e1:00:84:89:72:9f:a4:2f:b6:d6:7a:a4:81:c6:0c:64:ec:08:ab:1c:8b:85:eb:53:14:4e:00:99:24:45:e2:46:0e:c3:b7:db:97:09:7a:5e:4c:32:1a:08:e1:2b:83"

publicExponent= 3



message = "Ciao Stefano"
print(f"Messaggio da cifrare:{message}")
print()
num_str = message_conversion(message)
print(f"Conversione del messaggio in numero: {num_str}")
print()
esponente_privato = hex_converter(privateExponent)
modulo = hex_converter(modulus)
print(f"Conversione dell'esponente privato': {esponente_privato}")
print()
print(f"Conversione del modulo: {modulo}")
print()
cifratura = cypher_rsa(num_str,publicExponent,modulo)
print(f"Cifratura del messaggio: {cifratura}")
print()
decifratura = decypher_rsa(cifratura,esponente_privato,modulo)
print(f"Decifratura del messaggio: {decifratura}")
print()
riconversione=int_to_string(decifratura)
print(f"Riconversione del messaggio:{riconversione} ")




