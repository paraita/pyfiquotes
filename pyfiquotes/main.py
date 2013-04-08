#!/usr/bin/env python
# encoding: utf-8
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
import os
import jinja2

# macro
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Authenticator():
    """Authentication Manager
    """
    def auth(self):
        return "pas encore implémenté"

class PortfolioHandler():
    """Portfolio Manager
    """
    def get_portfolios(self):
        return "pas encore implémenté"



class MainHandler(webapp2.RequestHandler):
    """Handler par défaut
    """
    
    template_home = 'template.html'
    bloc_accueil = 'accueil.html'
    
    def home(self):
        template = jinja_env.get_template(self.template_home)
        return template
    
    def get(self):
        t = self.home()
        return self.response.out.write(t.render({}))
        #self.response.write('Hello world!')




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)