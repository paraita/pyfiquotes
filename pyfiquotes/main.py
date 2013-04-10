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
import datetime
from google.appengine.api import users
from model import *
from webapp2 import redirect

# macro
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Authenticator():
    """Authentication Manager
    """
    def auth(self):
        return "pas encore implémenté"


class PortfolioViewHandler(webapp2.RequestHandler):
    """Portfolio view controller
    """
    gerer_ptf_html = 'static/ptf.html'
    
    def get_portfolios(self, email):
        q = db.GqlQuery("SELECT * FROM Portfolio WHERE owner = :1", email)
        res = q.fetch(100)
        return res # bancal
        
    def create_ptf(self):
        ptf_name = self.request.get('name')
        user = users.get_current_user()
        p = Portfolio(assets=[],
                      name=ptf_name,
                      owner=user.email())
        new_key = p.put()
        # pour mettre a jour le cache BANCACACACACAL
        bancal_ptf = db.get(new_key)
        print "DEBUG: key du nouveau ptf:",str(bancal_ptf.key())
        print "DEBUG: nom du nouveau ptf:",bancal_ptf.name
        return self.generate_view()
    
    def delete_ptf(self, ptf_key):
        """ TODO
        """
        db.delete(ptf_key)
        return self.response.out.write(ptf_key)
    
    def export_ptf(self, ptf_key):
        """ TODO pas urgent
        """
        return self.response.out.write("export_ptf ok (ptf=" + ptf_key + ")")
    
    def remove_asset(self, ptf_key, asset_key):
        """ TODO
        """
        return self.response.out.write("rem asset ok")
    
    def add_asset_to_ref(self):
        asset = Asset(symbol=self.request.get('symbol'),
                      isin=self.request.get('isin'),
                      label=self.request.get('label'),
                      market=self.request.get('market'),
                      currency=self.request.get('curr'),
                      type=self.request.get('type'))
        asset_key = asset.put()
        # forcer la maj du cache
        asset_bancal = db.get(asset_key)
        return self.generate_view()
    
    def generate_view(self):
        t = jinja_env.get_template(self.gerer_ptf_html)
        user = users.get_current_user()
        if not user:
            return redirect("/")
        else:
            q = Asset.all()
            assets = []
            for a in q.fetch(10):
                assets.append(a)
                print a.symbol
                for caca in a.quotes:
                    print '\t',caca.value
            portfolios = self.get_portfolios(user.email())
            print "il y a",len(assets),"titres dans le referentiel !"
            print user.email(),"a",str(len(portfolios)),"portfolios"
            t_content = {'user': user,
                         'assets': assets,
                         'portfolios': portfolios,
                         'url_login': users.create_login_url('/'),
                         'url_logout': users.create_logout_url('/')}
            return self.response.out.write(t.render(t_content))
    
    def get(self):
        # TODO verifier les parametres de la requete (SANITIZE)
        action = self.request.get('action')
        if action == 'create_ptf':
            return self.create_ptf()
        if action == 'del_ptf':
            ptf = self.request.get('ptf')
            return self.delete_ptf(ptf)
        if action == 'declare_asset':
            return self.add_asset_to_ref()
        if action == 'rem_asset':
            ptf = self.request.get('ptf')
            asset = self.request.get('asset')
            return self.remove_asset(ptf, asset)
        return self.generate_view()


class MainHandler(webapp2.RequestHandler):
    """Home view controller
    """
    home_html = 'static/accueil.html'
    
    def get(self):
        t = jinja_env.get_template(self.home_html)
        user = users.get_current_user()
        #debug
        if user:
            print "user_email:",user.email()
            print "user_nickname:",user.nickname()
        else:
            print "user non connecté !"
        t_content = {'user': user,
                     'url_login': users.create_login_url('/'),
                     'url_logout': users.create_logout_url('/')}
        return self.response.out.write(t.render(t_content))


class MiseEnPlace(webapp2.RequestHandler):
    """Pour mettre en place le jeu de données
    """
    def get(self):
        p = Portfolio(assets=[],
                      name='Portefeuille Test de Paraita',
                      owner='paraita@hipopochat.com')
        p.put()
        a1 = Asset(symbol='AAPL',
                   isin='AAPLISINCODE',
                   label='Apple Inc.',
                   market='US',
                   currency='USD',
                   type='security')
        a1.put()
        a2 = Asset(symbol='IBM',
                   isin='US4592001014',
                   label='International Business Machines Corp',
                   market='US',
                   currency='USD',
                   type='security')
        a2.put()
        a3 = Asset(symbol='FR.PA',
                   isin='FR0000130338',
                   label='Valeo SA',
                   market='FR',
                   currency='EUR',
                   type='security')
        a3.put()
        a4 = Asset(symbol='GLE.PA',
                   isin='FR0000130809',
                   label='Societe Generale',
                   market='FR',
                   currency='EUR',
                   type='security')
        a4.put()
        a5 = Asset(symbol='EPA:ACA',
                   isin='AAPLISINCODE',
                   label='Credit Agricole SA',
                   market='FR',
                   currency='EUR',
                   type='security')
        a5.put()
        a6 = Asset(symbol='FB',
                   isin='US30303M1027',
                   label='Facebook, Inc.',
                   market='US',
                   currency='USD',
                   type='security')
        a6.put()
        a7 = Asset(symbol='GOOG',
                   isin='US38259P5089',
                   label='Google Inc.',
                   market='US',
                   currency='USD',
                   type='security')
        a7.put()
        Quote(value=567.49,
              ts=datetime.datetime.now(),
              volume=12345.6,
              asset=a1).put()
        Quote(value=207.92,
              ts=datetime.datetime.now(),
              volume=488.666,
              asset=a2).put()
        p.assets = [a1.key(), a2.key()];
        p.put()
        return self.response.out.write('ok')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/ptf', PortfolioViewHandler),
    ('/test', MiseEnPlace),
    ('/auth', Authenticator)
], debug=True)
