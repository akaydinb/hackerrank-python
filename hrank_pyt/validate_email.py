import re

# Validating Email Addresses With a Filter

def fun(s):
    return bool(re.match(r"^[\w-]+@[0-9a-zA-Z]+\.\w{1,3}$", s));
    #return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]{1,3}", s));
    # return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
