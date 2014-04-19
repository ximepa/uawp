# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'UserProfile.game_acc'
        db.delete_column(u'cabinet_userprofile', 'game_acc_id')


    def backwards(self, orm):
        # Adding field 'UserProfile.game_acc'
        db.add_column(u'cabinet_userprofile', 'game_acc',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cabinet.AccountData'], null=True, blank=True),
                      keep_default=False)


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'cabinet.accountdata': {
            'Meta': {'object_name': 'AccountData', 'db_table': "'account_data'", 'managed': 'False'},
            'access_level': ('django.db.models.fields.IntegerField', [], {}),
            'activated': ('django.db.models.fields.IntegerField', [], {}),
            'credits': ('django.db.models.fields.BigIntegerField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_force': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'last_ip': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'last_logout': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'last_mac': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'last_server': ('django.db.models.fields.IntegerField', [], {}),
            'membership': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '65'}),
            'profile_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cabinet.UserProfile']", 'null': 'True', 'blank': 'True'})
        },
        u'cabinet.playerappearance': {
            'Meta': {'object_name': 'PlayerAppearance', 'db_table': "'player_appearance'", 'managed': 'False'},
            'arm_length': ('django.db.models.fields.IntegerField', [], {}),
            'arm_thickness': ('django.db.models.fields.IntegerField', [], {}),
            'brow_angle': ('django.db.models.fields.IntegerField', [], {}),
            'brow_height': ('django.db.models.fields.IntegerField', [], {}),
            'brow_shape': ('django.db.models.fields.IntegerField', [], {}),
            'cheek_bones': ('django.db.models.fields.IntegerField', [], {}),
            'cheeks': ('django.db.models.fields.IntegerField', [], {}),
            'chest': ('django.db.models.fields.IntegerField', [], {}),
            'chin_height': ('django.db.models.fields.IntegerField', [], {}),
            'decoration': ('django.db.models.fields.IntegerField', [], {}),
            'ear_shape': ('django.db.models.fields.IntegerField', [], {}),
            'expression': ('django.db.models.fields.IntegerField', [], {}),
            'eye_angle': ('django.db.models.fields.IntegerField', [], {}),
            'eye_height': ('django.db.models.fields.IntegerField', [], {}),
            'eye_rgb': ('django.db.models.fields.IntegerField', [], {}),
            'eye_shape': ('django.db.models.fields.IntegerField', [], {}),
            'eye_size': ('django.db.models.fields.IntegerField', [], {}),
            'eye_space': ('django.db.models.fields.IntegerField', [], {}),
            'eye_width': ('django.db.models.fields.IntegerField', [], {}),
            'face': ('django.db.models.fields.IntegerField', [], {}),
            'face_contour': ('django.db.models.fields.IntegerField', [], {}),
            'face_shape': ('django.db.models.fields.IntegerField', [], {}),
            'facial_ratio': ('django.db.models.fields.IntegerField', [], {}),
            'foot_size': ('django.db.models.fields.IntegerField', [], {}),
            'forehead': ('django.db.models.fields.IntegerField', [], {}),
            'hair': ('django.db.models.fields.IntegerField', [], {}),
            'hair_rgb': ('django.db.models.fields.IntegerField', [], {}),
            'hand_size': ('django.db.models.fields.IntegerField', [], {}),
            'head_size': ('django.db.models.fields.IntegerField', [], {}),
            'height': ('django.db.models.fields.FloatField', [], {}),
            'hips': ('django.db.models.fields.IntegerField', [], {}),
            'jaw_line': ('django.db.models.fields.IntegerField', [], {}),
            'leg_length': ('django.db.models.fields.IntegerField', [], {}),
            'leg_thickness': ('django.db.models.fields.IntegerField', [], {}),
            'lip_height': ('django.db.models.fields.IntegerField', [], {}),
            'lip_rgb': ('django.db.models.fields.IntegerField', [], {}),
            'lip_shape': ('django.db.models.fields.IntegerField', [], {}),
            'lip_size': ('django.db.models.fields.IntegerField', [], {}),
            'mouth_size': ('django.db.models.fields.IntegerField', [], {}),
            'neck': ('django.db.models.fields.IntegerField', [], {}),
            'neck_length': ('django.db.models.fields.IntegerField', [], {}),
            'nose': ('django.db.models.fields.IntegerField', [], {}),
            'nose_bridge': ('django.db.models.fields.IntegerField', [], {}),
            'nose_tip': ('django.db.models.fields.IntegerField', [], {}),
            'nose_width': ('django.db.models.fields.IntegerField', [], {}),
            'player_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'shoulder_size': ('django.db.models.fields.IntegerField', [], {}),
            'shoulders': ('django.db.models.fields.IntegerField', [], {}),
            'skin_rgb': ('django.db.models.fields.IntegerField', [], {}),
            'smile': ('django.db.models.fields.IntegerField', [], {}),
            'tattoo': ('django.db.models.fields.IntegerField', [], {}),
            'torso': ('django.db.models.fields.IntegerField', [], {}),
            'voice': ('django.db.models.fields.IntegerField', [], {}),
            'waist': ('django.db.models.fields.IntegerField', [], {})
        },
        u'cabinet.players': {
            'Meta': {'object_name': 'Players', 'db_table': "'players'", 'managed': 'False'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cabinet.AccountData']"}),
            'account_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'advanced_stigma_slot_size': ('django.db.models.fields.IntegerField', [], {}),
            'arena_points': ('django.db.models.fields.IntegerField', [], {}),
            'bg_points': ('django.db.models.fields.IntegerField', [], {}),
            'bind_point': ('django.db.models.fields.IntegerField', [], {}),
            'brokerkinah': ('django.db.models.fields.BigIntegerField', [], {'db_column': "'brokerKinah'"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            'cube_size': ('django.db.models.fields.IntegerField', [], {}),
            'deletion_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'exp': ('django.db.models.fields.BigIntegerField', [], {}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'heading': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'last_online': ('django.db.models.fields.DateTimeField', [], {}),
            'mailboxletters': ('django.db.models.fields.IntegerField', [], {'db_column': "'mailboxLetters'"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'online': ('django.db.models.fields.IntegerField', [], {}),
            'partner_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'personal_rating': ('django.db.models.fields.IntegerField', [], {}),
            'player_class': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'race': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'recoverexp': ('django.db.models.fields.BigIntegerField', [], {}),
            'repletionstate': ('django.db.models.fields.BigIntegerField', [], {}),
            'title_id': ('django.db.models.fields.IntegerField', [], {}),
            'warehouse_size': ('django.db.models.fields.IntegerField', [], {}),
            'world_id': ('django.db.models.fields.IntegerField', [], {}),
            'x': ('django.db.models.fields.FloatField', [], {}),
            'y': ('django.db.models.fields.FloatField', [], {}),
            'z': ('django.db.models.fields.FloatField', [], {})
        },
        u'cabinet.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'coints': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_premium': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_vip': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'premium_end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'premium_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cabinet']