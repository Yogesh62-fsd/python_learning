import datetime
import sys


class SaleOrders:
    countproduct_id = 1
    countcustomer_id = 1
    countorder_id = 1

    def __init__(self):
        self.product_master ={'PRD1': {'name': 'pen', 'product_unit_price': 8, 'product_cost_price': 10, 'product_type': 'Stockable'},
                              'PRD2': {'name': 'pencil', 'product_unit_price': 8, 'product_cost_price': 10, 'product_type': 'Stockable'},
                              'PRD3': {'name': 'coffee', 'product_unit_price': 25, 'product_cost_price': 30, 'product_type': 'consumable'}}

        self.product_stock = {'PRD1': 90, 'PRD2': 98, 'PRD3': 20}

        self.customer_master = {'Cust1': {'name': 'yogesh', 'email': 'yogesh@83475893', 'phone': 35489348593},
                                'Cust2': {'name': 'ravi', 'email': 'ravi@573894', 'phone': 584359734}}

        self.customer_address = {'Cust1': {'address 1': 'jay residency', 'address 2': 'krishna medical', 'city': 'rajkot', 'state': 'gujarat', 'country': 'india', 'zipcode': 857348},
                                 'Cust2': {'address 1': 'cws', 'address 2': 'jayant', 'city': 'singrauli', 'state': 'mp', 'country': 'india', 'zipcode': 853894}}


        self.sale_order ={'SO1': {'customer': 'Cust1',
                                  'order_lines': [{'product_sku': 'PRD1', 'unit_price': 8, 'quantity': 87, 'subtotal': 696, 'state': 'cancel'},
                                                  {'product_sku': 'PRD2', 'unit_price': 8, 'quantity': 90, 'subtotal': 720, 'state': 'cancel'},
                                                  {'product_sku': 'PRD3', 'unit_price': 25, 'quantity': 234, 'subtotal': 5850, 'state': 'cancel'}],
                                  'order_date': '21:1:2023', 'state': 'cancel', 'order_total_amount': 7266},
                          'SO2': {'customer': 'Cust2',
                                  'order_lines': [{'product_sku': 'PRD1', 'unit_price': 8, 'quantity': 900, 'subtotal': 7200, 'state': 'draft'},
                                                  {'product_sku': 'PRD2', 'unit_price': 8, 'quantity': 890, 'subtotal': 7120, 'state': 'draft'},
                                                  {'product_sku': 'PRD3', 'unit_price': 25, 'quantity': 799, 'subtotal': 19975, 'state': 'draft'}],
                                  'order_date': '21:1:2023', 'state': 'cancel', 'order_total_amount': 34295}}

        self.order_lines = []

    def manage_product(self):
        product_details = self.prepare_product()
        print(product_details)
        self.create_product(product_details)

    def prepare_product(
            self):  # this method will take the input from user and generate product dictionary and return it
        product_name = input('enter the product name:')
        product_unit_price = eval(input('enter the product unit price:'))
        product_cost_price = eval(input('enter the product cost:'))
        while True:
            print('--------Product Type----------------------')
            print('1: Stockable')
            print('2: Consumable')
            print('3: Service')
            print('Select one of the product type from above ')
            choice = eval(input('enter your product type choice:'))
            if choice == 1:
                product_type = 'Stockable'
                break
            elif choice == 2:
                product_type = 'Consumable'
                break
            elif choice == 3:
                product_type = 'Service'
                break
            else:
                print('Warning please enter the valid product type')
        intial_stock_unit = eval(input('enter the intial stock unit:'))

        return {'name': product_name, 'product_unit_price': product_unit_price,
                'product_cost_price': product_cost_price, 'product_type': product_type,
                'intial_stock_unit': intial_stock_unit}

    def create_product(self, product_detail):

        def generate_product_key(count):
            product_key = 'PRD' + str(int(count))
            count = count + 1
            return product_key

        product_key = generate_product_key(self.countproduct_id)
        self.countproduct_id += 1
        stock_unit = product_detail.pop('intial_stock_unit')

        self.product_master.update({f'{product_key}': product_detail})
        self.product_stock.update({f'{product_key}': stock_unit})

        print(self.product_master)
        print(self.product_stock)
        return product_key

    def update_stock(self):
        while True:

            for key in self.product_stock:
                print(key, '--', self.product_master.get(key).get('name'))
            print()
            product_key = input('please enter the product id for which you want to update the sock unit ')
            if product_key in self.product_stock.keys():
                stock_value = eval(input('enter the stock value want to add:'))
                self.product_stock[product_key] = self.product_stock.get(product_key) + stock_value
                break
            else:
                print('Warning Please enter the correct Proudct id')
                # choice = 0
                while True:
                    print(" 1: Do you update stock again ")
                    print("2: Exit")
                    choice = eval(input('select one of option given above:'))
                    if choice != 1 and choice != 2:
                        print('please choose valid option among one of them :')
                    else:
                        break

                if choice == 1:
                    continue
                else:
                    break

            print(self.product_stock)

    def manage_customer(self):  # add this to your class
        customer_details = self.prepare_customer()
        # print(customer_details)

        self.create_customer(customer_details)

    def prepare_customer(self):  #
        customer_name = input('enter your name :')
        customer_email = input('enter your email :')
        customer_phone = eval(input('enter your phone :'))
        customer_address1 = input('enter the address 1 :')
        customer_address2 = input('enter the address 2 :')
        customer_city = input('enter the city name :')
        customer_state = input('enter your state name :')
        customer_country = input('enter the name of your country:')
        customer_zipcode = eval(input('enter the you are zipcode :'))
        return {'name': customer_name, 'email': customer_email, 'phone': customer_phone, 'address 1': customer_address1,
                'address 2': customer_address2, 'city': customer_city, 'state': customer_state,
                'country': customer_country,
                'zipcode': customer_zipcode}
    def create_customer(self, customer_details):
        def generate_customer_id(count):
            customer_id = 'Cust' + str(int(count))
            count += 1
            return customer_id
        customer_id = generate_customer_id(self.countcustomer_id)
        self.countcustomer_id += 1
        address1 = customer_details.pop('address 1')
        address2 = customer_details.pop('address 2')
        city = customer_details.pop('city')
        state = customer_details.pop('state')
        country = customer_details.pop('country')
        zipcode = customer_details.pop('zipcode')

        self.customer_master.update({customer_id: customer_details})
        self.customer_address.update({customer_id: {'address 1': address1,
                                                    'address 2': address2, 'city': city, 'state': state,
                                                    'country': country,
                                                    'zipcode': zipcode}})

        print(self.customer_master)
        print(self.customer_address)
        return customer_id
    def manage_order(self):
        order_details = self.prepare_order()
        self.create_order(order_details)
    def prepare_order(self):
        choice = 0
        currentdatetime = datetime.datetime.now()
        order_date = f'{currentdatetime.day}:{currentdatetime.month}:{currentdatetime.year}'
        state = 'draft'
        order_total_amount = 0
        while True:
            print('List of customer as follows :---')
            for customer_id in self.customer_master:
                print(customer_id, '--', self.customer_master.get(customer_id).get('name'))

            customer_id = input('please enter the Customer id for which you want to take the order from the above list:')
            print(customer_id)
            print(self.customer_master.keys())
            if customer_id in self.customer_master.keys():
                print('entered customer id is ', customer_id)
                choice = 0
                while True:
                    print('List of products as follows :---')
                    for product_sku in self.product_master:
                        print(product_sku, '--', self.product_master.get(product_sku).get('name'))
                    product_sku = input('enter the Product Id from the above list:')
                    if product_sku in self.product_master.keys():

                        product_qty = eval(input('enter the  quantity of the product:'))
                        found = False
                        for dt in self.order_lines:
                            if product_sku in dt.values():
                                dt['quantity'] = dt['quantity'] + product_qty
                                dt['subtotal'] = self.product_master.get(product_sku).get('product_unit_price') * dt[
                                    'quantity']
                                found = True
                        if not found:
                            self.order_lines.append({'product_sku': product_sku,
                                                     'unit_price': self.product_master.get(product_sku).get(
                                                         'product_unit_price'), 'quantity': product_qty,
                                                     'subtotal': self.product_master.get(product_sku).get(
                                                         'product_unit_price') * product_qty, 'state': state})
                        result = 0
                        while True:
                            print('1: Do you wan to add more products')
                            print('2: Exit ')
                            result = eval(input('select one option from above:'))
                            if result != 1 and result != 2:
                                print('please select the valid option: ')
                            else:
                                break
                        if result == 1:
                            print('------------ Want to add more products ------------------------')
                            continue
                        else:
                            break
                            print('Not want to add more products  ')
                        # pass # mod need add more code
                        #
                    else:
                        print('Warning ! Please ener the valid product_sku')
                        while True:
                            print('1: Do you want to try again and select the product id:')
                            print('2: Exit')
                            choice = eval(input('select one option from above:'))
                            if choice != 1 and choice != 2:
                                print('please select the valid option: ')
                            else:
                                break
                    if choice == 1:
                        continue
                    else:
                        break
                order_total_products = [total_for_product['subtotal'] for total_for_product in self.order_lines]
                order_total_amount = sum(order_total_products)
                # print("total order price for 1 customer is ",order_total_amount)
                # print('order 1 customer ',customer_id,self.order_lines,order_date,state,order_total_amount)
                break
            else:
                print('Warning ! Please ener the valid customer_id')
                while True:
                    print('1: Do you want to try again and select the customer:')
                    print('2: Exit')
                    choice = eval(input('select one option from above:'))
                    if choice != 1 and choice != 2:
                        print('please select the valid option: ')
                    else:
                        break
            if choice == 1:
                continue
            else:
                print('Order cannot be created without customer details:')
                break
        if (len(self.order_lines) != 0):
            return {'customer': customer_id, 'order_lines': self.order_lines, 'order_date': order_date, 'state': state,
                    'order_total_amount': order_total_amount}
        return {}

    def create_order(self, order_details):
        def generate_order_id(count):
            order_id = 'SO' + str(int(count))
            count += 1
            return order_id

        order_id = generate_order_id(self.countorder_id)
        self.countorder_id += 1

        self.sale_order.update({order_id: order_details})
        print('------------------------------------------------------')
        print(self.sale_order)
        self.order_lines = []
        return order_id

    def show_order_details(self):
        order_detail = self.sale_order
        choice = 0
        while True:
            print('Order No as follows :')
            for orderno in order_detail:
                print(orderno)
            orderno = input('Please Enter the order no for which you want to show order details:')
            print(orderno)
            if orderno in order_detail.keys():
                print("*********************Order Details************************")
                print(f'Order NO  {orderno}', '\t' * 7, 'Order Date:', order_detail.get(orderno).get('order_date'))
                print('Order Status :', order_detail.get(orderno).get('state'))

                tmpcustid = order_detail.get(orderno).get('customer')

                print('Customer  :', tmpcustid, self.customer_master.get(tmpcustid).get('name'), '\t' * 5,
                      ' Address 1 :',
                      self.customer_address.get(tmpcustid).get('address 1'))

                print(f'E-mail     :', self.customer_master.get(tmpcustid).get('email'), '\t' * 5, ' Address 2 :',
                      self.customer_address.get(tmpcustid).get('address 2'))

                print(f'PhoneNo   :', self.customer_master.get(tmpcustid).get('phone'), '\t' * 5, ' City and State :',
                      self.customer_address.get(tmpcustid).get('city'), ',',
                      self.customer_address.get(tmpcustid).get('state'))

                print(f'          \t' * 4, ' Pincode      :', self.customer_address.get(tmpcustid).get('zipcode'))

                print(f'          \t' * 4, ' Country      :', self.customer_address.get(tmpcustid).get('country'))

                print('Product Name\tProductPrice\tProduct Quantity\tSubtotal')
                print('================================================================')
                for i in order_detail.get(orderno).get('order_lines'):
                    print(self.product_master.get(i.get('product_sku')).get('name'), '\t' * 4,
                          self.product_master.get(i.get('product_sku')).get('product_unit_price'), '\t' * 4,
                          i.get('quantity'),
                          '\t' * 2, i.get('subtotal'))
                print('=================================================================')
                print('                             \t\t\tOrder Total-- ',
                      order_detail.get(orderno).get('order_total_amount'))

            else:
                print('Warning Please Enter the valid Order NO')
                while True:
                    print(" 1: Do you show details again ")
                    print("2: Exit")
                    choice = eval(input('select one of option given above:'))
                    if choice != 1 and choice != 2:
                        print('please choose valid option among one of them :')
                    else:break
                if choice == 1:continue
                else:break
    def set_draft_order(self):
        while True:
            print('order are as follows:')
            for order_id in self.sale_order:
                print(order_id)
            orderid = input('enter the order id  for which you want to update the state:')
            if orderid in self.sale_order.keys():
                order_state = self.sale_order.get(orderid).get('state')

                if order_state in ('draft', 'done','confirm') :
                    if order_state=='draft':pass
                    elif order_state=='confirm':
                        print('Order is Confirmed please first cancelled it before dong it draft')
                    else :print('Warning the Order Can not Draft Once Done !!!!!!!!!!!!')
                    pass
                else:
                    self.sale_order.get(orderid)['state'] = 'draft'
                    print('Order State has been changed successfully !!!!!!!!!!!!!!!!!')

                for statusorder in self.sale_order.get(orderid).get('order_lines'):
                            order_status=statusorder.get('state')
                            if  order_status in ('draft','done'):
                                if order_status == 'draft':pass
                                else:print('Warning the Order Can not Draft Once Done !!!!!!!!!!!!')
                                pass
                            else:
                                statusorder['state']='draft'
                                print('Product  State has been changed successfully !!!!!!!!!!!!!!!!! ')
                break
            else:
                print('Warning Please Enter the valid Order id')
                while True:
                    print(" 1: Do you update state of order again ")
                    print("2: Exit")
                    choice = eval(input('select one of option given above:'))
                    if choice != 1 and choice != 2:
                        print('please choose valid option among one of them :')
                    else:break
                if choice == 1:
                    continue
                else:break

        print(self.sale_order)
    def set_confirm_order(self):
        while True:
            print('order are as follows:')
            for order_id in self.sale_order:
                print(order_id)
            orderid = input('enter the order id  for which you want to update the state:')
            if orderid in self.sale_order.keys():
                order_state = self.sale_order.get(orderid).get('state')

                if order_state in ('confirm','done','cancel'):
                    if order_state =='confirm':pass
                    elif order_state=='cancel':
                        print('Order is cancelled please make it draft befor make it confirm')
                    else:print('Warning the Order Can not Confirm Once Done !!!!!!!!!!!!')
                    pass
                else:
                    self.sale_order.get(orderid)['state'] = 'confirm'
                    print('Order State has been changed successfully !!!!!!!!!!!!!!!!!')

                for statusorder in self.sale_order.get(orderid).get('order_lines'):
                    order_status = statusorder.get('state')
                    if order_status in ('confirm', 'done','cancel'):
                        if order_status == 'confirm':
                            pass
                        elif order_status=='cancel':
                            print('Product state is cancelled please make it draft before doing it confirm')
                        else:
                            print('Warning the Order Can not Confirm Once Done !!!!!!!!!!!!')
                        pass
                    else:
                        statusorder['state'] = 'confirm'
                        print('Product  State has been changed successfully !!!!!!!!!!!!!!!!! ')
                break
            else:
                print('Warning Please Enter the valid Order id')
                while True:
                    print(" 1: Do you update state of order again ")
                    print("2: Exit")
                    choice = eval(input('select one of option given above:'))
                    if choice != 1 and choice != 2:
                        print('please choose valid option among one of them :')
                    else:
                        break
                if choice == 1:
                    continue
                else:
                    break

        print(self.sale_order)

    def set_done_order(self):
        while True:
            print('order are as follows:')
            for order_id in self.sale_order:
                print(order_id)
            orderid = input('enter the order id  for which you want to update the state:')
            if orderid in self.sale_order.keys():
                order_state = self.sale_order.get(orderid).get('state')

                if order_state in ('cancel', 'draft'):
                    if order_state == 'draft':
                        print('Order is in draft Please Confirm it before doing it to Done !!')
                    elif order_state == 'cancel':
                        print('Order is cancelled it Cannot be Done Please make sure it to Confirmed '
                              'before doing it done  !!')
                else:
                    self.sale_order.get(orderid)['state'] = 'done'
                    print('Order State has been changed successfully !!!!!!!!!!!!!!!!!')

                for statusorder in self.sale_order.get(orderid).get('order_lines'):
                    order_status = statusorder.get('state')
                    if order_status in ('draft','cancel'):
                        if order_status == 'draft':
                            print('Product State is in draft Please Confirm it before doing it to Done !!')
                            pass
                        elif order_status=='cancel':
                            print('Product State is cancelled it Cannot be Done Please make sure it to Confirmed '
                                  'before doing it done  !!')
                    else:
                        statusorder['state'] = 'done'
                        print('Product  State has been changed successfully !!!!!!!!!!!!!!!!! ')
                break
            else:
                print('Warning Please Enter the valid Order id')
                while True:
                    print(" 1: Do you update state of order again ")
                    print("2: Exit")
                    choice = eval(input('select one of option given above:'))
                    if choice != 1 and choice != 2:
                        print('please choose valid option among one of them :')
                    else:
                        break
                if choice == 1:
                    continue
                else:
                    break

        print(self.sale_order)

    def set_cancel_order(self):
        while True:
            print('order are as follows:')
            for order_id in self.sale_order:
                print(order_id)
            orderid = input('enter the order id  for which you want to update the state:')
            if orderid in self.sale_order.keys():
                order_state = self.sale_order.get(orderid).get('state')
                if order_state in ('cancel', 'done'):
                    if order_state == 'done':
                         print('Order is Done it cannot be Cancelled !!')
                    else:pass
                else:
                    self.sale_order.get(orderid)['state'] = 'cancel'
                    print('Order State has been changed successfully !!!!!!!!!!!!!!!!!')

                for statusorder in self.sale_order.get(orderid).get('order_lines'):
                    order_status = statusorder.get('state')
                    if order_status in ('done', 'cancel'):
                        if order_status == 'done':
                            print(' Warning ! Product State is in done  it cannot be cancelled !!')
                        else:pass
                    else:
                        statusorder['state'] = 'cancel'
                        print('Product  State has been changed successfully !!!!!!!!!!!!!!!!! ')
                break
            else:
                print('Warning Please Enter the valid Order id')
                while True:
                    print(" 1: Do you update state of order again ")
                    print("2: Exit")
                    choice = eval(input('select one of option given above:'))
                    if choice != 1 and choice != 2:
                        print('please choose valid option among one of them :')
                    else:
                        break
                if choice == 1:
                    continue
                else:
                    break

        print(self.sale_order)

saleorderobj1 = SaleOrders()

while (True):
    print('================Welcome to Sale Order=================')
    print('1: Manage Product')
    print('2: Manage Customer')
    print('3: Manager Order')
    print('4: Update Stock')
    print('5: Set to Draft')
    print('6: Set to Confirm')
    print('7: Set to Done')
    print('8: Set to Cancel')
    print('9: Specific Order Details')
    print('10: Exit')
    choice = eval(input('Please Select any One Option: '))
    if choice == 1:
        saleorderobj1.manage_product()
    elif choice == 2:
        saleorderobj1.manage_customer()
    elif choice == 3:
        saleorderobj1.manage_order()
    elif choice == 4:
        saleorderobj1.update_stock()
    elif choice == 5:
        saleorderobj1.set_draft_order()
    elif choice == 6:
        saleorderobj1.set_confirm_order()
    elif choice == 7:
        saleorderobj1.set_done_order()
    elif choice == 8:
        saleorderobj1.set_cancel_order()
    elif choice == 9:
        saleorderobj1.show_order_details()
    elif choice == 10:
        print('Thank you for Using !')
        sys.exit()
    else:
        print('Warning : Please Enter the valid Option !')
