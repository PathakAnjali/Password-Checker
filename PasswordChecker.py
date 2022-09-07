import requests  
import hashlib  
import sys


# requesting url
def req_api(pswrd):
    url = 'https://api.pwnedpasswords.com/range/' + pswrd
    res = requests.get(url, allow_redirects=False)
    
    print(res.status_code)                                # to check the success status 20 (optional)


    if res.status_code != 200:
        raise RuntimeError(f'wrong url found {res.status_code},check it again')
    return res


# for getting the matched passwords

def read_req_api(r):                                      
    print(r.text)



# for getting the leaked password counts

def get_leaked_pswrd(hashes, hash_to_be_check):
    hashed = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashed:
        if h == hash_to_be_check:
            return count
    return 0



# code to check password

def checkPwned_Pass(password):
    # Using hashing type SHA1 to hash the  password
    ShaHashpass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()                   

    # TO GET THE FIRST FIVE CHAR OF PASSWORD AND THE REST CHARACTERS IN ANOTHER VARIABLE
    HeadFivechar, tail = ShaHashpass[:5], ShaHashpass[5:]
    response = req_api(HeadFivechar)

    # calling  read_req_api
    # return read_req_api(response)
    return get_leaked_pswrd(response, tail)

# checkPwned_Pass('123')


def main(args):
    for password in args:
        count = checkPwned_Pass(password)
        if count:
            print(f'{password} is found {count} times, you should change the password!!')
        else:
            print("Carry On!!")
    return "Done"


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))  # sys.exit going to return Done ,as it exits throufg the function return statements



    
# hashlib.sha1(password.encode('utf-8') > output as object so to convert 'hexdigest' method is used.
# and then to convert the string in upper case.
# hexdigest : returned as a string object twice the length , containing only hexadecimal digits....


# url = 'https://api.pwnedpassword.com/range/' + 'password'  
# Ex:  cbfdac6008f9cab4083784cbd1874f76618d2a97 is the hashed password of password123, using SHAH1 Hash generator
