#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import json
from controller.school_distance import SchoolDistanceController;

city_list = {
  "cities":[
      "台北市",
      "基隆市",
      "宜蘭縣",
      "新北市",
      "連江縣",
      "新竹市",
      "新竹縣",
      "桃園縣",
      "苗栗縣",
      "台中市",
      "南投縣",
      "彰化縣",
      "嘉義市",
      "嘉義縣",
      "雲林縣",
      "台南市",
      "澎湖縣",
      "金門縣",
      "高雄市",
      "台東縣",
      "屏東縣",
      "花蓮縣"]
  }


class SchoolListHandler(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'application/json'
    self.response.write(
       json.dumps(SchoolDistanceController().getSchoolList()))


class CityListHandler(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'application/json'
    self.response.write(
       json.dumps(city_list))


app = webapp2.WSGIApplication([
    ('/api/schoollist', SchoolListHandler),
    ('/api/citylist', CityListHandler)
], debug=True)
