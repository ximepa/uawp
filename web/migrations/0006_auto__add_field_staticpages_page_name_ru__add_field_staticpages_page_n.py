# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'StaticPages.page_name_ru'
        db.add_column(u'web_staticpages', 'page_name_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'StaticPages.page_name_en'
        db.add_column(u'web_staticpages', 'page_name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'StaticPages.title_ru'
        db.add_column(u'web_staticpages', 'title_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'StaticPages.title_en'
        db.add_column(u'web_staticpages', 'title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'StaticPages.text_ru'
        db.add_column(u'web_staticpages', 'text_ru',
                      self.gf('tinymce.models.HTMLField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'StaticPages.text_en'
        db.add_column(u'web_staticpages', 'text_en',
                      self.gf('tinymce.models.HTMLField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'StaticPages.seo_title_ru'
        db.add_column(u'web_staticpages', 'seo_title_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'StaticPages.seo_title_en'
        db.add_column(u'web_staticpages', 'seo_title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'StaticPages.seo_description_ru'
        db.add_column(u'web_staticpages', 'seo_description_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'StaticPages.seo_description_en'
        db.add_column(u'web_staticpages', 'seo_description_en',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'StaticPages.seo_keyword_ru'
        db.add_column(u'web_staticpages', 'seo_keyword_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'StaticPages.seo_keyword_en'
        db.add_column(u'web_staticpages', 'seo_keyword_en',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'NewsGroups.name_ru'
        db.add_column(u'web_newsgroups', 'name_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'NewsGroups.name_en'
        db.add_column(u'web_newsgroups', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'News.name_ru'
        db.add_column(u'web_news', 'name_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'News.name_en'
        db.add_column(u'web_news', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'News.description_ru'
        db.add_column(u'web_news', 'description_ru',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'News.description_en'
        db.add_column(u'web_news', 'description_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'News.text_ru'
        db.add_column(u'web_news', 'text_ru',
                      self.gf('tinymce.models.HTMLField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'News.text_en'
        db.add_column(u'web_news', 'text_en',
                      self.gf('tinymce.models.HTMLField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'News.seo_title_ru'
        db.add_column(u'web_news', 'seo_title_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'News.seo_title_en'
        db.add_column(u'web_news', 'seo_title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'News.seo_description_ru'
        db.add_column(u'web_news', 'seo_description_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'News.seo_description_en'
        db.add_column(u'web_news', 'seo_description_en',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'News.seo_keyword_ru'
        db.add_column(u'web_news', 'seo_keyword_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'News.seo_keyword_en'
        db.add_column(u'web_news', 'seo_keyword_en',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'StaticPages.page_name_ru'
        db.delete_column(u'web_staticpages', 'page_name_ru')

        # Deleting field 'StaticPages.page_name_en'
        db.delete_column(u'web_staticpages', 'page_name_en')

        # Deleting field 'StaticPages.title_ru'
        db.delete_column(u'web_staticpages', 'title_ru')

        # Deleting field 'StaticPages.title_en'
        db.delete_column(u'web_staticpages', 'title_en')

        # Deleting field 'StaticPages.text_ru'
        db.delete_column(u'web_staticpages', 'text_ru')

        # Deleting field 'StaticPages.text_en'
        db.delete_column(u'web_staticpages', 'text_en')

        # Deleting field 'StaticPages.seo_title_ru'
        db.delete_column(u'web_staticpages', 'seo_title_ru')

        # Deleting field 'StaticPages.seo_title_en'
        db.delete_column(u'web_staticpages', 'seo_title_en')

        # Deleting field 'StaticPages.seo_description_ru'
        db.delete_column(u'web_staticpages', 'seo_description_ru')

        # Deleting field 'StaticPages.seo_description_en'
        db.delete_column(u'web_staticpages', 'seo_description_en')

        # Deleting field 'StaticPages.seo_keyword_ru'
        db.delete_column(u'web_staticpages', 'seo_keyword_ru')

        # Deleting field 'StaticPages.seo_keyword_en'
        db.delete_column(u'web_staticpages', 'seo_keyword_en')

        # Deleting field 'NewsGroups.name_ru'
        db.delete_column(u'web_newsgroups', 'name_ru')

        # Deleting field 'NewsGroups.name_en'
        db.delete_column(u'web_newsgroups', 'name_en')

        # Deleting field 'News.name_ru'
        db.delete_column(u'web_news', 'name_ru')

        # Deleting field 'News.name_en'
        db.delete_column(u'web_news', 'name_en')

        # Deleting field 'News.description_ru'
        db.delete_column(u'web_news', 'description_ru')

        # Deleting field 'News.description_en'
        db.delete_column(u'web_news', 'description_en')

        # Deleting field 'News.text_ru'
        db.delete_column(u'web_news', 'text_ru')

        # Deleting field 'News.text_en'
        db.delete_column(u'web_news', 'text_en')

        # Deleting field 'News.seo_title_ru'
        db.delete_column(u'web_news', 'seo_title_ru')

        # Deleting field 'News.seo_title_en'
        db.delete_column(u'web_news', 'seo_title_en')

        # Deleting field 'News.seo_description_ru'
        db.delete_column(u'web_news', 'seo_description_ru')

        # Deleting field 'News.seo_description_en'
        db.delete_column(u'web_news', 'seo_description_en')

        # Deleting field 'News.seo_keyword_ru'
        db.delete_column(u'web_news', 'seo_keyword_ru')

        # Deleting field 'News.seo_keyword_en'
        db.delete_column(u'web_news', 'seo_keyword_en')


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
        u'web.news': {
            'Meta': {'object_name': 'News'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.NewsGroups']", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'seo_description': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'seo_description_en': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'seo_description_ru': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'seo_keyword': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'seo_keyword_en': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'seo_keyword_ru': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'seo_title': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'seo_title_en': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'seo_title_ru': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'show_news': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'text': ('tinymce.models.HTMLField', [], {}),
            'text_en': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'text_ru': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'})
        },
        u'web.newsgroups': {
            'Meta': {'object_name': 'NewsGroups'},
            'bootstrap_panel_class': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
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

    complete_apps = ['web']