# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PageOption'
        db.create_table(u'options_pageoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('greeting_page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['options.GreetingPageOption'])),
            ('greeting_page_pk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.StaticPages'], null=True, blank=True)),
            ('news_per_page', self.gf('django.db.models.fields.IntegerField')(max_length=50)),
            ('news_max_count', self.gf('django.db.models.fields.IntegerField')(max_length=50)),
        ))
        db.send_create_signal(u'options', ['PageOption'])

        # Adding model 'GreetingPageOption'
        db.create_table(u'options_greetingpageoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('choise', self.gf('django.db.models.fields.CharField')(max_length=14)),
        ))
        db.send_create_signal(u'options', ['GreetingPageOption'])

        # Adding model 'Cheat'
        db.create_table(u'options_cheat', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enable_cheats', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cheating_registered_users', self.gf('django.db.models.fields.CharField')(default=0, max_length=100, blank=True)),
            ('cheating_characters', self.gf('django.db.models.fields.CharField')(default=0, max_length=100, blank=True)),
        ))
        db.send_create_signal(u'options', ['Cheat'])


    def backwards(self, orm):
        # Deleting model 'PageOption'
        db.delete_table(u'options_pageoption')

        # Deleting model 'GreetingPageOption'
        db.delete_table(u'options_greetingpageoption')

        # Deleting model 'Cheat'
        db.delete_table(u'options_cheat')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'options.cheat': {
            'Meta': {'object_name': 'Cheat'},
            'cheating_characters': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '100', 'blank': 'True'}),
            'cheating_registered_users': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '100', 'blank': 'True'}),
            'enable_cheats': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'options.greetingpageoption': {
            'Meta': {'object_name': 'GreetingPageOption'},
            'choise': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'options.pageoption': {
            'Meta': {'object_name': 'PageOption'},
            'greeting_page': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['options.GreetingPageOption']"}),
            'greeting_page_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.StaticPages']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'news_max_count': ('django.db.models.fields.IntegerField', [], {'max_length': '50'}),
            'news_per_page': ('django.db.models.fields.IntegerField', [], {'max_length': '50'})
        },
        u'web.staticpages': {
            'Meta': {'object_name': 'StaticPages'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'page_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'page_name_en': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'page_name_ru': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'seo_description': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'seo_description_en': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'seo_description_ru': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'seo_keyword': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'seo_keyword_en': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'seo_keyword_ru': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'seo_title': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'seo_title_en': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'seo_title_ru': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'show_in_menu': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'text': ('tinymce.models.HTMLField', [], {}),
            'text_en': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'text_ru': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['options']