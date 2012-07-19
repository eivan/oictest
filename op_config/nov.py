#!/usr/bin/env python

import json

info = {
  "versions": {
    "oauth": "2.0",
    "openid": "3.0"
  },
  "features": {
    "registration":True,
    "discovery": True,
    "session_management": False
  },
  "client": {
    "redirect_uris": ["https://%s/"],
    "contact": ["nov@matake.jp"],
    "application_type": "web",
    "application_name": "Nov RP"
  },
  "provider": {
    "dynamic": "https://connect-op.heroku.com"
  },
  "interaction":[{
    "matches" : {
      "url": "https://connect-op.heroku.com/authorizations/new"
    },
    "page-type": "user-consent",
    "control": {
      "type": "form",
      "pick": {
        "form": {
          "action": "/authorizations",
          "class": "approve"
        }
      }
    }
  }, {
    "matches" : {
      "url": "https://connect-op.heroku.com/"
    },
    "page-type": "login",
    "control": {
      "type": "form",
      "pick": {
        "form":{
          "action": "/connect/fake"
        }
      }
    }
  }]
}

print json.dumps(info)