import time
# import csv
import mtds
import mysql.connector
import mysqlconnecter

bb_ctgry = []
bb_pname = []
bb_pprice = []
bb_qty = []
bb_csv_data = []

mtds.get_page('https://www.bigbasket.com/product/all-categories/')
time.sleep(5)

catagories = mtds.get_elements_using_css('.DropDownColum li a')


for i in range(len(catagories)):
    category = mtds.get_elements_using_css('.DropDownColum li a')[i]
    cat = category.text
    category.click()
    time.sleep(5)

    product = mtds.get_elements_using_css('.prod-name a')
    prices = mtds.get_elements_using_class('discnt-price')
    quantity = mtds.get_elements_using_xpath('//span[@ng-bind="vm.selectedProduct.w"]')
    for j in product:
        text1 = j.text
        bb_pname.append(text1)
        bb_ctgry.append(cat)
        # print(text1)

    for j in prices:
        text2 = j.text
        if text2.__contains__('MRP: '):
            text2 = text2.replace('MRP: ', '')
        bb_pprice.append(text2)
        # print(text2)

    for j in quantity:
        text3 = j.text
        bb_qty.append(text3)
        # print(text3)
    mtds.driver.back()
    time.sleep(2)

#For  Generating CSV File

# for i in range(len(bb_ctgry)):
#
#     # print("%s %s %s %s" % (ctgry[i], pname[i], pprice[i], qty[i]))
#
#     data = [bb_ctgry[i], bb_pname[i], bb_pprice[i], bb_qty[i]]  # the data
#     print(data)
#     bb_csv_data.append(data)


# with open('D:\Big_Basket_Scrap_Data.csv', 'a', encoding="utf-8") as f:
#     writer = csv.writer(f)  # this is the writer object
#     column_name = ['Product_Catagoty', 'Product_Name', 'Product_Price', 'Product_Quantity']
#     writer.writerow(column_name)
#     for i in bb_csv_data:
#         writer.writerow(i)  # this is the data
#     f.close()

#For add data into local_host

mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database="database"
)

mycursor = mydb.cursor()
sql = "INSERT INTO big_basket_scrap_data (Product_Category,Product_Name,Product_Price,Product_Quantity) VALUES (%s, %s, %s, %s)"

for i in range(len(bb_ctgry)):
    mysqlconnecter.insert_data((bb_ctgry[i], bb_pname[i], bb_pprice[i], bb_qty[i]))
    # val = (bb_ctgry[i], bb_pname[i], bb_pprice[i], bb_qty[i])
    # mycursor.execute(sql, val)
    # mydb.commit()

    print(mycursor.rowcount, "record inserted.")

time.sleep(5)


mtds.driver_close()
