import requests
import json

from common import Common

class TestSite:
    
    def setup(self):
        self.com = Common()
  
    # test get sales with correct token
    def test_sales_1(self):
      url = "/admin/sales"
      payload={}
      headers = {
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Inp6QHp6LmNvbSIsImlhdCI6MTY2ODc0MjE3OCwiZXhwIjoxNjc3MzgyMTc4fQ.F_MaqUc5sK7BW44K0hFGxrYAzOqdjM0-1kOUazTNDoM'
            }
      response = self.com.get(url, data = payload, headers = headers)
      assert response.status_code == 200
      
    # test get sales with incorrect token
    def test_sales_2(self):
      url = "/admin/sales"
      payload={}
      headers = {
            'Authorization': 'Bearer ayJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Ijk5OUAxMjMuY29tIiwiaWF0IjoxNjY4MTMwNDM5LCJleHAiOjE2NzY3NzA0Mzl9.pPhqWzmHAOk7bFTbrIWHObmOHZWagqx6SotdEIvkNxI'
            }
      response = self.com.get(url, data = payload, headers = headers)
      assert response.status_code == 401






