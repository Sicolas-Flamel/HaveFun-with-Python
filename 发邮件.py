# yagmail 对 smtplib 进行了更高级的封装

import yagmail      # 第一行

conn = yagmail.SMTP(
        user="邮箱地址@XXX.com",
        password="密码",
        host="smtp.exmail.qq.com",  #在邮箱设置里可查。
        port=465     #在邮箱设置里可查。
)    # 第二行，这里是为了美观分开的

conn.send(["xi@XXX.com",
           '55@163.com'],
          "晚安",
          "这是用来测试抄送的晚安邮件~。",
          ["0514XXX.xlsx","051XXXX.xlsx"]
         )
# 第三行   4个参数：收件人邮箱，主题，正文，附件
