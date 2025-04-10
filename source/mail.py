from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_mail(from_id, from_pass, to, subject, body):
    HOST = 'smtp.gmail.com'
    PORT = 587

    # メールの内容を作成
    msg = MIMEMultipart()
    msg.attach(MIMEText(body, 'html'))
    msg['Subject'] = subject
    msg['From'] = from_id
    msg['To'] = to

    # ここから送信処理
    try:
        # GmailのSMTPサーバーを利用
        server = SMTP(HOST, PORT)
        server.starttls()  # TLS（セキュリティ機能）を開始
        server.login(from_id, from_pass)  # 入力されたメールアドレスとパスワードでログイン
        server.send_message(msg)  # メール送信
        server.quit()  # 接続終了
        print("メールが送信されました")
    except Exception as e:
        print(f"エラーが発生しました: {e}")


if __name__ == "__main__":
    # ユーザーにメール情報を入力してもらう
    from_id = input("送信者のメールアドレスを入力してください: ")
    from_pass = input("送信者のメールアドレスのパスワードを入力してください: ")
    to = input("受信者のメールアドレスを入力してください: ")
    subject = input("メールの件名を入力してください: ")
    body = input("メールの本文を入力してください: ")

    send_mail(from_id, from_pass, to, subject, body)
