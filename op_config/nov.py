#!/usr/bin/env python

import json

info = {
  "client": {
    "redirect_uris": ["https://connect-rp.heroku.com"],
    "contact": ["nov@matake.jp"],
    "application_type": "web",
    "application_name": "Nov RP",
    "register": True
  },
  "provider": {
    "version": {
      "oauth": "2.0",
      "openid": "3.0"
    },
    "dynamic": "https://connect-op.heroku.com/"
  },
  "interaction":[
          {
          "matches" : {
              "url": "https://connect-op.heroku.com/authorizations/new"
          },
          "page-type": "user-consent",
          "control": {
              "type": "form",
              "pick": {
                  "form": {"action": "/authorizations",
                           "class": "approve"}
              }

          }
      },{
          "matches" : {
              "url": "https://connect-op.heroku.com/"
          },
          "page-type": "login",
          "control": {
              "type": "form",
              "pick":{
                  "form":{"action": "/connect/fake"}
              }
          }
      }
  ]
}

print json.dumps(info)