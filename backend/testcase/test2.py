import requests
import json

from common import Common

class TestMenu:
    
    def setup(self):
        self.com = Common()
    
    # test create menu with correct token
    def test_create_menu_1(self):
      url = "/menu/create"
      payload = json.dumps({
        "itemName": "test_1",
        "category": "Food",
        "price": "5.00",
        "description": "Bread, Bacon, Egg",
        "dietary": [
          "Gluten Free",
          "Vegan"
        ],
        "translationLanguage": [
          "ja",
          "ko"
        ],
        "options": [
          "Option 1",
          "Option 2"
        ]
      })
      headers = {
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJpYXQiOjE2Njg3NDEyMjIsImV4cCI6MTY3NzM4MTIyMn0.6o1OVvC-bTGdGMvU-7i1eO2fJavrENeL8WEC9gmpW7A',
            'Content-Type': 'application/json'
            }
      response = self.com.post(url, data = payload, headers = headers)
      assert response.status_code == 200

    # test create menu with incorrect token
    def test_create_menu_2(self):
      url = "/menu/create"
      payload = json.dumps({
        "itemName": "test_1",
        "category": "Food",
        "price": "5.00",
        "description": "Bread, Bacon, Egg",
        "dietary": [
          "Gluten Free",
          "Vegan"
        ],
        "translationLanguage": [
          "ja",
          "ko"
        ],
        "options": [
          "Option 1",
          "Option 2"
        ]
      })
      headers = {
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inp6QHp6LmNvbSIsImlhdCI6MTY2NjQzMTY0OSwiZXhwIjoxNjc1MDcxNjQ5fQ._YydPfJdY9OqeQWeQNBvMR2ATmrMQiDtiIpvCJk_qu',
            'Content-Type': 'application/json'
            }
      response = self.com.post(url, data = payload, headers = headers)
      assert response.status_code == 400

    # test create menu with no token
    def test_create_menu_3(self):
      url = "/menu/create"
      payload = json.dumps({
        "itemName": "test_1",
        "category": "Food",
        "price": "5.00",
        "description": "Bread, Bacon, Egg",
        "dietary": [
          "Gluten Free",
          "Vegan"
        ],
        "translationLanguage": [
          "ja",
          "ko"
        ],
        "options": [
          "Option 1",
          "Option 2"
        ]
      })
      headers = {
            'Content-Type': 'application/json'
            }
      response = self.com.post(url, data = payload, headers = headers)
      assert response.status_code == 401
      
    # test get menu with correct id
    def test_get_menu_1(self):
      url = "/menu/getmenu?id=6343c404adfe757095fddc17"
      payload={}
      headers = {}
      response = self.com.get(url, headers=headers, data=payload)
      assert response.status_code == 200
    
    # test get menu with incorrect id
    def test_get_menu_2(self):
      url = "/menu/getmenu?id=6343c404adfe757095fddc1"
      payload={}
      headers = {}
      response = self.com.get(url, headers=headers, data=payload)
      assert response.status_code == 500
      
    # test get menu with no id
    def test_get_menu_3(self):
      url = "/menu/getmenu"
      payload={}
      headers = {}
      response = self.com.get(url, headers=headers, data=payload)
      assert response.status_code == 400
    
    # test delete item with correct id
    def test_delete_item_1(self):
      url = "/menu/deleteitem"
      payload = json.dumps({
        "id": "6376f94955c183477b790ac0"
      })
      headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJpYXQiOjE2Njg3NDEyMjIsImV4cCI6MTY3NzM4MTIyMn0.6o1OVvC-bTGdGMvU-7i1eO2fJavrENeL8WEC9gmpW7A',
        'Content-Type': 'application/json'
      }
      response = self.com.delete(url, headers=headers, data=payload)
      assert response.status_code == 200

    # test delete item with incorrect id
    def test_delete_item_2(self):
      url = "/menu/deleteitem"
      payload = json.dumps({
        "id": "636e22d228db170daf3d2aa7"
      })
      headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Ijk5OUAxMjMuY29tIiwiaWF0IjoxNjY4MTI3NjMzLCJleHAiOjE2NzY3Njc2MzN9.EZuBk67qIct2OXYmLI9sZBUbm7AnrSSz3kfTOQVz0k0',
        'Content-Type': 'application/json'
      }
      response = self.com.delete(url, headers=headers, data=payload)
      assert response.status_code == 400
      
    # test add category with correct token and email
    def test_add_category_1(self):
      url = "/menu/category/add"
      payload = json.dumps({
        "email": "zz@zz.com",
        "category": {
          "food": None,
          "drink": None,
          "entree": None
        }
      })
      headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inp6QHp6LmNvbSIsImlhdCI6MTY2ODMxMjg4MSwiZXhwIjoxNjc2OTUyODgxfQ._5o5FayS1qBwKN2cEwV6ZVCOvXQOD5SuS8PUBscgfKA',
        'Content-Type': 'application/json'
      }
      response = self.com.patch(url, headers=headers, data=payload)
      assert response.status_code == 200
      
    # test add category with incorrect token
    def test_add_category_2(self):
      url = "/menu/category/add"
      payload = json.dumps({
        "email": "zz@zz.com",
        "category": {
          "food": None,
          "drink": None,
          "entree": None
        }
      })
      headers = {
        'Authorization': 'Bearer ayJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inp6QHp6LmNvbSIsImlhdCI6MTY2ODMxMjg4MSwiZXhwIjoxNjc2OTUyODgxfQ._5o5FayS1qBwKN2cEwV6ZVCOvXQOD5SuS8PUBscgfKA',
        'Content-Type': 'application/json'
      }
      response = self.com.patch(url, headers=headers, data=payload)
      assert response.status_code == 400
    
    # test get category with correct token
    def test_get_category_1(self):
      url = "/menu/category/get"
      payload={}
      headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inp6QHp6LmNvbSIsImlhdCI6MTY2ODMxMjg4MSwiZXhwIjoxNjc2OTUyODgxfQ._5o5FayS1qBwKN2cEwV6ZVCOvXQOD5SuS8PUBscgfKA'
      }
      response = self.com.get(url, headers=headers, data=payload)
      assert response.status_code == 200
    
    # test get category with incorrect token
    def test_get_category_2(self):
      url = "/menu/category/get"
      payload={}
      headers = {
        'Authorization': 'Bearer ayJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inp6QHp6LmNvbSIsImlhdCI6MTY2ODMxMjg4MSwiZXhwIjoxNjc2OTUyODgxfQ._5o5FayS1qBwKN2cEwV6ZVCOvXQOD5SuS8PUBscgfKA'
      }
      response = self.com.get(url, headers=headers, data=payload)
      assert response.status_code == 400
      
    # test get category with correct token
    def test_get_posMenu_1(self):
      url = "/menu/pos"
      payload={}
      headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Ijk5OUAxMjMuY29tIiwiaWF0IjoxNjY4MTI3NjMzLCJleHAiOjE2NzY3Njc2MzN9.EZuBk67qIct2OXYmLI9sZBUbm7AnrSSz3kfTOQVz0k0'
      }
      response = self.com.get(url, headers=headers, data=payload)
      assert response.status_code == 200
    
    # test get category with incorrect token
    def test_get_posMenu_2(self):
      url = "/menu/pos"
      payload={}
      headers = {
        'Authorization': 'Bearer ayJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Ijk5OUAxMjMuY29tIiwiaWF0IjoxNjY4MTI3NjMzLCJleHAiOjE2NzY3Njc2MzN9.EZuBk67qIct2OXYmLI9sZBUbm7AnrSSz3kfTOQVz0k0'
      }
      response = self.com.get(url, headers=headers, data=payload)
      assert response.status_code == 400
      
    # test edit menu with correct token
    def test_edit_menu_1(self):
      url = "/menu/edit"
      payload = json.dumps({
        "itemId": "6353bb410df5c923ee90f071",
        "itemName": "Bacon egg roll",
        "category": "Food",
        "price": "5.00",
        "description": "Bread, Bacon, Egg",
        "dietary": [
          "Gluten Free",
          "Vegan"
        ],
        "translationLanguage": [
          "ja",
          "ko"
        ],
        "options": [
          "Option 1",
          "Option 2"
        ]
      })
      headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inp6QHp6LmNvbSIsImlhdCI6MTY2ODMxMjg4MSwiZXhwIjoxNjc2OTUyODgxfQ._5o5FayS1qBwKN2cEwV6ZVCOvXQOD5SuS8PUBscgfKA',
        'Content-Type': 'application/json'
      }
      response = self.com.patch(url, headers=headers, data=payload)
      assert response.status_code == 200
      
    # test edit menu with incorrect token
    def test_edit_menu_2(self):
      url = "/menu/edit"
      payload = json.dumps({
        "itemId": "6353bb410df5c923ee90f071",
        "itemName": "Bacon egg roll",
        "category": "Food",
        "price": "5.00",
        "description": "Bread, Bacon, Egg",
        "dietary": [
          "Gluten Free",
          "Vegan"
        ],
        "translationLanguage": [
          "ja",
          "ko"
        ],
        "options": [
          "Option 1",
          "Option 2"
        ]
      })
      headers = {
        'Authorization': 'Bearer aJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inp6QHp6LmNvbSIsImlhdCI6MTY2ODMxMjg4MSwiZXhwIjoxNjc2OTUyODgxfQ._5o5FayS1qBwKN2cEwV6ZVCOvXQOD5SuS8PUBscgfKA',
        'Content-Type': 'application/json'
      }
      response = self.com.patch(url, headers=headers, data=payload)
      assert response.status_code == 400
      
    # test delete menu with incorrect item id
    def test_delete_menu_1(self):
      url = "/menu/edit"
      payload = json.dumps({
        "itemId": "2353bb410df5c923ee90f07",
        "itemName": "Bacon egg roll",
        "category": "Food",
        "price": "5.00",
        "description": "Bread, Bacon, Egg",
        "dietary": [
          "Gluten Free",
          "Vegan"
        ],
        "translationLanguage": [
          "ja",
          "ko"
        ],
        "options": [
          "Option 1",
          "Option 2"
        ]
      })
      headers = {
        'Authorization': 'Bearer aJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inp6QHp6LmNvbSIsImlhdCI6MTY2ODMxMjg4MSwiZXhwIjoxNjc2OTUyODgxfQ._5o5FayS1qBwKN2cEwV6ZVCOvXQOD5SuS8PUBscgfKA',
        'Content-Type': 'application/json'
      }
      response = self.com.patch(url, headers=headers, data=payload)
      assert response.status_code == 400