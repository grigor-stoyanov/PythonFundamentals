class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


msg = input()
emails = []
while not msg == 'Stop':
    tokens = msg.split(' ')
    sender = tokens[0]
    receiver = tokens[1]
    content = tokens[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    msg = input()
sent = [int(ele) for ele in input().split(', ')]
for ele in sent:
    emails[ele].send()
for i in range(len(emails)):
    print(emails[i].get_info())