from datetime import datetime, timedelta, timezone
from lib.db import db

class CreateActivity:
  def run(message, cognito_user_id, ttl):
    model = {
      'errors': None,
      'data': None
@@ -28,8 +28,8 @@ def run(message, user_handle, ttl):
    else:
      model['errors'] = ['ttl_blank']

    
    
    if cognito_user_id == None or len(cognito_user_id) < 1:
      model['errors'] = ['cognito_user_id_blank']

    if message == None or len(message) < 1:
      model['errors'] = ['message_blank'] 
@@ -43,16 +43,16 @@ def run(message, user_handle, ttl):
      }   
    else:
      expires_at = (now + ttl_offset)
      
      uuid = CreateActivity.create_activity(cognito_user_id,message,expires_at)

      object_json = CreateActivity.query_object_activity(uuid)
      model['data'] = object_json
    return model

  def create_activity(handle, message, expires_at):
  def create_activity(cognito_user_id, message, expires_at):
    sql = db.template('activities','create')
    uuid = db.query_commit(sql,{
      
      'cognito_user_id': cognito_user_id,
      'message': message,
      'expires_at': expires_at
    })
    return uuid
  def query_object_activity(uuid):
    sql = db.template('activities','object')
    return db.query_object_json(sql,{
      'uuid': uuid
    })