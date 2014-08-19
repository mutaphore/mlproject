# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Input'
        db.create_table(u'mltest_input', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('raw_x', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('raw_y', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('raw_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'mltest', ['Input'])


    def backwards(self, orm):
        # Deleting model 'Input'
        db.delete_table(u'mltest_input')


    models = {
        u'mltest.input': {
            'Meta': {'object_name': 'Input'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raw_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'raw_x': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'raw_y': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        }
    }

    complete_apps = ['mltest']