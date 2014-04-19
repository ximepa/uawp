# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FeedBackGroup'
        db.create_table(u'feed_back_feedbackgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'feed_back', ['FeedBackGroup'])

        # Adding model 'FeedBack'
        db.create_table(u'feed_back_feedback', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feed_back.FeedBackGroup'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('mail', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'feed_back', ['FeedBack'])


    def backwards(self, orm):
        # Deleting model 'FeedBackGroup'
        db.delete_table(u'feed_back_feedbackgroup')

        # Deleting model 'FeedBack'
        db.delete_table(u'feed_back_feedback')


    models = {
        u'feed_back.feedback': {
            'Meta': {'object_name': 'FeedBack'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feed_back.FeedBackGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'feed_back.feedbackgroup': {
            'Meta': {'object_name': 'FeedBackGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['feed_back']