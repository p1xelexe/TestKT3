import random

# -------------------

product = ("div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(4) "
           "div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child({}) div.product-thumb.transition div.{}")

# -------------------

element = "image > a:nth-child(1)"
button_buy = "button-group > button:nth-child(1)"
button_fav = "button-group > button:nth-child(2)"

# -------------------

review = ("div.container:nth-child(4) div.row div.col-sm-12 div.row div.col-sm-8 div.tab-content "
          "div.tab-pane.active:nth-child(3) form.form-horizontal div.form-group.required:nth-child(5) "
          "div.col-sm-12 > input:nth-child({})")

review_cs = ("div.container:nth-child(4) div.row div.col-sm-12 div.row div.col-sm-8 div.tab-content "
             "div.tab-pane.active:nth-child(3) form.form-horizontal div.form-group.required:nth-child(5) "
             "div.col-sm-12 > input:nth-child({})")

# -------------------

first = "uwu"
last = "uwu"
random_email = random.randrange(1, 1000)
email = "uwu" + str(random_email) + "@gmail.com"
tel = "123456789"
passw = "UwUPass"
conpassw = "UwUPass"
reviewt = "UwU review + 24 символа, потому что это очень большая строка"

# -------------------

input_texts = [first, last, email, tel, passw, conpassw, reviewt]
