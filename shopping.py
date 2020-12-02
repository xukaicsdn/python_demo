# dict_commodity_info = {
#     101: {"name": "屠龙刀", "price": 10000},
#     102: {"name": "倚天剑", "price": 10000},
#     103: {"name": "九阴白骨爪", "price": 8000},
#     104: {"name": "九阳神功", "price": 9000},
#     105: {"name": "降龙十八掌", "price": 8000},
#     106: {"name": "乾坤大挪移", "price": 10000}
# }
#
# list_order = []
#
#
# def gou_wu():
#     """
#         购物
#     :return:
#     """
#     while True:
#         item = input("1键购买，2键结算。")
#         if item == "1":
#             for key, value in dict_commodity_info.items():
#                 print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))
#             while True:
#                 cid = int(input("请输入商品编号："))
#                 if cid in dict_commodity_info:
#                     break
#                 else:
#                     print("该商品不存在")
#             count = int(input("请输入购买数量："))
#             list_order.append({"cid": cid, "count": count})
#             print("添加到购物车。")
#         elif item == "2":
#             total_price = 0
#             for item in list_order:
#                 commodity = dict_commodity_info[item["cid"]]
#                 print("商品：%s，单价：%d,数量:%d." % (commodity["name"], commodity["price"], item["count"]))
#                 total_price += commodity["price"] * item["count"]
#             while True:
#                 qian = float(input("总价%d元，请输入金额：" % total_price))
#                 if qian >= total_price:
#                     print("购买成功，找回：%d元。" % (qian - total_price))
#                     list_order.clear()
#                     break
#                 else:
#                     print("金额不足.")
#
#
# gou_wu()

























dict_commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

list_order = []


def select_menu():
    """
        购物
    :return:
    """
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            buying()
        elif item == "2":
            settlement()


def buying():
    # 打印订单
    print_commodity()
    # cid, count = create_order()
    # 创建订单
    order = create_order()
    # 添加订单
    list_order.append(order)
    print("添加到购物车。")



def settlement():
    print_order()
    get_total_price()
    pay()










def pay():
    """
        支付订单
    :return:
    """
    while True:
        money = float(input("总价%d元，请输入金额：" % get_total_price()))
        if money >= get_total_price():
            print("购买成功，找回：%d元。" % (money - get_total_price()))
            list_order.clear()
            break
        else:
            print("金额不足.")


def print_order():
    for item in list_order:
        commodity = dict_commodity_info[item["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (commodity["name"], commodity["price"], item["count"]))



def get_total_price():
    total_price = 0
    for item in list_order:
        commodity = dict_commodity_info[item["cid"]]
        total_price += commodity["price"] * item["count"]
    return total_price


def create_order():
    while True:
        cid = int(input("请输入商品编号："))
        if cid in dict_commodity_info:
            break
        else:
            print("该商品不存在")
    count = int(input("请输入购买数量："))
    # return cid, count   # 自动生成的
    return {"cid": cid, "count": count}  # 自己想返回的  让他返回字典




def print_commodity():
    for key, value in dict_commodity_info.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))









select_menu()