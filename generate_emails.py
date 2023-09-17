# pip install requests
# use API 1secmail.com/api (auto delete mail after 1 hour)

import requests
import random
import string
import time
import os

def get_domain_list():
	domains_req = f'{API}?action=getDomainList'
	responce = requests.get(domains_req).json()
	
	return responce

API = 'https://www.1secmail.com/api/v1/'
domain_list = get_domain_list()
domain = random.choice(domain_list)

def generate_username():
	name = string.ascii_lowercase + string.digits
	username = ''.join(random.choice(name) for i in range(10))

	return username

def check_mail(mail=''):
	req_link = f'{API}?action=getMessages&login={mail.split("@")[0]}&domain={mail.split("@")[1]}'
	responce = requests.get(req_link).json()
	length = len(responce)

	if length == 0:
		print('[INFO] Email hasn\'t new messages. New check after 5 seconds')
	else:
		id_list = []
		for id_message in responce:
			for key, value in id_message.items():
				if key == 'id':
					id_list.append(value)

		print(f'[+] You have {length} new messages. New check after 5 seconds')

		current_dir = os.getcwd()
		final_dir = os.path.join(current_dir, 'all_mails')

		if not os.path.exists(final_dir):
			os.makedirs(final_dir)

		for id_message in id_list:
			read_msg = f'{API}?action=readMessage&login={mail.split("@")[0]}&domain={mail.split("@")[1]}&id={id_message}'
			responce = requests.get(read_msg).json()

			sender = responce['from']
			subject = responce['subject']
			date = responce['date']
			attachments = responce['attachments']
			body = responce['body']
			text = responce['textBody']
			html = responce['htmlBody']

			if len(attachments) != 0:
				for attachment in attachments:
					download_attachments = f'{API}?action=download&login={mail.split("@")[0]}&domain={mail.split("@")[1]}&id={id_message}&file={attachment["filename"]}'
					with requests.get(download_attachments, stream=True) as responce:
						attachment_file_path = os.path.join(final_dir, f'{mail}_{id_message}_{attachment["filename"]}')
						with open(attachment_file_path, 'wb') as file:
							for chunk in responce.iter_content(chunk_size=16*1024):
								file.write(chunk)

			mail_file_path = os.path.join(final_dir, f'{mail}_{id_message}.txt')

			with open(mail_file_path, 'w') as file:
				file.write(f'Sender: {sender}\nTo: {mail}\nSubject: {subject}\nDate: {date}\nAttachments: {attachments}\nBody: {body}\nText: {text}\nHTML: {html}')

def delete_mail(mail=''):
	url = 'https://www.1secmail.com/mailbox'

	data = {
			'action': 'deleteMailbox',
			'login': mail.split('@')[0],
			'domain': mail.split('@')[1]
	}

	responce = requests.post(url, data=data)
	print(f'[x] Email {mail} deleted')

def main():
	try:
		username = generate_username()
		mail = f'{username}@{domain}'
		print(f'[+] Your email: {mail}')

		mail_req = requests.get(f'{API}?login={mail.split("@")[0]}&domain={mail.split("@")[1]}')

		while True:
			check_mail(mail=mail)
			time.sleep(5)

	except KeyboardInterrupt:
		delete_mail(mail=mail)
		print('App stoped')

if __name__ == '__main__':
	main()


