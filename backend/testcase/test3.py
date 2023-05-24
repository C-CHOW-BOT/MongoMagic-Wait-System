import requests
import json

from common import Common

class TestOrder:
    
    def setup(self):
        self.com = Common()
  
  
  
    # test create order with correct token
    def test_order_create_1(self):
        url = "/order/create"
        payload = json.dumps({
          "siteId": "6343c404adfe757095fddc17",
          "tableNumber": "7",
          "order": [
            {
              "item": "Bacon egg roll",
              "quantity": "1",
              "extras": [
                "Option 1",
                "Option 2"
              ],
              "price": "14"
            }
          ],
          "totalPrice": "14"
        })
        headers = {
          'Content-Type': 'application/json'
        }
        response = self.com.post(url, data = payload, headers = headers)
        assert response.status_code == 201
      
    # test create order with incorrect siteId
    def test_order_create_2(self):
        url = "/order/create"

        payload = json.dumps({
          "tableNumber": "8",
          "order": [
            {
              "item": "Bacon egg roll",
              "quantity": "1",
              "extras": [
                "Option 1",
                "Option 2"
              ],
              "price": "14"
            }
          ],
          "totalPrice": "14"
        })
        headers = {
          'Content-Type': 'application/json'
        }
        response = self.com.post(url, data = payload, headers = headers)
        assert response.status_code == 400
    
    # test update order with correct data
    def test_order_update_1(self):
        url = "/order/update"
        payload = json.dumps({
          "orderId": "6376fc8ad4bc9df76f582cd5",
          "addOn": [
            {
              "item": "Bacon egg roll",
              "quantity": "1",
              "extras": [
                "Option 1",
                "Option 2"
              ],
              "price": "14"
            }
          ],
          "totalPrice": "14"
        })
        headers = {
          'Content-Type': 'application/json'
        }
        response = self.com.patch(url, headers=headers, data=payload)
        assert response.status_code == 200
    
    # test update order without orderId
    def test_order_update_2(self):
        url = "/order/update"
        payload = json.dumps({
          "addOn": [
            {
              "item": "Bacon egg roll",
              "quantity": "1",
              "extras": [
                "Option 1",
                "Option 2"
              ],
              "price": "14"
            }
          ],
          "totalPrice": "14"
        })
        headers = {
          'Content-Type': 'application/json'
        }
        response = self.com.patch(url, headers=headers, data=payload)
        assert response.status_code == 400  
    
    # test finish order with correct data
    def test_order_finished_1(self):
        url = "/order/status/finishone"
        payload = json.dumps({
          "orderId": "6376fc8ad4bc9df76f582cd5"
        })
        headers = {
          'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inp6QHp6LmNvbSIsImlhdCI6MTY2ODc0MjE3OCwiZXhwIjoxNjc3MzgyMTc4fQ.F_MaqUc5sK7BW44K0hFGxrYAzOqdjM0-1kOUazTNDoM',
          'Content-Type': 'application/json'
        }
        response = self.com.post(url, headers=headers, data=payload)
        assert response.status_code == 200
    
    # test finish order without orderId
    def test_order_finished_2(self):
        url = "/order/status/finishone"
        payload = json.dumps({
        })
        headers = {
          'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inp6QHp6LmNvbSIsImlhdCI6MTY2ODMxMjg4MSwiZXhwIjoxNjc2OTUyODgxfQ._5o5FayS1qBwKN2cEwV6ZVCOvXQOD5SuS8PUBscgfKA',
          'Content-Type': 'application/json'
        }
        response = self.com.post(url, headers=headers, data=payload)
        assert response.status_code == 400
    
    # test change order status with incorrect token
    def test_order_finished_3(self):
        url = "/order/status/finishone"
        payload = json.dumps({
        })
        headers = {
          'Authorization': 'Bearer aJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inp6QHp6LmNvbSIsImlhdCI6MTY2ODMxMjg4MSwiZXhwIjoxNjc2OTUyODgxfQ._5o5FayS1qBwKN2cEwV6ZVCOvXQOD5SuS8PUBscgfKA',
          'Content-Type': 'application/json'
        }
        response = self.com.post(url, headers=headers, data=payload)
        assert response.status_code == 401
    
    # test change order status with correct orderId
    def test_order_paid_1(self):
        url = "/order/status/paid"
        payload = json.dumps({
          "orderId": "6376fc8ad4bc9df76f582cd5"
        })
        headers = {
          'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inp6QHp6LmNvbSIsImlhdCI6MTY2ODc0MjE3OCwiZXhwIjoxNjc3MzgyMTc4fQ.F_MaqUc5sK7BW44K0hFGxrYAzOqdjM0-1kOUazTNDoM',
          'Content-Type': 'application/json'
        }
        response = self.com.post(url, headers=headers, data=payload)
        assert response.status_code == 200
        
    # test change order status with incorrect orderId
    def test_order_paid_2(self):
        url = "/order/status/paid"
        payload = json.dumps({
          "orderId": "126373341565fd049c8d4fa709"
        })
        headers = {
          'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inp6QHp6LmNvbSIsImlhdCI6MTY2ODMxMjg4MSwiZXhwIjoxNjc2OTUyODgxfQ._5o5FayS1qBwKN2cEwV6ZVCOvXQOD5SuS8PUBscgfKA',
          'Content-Type': 'application/json'
        }
        response = self.com.post(url, headers=headers, data=payload)
        assert response.status_code == 400

    # test change order status with incorrect token
    def test_order_paid_3(self):
        url = "/order/status/paid"
        payload = json.dumps({
          "orderId": "6373341565fd049c8d4fa709"
        })
        headers = {
          'Authorization': 'Bearer ayJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inp6QHp6LmNvbSIsImlhdCI6MTY2ODMxMjg4MSwiZXhwIjoxNjc2OTUyODgxfQ._5o5FayS1qBwKN2cEwV6ZVCOvXQOD5SuS8PUBscgfKA',
          'Content-Type': 'application/json'
        }
        response = self.com.post(url, headers=headers, data=payload)
        assert response.status_code == 401
    
    # test get order with correct data
    def test_get_order_1(self):
        url = "/order/get/one?siteId=6344d3ae861de146d6695447&tableNumber=8"
        payload={}
        headers = {
          'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inp6QHp6LmNvbSIsImlhdCI6MTY2ODMxMjg4MSwiZXhwIjoxNjc2OTUyODgxfQ._5o5FayS1qBwKN2cEwV6ZVCOvXQOD5SuS8PUBscgfKA'
        }
        response = self.com.get(url, headers=headers, data=payload)
        assert response.status_code == 200
        
    # test get order with incorrect token
    def test_get_order_2(self):
        url = "/order/get/one?siteId=6344d3ae861de146d6695447&tableNumber=8"
        payload={}
        headers = {
          'Authorization': 'Bearer aJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inp6QHp6LmNvbSIsImlhdCI6MTY2ODMxMjg4MSwiZXhwIjoxNjc2OTUyODgxfQ._5o5FayS1qBwKN2cEwV6ZVCOvXQOD5SuS8PUBscgfKA'
        }
        response = self.com.get(url, headers=headers, data=payload)
        assert response.status_code == 401
    
    # test get current order with correct data
    def test_get_current_order_1(self):
        url = "/order/get/current?siteId=6344d3ae861de146d6695447"
        payload={}
        headers = {
          'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inp6QHp6LmNvbSIsImlhdCI6MTY2ODMxMjg4MSwiZXhwIjoxNjc2OTUyODgxfQ._5o5FayS1qBwKN2cEwV6ZVCOvXQOD5SuS8PUBscgfKA'
        }
        response = self.com.get(url, headers=headers, data=payload)
        assert response.status_code == 200
    
    # test get current order with incorrect token
    def test_get_current_order_2(self):
        url = "/order/get/current?siteId=6344d3ae861de146d6695447"
        payload={}
        headers = {
          'Authorization': 'Bearer aJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inp6QHp6LmNvbSIsImlhdCI6MTY2ODMxMjg4MSwiZXhwIjoxNjc2OTUyODgxfQ._5o5FayS1qBwKN2cEwV6ZVCOvXQOD5SuS8PUBscgfKA'
        }
        response = self.com.get(url, headers=headers, data=payload)
        assert response.status_code == 401
        
    # test get order unpaid with correct data
    def test_get_order_history_1(self):
        url = "/order/get/unpaid?siteId=6344d3ae861de146d6695447"
        payload={}
        headers = {
          'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inp6QHp6LmNvbSIsImlhdCI6MTY2ODMxMjg4MSwiZXhwIjoxNjc2OTUyODgxfQ._5o5FayS1qBwKN2cEwV6ZVCOvXQOD5SuS8PUBscgfKA'
        }
        response = self.com.get(url, headers=headers, data=payload)
        assert response.status_code == 200
    
    # test get order unpaid with incorrect token
    def test_get_order_history_2(self):
        url = "/order/get/unpaid?siteId=6344d3ae861de146d6695447"
        payload={}
        headers = {
          'Authorization': 'Bearer aJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inp6QHp6LmNvbSIsImlhdCI6MTY2ODMxMjg4MSwiZXhwIjoxNjc2OTUyODgxfQ._5o5FayS1qBwKN2cEwV6ZVCOvXQOD5SuS8PUBscgfKA'
        }
        response = self.com.get(url, headers=headers, data=payload)
        assert response.status_code == 401
        
    # test get order history with correct data
    def test_get_completed_order_1(self):
        url = "/order/get/completed?siteId=6344d3ae861de146d6695447&page=1&dateStart=2022-11-06&dateEnd=2022-11-06"
        payload={}
        headers = {
          'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inp6QHp6LmNvbSIsImlhdCI6MTY2ODMxMjg4MSwiZXhwIjoxNjc2OTUyODgxfQ._5o5FayS1qBwKN2cEwV6ZVCOvXQOD5SuS8PUBscgfKA'
        }
        response = self.com.get(url, headers=headers, data=payload)
        assert response.status_code == 200
    
    # test get order history with incorrect token
    def test_get_completed_order_2(self):
        url = "/order/get/completed?siteId=6344d3ae861de146d6695447&page=1&dateStart=2022-11-06&dateEnd=2022-11-06"
        payload={}
        headers = {
          'Authorization': 'Bearer ayJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inp6QHp6LmNvbSIsImlhdCI6MTY2ODMxMjg4MSwiZXhwIjoxNjc2OTUyODgxfQ._5o5FayS1qBwKN2cEwV6ZVCOvXQOD5SuS8PUBscgfKA'
        }
        response = self.com.get(url, headers=headers, data=payload)
        assert response.status_code == 401
    
    # test get order history without siteId
    def test_get_completed_order_3(self):
        url = "/order/get/completed?page=1&dateStart=2022-11-06&dateEnd=2022-11-06"
        payload={}
        headers = {
          'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inp6QHp6LmNvbSIsImlhdCI6MTY2ODMxMjg4MSwiZXhwIjoxNjc2OTUyODgxfQ._5o5FayS1qBwKN2cEwV6ZVCOvXQOD5SuS8PUBscgfKA'
        }
        response = self.com.get(url, headers=headers, data=payload)
        assert response.status_code == 400
    